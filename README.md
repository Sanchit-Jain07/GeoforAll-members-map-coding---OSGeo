# GeoforAll-members-map-coding---OSGeo
Scraping data from a page and then displaying the locations scraped in a map. (Python and Javascript)

The whole program's gist is Python communicating with Javascript. So lets see how I achieved that.

First thing was to scrape the data from the webpage. So I used the requests and beautiful soup modules to achieve this. Using the requests module I could get the whole page scraped. Then using Beautiful Soup and html parser, I parsed the webpage into textual form. Then I looked for the table containing all the information about the universities. The table had the class of "wikitable sortable jquery-tablesorter". So I used this information to extract the whole table using bs4. After extracting this huge amount of data, I had to so split these data into individual datas like name, location etc. From extracting the data, what i got was a multiline string for a single university with every thing like location, name, city being in different lines. So i used a python method called splitlines() to separate these information and store them in a list. And store these lists in a bigger list as the first list had information of a single university and the second list was the collection of these first lists. Then I had to clean things a bit as there were many empty strings and many things which i didnt need. 

for j in x:
            if j:
                temp.append(j.strip())
                
This bit of code removed all the empty strings from the lists. And to locate the university all I needed was the coordinates of the location but I also decided to include the name so it was easier to see. From the bigger data of having all things like city etc all i needed was the coordinates and name, so I extracted the name and coordinates from the lists.

for i in universities:
        try:
            coord = i[5].split(',')
            udata.append({"name": i[1],"location": [float(coord[0]), float(coord[1])]})
        except:
            continue
            
This block of coded iterates over the sub lists in the bigger list called "universities". One problem I faced was that the coordinates were currently in the form of a string but i needed them in the form of a list containing float numbers. So I had to split them using the split() method of python. And the reason I used the try and except blocks are that some universities did not have any coordinates available in the website and therefore were causing problems so if the conversion of coordinates was succesful it was well and good but if it fails that is an exception is raised then i handled the exception and let the loop continue and skip that specific university. Then I put these data in a dictionary as it is what the JSON format is about. Now we have the data ready and now I want to send it to Javascript so that I can use the openlayers maps to display things. First thing what i did now was to separate this into a separate module so I made a module called univ.py so that it was easier to call it. 

Now A problem was faced that how do i communicate to Javascript. I did some research and found out that Flask was perfect for it, and i had a good amount of experience with Flask. Flask is basically a micro web framework for python which is easy and very fun to use. So i started a web server using Flask. I created a temporary route called "/data" where i would call the module to scrape the data for me. "/" is the route where I will be displalying the maps.

Now after the Flask server is set up. I had to start working on the javascript. This javascript will be running on my "/" route. I used the fetch API to fetch the data from the "/data" route.

@app.route("/data", methods=["GET", "POST"])
def data():
    message = universities_scraper()
    return jsonify(message)

Notice that I have set the methods as GET and POST. So when the fetch API requests for data the "/data" route will return(POST) the data and I used jsonify to convert that data into JSON.
After getting the data in the javascript I had to dynamically create headings and divs to accomodate the amount of locations.

var h2 = document.createElement("h2");
h2.innerHTML = json.d[i].name;
document.body.appendChild(h2);
var div = document.createElement("div");
div.id = json.d[i].name;
div.className = 'map';
document.body.appendChild(div);

These dynamically create h2 and divs with the id of the respective university's name.

var map = new ol.Map({
                        target: json.d[i].name,
                        layers: [
                            new ol.layer.Tile({
                                source: new ol.source.OSM()
                            })
                        ],
                        view: new ol.View({
                            center: ol.proj.fromLonLat(json.d[i].location),
                            zoom: 15
                        })
                    });

Then after creating the divs I loaded the maps using the openlayers library and for the location I called the Value of json.d.location as it is now a Javascript object which has attributes. 

And this is how I achieved communication between Python and Javscript to display the respective maps of the universities with there names.

This Task helped me a lot to learn new things. I learned a lot about web scraping and how to extract the exact data you want. I learned a lot about JSON parsing. And the most exciting thing was to make Python and Javascript communicate with each other. I learned new things like fetch API. And last but not the least learnt about some really cool libraries like Openlayers and how we could use it for a product.
