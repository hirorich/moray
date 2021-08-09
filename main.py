import moray
import moray_dev #開発モードで実行

# main
if __name__ == "__main__":
    
    try:
        # ウェブコンテンツを持つフォルダ
        moray.init('web')
        
        # 最初に表示するhtmlページ
        moray.run(port=8080)
        
    except Exception as e:
        print(e)
