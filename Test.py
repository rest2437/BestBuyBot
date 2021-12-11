import time

# driver.find_element_by_class_name is no longer supported, so we need to import "By" to use new syntax.
from selenium.webdriver.common.by import By

from selenium import webdriver  # importing selenium

driver = webdriver.Chrome()

# # uncomment next line and insert a new link to test a product with a good yellow "add to cart" button
driver.get('https://www.bestbuy.com/site/nba-2k22-standard-edition-playstation-5/6471713.p?skuId=6471713')

# # website to scalp from (12/07/2021 PS5 link)
# driver.get(
#     'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')

foundButton = False  # saying "if the button i am looking for is false"

while not foundButton:  # if the button is not found

    addToCartButton = addButton = driver.find_element(
        By.CLASS_NAME, 'add-to-cart-button')

    # if the button has btn-disabled in its class name
    if('c-button-disabled' in addToCartButton.get_attribute('class')):

        time.sleep(3)  # wait some time for the button to appear (3 seconds)
        driver.refresh()  # refresh the page
    else:
        foundButton = True

addToCartButton.click()
