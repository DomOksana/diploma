import allure
from selenium.webdriver import ActionChains, Keys
from Tests_UI.locators.item_page_locators import BN_CHOICE_BRANDS, \
    BN_CHOOSING_ITEM, \
    BN_CHOICE_AAA, \
    BN_SORT_PRICE, \
    BN_SORTING_BY_PRICE, \
    BN_ADD_TO_CART, \
    BN_GO_TO_CART, \
    BN_SUPER, \
    BN_VISION, \
    TXT_PRODUCTS_PRICE, \
    BN_OFFERS
from Tests_UI.pages.base_page import BasePage


class ItemPage(BasePage):

    @property
    def laptop_price(self):
        return self.text(TXT_LAPTOP_PRICE)

    def select_by_name(self):
        with allure.step("Scroll to the desired button"):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*BN_SUPER))
        with allure.step("Select offers of items"):
            self.click(BN_CHOICE_BRANDS)
        with allure.step("Choosing the thing we dream about"):
            self.click(BN_CHOICE_APPLE)

    @allure.step("Sorting offers")
    def sort_by_lowest_price(self):
        """
        This function sorts the product by price in ascending order
        :return:
        """
        self.driver.execute_script("window.scrollTo(0, -200);")
        action = ActionChains(self.driver)
        selector = self.driver.find_element(*BN_SORTING_BY_PRICE)
        action.move_to_element(selector).perform()
        action.click().perform()
        for _ in range(1):
            selector.send_keys(Keys.ARROW_DOWN)
        selector.send_keys(Keys.ENTER)

    def choosing_item(self):
        with allure.step("Choosing item with the lowest price"):
            self.click(BN_CHOOSING_ITEM)

    def select_offers(self):
        with allure.step("Selection of sellers' offers"):
            self.click(BN_OFFERS)

    def choice_at_the_lowest_price(self):
        """
        This function selects the product at the lowest price
        :return:
        """
        action = ActionChains(self.driver)
        selector = self.driver.find_element(*BN_SORT_PRICE)
        action.move_to_element(selector).perform()
        action.click().perform()
        for _ in range(1):
            selector.send_keys(Keys.ARROW_DOWN)
        selector.send_keys(Keys.ENTER)

    @allure.step("Adding item to cart")
    def add_to_cart(self):
        """
        Adding item to cart
        :return:
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*BN_VISION))
        self.click(BN_ADD_TO_CART)

    @allure.step("Going to cart")
    def go_to_cart(self):
        """
        Go to the shopping cart
        :return:
        """
        self.click(BN_GO_TO_CART)