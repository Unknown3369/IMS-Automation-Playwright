import random
import pytest
import csv
import uuid
from Pages.Login import Login
from Pages.Masters.add_product_group import (AddProductGroupMasterPage)

print("\n==========Add Product Group Test==========\n")

def clear_csv(filename="CSV/product_groups.csv"):
   with open(filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Timestamp","Group Name","Group Code","Recommended Margin","Shelf Life"])
   print("CSV reset complete.")

def random_group_name():
   return f"{uuid.uuid4().hex[:6]}_Group"

def random_group_code():
   return f"{random.randint(1111, 9999)}"


def test_add_product_group_master(page, config_data):
   try:
      login_page = Login(page)
      login_page.perform_login(config_data)
   except: 
      print("Already Logged In")

   clear_csv("CSV/product_groups.csv")

   try:
      add_group = AddProductGroupMasterPage(page)
      add_group.navigate_to_add_product()
      add_group.select_item_group()

      add_group.fill_group_details_and_save(
         group_name=random_group_name(),
         group_code=random_group_code(),
         recommended_margin=random.randint(5, 20),
         shelf_life=random.randint(15, 90)
      )
      print("Product Group Added Successfully")

   except Exception as e:
      pytest.fail(
         f"Test failed due to: {str(e)}"
      )