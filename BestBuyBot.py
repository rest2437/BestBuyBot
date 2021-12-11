import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()  # if using firefox, comment out this line
# driver = webdriver.Firefox()

# # uncomment next line and insert a new link to test a product with a good yellow "add to cart" button
# driver.get('PASTE_TEST_LINK_HERE')

# # website to scalp from (12/07/2021 PS5 link)
# driver.get(
#     'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')

foundButton = False

while not foundButton:

    addToCartButton = addButton = driver.find_element(
        By.CLASS_NAME, 'add-to-cart-button')

    if('c-button-disabled' in addToCartButton.get_attribute('class')):

        # refresh time (default is 3 seconds, you can change it but be careful that the page deosnt crash)
        time.sleep(3)
        driver.refresh()
    else:
        foundButton = True

addToCartButton.click()
