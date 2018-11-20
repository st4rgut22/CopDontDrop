import requests 
import sys
import re
import time
import urllib.request
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#copy the url of any shoe on https://www.nike.com/launch/?s=in-stock as start_url
driver = webdriver.Chrome(executable_path='/Users/edwardcox/chromedriver/chromedriver')
wait = WebDriverWait(driver, 10)
driver.get("https://www.nike.com/launch/")
time.sleep(10) #log in to nike app
start_url='https://www.nike.com/launch/?s=upcoming'
driver.get(start_url)
shoe = wait.until(EC.element_to_be_clickable((By.XPATH,'//img[@title="AIR FORCE 1 UTILITY"]')))
shoe.click()
driver.execute_script("window.scrollTo(0,1000)")
size = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.label.border-medium-grey.ncss-brand.u-uppercase.pb3-sm.pb3-lg.prl5-sm.pt3-sm.pt3-lg.pl5-sm.u-full-width')))
size.click()
action = ActionChains(driver).move_to_element_with_offset(size,100,350)
action.click()
action.perform()
cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.ncss-brand.ncss-btn-black.pb3-sm.prl5-sm.pt3-sm.u-uppercase.u-full-width')))
#cart_btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div[2]/button")
cart_btn.click()
check_out_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[3]")))
check_out_btn.click()
guest_checkout = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="qa-guest-checkout"]')))
guest_checkout.click()
"""
first_name = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="firstName"]')))
first_name.send_keys("Edward")

last_name = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="lastName"]')))
last_name.send_keys("Cox")

address = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="address1"]')))
address.send_keys("")

city = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="city"]')))
city.send_keys("Walnut")

postal = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="postalCode"]')))
postal.send_keys("91789")

email = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="email"]')))
email.send_keys("ejcox24@gmail.com")

phone = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="phoneNumber"]')))
phone.send_keys("")

driver.find_element_by_xpath('//*[@id="state"]/option[text()="California"]').click()

save_continue = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Save & Continue")]')))
save_continue.click()

payment = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Continue to Payment")]')))
payment.click()

driver.switch_to.frame(driver.find_element_by_css_selector('.credit-card-iframe.mt1.u-full-width.prl2-sm'))

#credit_card = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="creditCardNumber"]')))
#credit_card.send_keys("")

#expiration = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="expirationDate"]')))
#expiration.send_keys("")

"""

iframe = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'iframe.credit-card-iframe-cvv.mt1.u-full-width')))
driver.switch_to.frame(iframe)

cv = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cvNumber"]')))
cv.send_keys("527")

#review = wait.until(EC.element_to_be_clickable((By.XPATH,'//section//button[contains(.,"Continue")]')))
#review.click()
driver.switch_to.default_content()

review = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Continue")]')))
review.click()
#place.click()



#state = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="state"]')))
#state.click()
#action = ActionChains(driver).move_to_element_with_offset(state,5,40)
#action.click()
#action.perform()

#buy_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section/figure[1]/div/div/figcaption/div/div/div[2]/a')
#element = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div[1]/div/button/div")))
#element.click()
#element.click()
#buy_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section/figure[1]/div/div/figcaption')
#hover = ActionChains(driver).move_to_element(buy_btn)
#hover.perform()
