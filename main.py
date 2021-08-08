import moray

# main
if __name__ == "__main__":
    
    try:
        # ウェブコンテンツを持つフォルダ
        moray.init('web')
        
        # 最初に表示するhtmlページ
        moray.run()
        
    except Exception as e:
        print(e)
