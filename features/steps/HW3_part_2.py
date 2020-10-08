from selenium import webdriver
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

INPUT_FIELD = (By.ID, "twotabsearchtextbox")
SEARCH_BTN = (By.CSS_SELECTOR, "input[type=submit]")
KEY_WORD = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")


@given("Open Amazon Customer Help Page")
def open_amazon_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@when('Input "Cancel Order" and click Search')
def search_cancel_order(context):
    input_field = context.driver.find_element(*INPUT_FIELD)
    input_field.clear()
    input_field.send_keys("Cancel Order")
    context.driver.find_element(*SEARCH_BTN).click()


@then('Verify that page contains "Cancel Order"')
def verify_text(context):
    key_word = context.driver.find_element(*KEY_WORD)
    assert "Cancel Order" in key_word.text, f"Expected 'Cancel Order', but got {key_word.text}"

