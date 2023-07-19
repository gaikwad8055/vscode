from selenium import webdriver
import pytest
from pobject.login import Login

class Testing:
    baseurl = "https://in.linkedin.com/"
    useremail = "rohitgaikwad9535@gmaol.com"
    userpass = "@abc123"

    def test_linkedin(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseurl)
        self.l = Login(self.driver)
        self.l.enter_email(self.useremail)
        self.l.enter_pass(self.userpass)
        self.l.submit()
        self.driver.close()