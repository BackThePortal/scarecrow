from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome()

agent = driver.execute_script("return navigator.userAgent")
print(agent)

driver.get("https://www.instagram.com/thetinmen/")

el = None
try:
    el = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "x1iyjqo2"))
    )
finally:
    print(el.get_attribute('class'))
    driver.quit()
