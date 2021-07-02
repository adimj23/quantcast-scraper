# Quantcast Scraper
# About
Using Selenium and Chrome Driver to automate the collection of demographics information from quantcast.com queries.

Must log in manually before automation kicks in.

# Required Libraries
- selenium
- gspread

# Setting up some constants
Install [ChromeDriver](https://chromedriver.chromium.org/downloads) for the version matching your computer's Chrome browser.
1. Rename `info-template.py` to `info.py`
2. In info.py copy the path of your Chrome Driver installation into DRIVER_PATH
3. Create a Google sheet and copy the name into SHEET_NAME

# Linking your Google Sheet
1. Go to console.cloud.google.com in your browser using your desire Google Account.
2. Create NEW PROJECT. Give it whatever name you like. Click CREATE.
3. Once the project has been created, via the search bar, enable the Google Drive API and Google Sheets API for this project.
4. In the credentials tab, click CREATE CREDENTIALS. Click Service Account and give it whatever name you like. Click CONTINUTE and DONE.
5. For this new service account, click on the pen and click ADD KEY > CREATE NEW KEY > JSON. Save this file in the folder as this app.
6. Rename this file to "creds.json"
7. In Google Drive, create and title a new Google Sheet. You will need this name later.
8. Open creds.json and copy the "client_email" value and share your Sheet with this email.

# Assumptions Made/Possible errors
- Did not thoroughly test handling if the query has no exact matches
- Did not account for queries that might result in "Not Enough Data"
- Possible bugs if 'NaN' is a result for certain data points
- Using implicit waits (`time.sleep`) for now, may need to change to explicit waits

