from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import time

def getQuery():
    print("Welcome to the shop bot!")
    print("Opening Chrome browser to Kith.com")
    print("What is the exact item name you would like to buy?")
    print("replace spaces between words with - ")
    # Get search input
    item = input("Search for: ")
    automate(item)

def automate(item):
    
    # Get response code - Should return 200
    url = driver.current_url
    resp = requests.get(url, timeout = 4)
    driver.get('https://shop.havenshop.com/products/' + item)
    resp2 = requests.get(url, timeout = 4)
    if (resp2 == 404):
        print("The item you are looking for does not exist, please try again")
        break
    else:
        itemPage()

def itemPage():
    # Land on product page
    select_box = driver.find_element_by_id("product-select")
    options = [x for x in select_box.find_elements_by_tag_name("option")]
    
    # Size select
    for element in options:
        print (element.text + "   id:    " + element.get_attribute("value") + "\n")
    print("Available size list")
    size = input("Enter the ID of your size to purchase: ")
    
    # Select Size and purchase
    select_box.click()
    driver.find_element_by_id("variant-" + size).click()
    
    # Confirm Purchase
    print("Buy? This action will complete checkout and confirm purchase")
    confirm = input('Y for Yes | N for No: ')
    if (confirm == "Y"):
        print("Adding to bag and going to checkout")
        driver.find_element_by_id("AddToCart").click()
        # Delay checkout for load
        time.sleep(1)
        checkout()
    elif(confirm == "N"):
        print("Thank you for using Kith Bot")
    else:
        print("Please enter Y or N")

def checkout():
    print("proceeding to checkout")
    driver.get("https://shop.havenshop.com/cart")
    driver.find_element_by_name("checkout").click()
    # Order 
    time.sleep(1)
    order()

def order():
    driver.find_element_by_id("checkout_email").send_keys(keys['email'])
    driver.find_element_by_id("checkout_shipping_address_first_name").send_keys(keys['first_name'])
    driver.find_element_by_id("checkout_shipping_address_last_name").send_keys(keys['last_name'])
    driver.find_element_by_id("checkout_shipping_address_address1").send_keys(keys['address'])
    driver.find_element_by_id("checkout_shipping_address_city").send_keys(keys['city'])
    driver.find_element_by_id("checkout_shipping_address_zip").send_keys(keys['postal_code'])
    driver.find_element_by_id("checkout_shipping_address_phone").send_keys(keys['phone'])
    print("Please click the recaptcha button on checkout")
    bot_check = input("Type Y once clicked: ")
    if (bot_check == "Y"):
        driver.find_element_by_class_name("step_footer_continue-btn btn").click()
    time.sleep(1)
    driver.find_element_by_class_name("step_footer_continue-btn btn").click()
    paymenr()

def payment():
    driver.find_element_by_id("number").send_keys(keys['card_number'])
    driver.find_element_by_id("name").send_keys(keys['card_name'])
    driver.find_element_by_id("expiry").send_keys(keys['card_expiry'])
    driver.find_element_by_id("verification_value").send_keys(keys['card_cvv'])
    print("Completing Order")
    driver.find_element_by_class_name("shown-if-js").click()




if __name__ == '__main__':
    # Load chrome
    driver = webdriver.Chrome('./chromedriver/chromedriver')
    driver.get("https://shop.havenshop.com/")
    getQuery()