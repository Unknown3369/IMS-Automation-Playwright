class Login:

    def __init__(self, page):
        self.page = page

        self.username = "//input[@placeholder='Username']"
        self.password = "//input[@placeholder='Password']"
        self.login_button = "//button[contains(text(), 'Login')]"
        self.logout_button = (
            "//button[contains(@class,'mat-flat-button') "
            "and .//span[normalize-space()='Sign out']]"
        )

    def perform_login(self, config_data):

        self.page.goto(config_data["url"])

        username_box = self.page.locator(self.username)
        username_box.wait_for(state="visible", timeout=35000)
        username_box.fill(config_data["username"])

        password_box = self.page.locator(self.password)
        password_box.wait_for(state="visible", timeout=35000)
        password_box.fill(config_data["password"])

        login_btn = self.page.locator(self.login_button)
        login_btn.wait_for(state="visible", timeout=35000)
        login_btn.click()

        print("Login button clicked!")

        self.page.wait_for_timeout(6000)

        try:
            popup_logout_btn = self.page.locator(self.logout_button)
            popup_logout_btn.wait_for(state="visible", timeout=5000)
            popup_logout_btn.click()

            print("Detected previous session popup and clicked Logout.")

            self.page.wait_for_timeout(2000)

            login_btn = self.page.locator(self.login_button)
            login_btn.wait_for(state="visible", timeout=20000)
            login_btn.click()

            print("Login button re-clicked!")

        except Exception:
            print("No previous session popup detected.")