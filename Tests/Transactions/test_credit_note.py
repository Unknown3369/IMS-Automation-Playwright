from Pages.Login import Login
from Pages.Transactions.credit_note import CreditNotePage


def test_generate_credit_note(page,config_data):
   try:
      login_page = Login(page)
      login_page.perform_login(config_data)
   except:
      print("Already Logged In")

   credit_note_page = CreditNotePage(page)
   print("Logged into IMS")
   credit_note_page.navigate_to_credit_note()
   credit_note_page.credit_note_entry()
   credit_note_page.save_credit_note()
   print("Credit Note created successfully")

   
