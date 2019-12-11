import requests
from bs4 import BeautifulSoup


def universities_scraper():
    URL = "https://wiki.osgeo.org/wiki/Edu_current_initiatives#Current_members_of_the_Geo_for_All_Labs_Network"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")
    my_table = soup.find("table", {"class": "wikitable sortable"})
    links = my_table.findAll("tr")
    universities = []
    for i in range(1, 2):
        x = links[i].text.strip().splitlines()
        temp = []
        for j in x:
            if j:
                temp.append(j.strip())
        universities.append(temp)
    udata = []
    for i in universities:

        udata.append([{"name": i[1],"location": [37.41, 8.82]}])
    return udata

