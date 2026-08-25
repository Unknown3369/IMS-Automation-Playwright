import pytest
import random
import uuid

from Pages.Login import Login
from Pages.Masters.add_category import AddProductCategoryPage

print("\n==========Add Category Test==========\n")

def random_category_name():

   prefixes = ["Liquor","Snacks"]
   return f"{random.choice(prefixes)}_{uuid.uuid4().hex[:6]}"

def test_add_product_category(page,config_data):

   login_page = Login(page)

   try:
      login_page.perform_login(config_data)
      page.wait_for_load_state("networkidle")
      page.wait_for_timeout(3000)
      print("Logged into IMS successfully!")

      add_category = AddProductCategoryPage(page)
      add_category.navigate_to_add_product()
      category_name = random_category_name()
      print(f"Generated Random Category: {category_name}")
      add_category.add_product_category(category_name)

   except Exception as e:
      pytest.fail(
         f"Test failed due to: {e}"
      )