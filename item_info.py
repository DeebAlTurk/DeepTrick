import time

from selenium import webdriver

import Validtors.url_methods as url
from Scraping_methods import *

# file = open("Item_links.json")
# links: dict = json.load(file)
# for key in links.keys():
#     print(str(links[key]))
with open('Item_links.json') as f:
    data = json.load(f)
base = "https://www.carrefouruae.com"
count = 0
links: list = []
target = {}
options: list = [0]
for key in data.keys():
    for i in data[key].split(","):
        links.append(
            url.get_full_url(base, str(i).replace('\'', "").replace('[', "").replace("]", "").replace(" ", '')))
        count += 1
browser = webdriver.Firefox()
count = len(links)
for link in links:
    browser.get(link)
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source, "lxml")
    # desc = {'label': str(soup.select_one('css-1i2z667')) + " desc", 'type': 'selector', 'name': '.css-a3q5me', 'exists': True,
    #         'isRange': 0, 'offset': 0, 'get_what': 'text'}
    img = {'label': str(soup.select_one('.css-1i2z667').text) + " img", 'type': 'selector',
           'name': '.swiper-lazy-loading',
           'exists': True, 'isRange': 1, 'start': 0, 'end': 0, 'get_what': 'attr', 'attr': 'src'}
    img['end'] = len(soup.select(".swiper-lazy-loading"))
    # options[0] = desc
    options[0] = img
    target = scraper(soup, options, target)
    count -= 1
    print(f"{count} left ")
    convert_dict_to_json(target, name="Desc")
