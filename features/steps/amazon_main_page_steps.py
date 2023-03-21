from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')

@when('Input text {search_word}')
def input_product_name(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)


@when('Click on search button')
def click_search_button(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then('Verify that text {expected_text} is shown')
def verify_search_result(context, expected_text):
    print(expected_text)
    actual_text = context.driver.find_element(By.XPATH, '//span[@class="a-color-state a-text-bold"]').text
    print(actual_text)
    assert expected_text == actual_text, f'Text does not match'



