from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import re
from time import sleep

used_codes_file = 'used_codes.txt'
with open(used_codes_file, 'r', encoding='utf-8') as file:
    used_codes = file.read().splitlines()

chrome_driver_path = '/Users/aguha2021/Desktop/chromedriver_mac_arm64/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get('https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJoaWRlX21lc3NhZ2UiOiJ0cnVlIiwicmVkaXJlY3RfYWZ0ZXJfbG9naW4iOiJodHRwczovL3R3ZWV0ZGVjay50d2l0dGVyLmNvbS8%2FdmlhX3R3aXR0ZXJfbG9naW49dHJ1ZSJ9%22%7D')
    sleep(5)  # Wait for the page to load

    # Step 1: Enter username
    try:
        username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="text"]')
        username_input.send_keys('aaranguha06') #follow me :)
        username_input.send_keys(Keys.RETURN)
        sleep(5)  # Wait for the next screen to load
    except Exception as e:
        print("Failed to locate the username input field.")
        print(e)

    # Step 2: Enter password
    try:
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys('**********') #cant show for safety reasons 
        password_input.send_keys(Keys.RETURN)
        sleep(5)  # Wait for the login process to complete
    except Exception as e:
        print("Failed to locate the password input field.")
        print(e)

    # Wait for the page to load after login
    sleep(2)

    print('Start')

    while True:
        print('Waiting for new tweets...')

        try:

            # Retrieve the tweets from the timeline
            tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

            # Specify the phrase to search for
            #search_phrase = "FREE3S"
            search_phrase = "FREE3S" 
            #--old one

            # Filter tweets based on the specified phrase
            matching_tweets = []
            for tweet in tweets:
                try:
                    tweet_text = tweet.text
                    if search_phrase in tweet_text:
                        matching_tweets.append(tweet_text)
                except StaleElementReferenceException:
                    continue


            if len(matching_tweets) > 0:
                # Save matching tweets to a text file
                with open('chipotle_tweets.txt', 'w', encoding='utf-8') as file:
                    for tweet in matching_tweets:
                        file.write(tweet)
                        file.write('\n')

                # Open 'chipotle_tweets.txt' file for reading
                with open('chipotle_tweets.txt', 'r', encoding='utf-8') as file:
                   
                    content = file.read()

                # Use regex pattern to extract strings starting with "FREETHREES" followed by alphanumeric characters
                #pattern = r'\W*\w*FREE3S\b'
                pattern = r'\bFREE[A-Z0-9$]+\b' 
                #--old regex pattern

                matching_tweets = re.findall(pattern, content)

                # Read the used codes from the file
                used_codes_file = 'used_codes.txt'
                with open(used_codes_file, 'r', encoding='utf-8') as file:
                    used_codes = file.read().splitlines()

                # Print the extracted matching tweets
                for tweet in matching_tweets:
                    if tweet not in used_codes:
                        print(tweet)

                # Save matching tweets to 'FREETHREES_tweets.txt' file
                with open('FREETHREES_tweets.txt', 'w', encoding='utf-8') as freethrees_file, open('used_codes.txt', 'a',
                                                                                                    encoding='utf-8') as used_codes_file:
                    for tweet in matching_tweets:
                        if tweet not in used_codes:
                            freethrees_file.write(tweet)
                            freethrees_file.write('\n')
                            used_codes_file.write(tweet)
                            used_codes_file.write('\n')
                            used_codes.append(tweet)

                file_path = 'FREETHREES_tweets.txt'
                from texting_part_twilio import send_messages_from_file
                send_messages_from_file(file_path)

        except Exception as e:
            print("An error occurred:", e)

        # Wait for a few seconds before checking for new tweets again
        sleep(1.5)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser window
    driver.quit()

