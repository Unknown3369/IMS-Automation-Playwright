import os

from playwright.sync_api import sync_playwright

from Pages.Login import Login
from Pages.Masters.bulk_price_change import BulkSalesPriceUpdate


def test_bulk_sales_price(page,config_data):

   login_page = Login(page)
   login_page.perform_login(config_data)
   print("Logged into IMS")

   bulk_price = BulkSalesPriceUpdate(page)
   bulk_price.navigate_to_bulk_sales_price()
   bulk_price.select_category()
   bulk_price.update_prices()
