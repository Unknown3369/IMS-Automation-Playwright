from Pages.Login import Login



def test_login_to_ims(page,config_data):
   print("\n==========Login Test==========\n")

   login_page = Login(page)
   login_page.perform_login(config_data)

   print("Login process completed.")

def verify_login(self):
   current_url = self.page.url

   if "#/pages/dashboard" in current_url:
      print(f"Test Successful, tested on {current_url}")
   else:
      print(f"Login failed or unexpected URL: {current_url}")

   


