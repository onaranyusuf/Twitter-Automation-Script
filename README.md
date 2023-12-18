# Twitter (X) Automation Script

## Overview

This Python script uses Selenium to automate interactions on Twitter (X). It can log in with multiple user accounts, like tweets, retweet, and optionally add comments. The script is designed to perform interactions with a list of specified tweets.

## Features

- Multi-account support
- Like tweets
- Retweet tweets
- Add comments to tweets (optional)
- Logging of activities

## Prerequisites

1. **Python:** Make sure you have Python installed. You can download it [here](https://www.python.org/downloads/).

2. **Selenium:** Install the Selenium library using the following command:
pip install selenium

3. **Webdriver:** Download the appropriate WebDriver for your browser. In this script, Chrome WebDriver is used. You can download it [here](https://sites.google.com/chromium.org/driver/).

## Configuration

1. **User Credentials:**
- Add Twitter usernames and passwords to the `usernames` and `passwords` lists in the script.

2. **Tweet Paths:**
- Specify the URLs of tweets in the `tweet_path` list.

3. **Tweet Interaction Settings:**
- Adjust the variables like `quotes_yes_no`, `quotes_number`, and `retweet_number` based on your preferences.


## Define your usernames, passwords, and tweet paths
```python
usernames = ["your_username1", "your_username2"]
passwords = ["your_password1", "your_password2"]

tweet_paths = [
    "https://twitter.com/example_tweet_path_1",
    "https://twitter.com/example_tweet_path_2",
]
```

## Usage

1. **Run the Script:**
- Execute the script by running the command:

  ```bash
  python TwitterSelenium.py
  ```

2. **Logging:**
- Check the `logs.txt` file for detailed logs of the script's activities.


## Notes

- The script uses Chrome WebDriver by default. Adjust the `webdriver.Chrome()` line if you use a different browser.

## Disclaimer

This script is for educational purposes only. Use it responsibly and be aware of Twitter's terms of service.

## Author

**Yusuf Onaran**
* Github: [@onaranyusuf](https://github.com/onaranyusuf)
* LinkedIn: [@Yusuf Onaran](https://www.linkedin.com/in/yusufonaran/)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/onaranyusuf/Twitter-Automation-Script/blob/main/LICENSE) file for details.

