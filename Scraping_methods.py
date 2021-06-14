# imports
import datetime
import json

from bs4 import BeautifulSoup


def convert_list_of_dicts_to_json(elms: list, indet: int = 4, name=""):
    for item in list:
        for keys in dict(item).keys():
            item[keys] = str(item[keys])
    if name == "":
        filename: str = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        with open(f"{filename}.json", 'a') as write_file:
            json.dumps(elms, indent=indet)
    else:
        with open(f"{name}.json", 'a') as write_file:
            json.dumps(elms, indent=indet)


def convert_dict_to_json(elms: dict, indent: int = 4, name=""):
    """
    this function convert the dictionary into a json file
    the name of the json file will be the current date and time
    :param elms: the dict that contains the data that will be converted to a JSON file
    :param indent: the indention of the JSON by default it is equal to 4
    :return: True if successful, False if unsuccessful
    """
    try:
        for k in elms.keys():
            elms[k] = str(elms[k])
        if name == "":
            with open(f"{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.json", "w") as write_file:
                json.dump(elms, write_file, indent=indent)
        else:
            with open(f"{name}.json", "w") as write_file:
                json.dump(elms, write_file, indent=indent)

    except OSError:
        return False
    return True


def is_css_selector_available(soup: BeautifulSoup, selector: str):
    """
    this function checks if the css Selector is available in the page
    :param soup: the BS object that contains the page
    :param selector: the selector the need to be checked
    :return:True if the selector is found in the page, else False
    """
    if soup.select_one(selector) is None:
        return False
    return True


def indexer(elms: list, negative: bool = False):
    # this function takes a list and print the index of each item in that list
    # you can also print the negative index of the list
    for i in range(len(elms)):
        print(f'[{i}] {elms[i]}')


def is_range_correct(elms: list, start: int, end: int):
    """
    this function checks if the range your entered returns items or not
    :param elms: list to check
    :param start: the start index
    :param end: the last index
    :return: True if the lists returns items else False
    """
    if not elms[start:end]:
        return False
    return True


def is_offset_valid(elms: list, offset: int):
    """
    this function returns if the offset is valid or not (in index of the range of the list)
    :type offset: object
    :param elms: the list to check
    :param offset: the index to check
    :return: True if the index is correct , otherwise False
    """
    max_length: int = len(elms)
    max_negative: int = len(elms) * -1
    if offset in range(max_negative, max_length):
        return True
    return False


def get_count(soup: BeautifulSoup, target_type: str, name: str):
    """
    this function get the count of a specific tag or class found in that page
    :param soup: the BS object that contains the content of the page
    :param target_type: the type of the search if it is for a tag or a class
    :param name: the name of tag/tag
    :returns:
      0   : tag or class is doesnt exist is the page
     -1  :  type is incorrect
    >=1 : the count of tag/class
    """
    res = 0
    if target_type == "tag":
        if is_tag_available(soup, name):
            res = len(soup.find_all(name))
    elif target_type == "class":
        if is_class_available(soup, name):
            res = len(soup.find_all(class_=name))
    else:
        res = -1
    return res


def is_class_available(soup: BeautifulSoup, cname: str):
    """
    this function checks if the class is exists or not
    :param soup: the BS object that contains the content of the page
    :param cname: the name of the class
    :return: True if the class exists in the page, False if the class doesnt exist
    """
    if soup.find(class_=cname):
        return True
    else:
        return False


def is_tag_available(soup: BeautifulSoup, tag: str):
    """
    this function checks if the tag is exists or not in the page
    :param soup: the BS object that contains the page
    :param tag: the tag name
    :return: True if the tag exists, False if the tag doesnt exist
    """
    if soup.find(tag):
        return True
    else:
        return False


def get_attr_of_tag(soup: BeautifulSoup, tag: str, attr: str, offset: int = 0):
    """
    the functions grabs attr of the targeted tag
    :param attr: the targeted attribute
    :param soup: the BS object that contains the page
    :param tag: the tag you want extract from the href
    :param offset: the index of the tag, Optional, if it is out of range it will be equal to 0
    :return: a string that contains the value of the attribute if attr not available it will return None
    """
    if len(soup.find_all(tag)) < offset or len(soup.find_all(tag)) * -1 > offset:
        offset = 0
    if soup.find_all(tag)[offset].has_attr(attr):
        return soup.find_all(tag)[offset].get(attr)
    else:
        return None


def get_attr_of_class(soup: BeautifulSoup, cname: str, attr: str, offset: int = 0):
    """
    this function grabs the attr of the targeted class
    :param attr: the attr you want to grav
    :param soup: the BS object that contains the page
    :param cname: the class name you want to extract from the attr
    :param offset: the index of the class, Optional, if it is out of range it will be equal to 0
    :return: a string that contains the attr of the class if the class doesnt contain a href it will return None
    """
    if len(soup.find_all(class_=cname)) < offset or len(soup.find_all(class_=cname)) * -1 > offset:
        offset = 0
    if soup.find_all(class_=cname)[offset].has_attr(attr):
        return soup.find_all(class_=cname)[offset].get(attr)
    return None


def get_attr_of_selector(soup: BeautifulSoup, selector: str, attr: str, offset: int = 0):
    """
    this function grabs the attr of the targeted selector
    :param attr: the attr you want to grav
    :param soup: the BS object that contains the page
    :param selector: the selector name you want to extract from the attr
    :param offset: the index of the selector, Optional, if it is out of range it will be equal to 0
    :return: a string that contains the attr of the selector if the selector doesnt contain a href it will return None
    """
    if len(soup.select(selector)) < offset or len(soup.select(selector)) * -1 > offset:
        offset = 0
    if soup.select(selector)[offset].has_attr(attr):
        return soup.select(selector)[offset].get(attr)
    return None


def get_attr_list_of_tags(soup: BeautifulSoup, name: str, attr: str, start: int, end: int):
    """
    this function get the list of attr value of a bs4 result
    :param soup: Beautiful soup object that contains the page content
    :param name: the name of the tag
    :param attr: the targeted attr
    :param start: the start index
    :param end: the last index
    :return: An list that contain the attr value of the tag, if the attr is not present then it will return None
    """
    result: list = []
    lst = soup.find_all(name)[start:end]
    for x in lst:
        if x.has_attr(attr):
            result.append(x.get(attr))
    if len(result) == 0:
        return None
    return result


def get_attr_list_of_class(soup: BeautifulSoup, name: str, attr: str, start: int, end: int):
    """
    this function get the list of attr value of a bs4 result
    :param soup: Beautiful soup object that contains the page content
    :param name: the name of the class
    :param attr: the targeted attr
    :param start: the start index
    :param end: the last index
    :return: An list that contain the attr value of the class, if the attr is not present then it will return None
    """
    result: list = []
    lst = soup.find_all(class_=name)[start:end]
    for x in lst:
        if x.has_attr(attr):
            result.append(x.get(attr))
    if len(result) == 0:
        return None
    return result


def get_attr_list_of_selector(soup: BeautifulSoup, name: str, attr: str, start: int, end: int):
    """
    this function get the list of attr value of a bs4 result
    :param soup: Beautiful soup object that contains the page content
    :param name: the name of the selector
    :param attr: the targeted attr
    :param start: the start index
    :param end: the last index
    :return: An list that contain the attr value of the selector, if the attr is not present then it will return None
    """
    result: list = []
    lst = soup.select(name)[start:end]
    for x in lst:
        if x.has_attr(attr):
            result.append(x.get(attr))
    if len(result) == 0:
        return None
    return result


def get_text_list_of_tags(soup: BeautifulSoup, name: str, start: int, end: int):
    """
    this function get the list of inner text  of a bs4 result
    :param soup: Beautiful soup object that contains the page content
    :param name: the name of the tag
    :param start: the start index
    :param end: the last index
    :return: An list that contain the inner text value of the tag, if not found None
    """
    result: list = []
    lst = soup.find_all(name)[start:end]
    for x in lst:
        result.append(x.text.strip())
    if len(result) == 0:
        return None
    return result


def get_text_list_of_class(soup: BeautifulSoup, name: str, start: int, end: int):
    """
    this function get the list of inner text  of a bs4 result
    :param soup: Beautiful soup object that contains the page content
    :param name: the name of the class
    :param start: the start index
    :param end: the last index
    :return: An list that contain the inner text value of the class, if not found None
    """
    result: list = []
    lst = soup.find_all(class_=name)[start:end]
    for x in lst:
        result.append(x.text.strip())
    if len(result) == 0:
        return None
    return result


def get_text_list_of_selector(soup: BeautifulSoup, name: str, start: int, end: int):
    """
    this function get the list of inner text  of a bs4 result
    :param soup: Beautiful soup object that contains the page content
    :param name: the name of the selector
    :param start: the start index
    :param end: the last index
    :return:An list that contain the inner text value of the selector,if not found None
    """
    result: list = []
    lst = soup.select(name)[start:end]
    for x in lst:
        result.append(x.text.strip())
    if len(result) == 0:
        return None
    return result


def scraper(current_page: BeautifulSoup, options_list: list, target: dict):
    for options in options_list:
        if options["isRange"] == 0:
            if options["type"] == "tag":
                if options["get_what"] == "attr":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            get_attr_of_tag(current_page, options["name"], options["attr"],
                                            options["offset"]))
                    else:
                        if get_attr_of_tag(current_page, options["name"], options["attr"],
                                           options["offset"]) is not None:
                            target[options["label"]] = str(
                                get_attr_of_tag(current_page, options["name"], options["attr"],
                                                options["offset"]))
                elif options["get_what"] == "text":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            current_page.find_all(options["name"])[options['offset']].text).strip()
                    else:
                        target[options["label"]] = str(
                            current_page.find_all(options["name"])[options['offset']].text).strip()
                else:
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            current_page.find_all(options["name"])[options['offset']])
                    else:
                        target[options["label"]] = str(current_page.find_all(options["name"])[options['offset']])

            elif options["type"] == "class":
                if options["get_what"] == "attr":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            get_attr_of_class(current_page, options["name"], options["attr"],
                                              options["offset"]))
                    else:
                        if get_attr_of_class(current_page, options["name"], options["attr"],
                                             options["offset"]) is not None:
                            target[options["label"]] = str(
                                get_attr_of_class(current_page, options["name"], options["attr"],
                                                  options["offset"]))
                elif options["get_what"] == "text":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            current_page.find_all(class_=options["name"])[options["offset"]].text).strip()
                    else:
                        target[options["label"]] = str(
                            current_page.find_all(class_=options["name"])[options["offset"]].text).strip()
                else:
                    if target.__contains__(options["label"]):
                        target[options["label"]] = target[options["label"]] + "\n" + str(
                            current_page.find_all(class_=options["name"])[options['offset']])
                    else:
                        target[options["label"]] = str(current_page.find_all(class_=options["name"])[options['offset']])

            elif options["type"] == "selector":
                if options["get_what"] == "attr":
                    if target.__contains__(options["label"]):
                        target[options["label"]] = target[options["label"]] + "\n" + str(
                            get_attr_of_selector(current_page, options["name"], options["attr"], options["offset"]))
                    else:
                        if get_attr_of_selector(current_page, options["name"], options["attr"],
                                                options["offset"]) is not None:
                            target[options["label"]] = str(
                                get_attr_of_selector(current_page, options["name"], options["attr"], options["offset"]))
                elif options["get_what"] == "text":
                    if target.__contains__(options["label"]):
                        target[options["label"]] = target[options["label"]] + "\n" + str(
                            current_page.select(options["name"])[options["offset"]].text).strip()
                    else:
                        target[options["label"]] = str(
                            current_page.select(options["name"])[options["offset"]].text).strip()
                else:
                    if target.__contains__(options["label"]):
                        target[options["label"]] = target[options["label"]] + "\n" + str(
                            current_page.select(options["name"])[options["offset"]])
                    else:
                        target[options["label"]] = str(current_page.select(options["name"])[options["offset"]])

        else:
            if options["type"] == "tag":
                if options["get_what"] == "tag":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            current_page.find_all(options["name"])[options["start"]:options["end"]])
                    else:
                        target[options["label"]] = str(
                            current_page.find_all(options["name"])[options["start"]:options["end"]])
                elif options["get_what"] == "attr":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            get_attr_list_of_tags(current_page, options["name"], options["attr"], options["start"],
                                                  options["end"]))
                    else:
                        target[options["label"]] = str(
                            get_attr_list_of_tags(current_page, options["name"], options["attr"], options["start"],
                                                  options["end"]))
                elif options["get_what"] == "text":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            get_text_list_of_tags(current_page, options["name"], options["start"],
                                                  options["end"]))
                    else:
                        target[options["label"]] = str(
                            get_text_list_of_tags(current_page, options["name"], options["start"],
                                                  options["end"]))
            elif options["type"] == "class":
                if options["get_what"] == "tag":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            current_page.find_all(options["name"])[options["start"]:options["end"]])
                    else:
                        target[options["label"]] = str(
                            current_page.find_all(options["name"])[options["start"]:options["end"]])
                elif options["get_what"] == "attr":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            get_attr_list_of_class(current_page, options["name"], options["attr"], options["start"],
                                                   options["end"]))
                    else:
                        target[options["label"]] = str(
                            get_attr_list_of_class(current_page, options["name"], options["attr"], options["start"],
                                                   options["end"]))
                elif options["get_what"] == "text":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            get_text_list_of_class(current_page, options["name"], options["start"],
                                                   options["end"]))
                    else:
                        target[options["label"]] = str(
                            get_text_list_of_class(current_page, options["name"], options["start"],
                                                   options["end"]))
            elif options["type"] == "selector":
                if options["get_what"] == "tag":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            current_page.select(options["name"])[options["start"]:options["end"]])
                    else:
                        target[options["label"]] = str(
                            current_page.select(options["name"])[options["start"]:options["end"]])
                elif options["get_what"] == "attr":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(
                            get_attr_list_of_selector(current_page, options["name"], options["attr"], options["start"],
                                                      options["end"]))
                    else:
                        target[options["label"]] = str(
                            get_attr_list_of_selector(current_page, options["name"], options["attr"], options["start"],
                                                      options["end"]))
                elif options["get_what"] == "text":
                    if target.__contains__(options["label"]):
                        target[options["label"]] += "\n" + str(get_text_list_of_selector(current_page, options["name"],
                                                                                         options["start"],
                                                                                         options["end"]))
                    else:
                        target[options["label"]] = str(get_text_list_of_selector(current_page, options["name"],
                                                                                 options["start"],
                                                                                 options["end"]))
    return target
