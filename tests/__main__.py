from tests.module import exposed
import moray

try:
    # moray起動
    moray.run('web', port=0)
    
except Exception as e:
    print(e)
