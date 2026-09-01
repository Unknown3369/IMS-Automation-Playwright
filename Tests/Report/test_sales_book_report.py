import pytest
import time
import os

from Pages.Login import Login
from Pages.Report.Sales_Book_Report import SalesBookReportPage


def test_sales_book_report(page,config_data):

    try:
        login_page = Login(page)
        login_page.perform_login(config_data)
    except:
        print('Already logged In')

    sales_report = SalesBookReportPage(page)
    sales_report.open_sales_book_report()
    sales_report.run_sales_book_report()

    page.wait_for_timeout(15000)
