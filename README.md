# Facebook Group Manager
### Overview

Facebook Group Manager is an app that allows you to automate repetitive tasks in your Facebook group.

  - Approve "pending users"
  - Write a welcome message to new users
  - Invite fans/friends to join your group
  - Get daily mail with number of sent invitations

### Installation
Facebook Group Manager requires [ Python 3.6](https://www.python.org/) + to run.

Download [ Chromedriver ](https://chromedriver.chromium.org/downloads) (or any other driver), uzip file and copy into ```fb_manager/fbm/driver```.

Install required dependencies.

```sh
$ pip install -r requirements.txt
```

In ```app.py``` insert your configuration data like Gmail etc. 
You can specify the headless option of webdriver (useful for debugging).

Run the app with this commend. 

```sh
$ python -m fbm
```
