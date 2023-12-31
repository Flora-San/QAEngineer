# loginPage.py
import time

from Web.Pages.loginPage import LoginPageLocators
from Web.Pages.productPage import ProductPageLocators
from Web.Locators.locators import CartPageLocators


def login(browser, username, password):
    username_input = browser.find_element(*LoginPageLocators.USERNAME_INPUT)
    password_input = browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
    login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()


# def products(browser, item_name):


def is_error_message_displayed(browser):
    error_message = browser.find_element(*LoginPageLocators.ERROR_MESSAGE)
    return error_message.is_displayed()


def is_product_label_displayed(browser):
    product_label = browser.find_element(*LoginPageLocators.MENU_ICON)
    return product_label.is_displayed()


def capture_screenshot(browser, filename):
    try:
        browser.save_screenshot(filename)
        return True
    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")
        return False


def perform_successful_login(browser, username, password, screenshot_filename=None):
    login(browser, username, password)
    if screenshot_filename:
        capture_screenshot(browser, screenshot_filename)


def perform_failed_login(browser, username, password, screenshot_filename=None):
    login(browser, username, password)
    if screenshot_filename:
        capture_screenshot(browser, screenshot_filename)


def add_item_to_cart(browser, screenshot_filename=None):
    item_name = browser.find_element(*LoginPageLocators.ITEM_BACKPACK)
    item_name.click()
    time.sleep(3)
    add_to_cart_button = browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON_BACKPACK)
    add_to_cart_button.click()

    if screenshot_filename:
        capture_screenshot(browser, screenshot_filename)

    # return get_cart_item_count(browser)


def check_cart_item(browser):
    cart_icon_click = browser.find_element(*CartPageLocators.CART_ICON)
    cart_icon_click.click()


def get_cart_item_count(browser):
    cart_icon = browser.find_element(*ProductPageLocators.CART_ICON)
    return cart_icon.text


def check_item_cart(browser, screenshot_filename=None):
    item_cart = browser.find_element(*ProductPageLocators.ITEM_BACKPACK)
    time.sleep(3)


def remove_item_cart(browser):
    remove_item = browser.find_element(*CartPageLocators.REMOVE_ITEM_BACKPACK)
    remove_item.click()
    # return remove_item.text


def continue_shopping_click(browser):
    continue_shopping_action = browser.find_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)
    continue_shopping_action.click()
