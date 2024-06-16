import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
#driver.get("https://www.onliner.by/")
driver.get("https://magento.softwaretestingboard.com/sale.html")

element = driver.find_element(By.CLASS_NAME, "page-main")
print(element)
print(element.tag_name)
print(element.text)

print()
print(driver.title)
print(driver.current_url)


#time.sleep(5)