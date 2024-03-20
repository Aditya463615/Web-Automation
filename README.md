
# Automation using selenuim with python
Selenium allows us to create our own automation to perform our task easly using python script. 
# Modules
```bash
pip install selenium
```
# Create Automation
```python
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

myAutomation = automation('<url>')      # go to webpage
myAutomation.execute('<JS script>')     # interact with page
myAutomation.quit()                     # exit the app

```
## Tips
- click an element 
```Javascript
document.querySelector(`<selector>`).click();
```
- input to an element 
```Javascript
document.querySelector(`<selector>`).value = `<value>`;
```
- scrap data into python 
```Javascript
return(<your Data from page>)
```
### [Know more about Javascript](https://www.w3schools.com/js/)
