from selenium import webdriver
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


@given("Open Amazon Home Page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Shopping Cart')
def open_shopping_cart(context):
    open_cart = context.driver.find_element(By.CSS_SELECTOR, "a#nav-cart")
    open_cart.click()


@then('Verify Shopping Cart is Empty')
def verify_text(context):
    result = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")
    assert "Cart is empty" in result.text, f"Expected 'Cart is empty', but got {result.text}"
