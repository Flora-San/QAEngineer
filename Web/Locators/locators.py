from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    MENU_ICON = (By.ID, "react-burger-menu-btn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-button")
    ITEM_BACKPACK = (By.ID, "item_4_title_link")


class ProductPageLocators:
    ITEM_BACKPACK = (By.ID, "item_4_title_link")
    ITEM_LIGHT = (By.ID, "item_0_title_link")
    ADD_TO_CART_BUTTON_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.ID, "")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # PRODUCT_LABEL = (By.CLASS_NAME, "product_label")


class CartPageLocators:
    ITEM_BACKPACK = (By.ID, "item_4_title_link")
    ITEM_LIGHT = (By.ID, "item_0_title_link")
    ADD_TO_CART_BUTTON_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_ITEM_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")


class CheckoutPageLocators:
    CHECKOUT_PAGE_INFO = (By.ID, "checkout_info_container")
    NAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")

    CHECKOUT_SUMMARY = (By.ID, "checkout_summary_container")
    FINISH_BUTTON = (By.ID, "finish")
    CHECKOUT_COMPLETED = (By.ID, "checkout_complete_container")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    PRICE_ELEMENT = (By.XPATH, "//div[@class='inventory_item_price']")
    QUANTITY_ELEMENT = (By.XPATH, "//div[@class='cart_quantity']")
    PRICE = "Price: $29.99"
    QUANTITY = "1"

