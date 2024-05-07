from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Initialize the web driver (ensure the appropriate WebDriver is installed)
driver = webdriver.Chrome()

# Function to search LinkedIn and extract relevant results
def search_linkedin(first_name, last_name):
    try:
        # Navigate to LinkedIn's homepage
        driver.get("https://www.linkedin.com")

        # Fixed wait to allow for page load
        time.sleep(5)  # Increase wait time to ensure full load

        # Perform a search
        search_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search']"))
        )

        search_query = f"{first_name} {last_name}"
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)

        # Wait for search results to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='reusable-search__entity-results-list list-style-none']//li"))
        )

        # Extract relevant search results
        results = []
        search_results = driver.find_elements(By.XPATH, "//ul[@class='reusable-search__entity-results-list list-style-none']//li")[:5]

        for result in search_results:
            try:
                name = result.find_element(By.XPATH, ".//span[@class='entity-result__title-text t-16']").text
                occupation = result.find_element(By.XPATH, ".//div[@class='entity-result__primary-subtitle t-14 t-black']").text
                location = result.find_element(By.XPATH, ".//div[@class='entity-result__secondary-subtitle t-14 t-black']").text
                results.append({"Name": name, "Occupation": occupation, "Location": location})
            except Exception as e:
                print("Error extracting search result:", e)

        return results

    except selenium.common.exceptions.TimeoutException as e:
        # Capture a screenshot to help debug the timeout
        driver.save_screenshot("timeout_screenshot.png")
        print("TimeoutException occurred:", e)
        return []

# Function to save results to a CSV file named "result.csv"
def save_to_csv(results):
    if not results:
        print("No results to save.")  # Handle empty results
        return

    # Write the results to a CSV file
    keys = results[0].keys()  # Use keys from the first result as the CSV header
    with open("result.csv", "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()  # Write the CSV header
        dict_writer.writerows(results)  # Write the results

    print("Results saved to 'result.csv'.")

# User input for first and last names
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

# Get LinkedIn search results and save them to "result.csv"
results = search_linkedin(first_name, last_name)
save_to_csv(results)

# Ensure the WebDriver is closed to avoid resource leakage
driver.quit()