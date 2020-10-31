from behave import given, then, when
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#  Scenario: User can open and close Amazon Applications
# Given Open Amazon T&C page
# When Store original windows
# And Click on Amazon applications link
# And Switch to the newly opened window
# Then Amazon app page is opened
# And User can close new window and switch back to original


LINK = (By.XPATH, '//*[@href="https://www.amazon.com/gp/feature.html?docId=1000625601"]')
APP_PAGE = (By.XPATH, "//*[contains(text(), 'app')]")


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get(
        f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon applications link')
def click_app_link(context):
    app_link = context.driver.find_element(*LINK)
    app_link.click()


@when('Switch to the newly opened window')
def switch_windows(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_windows = context.driver.window_handles
    for window in context.original_windows:
        new_windows.remove(window)
    context.driver.switch_to_window(new_windows[0])


#
@then('Amazon app page is opened')
def confirm_amazon_app_page(context):
    context.driver.find_element(*APP_PAGE)


@then('User can close new window and switch back to original')
def go_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
