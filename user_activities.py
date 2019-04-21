'''
This file contains all the user activities in flipkart like login, signup, searching a product, adding to cart etc.
According to the test case need, new user functionality can be added in the file
'''

import callhub_phonebook.common_functions as cf
import callhub_phonebook.logger_file as logger
import time

import sys
import callhub_phonebook.common_elements as ce

log=logger.set_log("user_activities")

#This function is for user login through username and password
def user_login(browser,username,password):
    try:
        login_key=browser.find_element_by_xpath(ce.login_key_element)
        cf.click_element(login_key)
        log.info("Login button is clicked")
        #Sending username
        element_user=browser.find_element_by_id(ce.username_element)
        cf.send_inputs(element_user, username)
        #Clicking next button
        next_btn=browser.find_element_by_id(ce.next_btn_element)
        cf.click_element(next_btn)
        time.sleep(3)
        #Sending password
        try:
            element_password=browser.find_element_by_id(ce.password_element)
            cf.send_inputs(element_password, password)
        except Exception as e:
            log.error("Username is not valid")
            log.error(str(e))
            sys.exit()
        login_btn=browser.find_element_by_id(ce.login_btn_element)
        cf.click_element(login_btn)
        time.sleep(5)
        log.info("Login is successful. Continue...")
    except Exception as e:
        log.error("Login is not successful")
        log.error(str(e))

#This function is for selecting elements from left panel of the web site
def select_left_panel_option(browser,find_by,option):
    if option=="Phonebook":
        phonebook_element=cf.find_an_element(browser, find_by, ce.phonebook_btn_element)
        cf.click_element(phonebook_element)
        log.info("Phonebook is selected")
    else:
        log.error("element is not present on left panel")
        sys.exit()

#This function is for creating a phonebook
def create_phonebook(browser,phonebook_name):
    try:
        new_phonebook=browser.find_element_by_partial_link_text(ce.new_phonebook_element)
        cf.click_element(new_phonebook)
        time.sleep(3)
        phonebook_name_elem=browser.find_element_by_name(ce.phonebook_name_element)
        phonebook_name_elem.send_keys(phonebook_name)#"CallHub QA Test"
        add_btn_element=browser.find_element_by_id(ce.add_phonebook_element)
        cf.click_element(add_btn_element)
        time.sleep(5)
        log.info("Phone book is created successfully")
    except Exception as e:
        log.error("Creating phonebook is not successful")
        log.error(str(e))

#This function is for searching a phonebook with name
def search_for_phonebook(browser, search_key):
    try:
        search=browser.find_element_by_xpath(ce.search_box_element)
        cf.send_inputs(search, search_key)
        time.sleep(5)
        log.info(search_key+" is found")
    except Exception as e:
        log.error(search_key+" is not found")
        log.error(str(e))

#This function is for clicking on add contact button
def add_contacts(browser):
    try:
        add_btn_element=browser.find_element_by_xpath(ce.add_contact_icon_element)
        cf.click_element(add_btn_element)
        time.sleep(5)
        log.info("Add contact button is clicked")
    except Exception as e:
        log.error("Add contact is not clicked")
        log.error(str(e))
 
#This function is for adding a contact in phonebook      
def user_information(browser,firstname,phonenumber,tag=None):
    try:
        firstname_element=browser.find_element_by_name(ce.firstname_element)
        phonenumber_element=browser.find_element_by_name(ce.number_element)
        
        cf.send_inputs(firstname_element, firstname)
        
        time.sleep(2)
        cf.send_inputs(phonenumber_element,phonenumber)
        
        time.sleep(2)
        if tag is not None:
            
            tag_element=browser.find_element_by_xpath(ce.tag_element)
            cf.send_inputs(tag_element,tag)
            time.sleep(3)
            #browser.send_keys(Keys.ENTER)
            select_tag=browser.find_element_by_xpath(ce.select_tag_element)
            select_tag.click()
    
        add_contact_btn=browser.find_element_by_id(ce.save_contact_btn_element)
        cf.execute_script_element(browser, add_contact_btn)
        time.sleep(5)
        log.info(firstname+ " is added successfully")
    except Exception as e:
        log.error(firstname+" is not added")
        log.error(str(e))
        
