from behave import given, then
from selenium.webdriver.common.by import By


COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name span.selection')

@given('Open Amazon Jeans {productid} Page')
def open_jeans_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/B07BJKRR25/{productid}/')


@then('Verify user can cycle through color selections')
def verify_jeans_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash',\
                       'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        color_text = context.driver.find_element(*SELECTED_COLOR)
        assert color_text == expected_colors[i], \
            f"Color doesn't match. Expected {expected_colors[i]} but got {colors[i].text}"
