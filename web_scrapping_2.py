import requests
from bs4 import BeautifulSoup
import pandas as pd



'''
Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You 
have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 
jobs data.
This task will be done in following steps:
1. First get the webpage https://www.naukri.com/
2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the 
location” field.
3. Then click the searchbutton.
4. Then scrape the data for the first 10 jobs results youget.
5. Finally create a dataframe of the scraped data.'''


# Step 1: Get the webpage
page = "https://www.naukri.com/"
response = requests.get(page)
print(response)

# Step 2: Enter search criteria
search_keyword = "Data Analyst"
location = "Bangalore"

# Step 3: Perform the search
payload = {
    "keyword": search_keyword,
    "location": location,
}
response = requests.get(page, data=payload)

# Step 4: Scrape the data
soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find_all("div", class_="nI-gNb-backdrop")
print(jobs)

job_data = []
for job in jobs[:10]:
    title = job.find("a", class_="title ellipsis").text.strip()
    location = job.find("li", class_="fleft br2 placeHolderLi location").text.strip()
    company = job.find("a", class_="subTitle ellipsis fleft").text.strip()
    experience = job.find("div", class_="ellipsis job-description").text.strip()

    job_data.append({
        "Job Title": title,
        "Location": location,
        "Company Name": company,
        "Experience Required": experience
    })

# Step 5: Create a dataframe
df = pd.DataFrame(job_data)
print(df)


'''
Q2:Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You 
have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
This task will be done in following steps:
1. First get the webpage https://www.naukri.com/
2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the 
location” field.
3. Then click the searchbutton.
4. Then scrape the data for the first 10 jobs results youget.
5. Finally create a dataframe of the scraped data.'''

# Step 1: Get the webpage
page = "https://www.naukri.com/"
response = requests.get(page)
print(response)

# Step 2: Enter search criteria
search_keyword = "Data Scientist"
location = "Bangalore"

# Step 3: Perform the search
payload = {
    "keyword": search_keyword,
    "location": location,
}
response = requests.get(page, data=payload)

# Step 4: Scrape the data
soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find_all("div", class_="nI-gNb-backdrop")[:10]
print(jobs)

job_data = []
for job in jobs:
    title = job.find("a", class_="title ellipsis").text.strip()
    location = job.find("li", class_="fleft br2 placeHolderLi location").text.strip()
    company = job.find("div",class_="companyInfo subheading").text.strip()
    experience = job.find("div", class_="ellipsis job-description").text.strip()

    job_data.append({
        "Job Title": title,
        "Location": location,
        "Company Name": company,
        "Experience Required": experience
    })

# Step 5: Create a dataframe
df2 = pd.DataFrame(job_data)
print(df2)

'''
Q3 You have to use the location and salary filter.
You have to scrape data for “Data Scientist” designation for first 10 job results.
You have to scrape the job-title, job-location, company name, experience required. 
The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
The task will be done as shown in the below steps:
1. first get thewebpage https://www.naukri.com/
2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
3. Then click the searchbutton.
4. Then apply the location filter and salary filter by checking the respectiveboxes
5. Then scrape the data for the first 10 jobs results youget.
6. Finally create a dataframe of the scrapeddata.'''


# Step 1: Get the webpage
page = "https://www.naukri.com/"
response = requests.get(page)

# Step 2: Enter search criteria
search_keyword = "Data Scientist"

# Step 3: Perform the search
payload = {
    "keyword": search_keyword,
}
response = requests.post(page, data=payload)

# Step 4: Apply location and salary filters
soup = BeautifulSoup(response.content, "html.parser")
location_filter = soup.find("span", class_="ellipsis fleft filterLabel")
#location_filter["value"] = "Bangalore/Bengaluru"
print(location_filter)

salary_filter = soup.find("span", class_="ellipsis fleft filterLabel")
#salary_filter["value"] = "0-3 Lakhs"

#response = requests.post(page, data=soup.find("form", id="root__ModalContainer--searchForm").attrs)



# Step 5: Scrape the data
soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find_all("div", class_="nI-gNb-backdrop")[:10]
print(jobs)

job_data = []
for job in jobs:
    title = job.find("a", class_="title ellipsis").text.strip()
    location = job.find("li", class_="fleft br2 placeHolderLi location").text.strip()
    company = job.find("div",class_="companyInfo subheading").text.strip()
    experience = job.find("div", class_="ellipsis job-description").text.strip()

    job_data.append({
        "Job Title": title,
        "Location": location,
        "Company Name": company,
        "Experience Required": experience
    })

# Step 6: Create a dataframe
df3 = pd.DataFrame(job_data)
print(df3)



'''
Q4. To scrape the data you have to go through following steps:
1. Go to Flipkart webpage by url :https://www.flipkart.com/
2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and 
click the search icon
3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the 
required data as usual.
4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
click on it.
5. Now scrape data from this page as usual
6. Repeat this until you get data for 100 sunglasses.'''


# Step 1: Go to Flipkart webpage
page = "https://www.flipkart.com/"
response = requests.get(page)
print(response)

# Step 2: Enter search criteria and perform the search
search_keyword = "sunglasses"
payload = {
    "q": search_keyword
}
response = requests.get(page, params=payload)

# Step 3-6: Scrape data from multiple pages
sunglasses_data = []
page_count = 0

while len(sunglasses_data) < 100:
    # Scrape data from the current page
    soup = BeautifulSoup(response.content, "html.parser")
    sunglasses = soup.find_all("div", class_="_36fx1h _6t1WkM _3HqJxg")
    

    for sunglass in sunglasses:
        brand = sunglass.find("div", class_="_2WkVRV").txt
        description = sunglass.find("a", class_="IRpwTa").txt
        price = sunglass.find("div", class_="_30jeq3").txt
        sunglasses_data.append({
            "brand": brand,
            "description":description,
            "Price": price
        })

        if len(sunglasses_data) == 100:
            break

    # Check if there are more pages and navigate to the next page
    next_button = soup.find("a", class_="_36fx1h _6t1WkM _3HqJxg")
    if next_button:
        next_url = page + next_button["href"]
        response = requests.get(next_url)
    else:
        break

# Print the scraped data
for sunglasses in sunglasses_data:
    print("brand:", sunglasses["brand"])
    print("description:", sunglasses["description"])
    print("Price:", sunglasses["Price"])
    print()





'''
Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
place=FLIPKART
1. Rating
2. Review summary
3. Full review
4. You have to scrape this data for first 100reviews.'''

# Step 1: Go to the Flipkart reviews page for iPhone 11
url = 'https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market'
response = requests.get(url)

# Step 2: Scrape reviews data
reviews_data = []
page_count = 0

while len(reviews_data) < 100:
    # Scrape data from the current page
    soup = BeautifulSoup(response.content, "html.parser")
    reviews = soup.find_all("div", class_="_1AtVbE")
    

    for review in reviews:
        rating = review.find("div", class_="_3LWZlK _1BLPMq").txt
        summary = review.find("p", class_="_2-N8zT").txt
        full_review = review.find("div", class_="t-ZTKy").txt

        reviews_data.append({
            "Rating": rating,
            "Review Summary": summary,
            "Full Review": full_review
        })

        if len(reviews_data) == 100:
            break

    # Check if there are more pages and navigate to the next page
    next_button = soup.find("a", class_="_1LKTO3")
    if next_button:
        next_url = url + next_button["href"]
        response = requests.get(next_url)
    else:
        break

# Print the scraped data
for review in reviews_data:
    print("Rating:", review["Rating"])
    print("Review Summary:", review["Review Summary"])
    print("Full Review:", review["Full Review"])
    print()
    
    
    
'''Q6 : Scrape data forfirst 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the 
search field.
You have to scrape 3 attributes of each sneaker:
1. Brand
2. ProductDescription
3. Price '''

# Step 1: Go to Flipkart webpage and perform the search
url = "https://www.flipkart.com/"
search_keyword = "sneakers"
payload = {
    "q": search_keyword
}
response = requests.get(url, params=payload)

# Step 2: Scrape data for the first 100 sneakers
sneakers_data = []
page_count = 0

while len(sneakers_data) < 100:
    # Scrape data from the current page
    soup = BeautifulSoup(response.content, "html.parser")
    sneakers = soup.find_all("div", class_="_2WkVRV")

    for sneaker in sneakers:
        brand = sneaker.find("div", class_="_2B_pmu").text.strip()
        description = sneaker.find("a", class_="IRpwTa").text.strip()
        price = sneaker.find("div", class_="_30jeq3 _1_WHN1").text.strip()

        sneakers_data.append({
            "Brand": brand,
            "Product Description": description,
            "Price": price
        })

        if len(sneakers_data) == 100:
            break

    # Check if there are more pages and navigate to the next page
    next_button = soup.find("a", class_="_1LKTO3")
    if next_button:
        next_url = url + next_button["href"]
        response = requests.get(next_url)
    else:
        break

# Print the scraped data
for sneaker in sneakers_data:
    print("Brand:", sneaker["Brand"])
    print("Product Description:", sneaker["Product Description"])
    print("Price:", sneaker["Price"])
    print()




'''
Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then 
set CPU Type filter to “Intel Core i7” as shown in the below image:
After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
1. Title
2. Ratings
3. Price'''

# Step 1: Go to Amazon webpage and perform the search
url = "https://www.amazon.in/"
search_keyword = "Laptop"
payload = {
    "k": search_keyword
}
response = requests.get(url, params=payload)
print(response)

# Step 2: Set the CPU Type filter to "Intel Core i7"
soup = BeautifulSoup(response.content, "html.parser")
cpu_filter = soup.find("span", class_="a-size-base a-color-base s-ref-text-link s-ref-text-gray")
cpu_filter_parent = cpu_filter.find_family("a")
cpu_filter_url = "https://www.amazon.in" + cpu_filter_parent["href"]

response = requests.get(cpu_filter_url)
print(response)

# Step 3: Scrape data for the first 10 laptops
laptop_data = []
page_count = 0

while len(laptop_data) < 10:
    # Scrape data from the current page
    soup = BeautifulSoup(response.content, "html.parser")
    laptops = soup.find_all("div", class_="sg-col-inner")

    for laptop in laptops:
        title = laptop.find("span", class_="a-size-medium a-color-base a-text-normal").text.strip()
        ratings = laptop.find("span", class_="a-icon-alt").text.strip()
        price = laptop.find("span", class_="a-price-whole").text.strip()

        laptop_data.append({
            "Title": title,
            "Ratings": ratings,
            "Price": price
        })

        if len(laptop_data) == 10:
            break

    # Check if there are more pages and navigate to the next page
    next_button = soup.find("span", class_="s-pagination-item s-pagination-next s-pagination-disabled")
    if not next_button:
        next_button_url = soup.find("a", class_="s-pagination-next")["href"]
        response = requests.get(url + next_button_url)
    else:
        break

# Print the scraped data
for laptop in laptop_data:
    print("Title:", laptop["Title"])
    print("Ratings:", laptop["Ratings"])
    print("Price:", laptop["Price"])
    print()
    
 
    
    
'''Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
The above task will be done in following steps:
1. First get the webpagehttps://www.azquotes.com/
2. Click on TopQuotes
3. Than scrap a) Quote b) Author c) Type Of Quotes
 '''   
    
    
    # Step 1: Go to AZQuotes webpage and click on Top Quotes
url = "https://www.azquotes.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

top_quotes_link = soup.find("a", text="Top Quotes")["href"]
top_quotes_url = url + top_quotes_link

response = requests.get(top_quotes_url)

# Step 2: Scrape data for the top 1000 quotes
quotes_data = []
page_count = 0

while len(quotes_data) < 1000:
    # Scrape data from the current page
    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("div", class_="title")

    for quote in quotes:
        quote_text = quote.find("a", class_="title").text
        author = quote.find("a", class_="author").text
        quote_type = quote.find("div", class_="kw-box").text

        quotes_data.append({
            "Quote": quote_text,
            "Author": author,
            "Type of Quote": quote_type
        })

        if len(quotes_data) == 1000:
            break

    # Check if there are more pages and navigate to the next page
    next_button = soup.find("a", text="Next")
    if next_button:
        next_url = url + next_button["href"]
        response = requests.get(next_url)
    else:
        break

# Print the scraped data
for quote in quotes_data:
    print("Quote:", quote["Quote"])
    print("Author:", quote["Author"])
    print("Type of Quote:", quote["Type of Quote"])
    print()



'''
Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, 
Term of office, Remarks) from https://www.jagranjosh.com/.
This task will be done in following steps:
1. First get the webpagehttps://www.jagranjosh.com/
2. Then You have to click on the GK option
3. Then click on the List of all Prime Ministers of India
4. Then scrap the mentioned data and make theDataFrame.
'''

# Step 1: Go to the Jagran Josh webpage and click on the GK option
url = "https://www.jagranjosh.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

gk_link = soup.find("a", text="GK")["href"]
gk_url = url + gk_link

response = requests.get(gk_url)
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Click on the List of all Prime Ministers of India
prime_ministers_link = soup.find("a", text="List of all Prime Ministers of India")["href"]
prime_ministers_url = url + prime_ministers_link

response = requests.get(prime_ministers_url)
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Scrape the data
table = soup.find("table", class_="table4")

data = []
rows = table.find_all("tr")

for row in rows[1:]:  # Exclude the header row
    columns = row.find_all("td")
    name = columns[0].text.strip()
    born_dead = columns[1].text.strip()
    term_of_office = columns[2].text.strip()
    remarks = columns[3].text.strip()

    data.append({
        "Name": name,
        "Born-Dead": born_dead,
        "Term of Office": term_of_office,
        "Remarks": remarks
    })

# Step 4: Create the DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)



'''
Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. 
Car name and Price) from https://www.motor1.com/
This task will be done in following steps:
1. First get the webpagehttps://www.motor1.com/
2. Then You have to type in the search bar ’50 most expensive cars’
3. Then click on 50 most expensive carsin the world..
4. Then scrap the mentioned data and make the dataframe'''


# Step 1: Go to the Motor1 webpage and search for '50 most expensive cars'
url = "https://www.motor1.com/"
search_keyword = "50 most expensive cars"
payload = {
    "q": search_keyword
}
response = requests.get(url, params=payload)
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Click on the '50 most expensive cars in the world' link
expensive_cars_link = soup.find("a", text="50 Most Expensive Cars In The World")["href"]
expensive_cars_url = url + expensive_cars_link

response = requests.get(expensive_cars_url)
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Scrape the data
table = soup.find("table", class_="article-body-table")

data = []
rows = table.find_all("tr")

for row in rows[1:]:  # Exclude the header row
    columns = row.find_all("td")
    car_name = columns[1].text.strip()
    price = columns[2].text.strip()

    data.append({
        "Car Name": car_name,
        "Price": price
    })

# Step 4: Create the DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
