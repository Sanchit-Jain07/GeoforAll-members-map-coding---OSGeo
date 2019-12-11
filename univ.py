import requests
from bs4 import BeautifulSoup


def universities_scraper():
    URL = "https://wiki.osgeo.org/wiki/Edu_current_initiatives#Current_members_of_the_Geo_for_All_Labs_Network"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")
    my_table = soup.find("table", {"class": "wikitable sortable"})
    links = my_table.findAll("tr")
    universities = []
    for i in links:
        x = i.text.strip().splitlines()
        temp = []
        for j in x:
            if j:
                temp.append(j.strip())
        universities.append(temp)
    udata = []
    for i in universities:
        try:
            coord = i[5].split(',')
            udata.append({"name": i[1],"location": [float(coord[0]), float(coord[1])]})
        except:
            continue
    udict = {'d':udata}
    return udict
    '''print(universities)
universities_scraper()'''