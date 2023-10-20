# 💰 TrackMyDollar V4.0 - Budget On The Go(BOTGo) 💰


This video shows only the new features and enhancement of some older features. All the other features from phase 3 are working as it is.
<hr>
<p align="center">
<a><img  height=360 width=550 
  src="https://github.com/deekay2310/MyDollarBot/blob/c56b4afd4fd5bbfffea0d0a4aade58596a5cb678/docs/0001-8711513694_20210926_212845_0000.png" alt="Expense tracking made easy!"></a>
</p>
<hr>

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/anuj672/MyDollarBot-BOTGo)](https://github.com/anuj672/MyDollarBot-BOTGo/graphs/contributors)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10023576.svg)](https://doi.org/10.5281/zenodo.10023576)
[![Test and Formatting](https://github.com/anuj672/MyDollarBot-BOTGo/actions/workflows/test.yml/badge.svg)](https://github.com/anuj672/MyDollarBot-BOTGo/actions/workflows/test.yml)
<!-- [![codecov](https://codecov.io/gh/sak007/MyDollarBot-BOTGo/branch/main/graph/badge.svg?token=5AYMR8MNMP)](https://codecov.io/gh/sak007/MyDollarBot-BOTGo) -->
[![GitHub issues](https://img.shields.io/github/issues/bhaveshittadwar/csc-510-se-group-49)](https://github.com/bhaveshittadwar/csc-510-se-group-49/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/bhaveshittadwar/csc-510-se-group-49)](https://github.com/bhaveshittadwar/csc-510-se-group-49/issues?q=is%3Aissue+is%3Aclosed)
![Fork](https://img.shields.io/github/forks/anuj672/MyDollarBot-BOTGo)

<hr>

## About TrackMyDollar

TrackMyDollar is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle 
With simple commands, this bot allows you to:
- Add/Record a new spending
- Show the sum of your expenditure for the current day/month
- Display your spending history
- Clear/Erase all your records
- Edit/Change any spending details if you wish to
- Add a recurring expense 
- User can add a new category and delete an existing category 
- User can see the budget value for the total expense 
- Added pie charts, bar graphs with and without budget lines 
- Deployment on GCP 

## What's new? (From Phase 3 to Phase 4)

- Email Transaction History: Users can request their complete transaction history via email for easy access and record-keeping.
- CSV Transaction History Extraction: Users can download their transaction history in CSV format, providing a versatile data export option for analysis.
- Receipt Management: Users can upload and retrieve receipts for specific transactions by date, simplifying expense tracking and documentation.
- Transaction Limit Notifications: Users can set transaction limits and receive alerts when expenses exceed the specified limits, helping them stay within budget.
- Github Actions Automation: Automated testing, code formatting, and syntax checks have been implemented through Github Actions. A minimum 80% code coverage is required for successful builds, ensuring code quality and testing standards are maintained.


## What more can be done?
Please refer to the issue list available [here](https://github.com/anuj672/MyDollarBot-BOTGo/issues) to see what more can be done to make MyDollarBot better. Please refer to the MyDollarBot project present [here](https://github.com/bhaveshittadwar/csc-510-se-group-49/projects) to have a look at the tasks done or in progress

## Demo

https://user-images.githubusercontent.com/72677919/140454147-f879010a-173b-47b9-9cfb-a389171924de.mp4

## Installation guide

The below instructions can be followed in order to set-up this bot at your end in a span of few minutes! Let's get started:

1. Clone this repository to your local system.

2. Start a terminal session in the directory where the project has been cloned. Run the following command to install the required dependencies:
```
  pip install -r requirements.txt
```

3. In Telegram, search for "BotFather". Click on "Start", and enter the following command:
```
  /newbot
```
Follow the instructions on screen and choose a name for your bot. After this, select a username for your bot that ends with "bot".

4. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy and save this token for future use.

5. Copy the token provided by the bot and add/replace it in the user.properties file (in the format api_token=<your_token>).

6. In the directory where this repo has been cloned, please run the below command to execute a bash script to run the Telegram Bot:
```
   ./run.sh
```
(OR)
```
   bash run.sh
```

(Please Note: You may require to run `chmod +x run.sh` on mac/linux)

A successful run will generate a message on your terminal that says "TeleBot: Started polling." 

7. In the Telegram app, search for your newly created bot by entering the username and open the same. Now, on Telegram, enter the "/start" or "/menu" command, and you are all set to track your expenses!

## Testing

We use pytest to perform testing on all unit tests together. The command needs to be run from the home directory of the project. The command is:
```
python -m pytest test/
```

## Code Coverage

Code coverage is part of the build. Every time new code is pushed to the repository, the build is run, and along with it, code coverage is computed. This can be viewed by selecting the build, and then choosing the codecov pop-up on hover.

Locally, we use the coverage package in python for code coverage. The commands to check code coverage in python are as follows:

```
coverage run -m pytest test/
coverage report
```

Please note: A coverage below 80% will cause the build to fail.

## Notes:
You can download and install the Telegram desktop application for your system from the following site: https://desktop.telegram.org/


<hr>
<p>Title:'Track My Dollar'</p>
<p>Version: '4.2'</p>
<p>Description: 'An easy to use Telegram Bot to track everyday expenses'</p>
<p>Authors(Iteration 4):'Anuj, Bhavesh, Jash, Vaibhavi'</p>
<p>Authors(Iteration 3):'Vraj, Alex, Leo, Prithvish, Seeya'</p>
<p>Authors(Iteration 2):'Athithya, Subramanian, Ashok, Zunaid, Rithik'</p>
<p>Authors(Iteration 1):'Dev, Prakruthi, Radhika, Rohan, Sunidhi'</p>
