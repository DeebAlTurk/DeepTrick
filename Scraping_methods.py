import datetime
import json

from bs4 import BeautifulSoup


def convert_to_json(elms: dict, indent: int = 4):
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
        with open(f"{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.json", "w") as write_file:
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
    if negative:
        x: dict = {}
        for i in range(-1, len(elms) * -1, -1):
            # print(f"[{i}] {elms[i]}")
            x[i] = elms[i]
        for k in reversed(x.keys()):
            print(f"[{k}] {x[k]}")
        return
    else:
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

# def get_data_of(soup: BeautifulSoup, name: str, type: str, all_tag=True, is_url=False, offset: int = 0, attr: str = "",
#                 base_url: str = ""):
#     if all_tag and not is_url:
#         if type == "tag":
#             if len(soup.find_all(name)) < offset or len(soup.find_all(name)) * -1 > offset:
#                 offset = 0
#             if soup.find_all(name)[offset] is not None:
#                 return soup.find_all(name)[offset]
#             else:
#                 return None
#         elif type == "class":
#             if len(soup.find_all(class_=name)) < offset or len(soup.find_all(class_=name)) * -1 > offset:
#                 offset = 0
#             if soup.find_all(class_=name)[offset] is not None:
#                 return soup.find_all(class_=name)[offset]
#             else:
#                 return None
#         elif type == "selector":
#             if len(soup.select(name)) < offset or len(soup.select(name)) * -1 > offset:
#                 offset = 0
#             if soup.select(name)[offset] is not None:
#                 return soup.select(name)[offset]
#             else:
#                 return None
#
#     if not all_tag and attr != "":
#         if type == "tag":
#             if len(soup.find_all(name)) < offset or len(soup.find_all(name)) * -1 > offset:
#                 offset = 0
#             if soup.find_all(name)[offset] is not None and soup.find_all(name)[offset].has_attr(attr):
#                 if is_url and not url_methods.is_url_absolute(soup.find_all(name)[offset].get(attr)):
#                     return url_methods.get_full_url(base_url, soup.find_all(name)[offset].get(attr))
#             else:
#                 return soup.find_all(name)[offset].get(attr)
#         elif type == "class":
#             if len(soup.find_all(class_=name)) < offset or len(soup.find_all(class_=name)) * -1 > offset:
#                 offset = 0
#             if soup.find_all(class_=name)[offset] is not None and soup.find_all(class_=name)[offset].has_attr(attr):
#                 if is_url and not url_methods.is_url_absolute(soup.find_all(class_=name)[offset].get(attr)):
#                     return url_methods.get_full_url(base_url, soup.find_all(class_=name)[offset].get(attr))
#             else:
#                 return soup.find_all(class_=name)[offset].get(attr)
#         elif type == "selector":
#             if len(soup.select(name)) < offset or len(soup.select(name)) * -1 > offset:
#                 offset = 0
#             if soup.select(name)[offset] is not None and soup.select(name)[offset].has_attr(attr):
#                 if is_url and not url_methods.is_url_absolute(soup.select(name)[offset].get(attr)):
#                     return url_methods.get_full_url(base_url, soup.select(name)[offset].get(attr))
#             else:
#                 return soup.select(name)[offset].get(attr)
