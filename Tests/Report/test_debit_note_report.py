import pytest

from Pages.Login import Login
from Pages.Report.Debit_Note_Report import DebitNoteBookReportPage

def test_generate_debit_note_book_report(page,config_data):

    try:
        login_page = Login(page)
        login_page.perform_login(config_data)
    except:
        print('Already Logged In')

    debit_report_page = DebitNoteBookReportPage(page)
    debit_report_page.generate_debit_note_book_report()
    debit_report_page.download_debit_note_report()

    print("Debit Note Book Report generated successfully.")
