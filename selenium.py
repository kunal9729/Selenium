from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize webdriver (Ensure chromedriver is in PATH or provide path here)
driver = webdriver.Chrome()

# Step 1: Open amazon.in
driver.get("https://www.amazon.in")

# Step 2: Search for "LG soundbar"
search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys("LG soundbar")
search_box.send_keys(Keys.RETURN)

# Wait for page to load
time.sleep(3)

# Step 3: Scrape product names and prices from the first search result page
product_elements = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
price_elements = driver.find_elements_by_xpath("//span[@class='a-price-whole']")

# Dictionary to store product names and their prices
product_price_dict = {}

# Step 4: Store product names and prices in a dictionary
for i in range(len(product_elements)):
    product_name = product_elements[i].text
    try:
        # Get the price and convert to int, handle missing prices
        product_price = int(price_elements[i].text.replace(',', ''))
    except (IndexError, ValueError):
        product_price = 0  # If price not available or invalid, consider as zero

    # Store in the dictionary
    product_price_dict[product_name] = product_price

# Step 5: Sort products by price
sorted_products = sorted(product_price_dict.items(), key=lambda x: x[1])

# Step 6: Print sorted product list
for product, price in sorted_products:
    print(f"{price} {product}")

# Close the browser
driver.quit()
