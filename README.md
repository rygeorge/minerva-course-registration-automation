# Minerva Course Registration Automation
- A Course Registration Bot for McGill University's Minerva platform 

# Housekeeping: 
Before using the script, ensure that the correct chromedriver is installed. In a Chrome tab, go to _Settings_ > _About Chrome_ and verify that the version of your chrome is the same version as your chromedriver. 

# Setting up the CSV 
The CSV has three columns, the first is the course code where you can put the 7 character class code found on visual schedule builder. This is mainly for organization, as you may move numbers around when attempting to adjust your schedule. The second column is the Course Registration Number (CRN), this is also found in VSB and is what Minerva needs from you to add/drop a course. The last column is the CRN_id, this is for the script to know where to place the CRN numbers on the website. **DO NOT DELETE** the CRN_id column, otherwise the script **WILL NOT** work. 

# Note on Login Information: 
To avoid any issues with security, the script will prompt you to put in your login information in the command console. It does not store any passwords or sensitive information, as you can see in the source code itself, however feel free to modify the script on your end if you would like to "hard-code" your user info to each of the respective variables. 

# Warning:
**This was developed for educational purposes, please use the script responsibly. Thanks and enjoy! :)**
