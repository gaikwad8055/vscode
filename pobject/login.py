from selenium import webdriver
from selenium.webdriver.common.by import By
class Login:
    user_email_id = "session_key"
    user_pass_id = "session_password"
    user_click = "//button[@type='submit']"

    def __int__(self,driver):
        self.driver=driver


    def enter_email(self,username):
        self.driver.find_element(By.ID,"user_email_id").send_keys(username)

    def enter_pass(self,password):
        self.driver.find_element(By.ID," user_pass_id").send_keys(password)


    def submit(self,username):
        self.driver.find_element(By.XPATH,"user_click").click()


