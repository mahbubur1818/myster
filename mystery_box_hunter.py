from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

user = "mahbuburrahman0bd@gmail.com"
pas = "********"
product_link = "https://www.daraz.com.bd/products/100-i184736473-s1129914674.html?spm=a2a0e.home.just4u.5.735212f7a3mc0J&scm=1007.28811.276117.0&pvid=248f1254-1e01-4f86-9c0d-154f29ae9eeb&clickTrackInfo=pvid%3A248f1254-1e01-4f86-9c0d-154f29ae9eeb%3Bchannel_id%3A0000%3Bmt%3Ai2i%3Bitem_id%3A184736473%3B"

driver = webdriver.Chrome(executable_path=r'D:\Software\Download\chromedriver.exe')

def isPresent():
	try:
		driver.find_element_by_css_selector(".add-to-cart-buy-now-btn")
		return True
	except Exception as e:
		print(str(e))
		return False


driver.get('https://www.daraz.com.bd')
time.sleep(5)

# login

login = driver.find_element_by_id("anonLogin")
login.click()
time.sleep(2)


username = driver.find_element_by_css_selector("input[type='text']")
username.click()
username.clear()
username.send_keys(user)
time.sleep(3)

password = driver.find_element_by_css_selector("input[type='password']")
username.click()
username.clear()
password.send_keys(pas)
time.sleep(1)

password = driver.find_element_by_css_selector("button[type='submit']")
password.click()
print("logged in successfully")  #login successful
time.sleep(5)


driver.get(product_link)
time.sleep(0.5)

while True:
	if isPresent():
		buy_now = driver.find_element_by_css_selector(".add-to-cart-buy-now-btn")
		buy_now.click()
		try:
			proceed = driver.find_element_by_css_selector(".checkout-order-total-button")[1]
			proceed.click()
			time.sleep(1)
			print("proceed clicked")
		except:
			print("proceed not worked")
			driver.execute_script("window.history.go(-1)")
			driver.refresh()
			continue
		break
	else:
		driver.refresh()

print("ordered successfully")

time.sleep(25)


# voucher = #automation-voucher-input
