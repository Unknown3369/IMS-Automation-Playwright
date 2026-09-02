from Pages.Login import Login
from Pages.Report.Stock_Summary_Report import StockSummaryReport


def test_stock_summary_report(page,config_data):
    try:
        login_page = Login(page)
        login_page.perform_login(config_data)
    except:
        print('Already Logged In')

    stock_report = StockSummaryReport(page)
    stock_report.open_stock_summary_report()
    stock_report.run_report()
    stock_report.download_stock_summary_report()

    print("Stock Summary Report generated successfully.")