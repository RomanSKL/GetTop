from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep


@given('Open GetTop')
def open_main_page(context):
    context.app.main_page.open_main_page()
