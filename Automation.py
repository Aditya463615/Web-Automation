from selenium import webdriver

class automation:
    def __init__(self, url, browser='Chrome'):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.url = url

    def execute(self,script):
        result = self.driver.execute_script(script)
        return(result)
        
    def quit(self):
        self.driver.quit()

