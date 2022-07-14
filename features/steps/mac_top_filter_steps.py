from selenium.webdriver.common.by import By
from behave import given, when, then, step


ALL_ITEMS_UNDER_MAC = (By.CSS_SELECTOR, "a[href='https://gettop.us/product-category/macbook/']")


@when('Hover over MAC')
def hover_over_mac(context):
    context.app.main_page.hover_over_mac()


@when('Click on MacBook Pro 13-inch')
def click_pro_13(context):
    context.app.header.click_pro_13()


@when('Click on MacBook Pro 16-inch')
def click_pro_16(context):
    context.app.header.click_pro_16()


@when('Click on MacBook Air')
def click_air(context):
    context.app.header.click_air()


@when('Click on link under You may also like…')
def click_link_under_you_may_also_like(context):
    context.app.header.click_link_under_you_may_also_like()


@then('Verify all {expected} items under MAC')
def verify_all_items(context, expected):
    expected = int(expected)
    all_items_under_mac = context.driver.find_elements(*ALL_ITEMS_UNDER_MAC)
    assert len(all_items_under_mac) == expected, f'Expected {expected} links, but got {len(all_items_under_mac)}'


@then('Verify MacBook Pro 13-inch page is opened')
def verify_pro_13_open(context):
    context.app.header.verify_pro_13_open()


@then('Verify MacBook Pro 16-inch page is opened')
def verify_pro_16_open(context):
    context.app.header.verify_pro_16_open()


@then('Verify MacBook Air page is opened')
def verify_air_open(context):
    context.app.header.verify_air_open()


@when('Verify You may also like… text is present')
def verify_you_may_also_like(context):
    context.app.header.verify_you_may_also_like()


@then('Verify correct MacBook page is opened')
def verify_correct_macbook_page_is_opened(context):
    context.app.header.verify_correct_macbook_page_is_opened()


