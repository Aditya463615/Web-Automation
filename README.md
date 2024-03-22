
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
- Find an element
```python
element = driver.find_element(By.ID, "id")
element = driver.find_element(By.NAME, "name")
element = driver.find_element(By.XPATH, "xpath")
element = driver.find_element(By.LINK_TEXT, "link text")
element = driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
element = driver.find_element(By.TAG_NAME, "tag name")
element = driver.find_element(By.CLASS_NAME, "class name")
element = driver.find_element(By.CSS_SELECTOR, "css selector")
```
- click an element 
```Javascript
document.querySelector(`<selector>`).click();
```
```python
element.click()
```
- input to an element 
```Javascript
document.querySelector(`<selector>`).value = `<value>`;
```
```python
element.send_keys("some text")
element.clear()
```
- scrap data into python 
```Javascript
return(<your Data from page>)
```
- Wait 
```python
driver.implicitly_wait(10) # wait without any condition
# wait until the element#myDynamicElement appears lasts 10 seconds otherwise quit
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
# other conditions to wait
'''
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
'''
```
### [Know more about Javascript](https://www.w3schools.com/js/)
