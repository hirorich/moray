import moray

# main
if __name__ == "__main__":
    
    try:
        # moray起動
        moray.run('web')
        
    except Exception as e:
        print(e)
