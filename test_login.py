from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

# Path to the WebDriver executable (replace with your actual path)
webdriver_path = 'C:\chromedriver\chromedriver.exe'

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode

# Create a WebDriver instance (for Chrome)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# Navigate to the login page
driver.get('https://ca.lorealpartnershop.com/en/login/')

# Find the username and password fields and enter your credentials
username_field = driver.find_element(By.CLASS_NAME, "username .accountnumber")
username_field.send_keys('david@cosmeticworld.ca')  # Replace 'your_username' with your actual username

password_field = driver.find_element(By.CLASS_NAME,'password .input-text')
password_field.send_keys('Loreal123!')  # Replace 'your_password' with your actual password

remember_me = driver.find_element(By.NAME, "dwfrm_login_rememberme")

driver.execute_script("arguments[0].click();", remember_me)

# Submit the login form
login_button = driver.find_element(By.NAME,'dwfrm_login_login')
login_button.click()

# Retrieve cookies
cookies = driver.get_cookies()

for cookie in cookies:
    if cookie['name'] == 'dwsid':
        print(cookie['value'])
