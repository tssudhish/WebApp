import os
from bs4 import BeautifulSoup as BS
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import wikipedia

import ssl

# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
    """     
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    response  = session.get(url)
    """
     # response will be provided in JSON format
    return response.text

def extract_aircraft_list(url):
    html = getHTMLdocument(url)
    soup = BS(html)
    h3_list = soup.find_all("span", {"class":"mw-headline"})
    print(f"There are {len(h3_list)} items in this page")
    for family_name in h3_list:
        print(f"Aircraft family name: {family_name}")

    a_list = soup.find_all("a")
    print(f"There are {len(a_list)} items in this page")
    for ref_name in a_list:
        print(f"Aircraft family name: {ref_name}")






def main():
    print("Main Code to call data extraction")
    url = "https://en.wikipedia.org/wiki/List_of_civil_aircraft"
    extract_aircraft_list(url)


if __name__ =="__main__":
    main()