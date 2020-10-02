from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input Dress into Amazon search field')
def input_search_word(context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Dress")


@when('Click on Amazon search icon')
def click_search_icon(context):
    search_icon = context.driver.find_element(By.XPATH, "//input[@value='Go']")
    search_icon.click()


@then('Search Result Dress is shown')
def verify_search_result(context):
    result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
    assert result.text == '"Dress"', f'Error. Expect Dress, but got {result.text}'
