from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
import time
from bs4 import BeautifulSoup
import requests


'''
1. Scrape the details of most viewed videos on YouTube from Wikipedia.
Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos
You need to find following details:
A) Rank
B) Name
C) Artist
D) Upload date
E) Views'''

# Set up the Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")  # To run Chrome in headless mode
service = Service("path/to/chromedriver")  # Set the path to your chromedriver executable
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"
driver.get(url)

# Find the table containing the video details
table = driver.find_element(By.CLASS_NAME, "wikitable")
rows = table.find_elements(By.TAG_NAME, "tr")

# Initialize lists to store the details
rank_list = []
name_list = []
artist_list = []
upload_date_list = []
views_list = []

# Iterate over the rows in the table (skipping the header row)
for row in rows[1:30]:
    # Extract the data from each column
    columns = row.find_elements(By.TAG_NAME, "td")
    rank = columns[0].text.strip()
    name = columns[1].text.strip()
    artist = columns[2].text.strip()
    upload_date = columns[3].text.strip()
    views = columns[4].text.strip()
    
    # Append the data to the respective lists
    rank_list.append(rank)
    name_list.append(name)
    artist_list.append(artist)
    upload_date_list.append(upload_date)
    views_list.append(views)

# Print the scraped details
for i in range(len(rank_list)):
    print("Rank:", rank_list[i])
    print("Name:", name_list[i])
    print("Artist:", artist_list[i])
    print("Upload Date:", upload_date_list[i])
    print("Views:", views_list[i])
    print()

# Close the browser
driver.quit()




'''
2. Scrape the details teamIndia’sinternationalfixtures from bcci.tv. 
Url = https://www.bcci.tv/.
You need to find following details:
A) Match title (I.e. 1stODI)
B) Series
C) Place
D) Date
E) Time
Note: - From bcci.tv home page you have reach to the international fixture page through code.
'''

# Instantiate a new Chrome driver
driver = webdriver.Chrome()

# Navigate to the BCCI website
driver.get("https://www.bcci.tv/international/fixtures")

# Find the "International" menu item and click it
international_menu = driver.find_element(By.XPATH, '//*[@id="navigation"]/ul[1]/li[2]/a')
international_menu.click()

# Find the "Fixtures" submenu item and click it
fixtures_submenu = driver.find_element(By.XPATH, '//*[@id="fixtures-tab"]')
fixtures_submenu.click()

# Wait for the fixtures to load (you can adjust the wait time as needed)
driver.implicitly_wait(10)

# Find all the fixture elements
fixtures = driver.find_elements(By.CLASS_NAME, "nav-link active ")

# Iterate over the fixtures and extract the required information
for fixture in fixtures:
    match_title = fixture.find_element(By.CLASS_NAME, "fixture__description").text
    series = fixture.find_element(By.CLASS_NAME, "fixture__format-strip").text
    place = fixture.find_element(By.CLASS_NAME, "fixture__additional-info").text
    date = fixture.find_element(By.CLASS_NAME, "fixture__date").text
    time = fixture.find_element(By.CLASS_NAME, "fixture__time").text

    print("Match Title:", match_title)
    print("Series:", series)
    print("Place:", place)
    print("Date:", date)
    print("Time:", time)
    print("")

# Close the browser
driver.quit()


'''
3. Scrape the details of State-wise GDP ofIndia fromstatisticstime.com. 
Url = http://statisticstimes.com/
You have to find following details:
A) Rank
B) State
C) GSDP(18-19)- at current prices
D) GSDP(19-20)- at current prices
E) Share(18-19)
F) GDP($ billion)
Note: - From statisticstimes home page you have to reach to economy page through code.
'''

# Launch Chrome browser and open the website
driver = webdriver.Chrome()
driver.get("http://statisticstimes.com/")

# Find and click the "Economy" link on the home page
economy_link = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div[2]/div[2]/button'))
)
economy_link.click()

# Find and click the "GDP of Indian states" link on the Economy page
gdp_states_link = driver.find_elements(By.XPATH, '//*[@id="main"]/div[1]/h1')
for element in gdp_states_link:
    element.click()
    # Perform additional actions for each element if needed



driver.implicitly_wait(10)

# Wait for the table with state-wise GDP data to load
gdp_table = driver.find_elements(By.XPATH, '//table[@id="table_id"]/tbody')

# Scrape the details from the table
#rows = gdp_table.find_elements(By.TAG_NAME, "tr")
rows =[]
for element in gdp_table:
    rows1 = element.find_element(By.TAG_NAME, "tr")
    rows.append(rows1)
    # Perform actions on the row element

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 6:
        rank = cells[0].text
        state = cells[1].text
        gdp_1819 = cells[2].text
        gdp_1920 = cells[3].text
        share_1819 = cells[4].text
        gdp_billion = cells[5].text
        
        print("Rank:", rank)
        print("State:", state)
        print("GSDP(18-19) at current prices:", gdp_1819)
        print("GSDP(19-20) at current prices:", gdp_1920)
        print("Share(18-19):", share_1819)
        print("GDP ($ billion):", gdp_billion)
        print("--------------------------------------------")

# Close the browser
driver.quit()


'''4. Scrape the details of trending repositories on Github.com. 
Url = https://github.com/
You have to find the following details:
A) Repository title
B) Repository description
C) Contributors count
D) Language used
'''



# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: Run Chrome in headless mode to hide the browser window
driver = webdriver.Chrome(options=options)  # Make sure the chromedriver is in your system PATH

# Navigate to the GitHub homepage
url = 'https://github.com/trending'
driver.get(url)

# Wait for the Explore menu to load
driver.implicitly_wait(10)

# Click on the trending option from the Explore menu

explore_menu = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/main/div[1]/nav/div')
for element in explore_menu:
   element.click()

driver.implicitly_wait(10)
trending_option = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/main/div[1]/nav/div/a[3]')
for elem in trending_option:   
    elem.click()

# Wait for the trending repositories page to load
time.sleep(2)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all the repository cards on the page
repo_cards = soup.find_all('article', class_='Box-row')




title=[]
description=[]
count=[]
language=[]
used=[]
# Scrape the details for each repository
for card in repo_cards:

    title.append(card.find('h2').text.strip())
    element = card.find('p', class_='mb-1')
    element = card.find('a', class_='muted-link')
    element = card.find('span', itemprop='programmingLanguage')
    if element is not None:
        description.append(element.text.strip())
        count.append(element.text.strip())
        language.append(element.text.strip())
    else:
        description.append("No description available")
        count.append("No description available")
        language.append("No description available")


    used.append(language.text.strip() if isinstance(language, bs4.Tag) else 'N/A')




# Print the details
print('Repository Title:', title)
print('Repository Description:', description)
print('Contributors Count:', count)
print('Language Used:', used)
print()

# Close the browser
driver.quit()




'''
5. Scrape the details of top 100 songs on billiboard.com. 
Url = https:/www.billboard.com/
You have to find the following details:
A) Song name
B) Artist name
C) Last week rank
D) Peak rank
E) Weeks on board
Note: - From the home page you have to click on the charts option then hot 100-page link through code.'''



# Set up Selenium webdriver
driver = webdriver.Chrome()
driver.get("https://www.billboard.com/")

# Click on the "Charts" option
charts_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Charts")))
driver.execute_script("arguments[0].scrollIntoView(true);", charts_option)
driver.execute_script("arguments[0].click();", charts_option)

# Click on the "Hot 100" page link
hot_100_link = driver.find_elements(By.XPATH, '//*[@id="post-1479786"]/div[1]/div/div/div[2]/div[3]/div/nav/ul/li[1]/a')
for hot in hot_100_link:
   hot.click()



# Get the HTML content of the page after navigating to the Hot 100 page
page_html = driver.page_source

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page_html, "html.parser")

# Find the container element that holds the song details
chart_container = soup.find_all("div", class_="chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max")
song_name=[]
artist_name=[]
last_week_rank=[]
peak_rank=[]
weeks_on_board=[]

# Iterate over each song entry and extract the required details
for song_entry in chart_container:
    # Extract the song name, artist name, last week rank, peak rank, weeks on board
    song_name.append(song_entry.find('h3', class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").text.strip())
    artist_name.append(song_entry.find("span", class_="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet").text.strip())
    last_week_rank.append(song_entry.find("span", class_="chart-element__rank__last-week").text.strip())
    peak_rank.append(song_entry.find("span", class_="chart-element__rank__peak").text.strip())
    weeks_on_board.append(song_entry.find("span", class_="chart-element__weeks-on-chart").text.strip())

    # Print the extracted details
print("Song:", song_name)
print("Artist:", artist_name)
print("Last Week Rank:", last_week_rank)
print("Peak Rank:", peak_rank)
print("Weeks on Board:", weeks_on_board)
print("----------------------")

# Close the Selenium webdriver
driver.quit()



'''
6. Scrape the details of Highest sellingnovels.
Url = https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-greycompare
You have to find the following details:
A) Book name
B) Author name
C) Volumes sold
D) Publisher
E) Genre'''



url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the book details
table = soup.find("table")

# Initialize empty lists to store the details of each book
book_names = []
author_names = []
volumes_sold = []
publishers = []
genres = []

# Loop through each row in the table (excluding the header row)
for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    
    # Skip rows with missing data
    if len(columns) < 6:
        continue
    
    book_name = columns[1].text.strip()
    author_name = columns[2].text.strip()
    volume_sold = columns[3].text.strip()
    publisher = columns[4].text.strip()
    genre = columns[5].text.strip()

    book_names.append(book_name)
    author_names.append(author_name)
    volumes_sold.append(volume_sold)
    publishers.append(publisher)
    genres.append(genre)

# Print the scraped details
for i in range(len(book_names)):
    print(f"Book Name: {book_names[i]}")
    print(f"Author Name: {author_names[i]}")
    print(f"Volumes Sold: {volumes_sold[i]}")
    print(f"Publisher: {publishers[i]}")
    print(f"Genre: {genres[i]}")
    print("------------------------")


'''
7. Scrape the details most watched tv series of all time from imdb.com. 
Url = https://www.imdb.com/list/ls095964455/
You have to find the following details:
A) Name
B) Year span
C) Genre
D) Run time
E) Ratings
F) Votes
'''

url = "https://www.imdb.com/list/ls095964455/"

# Send a GET request to the URL and fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the container that holds the TV series details
container = soup.find("div", class_="lister-list")

# Find all the list items representing each TV series
tv_series = container.find_all("div", class_="lister-item-content")

# Loop through each TV series and extract the details
for series in tv_series:
    name = series.find("h3").a.text
    year_span = series.find("span", class_="lister-item-year").text.strip("()")
    genre = series.find("span", class_="genre").text.strip()
    run_time = series.find("span", class_="runtime").text.strip()
    rating = series.find("div", class_="ipl-rating-star").text.strip()
    votes = series.find("span", attrs={"name": "nv"}).text.strip().replace(",", "")

    print(f"Name: {name}")
    print(f"Year Span: {year_span}")
    print(f"Genre: {genre}")
    print(f"Run Time: {run_time}")
    print(f"Rating: {rating}")
    print(f"Votes: {votes}")
    print("------------------------")

'''
8. Details of Datasetsfrom UCI machine learning repositories. 
Url = https://archive.ics.uci.edu/
You have to find the following details:
A) Dataset name
B) Data type
C) Task
D) Attribute type
E) No of instances
F) No of attribute
G) Year
Note: - from the home page you have to go to the ShowAllDataset page through code.
'''

url = "https://archive.ics.uci.edu/"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the UCI Machine Learning Repository homepage
driver.get(url)

driver.implicitly_wait(10)

# Find the link to the Show All Dataset page
show_all_link = driver.find_elements(By.XPATH, "/html/body/div/div[1]/div[1]/header/nav/ul/li[1]/a")


# Click on the Show All Dataset link
for link in show_all_link:
    link.click()

driver.implicitly_wait(10)
# Find the table containing the dataset details
table = driver.find_elements(By.XPATH, "/html/body/div/div[1]/div[1]/main/div/div[2]/div[2]")


# Find all the rows representing each dataset within the table
rows=[]
for tab in table:
   rows.append(tab.find_elements(By.XPATH, "/html/body/div/div[1]/div[1]/main/div/div[2]/div[2]/div[1]"))

dataset_name=[]
data_type=[]
task=[]
attribute_type=[]
no_of_instances=[]
no_of_attributes=[]
year=[]
# Loop through each dataset and extract the details

for columns in rows:
    # Skip rows with missing data
    if len(columns) < 7:
        continue
    dataset_name.append(columns[0].text.strip())
    data_type.append(columns[1].text.strip())
    task.append(columns[2].text.strip())
    attribute_type.append(columns[3].text.strip())
    no_of_instances.append(columns[4].text.strip())
    no_of_attributes.append(columns[5].text.strip())
    year.append(columns[6].text.strip())

print(f"Dataset Name: {dataset_name}")
print(f"Data Type: {data_type}")
print(f"Task: {task}")
print(f"Attribute Type: {attribute_type}")
print(f"No. of Instances: {no_of_instances}")
print(f"No. of Attributes: {no_of_attributes}")
print(f"Year: {year}")
print("------------------------")

# Close the browser
driver.quit()


'''
9. Scrape the details of Data science recruiters Url = https://www.naukri.com/hr-recruiters-consultants
You have to find the following details: 
A) Name
B) Designation
C)Company 
D)Skills they hire for 
E) Location
Note: - From naukri.com homepage click on the recruiters option and the on the search pane type Data science and 
click on search. All this should be done through code'''

# Send a GET request to the Naukri.com recruiters page
response = requests.get("https://www.naukri.com/hr-recruiters-consultants")
print(response)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the recruiter profiles
name=[]
designation=[]
company=[]
skills=[]
location=[]
recruiter_profiles = soup.find_all("div", class_="recInfo")

# Loop through each recruiter profile and extract the details
for recruiter_profile in recruiter_profiles:
    name = recruiter_profile.find("span", class_="fl").text.strip()
    designation = recruiter_profile.find("span", class_="designation").text.strip()
    company = recruiter_profile.find("p", class_="org").text.strip()
    skills = recruiter_profile.find("div", class_="rec-skill").text.strip()
    location = recruiter_profile.find("p", class_="loc").text.strip()

print(f"Name: {name}")
print(f"Designation: {designation}")
print(f"Company: {company}")
print(f"Skills they hire for: {skills}")
print(f"Location: {location}")
print("------------------------")
