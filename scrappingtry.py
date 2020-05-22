# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://ebookskenya.co.ke/download-cpa-section-3-past-papers/'


# Connect to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
data = soup.findAll('a')
#try to see if the list starts at 20
print(data[20]['href'])
print(data[20].text)

line_count = 1 #variable to track what line you are on
for tags in data:  #'a' tags are for links
    if line_count >= 20: #code for text files starts at line 36
        download_url = tags['href']
        urllib.request.urlretrieve(download_url,tags.text+".pdf")
        print("Succesfully downloaded "+ str(line_count))
        time.sleep(1) #pause the code for a sec
    #add 1 for next line
    line_count +=1
    if line_count>49:
    	break
