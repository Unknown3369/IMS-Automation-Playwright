import csv
import random
import time
from playwright.sync_api import sync_playwright
from Pages.Login import Login
from Pages.Transactions.Purchase_invoice import PurchaseInvoice


def read_products_from_csv(file_path):
   products = []

   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
   return products

def test_purchase_invoice(page,config_data):

   try:
      login_page = Login(page)

      login_page.perform_login(config_data)
   except: 
      print("Already Logged In")
   
   purchase_invoice = PurchaseInvoice(page)
   products = read_products_from_csv("product_details.csv")
   random_invoice_no = "IRD_REFNO." + str(random.randint(10000, 99999))
   purchase_invoice.purchase_invoice(random_invoice_no)
   time.sleep(1)
   for product in products:

      item_code = product['Item Code']
      random_quantity = str(random.randint(100, 999))
      purchase_invoice.purchase_invoice_test(
         item_code,
         random_quantity
      )

   purchase_invoice.save_button_click()