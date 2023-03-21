from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

RETURNS_ORDERS = (By.ID, 'nav-orders')
TEXT = (By.CSS_SELECTOR, 'h1.a-spacing-small')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')
@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('User click on Returns and orders')
def click_ReturnsAndOrders(context):
    context.driver.wait.until(EC.element_to_be_clickable(RETURNS_ORDERS), message="Button is not clickable").click()


@then('Verify that user sees Sign in page')
def display_SignIn(context):
    expected_text = context.driver.wait.until(EC.presence_of_element_located(TEXT), message="Element is not located").text
    print(expected_text)
    assert expected_text == 'Sign in', f'Text does not match'


@then('Verify that Sign in popup is shown')
def verify_sign_in_popup_shown(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BTN), message="Sign in button is not visible")



@when('Wait for {sec} sec')
def wait_for_sec(context,sec):
    sleep(int(sec))


@then('Verify Sign in popup disappears')
def signin_popup_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGNIN_BTN), message="Signin btn did not disappear")