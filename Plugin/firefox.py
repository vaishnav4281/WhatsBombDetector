from selenium import webdriver

# Replace with the path to your Firefox driver executable
driver_path = '/path/to/geckodriver'

# Create a Firefox driver instance
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')  # Optional, to run Firefox in headless mode
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)

# Use the driver to automate Firefox
driver.get('https://www.google.com/')
search_box = driver.find_element_by_name('q')
search_box.send_keys('Selenium Firefox')
search_box.submit()

# Close the browser window
driver.quit()

