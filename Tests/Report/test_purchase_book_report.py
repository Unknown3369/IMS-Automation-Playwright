import time
import os

from Pages.Login import Login
from Pages.Report.Purchase_Book_Report import PurchaseBookReport

def test_purchase_book_report(page,config_data):
    try:
        login_page = Login(page)
        login_page.perform_login(config_data)
    except:
        print("already logged in")
    purchase_report = PurchaseBookReport(page)

    purchase_report.open_purchase_book_report()

    time.sleep(8)
