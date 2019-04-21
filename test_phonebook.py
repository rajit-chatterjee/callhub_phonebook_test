'''
This is the test case file of the given feature
Testcase steps:
Create a phonebook with name 'CallHub QA Test'
Add 2 contacts to this phonebook
Add a tag 'testing' to one of the contacts in this phonebook
Prerequisite:
Create a tag named 'testing' manually. This part is not automated
'''


import callhub_phonebook.common_functions as cf
import callhub_phonebook.featureconfig as fc
import callhub_phonebook.user_activities as ua
import unittest

class test_callhub(unittest.TestCase):
    def test_callhub_phonebook(self):
        browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))
        #Opening the URL
        cf.go_to_url(browser, fc.browser_details.get("url"))
        #login to the account
        ua.user_login(browser, fc.user_login_details.get("username"),fc.user_login_details.get("password"))
        #Selecting phonebook from the left panel
        ua.select_left_panel_option(browser, fc.find_element_by.get("linktext"), fc.left_panel_element.get(1))
        #Creating phonebook
        ua.create_phonebook(browser, fc.phone_book_details.get("name"))
        #Searching for created phonebook
        ua.search_for_phonebook(browser, fc.phone_book_details.get("name"))
        #Click on add contact button
        ua.add_contacts(browser)
        #Adding user into phonebook and save
        ua.user_information(browser, fc.contact_info_1.get("firstname"), fc.contact_info_1.get("phonenumber"), fc.contact_info_1.get("tag"))
        #Click on add contact button
        ua.add_contacts(browser)
        #Adding user into phonebook and save
        ua.user_information(browser, fc.contact_info_2.get("firstname"), fc.contact_info_2.get("phonenumber"))
        #Terminate the execution
        browser.quit()