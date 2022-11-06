import os
import wikipedia
import re
import json

LENGTH = r"(\d+.?\d+)\sm"
FILE_NAME="output.json"


"""
# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    response  = session.get(url)
     # response will be provided in JSON format
    return response.text

"""

"""
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

"""

def get_aircraft_spec(wiki_page):
    data_names = ["Length", 
                  "Wingspan", 
                  "Height", 
                  "Wing area", 
                  "Crew", 
                  "Aspect", 
                  "Airfoil",
                  "Empty weight",
                  "Max takeoff weight",
                  "Fuel capacity",
                  "Powerplant",
                  "Propellers",
                  "Maximum speed",
                  "Cruise speed",
                  "Stall speed",
                  "Range",
                  "Service ceiling",
                  "Rate of climb",
                  "Take-off run",
                  "Landing run",
                  "Cockpit Crew",
                  "Cross section",
                  "Maximum Payload",
                  "MTOW",
                  "Max fuel",
                  "Engines",
                  "Thrust",
                  "speed",
                  "Ceiling",
                  "Range"]
    data_lines = []
    load_page = get_wiki_page(wiki_page)
    if load_page is not None:
        data_lines = get_data(load_page.content, data_names)
    # Length\:\s(\d+.?\d+)\sft\s((\d+.?\d+)\sin)?\s\((\d+.?\d+)\sm\)
    return {wiki_page : data_lines}

def get_data(content, names):
    lines = []
    for name in names:
        lines += [x for x in content.split("\n") if x.startswith(name)]
    return lines


def get_wiki_page(name):
    try:
        wiki_page = wikipedia.page(name)
        return wiki_page
    except:
        #raise WikipediaPageNotFoundError(name)
        return None





def main():
    print("Main Code to call data extraction")
    name = "List_of_civil_aircraft"
    air_page = wikipedia.page(name)
    with open(FILE_NAME , "w") as fod:
        for wiki_page in air_page.links:
            print(f"Working on aircraft: {wiki_page}")
            spec = get_aircraft_spec(wiki_page)
            fod.write(f"{spec}\n")
        


if __name__ =="__main__":
    main()