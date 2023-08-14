#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver

path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
CHROME_PATH = path  # Replace this with the path to your chrome.exe
options = webdriver.ChromeOptions()
options.binary_location = CHROME_PATH
options.add_argument("--headless")  # to run in headless mode

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()