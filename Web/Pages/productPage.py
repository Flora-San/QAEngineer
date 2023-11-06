# loginPage.py
import time

from Web.Locators.locators import LoginPageLocators, ProductPageLocators


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


def get_cart_item_count(browser):
    cart_icon = browser.find_element(*ProductPageLocators.CART_ICON)
    return cart_icon.text


def logout_user(browser):
    open_menu = browser.find_element(*LoginPageLocators.MENU_ICON)
    open_menu.click()
    time.sleep(1)
    logout_user_action = browser.find_element(*ProductPageLocators.LOGOUT_LINK)
    logout_user_action.click()
