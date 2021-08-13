import moray
import _moray_dev #開発モードで実行

# main
if __name__ == "__main__":
    
    try:
        # moray起動
        moray.run('web')
        
    except Exception as e:
        print(e)
