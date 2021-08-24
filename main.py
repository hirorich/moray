import moray
from sample_module import sub_module

# main
if __name__ == "__main__":
    
    try:
        # moray起動
        moray.run('web', port=0)
        
    except Exception as e:
        print(e)
