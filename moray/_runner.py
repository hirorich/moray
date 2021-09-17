"""
サーバ起動とブラウザ起動を制御

ToDo:
    デコレータによる例外時のログ出力・終了処理
"""

import logging, requests
from threading import Thread

from moray import _browser, _config, _server
from moray.exception import MorayRuntimeError

_logger = logging.getLogger(__name__)

def run():
    """
    スレッドを分ける
    メインスレッド: 内部サーバ起動
    デーモンスレッド: 起動確認 -> ブラウザ起動
    """
    
    # ブラウザ起動(別スレッド)
    deamon_t = Thread(target=open_browser)
    deamon_t.setDaemon(True)
    deamon_t.start()
    
    # サーバ起動
    _server.run()

def open_browser():
    """
    requestsによるGETでサーバーが起動しているか確認
    アプリモードでブラウザ表示
    
    Raises:
        MorayRuntimeError: サーバ起動エラー
        requests.exceptions.xxx: サーバ起動タイムアウトエラー
    
    ToDo:
        デコレータによる例外時のログ出力・終了処理
    """
    
    # サーバ起動確認
    connect_timeout = 3.0
    read_timeout = 5.0
    _logger.debug('confirming server running.')
    try:
        res = requests.get(
            _server.generate_confirm_running_url(),
            timeout = (connect_timeout, read_timeout)
        )
        if not res.ok:
            raise MorayRuntimeError('Could not confirm server run.')
    except Exception as e:
        # requests.exceptions.Timeout など
        raise
    
    # 初期表示URL生成
    url = _server.generate_start_url()
    
    # 初期ページ表示
    _logger.debug('opening start page.')
    _browser.open(_config.browser, url, _config.cmdline_args)
    
    # 接続がない場合は終了
    _server.check_exist_websocket()
