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

start_url='https://www.nike.com/launch/?s=upcoming'

driver = webdriver.Chrome(executable_path='/Users/edwardcox/chromedriver/chromedriver')
wait = WebDriverWait(driver, 10)
driver.get(start_url)
shoe = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section/figure[4]/div/div/a/img")
#getshoe = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section/figure[4]/div/div/figcaption/div/div/div[2]')))
shoe.click()
driver.execute_script("window.scrollTo(0,1000)")
el = driver.find_element_by_css_selector(".label.border-medium-grey.ncss-brand.u-uppercase.pb3-sm.pb3-lg.prl5-sm.pt3-sm.pt3-lg.pl5-sm.u-full-width")
el.click()
action = ActionChains(driver).move_to_element_with_offset(el,100,350)
action.click()
action.perform()
cart_btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div[2]/button")
cart_btn.click()
check_out_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[3]")))
check_out_btn.click()
guest_checkout = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="qa-guest-checkout"]')))
guest_checkout.click()

first_name = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="firstName"]')))
first_name.send_keys("Edward")

last_name = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="lastName"]')))
last_name.send_keys("Cox")

address = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="address1"]')))
address.send_keys("20476 Barnard Ave.")

city = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="city"]')))
city.send_keys("Walnut")

postal = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="postalCode"]')))
postal.send_keys("91789")

email = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="email"]')))
email.send_keys("ejcox24@gmail.com")

phone = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="phoneNumber"]')))
phone.send_keys("562-396-8859")

driver.find_element_by_xpath('//*[@id="state"]/option[text()="California"]').click()

save_continue = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Save & Continue")]')))
save_continue.click()

payment = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Continue to Payment")]')))
payment.click()

driver.switch_to.frame(driver.find_element_by_css_selector('.credit-card-iframe.mt1.u-full-width.prl2-sm'))

credit_card = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="creditCardNumber"]')))
credit_card.send_keys("123124124124")

expiration = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="expirationDate"]')))
expiration.send_keys("41221")

cv = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cvNumber"]')))
cv.send_keys("444")

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
