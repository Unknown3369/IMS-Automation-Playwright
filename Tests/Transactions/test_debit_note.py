# tests/test_debit_note.py

from conftest import browser
import csv
import os
import random
import pytest
from playwright.sync_api import sync_playwright
from Pages.Login import Login
from Pages.Transactions.debit_note import DebitNote

print("\n==========Debit Note Test==========\n")

def read_products_from_csv(file_path):
   products = []

   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
      return products

def test_debit_note(page,config_data):

   try:
      login_page = Login(page)
      login_page.perform_login(config_data)
   except:
      print('Already Logged In')

   debit_note = DebitNote(page)
   products = read_products_from_csv("CSV/product_details.csv")
   random_ref_no = "REF_NO" + str(random.randint(10000, 99999))
   debit_note.enter_debit_note()
   debit_note.debit_note_entry(str(random_ref_no))

   for product in products:
      item_code = product["Item Code"]
      random_quantity = 10
      debit_note.debit_note_test(item_code, random_quantity)
      page.wait_for_timeout(1000)

   debit_note.save_button_click()
   print("Completed Debit Note")

   print("Test finished")