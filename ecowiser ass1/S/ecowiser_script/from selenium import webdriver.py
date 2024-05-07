from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv


import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_and_submit_form(data1, data2):
    driver = webdriver.Chrome()  
    driver.get("https://www.linkedin.com/login")
    time.sleep(2) 

    input_box1 = driver.find_element(By.ID, "username")
    input_box1.send_keys(data1)

    input_box2 = driver.find_element(By.ID, "password")
    input_box2.send_keys(data2)

    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    time.sleep(5)  

    driver.get("https://www.linkedin.com/search/results/people/?keywords=&origin=GLOBAL_SEARCH_HEADER")

    # for i in range(5):  
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(2)

    profiles = driver.find_elements(By.CLASS_NAME, "search-result__wrapper")
    data = []
    for profile in profiles: 
        try:
            full_name = profile.find_element(By.CLASS_NAME, "actor-name").text
            first_name, last_name = full_name.split(" ", 1)
            data.append({'First Name': first_name, 'Last Name': last_name})
        except Exception as e:
            print("Error:", e)
            continue

    driver.quit()
    return data

def save_to_csv(data):
    with open('linkedin_people_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['First Name', 'Last Name'])
        writer.writeheader()
        for person in data:
            writer.writerow(person)

def main():
    data1 = "enter your gmail"
    data2 = "enter your password"
    scraped_data = fill_and_submit_form(data1, data2)
    save_to_csv(scraped_data)
    print("Data saved to linkedin_people_data.csv")

if __name__ == "__main__":
    main()
