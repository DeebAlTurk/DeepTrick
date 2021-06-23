import json

import Validtors.url_methods as url

# file = open("Item_links.json")
# links: dict = json.load(file)
# for key in links.keys():
#     print(str(links[key]))
with open('Item_links.json') as f:
    data = json.load(f)
base = "https://www.carrefouruae.com"
count = 0
for key in data.keys():
    for i in data[key].split(","):
        print(url.get_full_url(base, str(i).replace('\'', "").replace('[', "").replace("]", "").replace(" ", '')))
        count += 1
