import random
import csv
from Pages.Login import Login
from Pages.Transactions.Stock_issue import StockIssuePage


def read_products_from_csv(file_path):
   products = []

   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
   return products

def test_stock_issue_entry(page, config_data):

    login_page = Login(page)
    login_page.perform_login(config_data)

    products = read_products_from_csv(
        "CSV/product_details.csv"
    )

    # Get product from CSV
    product = products[0]

    item_code = product["Item Code"]
    enter_quantity = "20"

    print(f"Item Code: {item_code}")
    print(f"Quantity: {enter_quantity}")

    stock_issue = StockIssuePage(page)

    stock_issue.generate_stock_issue(
        item_code,
        enter_quantity
    )

    print("Stock Issue entry created successfully.")
