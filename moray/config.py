"""
morayの設定情報

"""

from moray import chrome

root = None
start_page = 'index.html'
browser = chrome.name
cmdline_args = ['--disable-http-cache', '--incognito']
position = None
size = None
host = 'localhost'
port = 0

develop_mode = False
is_initialized = False
generated_port = 0
