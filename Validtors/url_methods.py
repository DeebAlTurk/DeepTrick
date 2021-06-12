import re
import urllib.parse

import requests


def get_full_url(base: str, relative: str):
    return urllib.parse.urljoin(base, relative)


def is_url_absolute(url: str):
    """
    this function checks if a url is absolute or relative
    :param url: the url you want to check
    :return: True if the url is absolute, False is the url is relative
    """
    return bool(urllib.parse.urlparse(url).netloc)


def check_url_format(url: str):
    """
    this parameter check if the string is a valid url or not
    :param url:
    :return: true if the url is has a valid format else it will return false
    """
    regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url = url.strip()
    x = re.fullmatch(regex, url)
    if x:
        res: bool = True
    else:
        res: bool = False

    return res


def check_url_exists(url: str):
    """
    :param url:
    :return: True if the url have incorrect format and exists on the internet
            False if the url have incorrect format or doesnt exist on the internet
    """
    res: bool = False
    user_agent = {'User-agent': 'Mozilla/5.0'}
    is_valid: bool = check_url_format(url)
    # the request.get function will return the response of the url
    # thus we can check if the statues if 200 the website is up and running
    try:
        requests.get(url, headers=user_agent)

    except:
        is_valid = False
    if is_valid and requests.get(url, headers=user_agent).status_code == 200:
        res = True

    return res
