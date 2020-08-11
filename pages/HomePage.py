class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get('https://rp.x-coding.pl/pl/')