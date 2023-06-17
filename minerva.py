import selenium as se
import time
import os
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass

# Enter the term you want to register for
term = input('Enter the term you want to register for (ex. Fall 2023): ')

crn_file = pd.read_csv('CRN.csv')
crn_values = crn_file['CRN'].tolist()

crn_list = crn_file['crn_id'].tolist()


# Enter your username and password
login_username = input('Enter your username: ') 
login_password = getpass('Enter your password: ') 

# Path to the chromedriver executable
chromedriver = r"C:\Users\Documents\chromedriver_win32"

# Set up the driver 
driver = webdriver.Chrome()

try:
    # URL to the Minerva login page
    url = "https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin"

    # Navigate to the login page
    driver.get(url)

    # Wait for the page to load
    time.sleep(2)

    # Find the username and password fields
    username = driver.find_element(By.XPATH,"//*[@id=\"mcg_un\"]")
    password = driver.find_element(By.XPATH,"//*[@id=\"mcg_pw\"]") 

    # Enter the username and password
    username.send_keys(login_username)
    password.send_keys(login_password)

    time.sleep(2)

    # Find the login button and click it
    login_button = driver.find_element(By.XPATH,"//*[@id=\"mcg_un_submit\"]")
    login_button.click()

    time.sleep(2)

    # Navigate to the registration page
    driver.get("https://horizon.mcgill.ca/pban1/bwskfreg.P_AltPin")

    # Find the term dropdown menu and select the desired term
    # term_dropdown = driver.find_element(By.NAME,"term_in")
    term_dropdown = driver.find_element(By.XPATH,"//*[@id=\"term_id\"]")
    term_dropdown.click()
    term_dropdown.send_keys(term)
    term_dropdown.send_keys(Keys.RETURN)

    # term_dropdown.send_keys("202309") # TODO: Make this dynamic based on the current term (Fall 2023 = 202309) etc.
    time.sleep(5) 

    # Find the submit button and click it
    submit_button = driver.find_element(By.XPATH,"/html/body/div[3]/form/input") # Fix this
    submit_button.click()
    time.sleep(2)

    # Quick-add a course by CRN
    for crn_id, crn_value in zip(crn_list, crn_values):
    # Construct the XPath expression using the CRN ID
        xpath_expression = f"//*[@id='{crn_id}']"

    # Find the element using the XPath expression
        crn = driver.find_element(By.XPATH, xpath_expression)

    # Send the corresponding value to the element
        crn.send_keys(crn_value)

# When done adding courses, click the submit button
    wadd_button = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[19]")
    wadd_button.click()
    

except Exception as e:
    print("An error occurred:", str(e))
    # Add error handling or logging as needed

# Keep the browser window open even if an exception occurs
input("Press Enter to quit...")

# Close the browser window manually when ready
driver.quit()
