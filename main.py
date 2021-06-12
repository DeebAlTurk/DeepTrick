from time import sleep

from selenium import webdriver

from Scraping_methods import *
from Validtors.url_methods import *

url = input("please enter a valid URL : ")
if not check_url_exists(url):
    print("Invalid URL")
    exit("Exiting Deep Trick")

browser = webdriver.Firefox()
browser.get(url)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(10)
# the user agent to mimic access websites that doesnt allow the default user agent of the BS
user_agent = {'User-agent': 'Mozilla/5.0'}
# the response of the get request the was sent
# response = requests.get(url, headers=user_agent)
# the BS object that contain the HTML of the page
current_page = BeautifulSoup(browser.page_source, 'lxml')
# print the page because some websites like Zomato changes the CSS classes with each request
# the prettify method to make the html for readable
print(current_page.prettify())
# the output of the single page mode is here
target: dict = {}
# the options for the multi page mode is here
options_list: list = []
# the out of the multi page mode is here
targets_list: list = []
# contains the option of the next link
next_link_options: dict = {}
next_link = ""
# options of the targeted item
options: dict = {}
print("Type of scraping")
# interact with the page
print("[0]=> one page only")
print("[1]=> multiple pages")
scraping_type: int = 0
try:
    scraping_type = int(input("choose one : "))
except ValueError:
    print("invalid input")
    exit("Exiting Deep Trick")
print("To Exit type EXIT_NOW in the label of the item")
while scraping_type not in [0, 1]:
    try:
        scraping_type = int(input("choose one"))
    except ValueError:
        print("invalid input")
        exit("Exiting Deep Trick")
if scraping_type == 1:
    print(" the next link is a ?")
    print("[0]=> Tag ")
    print("[1]=> Class ")
    print("[2]=> CSS Selector ")
    user_input = ""
    # if the user tries to enter a string or something other than a int the script will exit with an -1 statues
    try:
        user_input = int(input("Choose one : "))
    except ValueError:
        print("invalid input")
        exit("Exiting Deep Trick")
    # if the user enter an in other than 0 1 2, the user will be stuck in a loop until he/she enter a valid option
    while user_input not in [0, 1, 2]:
        try:
            user_input = int(input("choose only 0 or 1 or 2: "))
        except ValueError:
            print("invalid input")
            exit("Exiting Deep Trick")
    # the type of the next link
    if user_input == 0:
        next_link_options["type"] = "tag"
    elif user_input == 1:
        next_link_options["type"] = "class"
    elif user_input == 2:
        next_link_options["type"] = "selector"

    # getting the name of the target
    user_input = str(input(f"enter the {next_link_options['type']} name : "))
    # stripping the leading and ending spaces
    next_link_options["name"] = user_input.strip()
    # checking if the target is available in the HTML
    if next_link_options["type"] == "tag":
        next_link_options["exists"] = is_tag_available(current_page, next_link_options["name"])
        if next_link_options["exists"]:
            # print all the targeted tags
            indexer(current_page.find_all(next_link_options["name"]), True)
    elif next_link_options["type"] == "class":
        next_link_options["exists"] = is_class_available(current_page, next_link_options["name"])
        if next_link_options["exists"]:
            # print all the targeted classes
            indexer(current_page.find_all(class_=next_link_options["name"]), True)
    elif next_link_options["type"] == "selector":
        next_link_options["exists"] = is_css_selector_available(current_page, next_link_options["name"])
        if next_link_options["exists"]:
            indexer(current_page.select(next_link_options["name"]), True)

    if not next_link_options["exists"]:
        print(f"This {next_link_options['type']} Doesnt exists")
    # getting the offset of the target, it can be in negative because this is python
    # validating the user input
    try:
        user_input = int(input("enter the offset (by default 0) : ") or 0)
    except ValueError:
        print("invalid input")
        exit("Exiting Deep Trick")
    next_link_options["offset"] = user_input

    user_input = input("Enter the attribute you want to get from the target : ")
    next_link_options["attr"] = user_input

    # if the next link the link using the attr
    if next_link_options["exists"]:
        if next_link_options["type"] == "tag" and get_attr_of_tag(current_page, next_link_options["name"],
                                                                  next_link_options["attr"]) is not None:
            next_link = get_attr_of_tag(current_page, next_link_options["name"], next_link_options["attr"],
                                        next_link_options["offset"])
        elif next_link_options["type"] == "class" and get_attr_of_class(current_page, next_link_options["name"],
                                                                        next_link_options["attr"]) is not None:
            next_link = get_attr_of_class(current_page, next_link_options["name"], next_link_options["attr"],
                                          next_link_options["offset"])
        elif next_link_options["type"] == "selector" and get_attr_of_selector(current_page, next_link_options["name"],
                                                                              next_link_options["attr"]) is not None:
            next_link = get_attr_of_selector(current_page, next_link_options["name"], next_link_options["attr"],
                                             next_link_options["offset"])

    if check_url_exists(get_full_url(url, next_link)):
        next_link = get_full_url(url, next_link)
    else:
        print("failed to get next link check your input")
        next_link = url

# Phase 2
# TODO split the loops one for gathering option another for scraping the pages automatically

while scraping_type == 0:
    # getting user input
    user_input = str(input("enter the label of the item : "))
    if user_input == "EXIT_NOW":
        break
    options["label"] = user_input
    print("Choose one : ")
    print("[0]=> Tag ")
    print("[1]=> Class ")
    print("[2]=> CSS Selector ")
    try:
        user_input = int(input("Choose one : "))
    except ValueError:
        print("invalid input")
        continue

    while user_input not in [0, 1, 2]:
        try:
            user_input = int(input("choose only 0 or 1 or 2 : "))
        except ValueError:
            print("invalid input")
            continue
    if user_input == 0:
        options["type"] = "tag"
    elif user_input == 1:
        options["type"] = "class"
    elif user_input == 2:
        options["type"] = "selector"
    user_input = str(input(f"enter {options['type']} name : "))
    options["name"] = user_input
    if options["type"] == "tag":
        options["exists"] = is_tag_available(current_page, options["name"])
    elif options["type"] == "class":
        options["exists"] = is_class_available(current_page, options["name"])
    elif options["type"] == "selector":
        options["exists"] = is_css_selector_available(current_page, options["name"])
    if not options["exists"]:
        print(f"{options['name']} does not exist in the page")
        continue

    show_index = str(input("show tags that satisfies the target (y or n)"))
    if show_index in ['n', 'y', 'N', 'Y']:
        if show_index in ['Y', 'y']:
            if options["type"] == 'tag':
                indexer(current_page.find_all(options["name"]))
            elif options["type"] == 'class':
                indexer(current_page.find_all(class_=options["name"]))
            else:
                indexer(current_page.select(options["name"]))
    print("choose one : ")
    print("[0]=> one element")
    print("[1]=> range ")
    try:
        user_input = int(input("Choose one : "))
    except ValueError:
        print("invalid input")
        continue

    while user_input not in [0, 1]:
        try:
            user_input = int(input("choose only 0 or 1 : "))
        except ValueError:
            print("invalid input")
            continue
    options["isRange"] = user_input
    if options["isRange"] == 1:
        try:
            start_index = int(input("enter start index"))
            end_index = int(input("enter end index (exclusive)"))
            options["start"] = start_index
            options["end"] = end_index
            if options["type"] == "tag":
                if not is_range_correct(current_page.find_all(options["name"]), start_index, end_index):
                    raise ValueError
            elif options["type"] == "class":
                if not is_range_correct(current_page.find_all(class_=options["name"]), start_index, end_index):
                    raise ValueError
            elif options["type"] == "selector":
                if not is_range_correct(current_page.select(options["name"]), start_index, end_index):
                    raise ValueError
        except ValueError:
            print("invalid range")
            continue
    else:
        try:
            user_input = int(input("enter the offset (by default 0) : ") or 0)
            options["offset"] = user_input
        except ValueError:
            print("invalid input")
            continue
    # user_input = str(input('enter the name of the attribute you want to get (for all tag enter 0) ') or "0")
    print("[0]=> all tag ")
    print("[1]=> an attribute ")
    print("[2]=> inner text only ")
    try:
        user_input = int(input("choose one : ") or 0)
        if user_input not in [0, 1, 2]:
            raise ValueError
        else:
            if user_input == 0:
                options["get_what"] = "tag"
            elif user_input == 1:
                options["get_what"] = "attr"
            elif user_input == 2:
                options["get_what"] = "text"
    except ValueError:
        print("invalid input")
        continue
    if options["get_what"] == "attr":
        options["attr"] = input("enter attribute name ")
    if options["isRange"] == 0:
        if options["type"] == "tag":
            if options["get_what"] == "attr":
                if get_attr_of_tag(current_page, options["name"], options["attr"], options["offset"]) is not None:
                    target[options["label"]] = get_attr_of_tag(current_page, options["name"], options["attr"],
                                                               options["offset"])
            elif options["get_what"] == "text":
                target[options["label"]] = str(current_page.find_all(options["name"])[options['offset']].text).strip()
            else:
                target[options["label"]] = str(current_page.find_all(options["name"])[options['offset']])
        elif options["type"] == "class":
            if options["get_what"] == "attr":
                if get_attr_of_class(current_page, options["name"], options["attr"], options["offset"]) is not None:
                    target[options["label"]] = get_attr_of_class(current_page, options["name"], options["attr"],
                                                                 options["offset"])
            elif options["get_what"] == "text":
                target[options["label"]] = str(
                    current_page.find_all(class_=options["name"])[options["offset"]].text).strip()
            else:
                target[options["label"]] = str(current_page.find_all(class_=options["name"])[options['offset']])
        elif options["type"] == "selector":
            if options["get_what"] == "attr":
                if get_attr_of_selector(current_page, options["name"], options["attr"], options["offset"]) is not None:
                    target[options["label"]] = get_attr_of_selector(current_page, options["name"], options["attr"],
                                                                    options["offset"])
            elif options["get_what"] == "text":
                target[options["label"]] = str(current_page.select(options["name"])[options["offset"]].text).strip()
            else:
                target[options["label"]] = str(current_page.select(options["name"])[options["offset"]])
    else:
        if options["type"] == "tag":
            if options["get_what"] == "tag":
                target[options["label"]] = str(current_page.find_all(options["name"])[options["start"]:options["end"]])
            elif options["get_what"] == "attr":
                target[options["label"]] = str(
                    get_attr_list_of_tags(current_page, options["name"], options["attr"], options["start"],
                                          options["end"]))
            elif options["get_what"] == "text":
                target[options["label"]] = get_text_list_of_tags(current_page, options["name"], options["start"],
                                                                 options["end"])
        elif options["type"] == "class":
            if options["get_what"] == "tag":
                target[options["label"]] = str(current_page.find_all(options["name"])[options["start"]:options["end"]])
            elif options["get_what"] == "attr":
                target[options["label"]] = str(
                    get_attr_list_of_class(current_page, options["name"], options["attr"], options["start"],
                                           options["end"]))
            elif options["get_what"] == "text":
                target[options["label"]] = get_text_list_of_class(current_page, options["name"], options["start"],
                                                                  options["end"])
        elif options["type"] == "selector":
            if options["get_what"] == "tag":
                target[options["label"]] = str(current_page.select(options["name"])[options["start"]:options["end"]])
            elif options["get_what"] == "attr":
                target[options["label"]] = str(
                    get_attr_list_of_selector(current_page, options["name"], options["attr"], options["start"],
                                              options["end"]))
            elif options["get_what"] == "text":
                target[options["label"]] = get_text_list_of_selector(current_page, options["name"], options["start"],
                                                                     options["end"])

    options.clear()
    print("[0]=> continue")
    print("[1]=> print the output so far")
    print("[2]=> change the current page")
    print("[3]=> end")
    try:
        user_input = int(input("Choose one : "))
    except ValueError:
        print("invalid input")
        continue
    while user_input not in [0, 1, 2, 3]:
        try:
            user_input = int(input("Choose only from 0, 1 ,2 ,3 : "))
        except ValueError:
            print("invalid input")
            continue
    if user_input == 1:
        for key in target.keys():
            print(f"{key} : {target[key]}")
    elif user_input == 2:
        url = input("please enter a valid new URL : ")
        if not check_url_exists(url):
            print("Invalid URL")
            continue
        response = requests.get(url, headers=user_agent)
        current_page = BeautifulSoup(response.content, 'lxml')
    elif user_input == 3:
        print("Exiting")
        break
if scraping_type == 0:
    if not convert_dict_to_json(target):
        exit("UNABLE TO SAVE TO JSON")

while scraping_type == 1:
    print("to exit enter the label EXIT_NOW")
    # getting user input
    user_input = str(input("enter the label of the item : "))
    if user_input == "EXIT_NOW":
        break
    options["label"] = user_input
    print("Choose one : ")
    print("[0]=> Tag ")
    print("[1]=> Class ")
    print("[2]=> CSS Selector ")
    try:
        user_input = int(input("Choose one : "))
    except ValueError:
        print("invalid input")
        continue

    while user_input not in [0, 1, 2]:
        try:
            user_input = int(input("choose only 0 or 1 or 2 : "))
        except ValueError:
            print("invalid input")
            continue
    if user_input == 0:
        options["type"] = "tag"
    elif user_input == 1:
        options["type"] = "class"
    elif user_input == 2:
        options["type"] = "selector"
    user_input = str(input(f"enter {options['type']} name : "))
    options["name"] = user_input
    if options["type"] == "tag":
        options["exists"] = is_tag_available(current_page, options["name"])
    elif options["type"] == "class":
        options["exists"] = is_class_available(current_page, options["name"])
    elif options["type"] == "selector":
        options["exists"] = is_css_selector_available(current_page, options["name"])
    if not options["exists"]:
        print(f"{options['name']} does not exist in the page")
        continue

    show_index = str(input("show tags that satisfies the target (y or n)"))
    if show_index in ['n', 'y', 'N', 'Y']:
        if show_index in ['Y', 'y']:
            if options["type"] == 'tag':
                indexer(current_page.find_all(options["name"]))
            elif options["type"] == 'class':
                indexer(current_page.find_all(class_=options["name"]))
            else:
                indexer(current_page.select(options["name"]))
    print("choose one : ")
    print("[0]=> one element")
    print("[1]=> range ")
    try:
        user_input = int(input("Choose one : "))
    except ValueError:
        print("invalid input")
        continue

    while user_input not in [0, 1]:
        try:
            user_input = int(input("choose only 0 or 1 : "))
        except ValueError:
            print("invalid input")
            continue
    options["isRange"] = user_input
    if options["isRange"] == 1:
        try:
            start_index = int(input("enter start index"))
            end_index = int(input("enter end index (exclusive)"))
            options["start"] = start_index
            options["end"] = end_index
            if options["type"] == "tag":
                if not is_range_correct(current_page.find_all(options["name"]), start_index, end_index):
                    raise ValueError
            elif options["type"] == "class":
                if not is_range_correct(current_page.find_all(class_=options["name"]), start_index, end_index):
                    raise ValueError
            elif options["type"] == "selector":
                if not is_range_correct(current_page.select(options["name"]), start_index, end_index):
                    raise ValueError
        except ValueError:
            print("invalid range")
            continue
    else:
        try:
            user_input = int(input("enter the offset (by default 0) : ") or 0)
            options["offset"] = user_input
        except ValueError:
            print("invalid input")
            continue
    # user_input = str(input('enter the name of the attribute you want to get (for all tag enter 0) ') or "0")
    print("[0]=> all tag ")
    print("[1]=> an attribute ")
    print("[2]=> inner text only ")
    try:
        user_input = int(input("choose one : ") or 0)
        if user_input not in [0, 1, 2]:
            raise ValueError
        else:
            if user_input == 0:
                options["get_what"] = "tag"
            elif user_input == 1:
                options["get_what"] = "attr"
            elif user_input == 2:
                options["get_what"] = "text"
    except ValueError:
        print("invalid input")
        continue
    if options["get_what"] == "attr":
        options["attr"] = input("enter attribute name ")
    options_list.append(options.copy())
    options.clear()
    for x in options_list:
        print(x)
old_links = []
del options
try:
    print("zero depth (scrap until it reach the max)")
    depth: int = int(input("enter the depth of the search") or 0)
except ValueError:
    exit("Depth >= 0")
count: int = 0

while scraping_type == 1:
    if count == depth and depth != 0:
        break
    # TODO add append
    target = scraper(current_page, options_list, target)
    # check if the next link exists
    if next_link_options["type"] == "tag":
        next_link_options["exists"] = is_tag_available(current_page, next_link_options["name"])
    elif next_link_options["type"] == "class":
        next_link_options["exists"] = is_class_available(current_page, next_link_options["name"])
    elif next_link_options["type"] == "selector":
        next_link_options["exists"] = is_css_selector_available(current_page, next_link_options["name"])
    # get the next link
    try:
        if next_link_options["exists"]:
            if next_link_options["type"] == "tag":
                next_link = get_attr_of_tag(current_page, next_link_options["name"], next_link_options["attr"],
                                            next_link_options["offset"])
            elif next_link_options["type"] == "class":
                next_link = get_attr_of_class(current_page, next_link_options["name"], next_link_options["attr"],
                                              next_link_options["offset"])
            elif next_link_options["type"] == "selector":
                next_link = get_attr_of_selector(current_page, next_link_options["name"], next_link_options["attr"],
                                                 next_link_options["offset"])
    except ValueError:
        exit("INVALID OFFSET")
    next_link = get_full_url(url, next_link)
    # if next_link in old_links:
    #     print("Done")
    #     break
    if next_link_options["exists"]:
        # response = requests.get(next_link, headers=user_agent)
        browser.get(url)
        old_links.append(next_link)
        # current_page = BeautifulSoup(response.content, 'lxml')
        current_page = BeautifulSoup(browser.page_source, 'lxml')
    print(next_link)
    count += 1
for x in target.keys():
    print(f"{x} => {target[x]}")
convert_dict_to_json(target, 4)
