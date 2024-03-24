import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Make example the chromedriver is installed
chromedriver_autoinstaller.install()

# Create a ChromeOptions object
chrome_options = Options()

# Add an experimental option to the ChromeOptions object
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Create a new Chrome webdriver instance with the ChromeOptions object
driver = webdriver.Chrome(options=chrome_options)  
