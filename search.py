from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Smartwatch")
search_box.send_keys(Keys.ENTER)

time.sleep(2)

items = driver.find_elements(By.XPATH, "//a[@rel='noopener noreferrer']")
if items:
    items[0].click()

time.sleep(2)

window_handles = driver.window_handles
driver.switch_to.window(window_handles[0])
time.sleep(2)
driver.switch_to.window(window_handles[1])

time.sleep(2)

xpath_to_click = "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button"
buy_now_button = driver.find_element(By.XPATH, xpath_to_click)
buy_now_button.click()

time.sleep(2)


#login
driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[1]/input").send_keys("ashish.gaurav2003@gmail.com")
driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[1]/input").send_keys(Keys.ENTER)
time.sleep(20)

continue_button = driver.find_element(By.XPATH, '//*[@id="to-payment"]/button')
continue_button.click()
time.sleep(2)

try:
    offer_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/button')
    offer_button.click()
except:
    print("Offer button not found")

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[1]/div[4]/div/div/div[2]/div/label[3]/div[2]/div/div').click()
driver.find_element(By.NAME, 'cardNumber').send_keys('123456789')
driver.find_element(By.NAME, 'cvv').send_keys('123')

driver.quit()
