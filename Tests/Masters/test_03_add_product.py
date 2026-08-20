from Pages.Login import Login
from Pages.Masters.add_product import Add_prod
import random
import csv
import os
import uuid
import time
MAX_PRODUCTS = 10

def random_name():
   return "PRODUCT" + uuid.uuid4().hex[:4]

def clear_csv(filename="added_products.csv"):
   with open(filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Item Code", "Item Name", "HS Code", "Description", "Purchase Price", "Sales Price", "Vatable"])
   print("CSV reset complete.")

def product_group(filename="product_groups.csv"):
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        if not rows:
            raise Exception("No Product Groups found in CSV")

        return rows[-1]["Group Name"]

def get_vendor_from_csv(filename="vendors.csv"):
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        raise Exception("No vendors found in CSV")

    return rows[-1]["ACNAME"]

def save_product_to_csv(item_code,item_name,hs_code,description,purchase_price,sales_price,vatable,filename="product_details.csv"):

   header = ["Item Code", "Item Name", "HS Code", "Description", "Purchase Price", "Sales Price", "Vatable"]

   rows = []

   if os.path.exists(filename):
      with open(filename, "r", newline="", encoding="utf-8") as f:
         reader = list(csv.reader(f))

         if reader:
            if reader[0] == header:
               rows = reader[1:]
            else:
               rows = reader

   rows.append([item_code,item_name,hs_code,description,purchase_price,sales_price,vatable])

   while len(rows) > MAX_PRODUCTS:
      rows.pop(0)  

   with open(filename, "w", newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow(header)
      writer.writerows(rows)

   print(f"FIFO updated: {len(rows)} rows")


def test_add_prod(page, config_data):

   try:
      login_page = Login(page)
      login_page.perform_login(config_data)
   except: 
      print("Already logged in")
   add_prod_page = Add_prod(page)
   clear_csv("product_details.csv")
   page.wait_for_load_state("networkidle")
   page.wait_for_timeout(3000)
   
   for i in range(1):
      add_prod_page.masters_click_test()
      random_item_name = random_name()
      random_hs_code = str(random.randint(1000, 9999))
      stock_unit = "Pkt."
      random_description = "Test Product Description"
      random_purchase_price = random.randint(50, 180)
      random_sales_price = random.randint(200, 350)
      selected_group = product_group()
      selected_vendor = get_vendor_from_csv()
      item_code, vatable_status = add_prod_page.add_prod_test(
         input_itemname=random_item_name,
         input_hscode=random_hs_code,
         input_description=random_description,
         stock_units=stock_unit,
         prod_group=selected_group,
         vendor_name=selected_vendor,
         input_purchase_price=random_purchase_price,
         input_sales_price=random_sales_price,
         iteration=i
      )

      add_prod_page.save_button()

      save_product_to_csv(item_code=item_code,item_name=random_item_name,hs_code=random_hs_code,description=random_description,purchase_price=random_purchase_price,sales_price=random_sales_price,vatable=vatable_status)

      page.wait_for_timeout(2000)
      time.sleep(8)