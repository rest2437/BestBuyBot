# To Install the Best Buy Bot

## Clone this Repo to your machine.

- link
- Open in VScode.

---

## Is Python installed?

### No:

- Please reference the Python documentation for installing Python.

### Yes:

- Move onto the next step.

---

### Install Selenium.

- 1. Open the VScode built in terminal.
- 2. install selenium using "pip3 install selenium" or if you are using an older
     version of python use "pip install selenium".

---

### Download web driver for Chrome. If using Firefox, please see next step

- 1. Find out which version of chrome you are using by typing "chrome://version" in your chrome search bar.
- 2. If you are using Chrome version 97, please download [ChromeDriver 97.0.4692.36](https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.36/)
- 3. If you are using Chrome version 96, please download [ChromeDriver 96.0.4664.45](https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/)
- 4. If you are using Chrome version 95, please download [ChromeDriver 95.0.4638.69](https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.69/)
- 5. Once it appears in your downloads folder, extract the zip file and move the "chromedriver" file from the downloads
     folder to the "/usr/local/bin" PATH.

---

### If you are using Firefox

- 1. Download Geckodriver which can be found [here](https://github.com/mozilla/geckodriver/releases)
- 2. Based on your CPU model, the file will either be [geckodriver-v0.30.0-macos-aarch64.tar.gz](https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-macos-aarch64.tar.gz) or [geckodriver-v0.30.0-macos.tar.gz](https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-macos.tar.gz)
- 3. Once it appears in your downloads folder, extract the zip file and move the "geckodriver" file from the downloads
     folder to the "/usr/local/bin" PATH.
- 4. Comment out line 8
- 5. Uncomment line 9

### Test program

- 1. Locate an item on best buys webpage that is in stock and copy the items link.
- 2. In BestBuyBot.py, locate the comment on line 11 that reads "driver.get('PASTE_TEST_LINK_HERE')" and paste a the copied link there.
- 3. Uncomment line 12
- 4. Save the file
- 5. Run the scrypt by pressing the play button on the upper right corner of the screen.
- 6. If everything works fine, comment out line 11 and uncomment lines 15 and 16 that are preset to PS5

---

### Notes

- If you wish to buy a different item on Best Buys Website, you can locate the item and paste the link in.
- THIS BOT WILL ONLY ADD THE ITEM TO THE CART. IT WILL NOT BUY THE ITEM FOR YOU.
- If you do not know how to Uncomment or Comment out items, click on the line number and press "command and /"

---

### Stretch Global

- I want this bot to eventually be able to go through with the purchase and input the customers info.
