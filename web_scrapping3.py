import time
import requests
import urllib.request
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from googleapiclient.discovery import build
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import googleapiclient.discovery




'''
1. Write a python program which searches all the product under a particular product from www.amazon.in. The 
product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for 
guitars.'''

def search_amazon_products(search_query):
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.in/')

    # Find the search input field and enter the search query
    search_input = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
    search_input.send_keys(search_query)
    search_input.submit()
    time.sleep(3)
    

    
        
    

    # Close the browser
    driver.quit()

# Prompt the user for input
userinput = input('Enter the product to search on Amazon.in: ')

# Call the function to search for products
search_amazon_products(userinput)





'''
2.In the above question, now scrape the following details of each product listed in first 3 pages of your search 
results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then 
scrape all the products available under that product name. Details to be scraped are: "Brand 
Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
“Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. '''

# Set up Selenium webdriver
driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')
# Function to scrape product details from a single page
def scrape_page():
    product_details = []
    product_elements = driver.find_elements(By.XPATH, '//div[@class="product"]')

    for product_element in product_elements:
        try:
            brand_name = product_element.find_element_by_class_name('brand').text.strip()
            product_name = product_element.find_element_by_class_name('name').text.strip()
            price = product_element.find_element_by_class_name('price').text.strip()
            exchange = product_element.find_element_by_class_name('exchange').text.strip()
            expected_delivery = product_element.find_element_by_class_name('delivery').text.strip()
            availability = product_element.find_element_by_class_name('availability').text.strip()
            product_url = product_element.find_element_by_class_name('product_url').text.strip()
            
        
            product_details.append({
            brand_name, product_name, price, exchange, expected_delivery, availability, product_url})
        except NoSuchElementException:
            product_details.append('-')   

    return product_details

# Function to scrape details from multiple pages
def scrape_pages():
    base_url = 'https://www.amazon.in/s?k=guitar&i=electronics&rh=n%3A1389401031&qid=1687546024&ref=sr_pg_'
    num_pages = 3
    all_product_details = []

    for page in range(1, num_pages+1):
        url = base_url + str(page)
        driver.get(url)
        time.sleep(3)  # Add a delay to allow the page to load
        
        product_details = scrape_page()
        all_product_details.extend(product_details)

    return all_product_details

# Scrape the pages and store the data in a DataFrame
product_data = scrape_pages()
df = pd.DataFrame(product_data)

# Replace missing values with "-"
df.fillna('-', inplace=True)

# Save the DataFrame to a CSV file
df.to_csv('product_details.csv', index=False)

# Quit the browser
driver.quit()




'''
3. Write a python program to access the search bar and search button on images.google.com and scrape 10 
images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. '''


# Set up Selenium webdriver
driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
for _ in range(10):
    driver.execute_script('')
#driver.maximize_window()

# Define the list of keywords
keywords = ['fruits', 'cars', 'Machine Learning', 'Guitar', 'Cakes']

# Function to search for images and scrape them
def scrape_images(keyword):
    # Navigate to Google Images
    driver.get('https://images.google.com/')
    time.sleep(3)  # Add a delay to allow the page to load
    
    # Scroll to the end of the page to load more images'''
    for _ in range(3):
        driver.execute_script('window.scrollBy(0, 100)')#document.body.scrollHeight)')
        time.sleep(2)  # Add a delay to allow the page to load
    
    # Find all the image elements on the page
    image_elements = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
    
    # Create a directory for the keyword if it doesn't exist
    if not os.path.exists(keyword):
        os.makedirs(keyword)
    
    # Download and save the images
    for i, image_element in enumerate(image_elements[:10]):
        # Get the image source URL
        image_url = image_element.get_attribute('src')
        
        # Save the image to disk
        file_name = f'{keyword}/{keyword}_{i+1}.jpg'
        urllib.request.urlretrieve(image_url, file_name)
    
    print(f'Scraped 10 images for "{keyword}"')

# Scrape images for each keyword
for keyword in keywords:
    scrape_images(keyword)

# Quit the browser
driver.quit()



'''
4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand 
Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, 
“Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
details is missing then replace it by “- “. Save your results in a dataframe and CSV. 
'''

# Set up Selenium webdriver
driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/')
# Function to scrape product details from a single page
def scrape_page():
    product_details = []
    product_elements = driver.find_elements(By.XPATH, '//div[@class="product"]')
    for product_element in product_elements:
        try:
            brand_name = product_element.find_element_by_class_name('brand').text.strip()
            smartphone_name = product_element.find_element_by_class_name('name').text.strip()
            price = product_element.find_element_by_class_name('price').text.strip()
            colour = product_element.find_element_by_class_name('colour').text.strip()
            ram = product_element.find_element_by_class_name('ram').text.strip()
            primary_camera = product_element.find_element_by_class_name('primary_camera').text.strip()
            secondary_camera = product_element.find_element_by_class_name('secondary_camera').text.strip()
            display_size = product_element.find_element_by_class_name('display_size').text.strip()
            storage = product_element.find_element_by_class_name('storage').text.strip()
            battery_capacity = product_element.find_element_by_class_name('battery_capacity').text.strip()
            product_url = product_element.find_element_by_class_name('product_url').text.strip()
            
        
            product_details.append({
            brand_name, smartphone_name, price, colour, ram, primary_camera, secondary_camera, display_size, storage, battery_capacity, product_url})
        except NoSuchElementException:
            product_details.append('-')   

    return product_details

# Function to scrape details from multiple pages
def scrape_pages():
    base_url = 'https://www.flipkart.com/search?q={keyword}&page=1'

    all_product_details = []
    url = base_url 
    driver.get(url)
    time.sleep(3)  # Add a delay to allow the page to load
        
    product_details = scrape_page()
    all_product_details.extend(product_details)

    return all_product_details

# Scrape the pages and store the data in a DataFrame
product_data = scrape_pages()
df = pd.DataFrame(product_data)

# Replace missing values with "-"
df.fillna('-', inplace=True)

# Save the DataFrame to a CSV file
df.to_csv('product_details.csv', index=False)

# Quit the browser
driver.quit()




'''5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps. '''

def get_geolocation(city):
    api_key = "My-api_key"  # Replace with your Google Maps API key

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": city,
        "key": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "OK":
        results = data["results"]
        location = results[0]["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return latitude, longitude
    else:
        return None

# Example usage
city = input("Enter a city: ")
coordinates = get_geolocation(city)

if coordinates:
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Could not retrieve geolocation for the specified city.")



'''6. Write a program to scrap all the available details of best gaming laptops from digit.in. '''

# Set up Selenium webdriver
driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable


# Navigate to the website
url = "https://www.digit.in/top-products/best-hp-gaming-laptop-3933.html"#'https://www.digit.in/top-products/best-gaming-laptops-40.html' 
driver.get(url)
time.sleep(3)  # Add a delay to allow the page to load

# Find the container element that holds the laptop details
laptop_container = driver.find_element(By.ID, "search")

# Find all the laptop details within the container
laptop_details = laptop_container.find_elements(By.CLASS_NAME, "TopNumbeBlock")

# Scrape the details for each laptop
product_details = []
for laptop in laptop_details:
    laptop_name = laptop.find_element(By.CLASS_NAME, "TopNumbeProductTitle").text.strip()
    laptop_specs = laptop.find_element(By.CLASS_NAME, "TopNumbeProductSpecs").text.strip()
    
    product_details.append({
        "Laptop Name": laptop_name,
        "Specifications": laptop_specs
    })

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_details)

# Save the DataFrame to a CSV file
df.to_csv("digit_gaming_laptops.csv", index=False)

# Quit the browser
driver.quit()






'''
7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
“Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. '''

# Set up the Chrome webdriver
driver = webdriver.Chrome()

# Navigate to the Forbes billionaires page
url = 'https://www.forbes.com/billionaires/'
driver.get(url)
driver.maximize_window


# Find the container that holds the billionaire details

def scrape_page():
  billionaire_details=[]
  billionaire_items = driver.find_element(By.XPATH, '//*[@id="row-0"]')
  time.sleep(3)  

   # Iterate over each billionaire item and scrape the details

  for billionaire_item in billionaire_items:
    try:
      # Scrape the required details for each billionaire
      rank = billionaire_item.find_element_by_class_name('rank').text
      name = billionaire_item.find_element_by_class_name('personName').text
      net_worth = billionaire_item.find_element_by_class_name('netWorth').text
      age = billionaire_item.find_element_by_class_name('age').text
      citizenship = billionaire_item.find_element_by_class_name('countryOfCitizenship').text
      source = billionaire_item.find_element_by_class_name('source').text
      industry = billionaire_item.find_element_by_class_name('category').text
      
      billionaire_details.append({rank, name, net_worth, age, citizenship, source, industry})
      
    except NoSuchElementException:
      billionaire_details.append('-')      
      
    

    # Print the details of the billionaire
    print('Rank:', rank)
    print('Name:', name)
    print('Net Worth:', net_worth)
    print('Age:', age)
    print('Citizenship:', citizenship)
    print('Source:', source)
    print('Industry:', industry)
    print('-')
    
  return billionaire_details   

# Close the browser
driver.quit()


'''
8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted 
from any YouTube Video. '''

# Set up API credentials
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Remove this line for production use
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"  # Remove this line for production use

# Create YouTube API client
api_service_name = "youtube"
api_version = "v3"
api_key = "xxxxxxxxxxxx"  # Replace with your YouTube API key
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

# Set video ID for the YouTube video you want to extract comments from
video_id = "Kziw_hiXqzs"  # Replace with the actual YouTube video ID

# Define the number of comments to extract
num_comments_to_extract = 500

# Make API request to retrieve video comments
response = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=num_comments_to_extract,
    textFormat="plainText"
).execute()

# Process API response to extract comments, comment upvotes, and time
comments = []
comment_upvotes = []
comment_times = []

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    comment_upvote = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
    comment_time = item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]

    comments.append(comment)
    comment_upvotes.append(comment_upvote)
    comment_times.append(comment_time)

# Print the extracted data
for i in range(len(comments)):
    print("Comment:", comments[i])
    print("Upvotes:", comment_upvotes[i])
    print("Time:", comment_times[i])
    print()

'''
9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
“London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
reviews, privates from price, dorms from price, facilities and property description. '''

# Set up Selenium webdriver
driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
driver.maximize_window()

# Navigate to the website
url = "https://www.hostelworld.com/search?search_keywords=London,%20England&country=England&city=London&type=city&id=3&from=2023-06-01&to=2023-06-08&guests=1"
driver.get(url)
time.sleep(2)  # Add a delay to allow the page to load

# Find all the hostel containers
#hostel_containers = driver.find_elements_by_id("__nuxt")
hostel_containers = driver.find_element(By.CSS_SELECTOR, "#__nuxt")

# Create a list to store the scraped data
hostels_data = []

# Iterate over each hostel container and extract the required information
for hostel in hostel_containers:
    hostel_name = hostel.find_element_by_tag_name("name").text
    distance = hostel.find_element_by_class_name("description").text
    ratings = hostel.find_element_by_class_name("score").text
    total_reviews = hostel.find_element_by_class_name("reviews").text
    overall_reviews = hostel.find_element_by_class_name("overall-rating").text
    privates_price = hostel.find_element_by_css_selector(".price-col").text
    dorms_price = hostel.find_element_by_css_selector(".price-col.dorms-col").text
    facilities = [fac.text for fac in hostel.find_elements_by_class_name("facilities")]
    description = hostel.find_element_by_class_name("more-details").text

    # Append the hostel data to the list
    hostels_data.append({
        "Hostel Name": hostel_name,
        "Distance from City Centre": distance,
        "Ratings": ratings,
        "Total Reviews": total_reviews,
        "Overall Reviews": overall_reviews,
        "Privates From Price": privates_price,
        "Dorms From Price": dorms_price,
        "Facilities": facilities,
        "Property Description": description
    })

# Create a DataFrame from the scraped data
df = pd.DataFrame(hostels_data)

# Save the DataFrame to a CSV file
df.to_csv("hostels_data.csv", index=False)

# Quit the browser
driver.quit()






