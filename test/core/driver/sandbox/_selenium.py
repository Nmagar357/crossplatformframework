from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.platform_name = 'mac'
options.page_load_strategy = 'normal'
options.accept_insecure_certs = True
options.add_argument("--window-size=1080,1920")

driver = webdriver.Chrome(options=options)
print("Connection to server successful! Loading Website URL...")

print("Opening URL...")
driver.get("https://www.nytimes.com")