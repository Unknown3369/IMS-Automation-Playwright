import pytest

from Pages.Login import Login
from Pages.Report.Credit_Note_Report import CreditNoteBookReportPage


def test_generate_credit_note_book_report(page,config_data):
   try:
      login_page = Login(page)
      login_page.perform_login(config_data)
   except:
      print('Already Logged In')

   credit_report_page = CreditNoteBookReportPage(page)
   credit_report_page.generate_credit_note_book_report()
   credit_report_page.download_credit_note_report()

   print("Credit Note Book Report generated successfully.")
