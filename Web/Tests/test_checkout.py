# tests/test_add_to_cart.py
import pytest
import time
from selenium import webdriver
from Web.Pages.loginPage import (
    perform_successful_login,
)
from Web.Pages.productPage import add_item_to_cart, logout_user
from Web.Pages.cartPage import check_cart_item
from Web.Pages.checkoutPage import checkout_customer_ok, checkout_click, checkout_return_home, \
    click_finish_button, assert_price, assert_quantity

SAUCE_DEMO_URL = "https://www.saucedemo.com/"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_item_cart_and_checkout(browser):
    browser.get(SAUCE_DEMO_URL)

    perform_successful_login(browser, "standard_user", "secret_sauce")
    browser.save_screenshot("screenshots/successful_login.png")
    time.sleep(5)

    add_item_to_cart(browser)
    browser.save_screenshot("screenshots/add_item_to_cart.png")
    time.sleep(3)

    check_cart_item(browser)
    time.sleep(2)
    browser.save_screenshot("screenshots/check_cart_item.png")
    checkout_click(browser)
    time.sleep(1)

    checkout_customer_ok(browser, name="tom", lastname="testing")
    browser.save_screenshot("screenshots/checkout_customer.png")
    time.sleep(2)

    assert_price(browser)
    assert_quantity(browser)
    browser.save_screenshot("screenshots/assert_price_qqty.png")
    time.sleep(2)

    click_finish_button(browser)
    browser.save_screenshot("screenshot/click_finish_button.png")
    time.sleep(1)

    checkout_return_home(browser)
    time.sleep(1)
    browser.save_screenshot("screenshots/return_home.png")

    logout_user(browser)
    time.sleep(2)
    browser.save_screenshot("screenshots/logout_user.png")


if __name__ == "__main__":
    pytest.main()
