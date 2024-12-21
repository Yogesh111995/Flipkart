import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

service = Service()  # Automatically downloads and manages ChromeDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(3)

action = ActionChains(driver)
driver.find_element(By.CLASS_NAME,"Pke_EE").send_keys("samsung s24 ultra")
driver.find_element(By.CLASS_NAME,"Pke_EE").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]").click()
time.sleep(5)

handles = driver.window_handles
driver.switch_to.window(handles[1])
item_url= driver.current_url

# 256 GB Adding
add_to_cart_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
time.sleep(3)

driver.get(item_url)
storage_512_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[6]/div/div[2]/div[1]/div/ul/li[2]/a").click()
time.sleep(3)
add_to_cart_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
time.sleep(3)

remove_button= driver.find_element(By.CSS_SELECTOR,"div._5jL4tC.gRTtwM.f-DWwy > div.sBxzFz:nth-of-type(2)")
driver.execute_script("arguments[0].scrollIntoView(true);", remove_button)
remove_button.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".A0MXnh").click()
time.sleep(2)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
remove_button= driver.find_element(By.CSS_SELECTOR,"div._5jL4tC.gRTtwM.f-DWwy > div.sBxzFz:nth-of-type(2)")
driver.execute_script("arguments[0].scrollIntoView(true);", remove_button)
remove_button.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".A0MXnh").click()
time.sleep(2)

# enter_pincode_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/button").click()
# time.sleep(3)
# driver.find_element(By.CLASS_NAME,"a1Ny53").send_keys("600042")
# time.sleep(1)
# driver.find_element(By.CLASS_NAME, "Ji2MFX").click()
# time.sleep(3)

driver.close()
driver.switch_to.window(handles[0])
time.sleep(3)

driver.find_element(By.CLASS_NAME,"W5mR4e").click()
time.sleep(5)
driver.close()