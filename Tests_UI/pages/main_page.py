import allure
from Tests_UI.locators.main_page_locators import BN_CATALOG, BN_SECTION, BN_PRODUCTS
from Tests_UI.pages.base_page import BasePage


@allure.feature("Catalog Page Tests")
class CatalogPage(BasePage):

    def click_catalog(self):
        with allure.step("Select catalog"):
            self.click(BN_CATALOG)


    def section(self):
        with allure.step("Select section"):
            self.click(BN_SECTION)

    @allure.title("Test choosing")
    def choosing_products(self):
        with allure.step("Select products"):
            self.click(BN_PRODUCTS)