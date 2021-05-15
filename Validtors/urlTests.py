from Validtors.url_methods import *

assert check_url_format("www.google.com") == False
assert check_url_format("www.com.com") == False
assert check_url_format("https://realpython.com/python-testing/") == True
assert check_url_format("https://www.w3schools.com/python/python_try_except.asp") == True
assert check_url_format("https://www.zomato.com/beirut/diwan-mart-tariq-el-jdide-beirut-district") == True
assert check_url_format("https:/www.zomato.com/beirut/diwan-mart-tariq-el-jdide-beirut-district") == False
assert check_url_format("luluhypermarket.com/en-kw/") == False
assert check_url_format("https://www.luluhypermarket.com/en-kw//") == True
assert check_url_format("http://this.is.not.alink.com") == True
assert check_url_format("ftp://this.is.not.alink.net") == False
assert check_url_format("http://this.is.not.alink.xyz") == True
assert check_url_format("https://this.is.not.alink.xyz") == True

assert check_url_exists("https://www.luluhypermarket.com/en-kw/department-store-home-living-cooking-dinning/c/HY00216080") == True
assert check_url_exists("https://www.zomato.com/beirut/diwan-mart-tariq-el-jdide-beirut-district") == True
assert check_url_exists("https://https://www.zomato.com/beirut") == False
assert check_url_exists("https://www.crummy.com/software/BeautifulSoup/bs4/doc/") == True
assert check_url_exists("https://www.luluhypermarket.com/en-kw/grocery-fresh-food-fresh-food-bakery-cakes/c/HY00216097") == True
assert check_url_exists("http://111111111111111111111111111111111111111111111111111111111111.com/") == True
assert check_url_exists("https://aab1098.000webhostapp.com/uqu.edu.sa/Sso/Login.html") == True
assert check_url_exists("https://bit.ly/it_uqu") == True
