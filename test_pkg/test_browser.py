"""
my_package.browser のテスト

"""

from my_package import browser

# main
def test():
    
    browser_name = 'chrome'
    url = r'https://www.google.co.jp/'
    cmdline_args = ['--incognito']
    browser.open(browser_name, url, cmdline_args)
