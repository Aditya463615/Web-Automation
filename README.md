
# Automation using selenuim with python
Selenium allows us to create our own automation to perform our task easly using python script. 
# Modules
```bash
pip install selenium
```
# Create Automation
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
```
```python
driver = webdriver.Chrome()
url = r'https://www.example.com/'
driver.get(url)
```
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
```
> [!TIP]
> title_is
  ```python
element = WebDriverWait(driver, 10).until(
    EC.title_is("expected title")
)
  ```
> [!TIP]
> title_contains
```python
element = WebDriverWait(driver, 10).until(
    EC.title_contains("expected title")
)
```
> [!TIP]
> presence_of_element_located
```python
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myDynamicElement"))
)
```
> [!TIP]
> visibility_of_element_located
```python
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "myDynamicElement"))
)
```
> [!TIP]
> visibility_of
```python
element = WebDriverWait(driver, 10).until(
    EC.visibility_of(driver.find_element_by_id("myDynamicElement"))
)
```
> [!TIP]
> presence_of_all_elements_located
```python
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "myDynamicElement"))
)
```
> [!TIP]
> text_to_be_present_in_element
```python
element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "myDynamicElement"), "expected text")
)
```
> [!TIP]
> text_to_be_present_in_element_value
```python
element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element_value((By.ID, "myDynamicElement"), "expected text")
)
```
> [!TIP]
> frame_to_be_available_and_switch_to_it
```python
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "myDynamicFrame"))
)
```
> [!TIP]
> invisibility_of_element_located
```python
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "myDynamicElement"))
)
```
> [!TIP]
> element_to_be_clickable
```python
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "myDynamicElement"))
)
```
> [!TIP]
> staleness_of
```python
WebDriverWait(driver, 10).until(
    EC.staleness_of(driver.find_element_by_id("myDynamicElement"))
)
```
> [!TIP]
> element_to_be_selected
```python
WebDriverWait(driver, 10).until(
    EC.element_to_be_selected((By.ID, "myDynamicElement"))
)
```
> [!TIP]
> element_located_to_be_selected
```python
WebDriverWait(driver, 10).until(
    EC.element_located_to_be_selected((By.ID, "myDynamicElement"))
)
```
> [!TIP]
> element_selection_state_to_be
```python
WebDriverWait(driver, 10).until(
    EC.element_selection_state_to_be(
        (By.ID, "myDynamicElement"), "all"
    )
)
```
> [!TIP]
> element_located_selection_state_to_be
```python
WebDriverWait(driver, 10).until(
    EC.element_located_selection_state_to_be(
        (By.ID, "myDynamicElement"), "all"
    )
)
```
> [!TIP]
> alert_is_present
```python
WebDriverWait(driver, 10).
```
### [Know more about Javascript](https://www.w3schools.com/js/)
### [Know more about Selenium](https://selenium-python.readthedocs.io/)
