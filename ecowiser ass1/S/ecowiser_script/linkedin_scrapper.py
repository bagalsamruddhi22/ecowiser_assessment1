from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time

# Define the web driver (using Chrome in this example)
driver = webdriver.Chrome()  # Ensure you have installed ChromeDriver

# Function to search LinkedIn for a given name and extract the first few results
def search_linkedin(first_name, last_name):
    # Navigate to LinkedIn's search page
    driver.get("https://www.linkedin.com")

    # Wait for the page to load
    time.sleep(10)

    # Login to LinkedIn (requires valid credentials)
    # Note: LinkedIn may block automated logins, consider manual input if required
    # driver.find_element(By.ID, "session_key").send_keys("YOUR_EMAIL")
    # driver.find_element(By.ID, "session_password").send_keys("YOUR_PASSWORD")
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for login to complete (if using login)
    # time.sleep(5)

    # Perform the search for the given name
    search_bar = driver.find_element(By.XPATH, "//input[@aria-label='Search']")
    search_query = f"{first_name} {last_name}"
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(10)

    # Extract the first 10 search results
    results = []
    search_results = driver.find_elements(By.XPATH, "//ul[@class='reusable-search__entity-results-list list-style-none']//li")[:10]

    for result in search_results:
        name = result.find_element(By.XPATH, ".//span[@class='entity-result__title-text t-16']").text
        occupation = result.find_element(By.XPATH, ".//div[@class='entity-result__primary-subtitle t-14 t-black']").text
        location = result.find_element(By.XPATH, ".//div[@class='entity-result__secondary-subtitle t-14 t-black']").text

        # Save the extracted information
        results.append({"Name": name, "Occupation": occupation, "Location": location})

    # Return the results
    return results

# Function to save results to a CSV file
def save_to_csv(results, filename="linkedin_results.csv"):
    keys = results[0].keys()  # Get CSV header from keys
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(results[:5])  # Save only the first 5 results

# Example usage
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

results = search_linkedin(first_name, last_name)
save_to_csv(results)

print("Results saved to 'linkedin_results.csv'")