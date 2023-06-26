
# Program for Extracting Chipotle Codes from Twitter during NBA Finals

This program is designed to extract Chipotle codes from tweets posted by @ChipotleTweets during the 2023 NBA Finals. It utilizes Selenium, a web automation framework, to interact with the Twitter website and retrieve relevant tweets. The extracted codes are then sent to the designated Chipotle Number using the Twilio messaging service.

# Prerequisites

Python 3.x
Selenium package (pip install selenium)
ChromeDriver executable for your Chrome version (download from https://chromedriver.chromium.org/downloads)

# Usage

# File 1: chipotle_extractor.py
Ensure that you have the ChromeDriver executable file (e.g., chromedriver) and its path correctly specified in the chrome_driver_path variable.

Modify the username_input.send_keys('aaranguha06') line to input your Twitter username.

Replace password_input.send_keys('**********') with your Twitter account password.

Note: Ensure that you keep your password secure and do not share it.

Adjust the search_phrase variable to match the specific Chipotle code phrase you are looking for. The default is set to "FREE3S".
Save the file.

# File 2: texting_part_twilio.py

No modifications are required for this file as it handles the message sending functionality using Twilio.

# Running the program

Open a terminal or command prompt.

Navigate to the directory containing the two Python files.

Execute the command python chipotle_extractor.py to run the program.

# Additional Notes
The program will log into your Tweetdeck account using the provided credentials and monitor the tweets by @ChipotleTweets during the NBA Finals.

When a tweet containing the specified code phrase is found, the program will save the tweet to a file named FREETHREES_tweets.txt and update the used_codes.txt file.

The Twilio messaging functionality, implemented in texting_part_twilio.py, will then send the extracted codes to the designated Chipotle Number.

Ensure that you have a working internet connection while running the program.

Note that the program includes a delay between checking for new tweets to avoid overwhelming the Twitter servers.

Please exercise caution when using this program, ensuring that you comply with Twitter's terms of service and any relevant legal requirements.