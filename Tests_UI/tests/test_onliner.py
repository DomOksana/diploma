import allure
import time
import pytest
from Test_UI.pages.cart_page import CartPage
from Test_UI.pages.main_page import MainPage
from Test_UI.pages.item_page import ItemPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


class TestAppleLaptop:

    @allure.feature("Buying Apple Laptop")
    @allure.story("User buys an Apple laptop from the catalog")
    def test_buy_apple_laptop(self, item_page, catalog_page, cart_page, driver):
        catalog_page.click_catalog()
        catalog_page.computers()
        catalog_page.choosing_laptop()
        item_page.select_by_name()
        item_page.sort_by_lowest_price()
        time.sleep(1)
        item_page.choosing_item()
        item_page.select_offers()
        item_page.choice_at_the_lowest_price()
        item_page.add_to_cart()
        item_page.go_to_cart()
        cart_page.check_cart_title()
        cart_page.check_button_is_clickable()
        cart_page.check_cart_count(num_items=1)