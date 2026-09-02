from playwright.sync_api import Page
import time
class StockIssuePage:

    def __init__(self, page: Page):
        self.page = page

    def generate_stock_issue(self,item_code: str, enter_quantity: int):

        self.page.get_by_title("Transactions").first.click()
        self.page.get_by_title("Inventory Movement").nth(1).click()
        self.page.get_by_role("link", name="Stock Issue",exact=True).click()

        from_wh = self.page.locator("//select[@id='stockissueFromWH']")
        from_wh.wait_for(state="visible",timeout=30000)
        from_wh.select_option(label="Main Warehouse")
        print("Selected From Warehouse: Main Warehouse")

        remark_field = self.page.locator("textarea")
        remark_field.wait_for(state="visible",timeout=30000)
        remark_field.fill("Stock Issue Automation Entry")
        print("Remark added.")

        to_wh = self.page.locator("//select[@style='width: 70%;' and contains(@class,'ng-valid')]").nth(1)
        to_wh.wait_for(state="visible",timeout=30000)
        to_wh.select_option(value="0: Main Warehouse")

        item_to_select = self.page.locator("//input[@id='barcodeField']")
        item_to_select.wait_for(state="visible",timeout=30000)
        item_to_select.fill(item_code)
        item_to_select.press("Enter")
        time.sleep(1)
        print("Item name selected successfully!")

        quantity = self.page.locator("//input[@id='quantityBarcode']")
        quantity.fill(str(enter_quantity))
        quantity.press("Enter")
        time.sleep(1)
        print("Quantity entered successfully!")
        self.page.wait_for_timeout(2000)

        # STEP 7: Save
        print("Saving Stock Issue...")

        save_button = self.page.locator(
            "//button[contains(normalize-space(),'SAVE [End]')]"
        )

        save_button.wait_for(
            state="visible",
            timeout=30000
        )

        try:
            save_button.click()
        except Exception:
            # Use force click only if normal click is intercepted
            save_button.click(force=True)

        print("Stock Issue Saved Successfully!")