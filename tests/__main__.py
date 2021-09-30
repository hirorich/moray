from tests.module import exposed
import moray

try:
    # moray起動
    moray.run('web', port=0, cmdline_args = ['--disable-http-cache', '--incognito'])
    
except Exception as e:
    print(e)
