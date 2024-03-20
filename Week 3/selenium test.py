from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

try:
    driver.get("https://www.gitam.edu/")

    # Find all the links on the page
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        url = link.get_attribute("href")
        if url:
            # Send a HTTP HEAD request to check the link
            response = requests.head(url)
            if response.status_code == 200:
                print(f"Link {url} is working")
            else:
                print(f"Link {url} is broken (HTTP {response.status_code})")

except Exception as e:
    print(f"An error occurred: {e}")