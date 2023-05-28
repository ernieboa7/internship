import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1) Write a python program to display all the header tags from wikipedia.org and make data frame.

# Make a request to Wikipedia.org
url = 'https://en.wikipedia.org/wiki/Main_Page'
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all header tags
header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4'])

# Extract the header text
header_text = [tag.text.strip() for tag in header_tags]

# Create a DataFrame from the header text
df = pd.DataFrame({'Header': header_text})

# Display the DataFrame
print(df)


''' 2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
from https://presidentofindia.nic.in/former-presidents.htm and make data frame.'''




# Make a request to the President of India's website
url = 'https://presidentofindia.nic.in/former-presidents.htm'
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the container div that holds the former Presidents' information
container = soup.find('div', class_='panel-pane pane-entity-field')

if container:
    # Extract the data from the container
    data = []
    presidents = container.find_all('div', class_='former_president')[1:11]

    for president in presidents:
        name = president.find('div', class_='field-item').text.strip()
        term_of_office = president.find('span', class_='field-content').text.strip()
        data.append([name, term_of_office])

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Name', 'Term of Office'])

    # Display the DataFrame
    print(df)
else:
    print("Container not found on the webpage.")







'''
3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data framea) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
b) Top 10 ODI Batsmen along with the records of their team andrating.
c) Top 10 ODI bowlers along with the records of their team andrating.
'''
# Scrape Top 10 ODI teams
team_url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
team_response = requests.get(team_url)
team_soup = BeautifulSoup(team_response.content, 'html.parser')

team_table = team_soup.find('table', class_='table')

team_data = []
team_rows = team_table.tbody.find_all('tr')

for row in team_rows:
    cells = row.find_all('td')
    team_rank = cells[0].text.strip()
    team_name = cells[1].text.strip()
    team_matches = cells[2].text.strip()
    team_points = cells[3].text.strip()
    team_rating = cells[4].text.strip()
    team_data.append([team_rank, team_name, team_matches, team_points, team_rating])

team_df = pd.DataFrame(team_data, columns=['Rank', 'Team', 'Matches', 'Points', 'Rating'])
top_10_teams = team_df.head(10)



# Scrape Top 10 ODI batsmen
batsmen_url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'
batsmen_response = requests.get(batsmen_url)
batsmen_soup = BeautifulSoup(batsmen_response.content, 'html.parser')

batsmen_table = batsmen_soup.find('table', class_='table')

batsmen_data = []
batsmen_rows = batsmen_table.find_all('tr')[1:11]

for row in batsmen_rows:
    cells = row.find_all('td')
    batsmen_rank = cells[0].text.strip()
    batsmen_name = cells[1].text.strip()
    batsmen_team = cells[2].text.strip()
    batsmen_rating = cells[3].text.strip()
    batsmen_data.append([batsmen_rank, batsmen_name, batsmen_team, batsmen_rating])

batsmen_df = pd.DataFrame(batsmen_data, columns=['Rank', 'Batsman', 'Team', 'Rating'])
top_10_batsmen = batsmen_df.head(10)


# Scrape Top 10 ODI bowlers
bowlers_url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'
bowlers_response = requests.get(bowlers_url)
bowlers_soup = BeautifulSoup(bowlers_response.content, 'html.parser')

bowlers_table = bowlers_soup.find('table', class_='table')

bowlers_data = []
bowlers_rows = bowlers_table.find_all('tr')[1:11]

for row in bowlers_rows:
    cells = row.find_all('td')
    bowlers_rank = cells[0].text.strip()
    bowlers_name = cells[1].text.strip()
    bowlers_team = cells[2].text.strip()
    bowlers_rating = cells[3].text.strip()
    bowlers_data.append([bowlers_rank, bowlers_name, bowlers_team, bowlers_rating])

bowlers_df = pd.DataFrame(bowlers_data, columns=['Rank', 'Bowler', 'Team', 'Rating'])
top_10_bowlers = bowlers_df.head(10)


# Display the DataFrames
print("Top 10 ODI Teams:")
print(top_10_teams)
print("\nTop 10 ODI Batsmen:")
print(top_10_batsmen)
print("\nTop 10 ODI Bowlers:")
print(top_10_bowlers)




'''
4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data framea) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
b) Top 10 women’s ODI Batting players along with the records of their team and rating.
c) Top 10 women’s ODI all-rounder along with the records of their team and rating.
'''
# Function to scrape and create data frames
def scrape_and_create_dataframe(url, header_index, rows_range):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the rankings
    table = soup.find('table', class_='table')

    # Extract the data from the table and store it in lists
    data = []

    rows = table.find_all('tr')[header_index:rows_range]  # Exclude the header row and get desired rows

    for row in rows:
        columns = row.find_all('td')
        record = [column.text.strip() for column in columns]
        data.append(record)

    # Create a DataFrame using the extracted data
    df = pd.DataFrame(data)

    return df

# a) Top 10 ODI teams in women’s cricket along with the records for matches, points, and rating
url_teams = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
df_teams = scrape_and_create_dataframe(url_teams, 1, 11)

print("Top 10 ODI teams in women's cricket:")
print(df_teams)
print()

# b) Top 10 women’s ODI Batting players along with the records of their team and rating
url_batting = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
df_batting = scrape_and_create_dataframe(url_batting, 1, 11)

print("Top 10 women's ODI batting players:")
print(df_batting)
print()

# c) Top 10 women’s ODI all-rounders along with the records of their team and rating
url_all_rounders = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder"
df_all_rounders = scrape_and_create_dataframe(url_all_rounders, 1, 11)

print("Top 10 women's ODI all-rounders:")
print(df_all_rounders)





'''
5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
make data frame
i) Headline
ii) Time
iii) News Link'''

# URL of the news website
url = "https://www.cnbc.com/world/?region=world"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container for the news articles
container = soup.find('div', class_='PageBuilder-content')

# Find all the news articles
articles = container.find_all('div', class_='Card-titleContainer')[0]

# Extract the data from the articles and store it in lists
headlines = []
times = []
links = []

for article in articles:
    headline = article.find('a').text.strip()
    time = article.find('time').text.strip()
    link = "https://www.cnbc.com" + article.find('a')['href']
    
    headlines.append(headline)
    times.append(time)
    links.append(link)

# Create a DataFrame using the extracted data
data = {
    'Headline': headlines,
    'Time': times,
    'News Link': links
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)




'''
6) Write a python program to scrape the details of most downloaded articles from AI in last 90
days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
Scrape below mentioned details and make data frame i) Paper Title
ii) Authors
iii) Published Date
iv) Paper URL
'''

# URL of the most downloaded articles page
url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container for the articles
container = soup.find('ol', class_='article-list')

# Check if the container exists
if container is not None:
    # Find all the articles
    articles = container.find_all('li', class_='article-list-item')

    # Extract the data from the articles and store it in lists
    titles = []
    authors = []
    dates = []
    urls = []

    for article in articles:
        title = article.find('h2').text.strip()
        author = article.find('span', class_='author-list').text.strip()
        date = article.find('span', class_='published-date').text.strip()
        url = article.find('a')['href']
        
        titles.append(title)
        authors.append(author)
        dates.append(date)
        urls.append(url)

    # Create a DataFrame using the extracted data
    data = {
        'Paper Title': titles,
        'Authors': authors,
        'Published Date': dates,
        'Paper URL': urls
    }

    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)
else:
    print("No articles found.")


'''
7) Write a python program to scrape mentioned details from dineout.co.inand make data framei) Restaurant name
ii) Cuisine
iii) Location
iv) Ratings
v) Image URL'''

# URL of the website to scrape
url = "https://www.dineout.co.in/delhi-restaurants"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container for the restaurants
container = soup.find('div', class_='restnt-main-wrapper')

# Check if the container exists
if container is not None:
    # Find all the restaurant items
    restaurants = container.find_all('div', class_='restnt-card')

    # Extract the data from the restaurant items and store it in lists
    restaurant_names = []
    cuisines = []
    locations = []
    ratings = []
    image_urls = []

    for restaurant in restaurants:
        name = restaurant.find('div', class_='restnt-name ellipsis').text.strip()
        cuisine = restaurant.find('div', class_='restnt-loc ellipsis').text.strip()
        location = restaurant.find('div', class_='restnt-locality ellipsis').text.strip()
        rating = restaurant.find('span', class_='restnt-rating').text.strip()
        image_url = restaurant.find('img', class_='res_img')['src']
        
        restaurant_names.append(name)
        cuisines.append(cuisine)
        locations.append(location)
        ratings.append(rating)
        image_urls.append(image_url)

    # Create a DataFrame using the extracted data
    data = {
        'Restaurant Name': restaurant_names,
        'Cuisine': cuisines,
        'Location': locations,
        'Ratings': ratings,
        'Image URL': image_urls
    }

    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)
else:
    print("No restaurants found.")
