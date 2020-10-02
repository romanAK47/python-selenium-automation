from time import sleep
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path=r'C:\bin\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# Class 2 Example
# open the url

driver.get("https://www.amazon.com/")

# Search for Dress
input_field = driver.find_element(By.ID, "twotabsearchtextbox")
input_field.send_keys("Dress")

# Click GO
search_icon = driver.find_element(By.XPATH, "//input[@value='Go']")
search_icon.click()

# Check Result
result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
assert result.text == '"Dress"', f'Error. Expect Dress, but got {result.text}'
driver.quit()


# HOMEWORK 2 part 1 - disregard ".click" and "driver.quit" after each step. Used for testing only
# keep Open SIGN IN page uncommented
# comment out each step after completed before running next test


# Open SIGN IN page
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# Amazon Logo
logo_icon = driver.find_element(By.XPATH, "//*[@href='/ref=ap_frn_logo']")
logo_icon.click()
driver.quit()

# Search Bar/Continue
search_bar = driver.find_element(By.ID, "continue")
search_bar.click()
driver.quit()

# Help Expand
help_expand = driver.find_element(By.XPATH, "//*[@class='a-expander-header a-declarative a-expander-inline-header a-link-expander']")
help_expand.click()

# Help Expand>Forgot Password
forgot_password = driver.find_element(By.ID, 'auth-fpp-link-bottom')
forgot_password.click()
driver.quit()

# Help Expand>Other Issues With Sign-In
other_issues = driver.find_element(By.ID, 'ap-other-signin-issues-link')
other_issues.click()
driver.quit()

# Create Account Button
create_account_button = driver.find_element(By.ID, 'createAccountSubmit')

# Extra credit - Conditions of Use and Privacy Notice
conditions_link = driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")
conditions_link.click()
driver.quit()

privacy_link = driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")
privacy_link.click()
driver.quit()


# HOMEWORK 2 - part 2

# Open Customer Help
driver.get("https://www.amazon.com/gp/help/customer/display.html ")

# Search for Cancel Order
input_field = driver.find_element(By.ID, "helpsearch")
input_field.send_keys("Cancel Order")

# since there is no GO button I had to use send_keys to press ENTER; had to import "Keys" above
input_field = driver.find_element(By.ID, "helpsearch").send_keys(Keys.ENTER)

# Verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[contains(@class,'a-box-inner')]").text
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[contains(@class,'cs-search-result-wrapper')]").text

driver.quit()
