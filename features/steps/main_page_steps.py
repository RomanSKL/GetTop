from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep

BANNER2 = (By.CSS_SELECTOR, "a[href='/product-category/macbook/']")
BANNER1 = (By.CSS_SELECTOR, "a[href='/product-category/ipad/']")


@given('Open GetTop')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Hover over Banner 1')
def hover_over_banner1(context):
    context.app.main_page.hover_over_banner1()


@when('Click right arrow')
def click_right_arrow(context):
    context.app.main_page.click_right_arrow()


@when('Click left arrow')
def click_left_arrow(context):
    context.app.main_page.click_left_arrow()


@when('Click right dott')
def click_right_dott(context):
    context.app.main_page.click_right_dott()


@when('Click left dott')
def click_left_dott(context):
    context.app.main_page.click_left_dott()


@when('Click on Banner 1')
def click_banner1(context):
    context.app.main_page.click_banner1()


@when('Click on Banner 2')
def click_banner2(context):
    context.app.main_page.click_banner2()


@when('Verify Banner 2')
def verify_banner2(context):
    context.driver.wait.until(EC.element_to_be_clickable(BANNER2), 'Banner 2 is not present')


@then('Verify Banner 1')
def verify_banner1(context):
    context.driver.wait.until(EC.element_to_be_clickable(BANNER1), 'Banner 1 is not present')


@then('Verify correct category page is open for Banner 1')
def click_banner1_page_opened(context):
    context.app.main_page.click_banner1_page_opened()


@then('Verify correct category page is open for Banner 2')
def click_banner2_page_opened(context):
    context.app.main_page.click_banner2_page_opened()

