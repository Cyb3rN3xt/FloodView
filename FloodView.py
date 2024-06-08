from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

def visit_website(url):
    # Define a list of user agents to simulate different browsers
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
    ]

    # Set up the WebDriver with a random user agent
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents)}")
    driver = webdriver.Chrome(options=options)

    try:
        # Open the website
        driver.get(url)
        
        # Simulate human-like behavior (scrolling, clicking, etc.)
        for _ in range(random.randint(3, 5)):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(1, 3))

        # Close the browser window
        driver.quit()
        print("Visited:", url)

    except Exception as e:
        print("Error:", e)
        driver.quit()

if __name__ == "__main__":
    website_url = input("Enter the website URL you want to boost traffic for: ")
    visit_website(website_url)
