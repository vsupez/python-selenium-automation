from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')


# @given('Open amazon page')
# def open_amazon(context):
#     # context.driver.get('https://www.amazon.com/')
#     context.app.main_page.open_main()

# @when('Input text {search_word}')
# def input_product_name(context, search_word):
#     # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)
#     context.app.header.input_search_text(search_word)

# @when('Click on search button')
# def click_search_button(context):
#     # context.driver.find_element(*SEARCH_ICON).click()
#     context.app.header.click_search()

@given('Open New Arrivals page')
def open_new_arrivals(context):
    context.app.main_page.open_new_arrivals()

@when('Hover over language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()

@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()


@then('Verify spanish option is present')
def verify_lang_shown(context):
    context.app.header.verify_lang_shown()


@then('Verify that text {expected_text} is shown')
def verify_search_result(context, expected_text):
    context.app.search_results_page.verify_search_result(expected_text)


@then('Verify hamburger menu icon is present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@when('Select department by alias {alias}')
def select_department_books(context, alias):
    context.app.header.select_department(alias)


@then('Verify {category} department is selected')
def verify_selected_dept(context, category):
    context.app.search_results_page.verify_selected_dept(category)

@then("Verify that user sees deals")
def verify_deals_present(context):
    context.app.main_page.verify_deals_present()

