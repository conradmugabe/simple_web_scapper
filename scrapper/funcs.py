import requests
from bs4 import BeautifulSoup


def readTextFile(file_path):
    """
    takes a txt file and returns a list text in the file

    param -> string: takes file path

    return -> list: list of contents in file
    """
    try:
        file_contents = []
        with open(file_path, "r") as file:
            contents = file.readlines()
            for content in contents:
                file_contents.append(content.strip())

        return file_contents
    except FileNotFoundError as err:
        return err


def writeTextFile(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return True
    except FileNotFoundError as err:
        return err


def appendFile(file_name, content, more_content):
    try:
        with open(file_name, "a") as file:
            file.write(content + " : " + more_content + "\n")
    except FileNotFoundError as err:
        return err


def mapTwoListsToDic(list_one, list_two):
    if len(list_one) != len(list_two):
        return False
    else:
        new_dict = {}
        i = 0
        while i < len(list_one):
            new_dict[list_one[i]] = list_two[i]
            i += 1

    return new_dict


def getWebsiteStatus(website_name, search=None):
    """
    param1: takes website_url

    param2: optional (search to be done on the website)

    return: returns dict with status code and website content
    """
    webiste_status = {"succedded": False, "content": None}
    if search:
        website_name = website_name + "/search"
        response = requests.get(website_name, params={"q": search})
    else:
        response = requests.get(website_name)
    status = response.status_code
    if status == 200:
        webiste_status["succedded"] = True
        webiste_status["content"] = response.content

    return webiste_status


def linksOnWebsite(webiste_status_dic):
    """
    param: takes a dict with website content

    return: list of urls on the site
    """
    urls = []
    soup = BeautifulSoup(webiste_status_dic["content"], "lxml")
    for link in soup.find_all("a"):
        urls.append(link.get("href"))

    return urls


def getUrlWithRegex(url_list):
    all_urls = []
    for url in url_list:
        if "q=http" in url:
            url = url[url.find("=") + 1 :]
            all_urls.append(url)
    return all_urls


def getFacebookUrlInList(url_list):
    """
    """
    facebook_urls = []
    for url in url_list:
        if "https://www.facebook.com" in url:
            url = url[: url.rindex("/")]
            facebook_urls.append(url)

    return facebook_urls


def facebookAboutPageUrl(webiste_status_dic):
    urls = []
    soup = BeautifulSoup(webiste_status_dic["content"], "lxml")
    for link in soup.find_all("a"):
        if "About" in link.text:
            urls.append(link.get("href"))

    return urls


def getEmailFromFacebookAboutPage(webiste_status_dic):
    soup = BeautifulSoup(webiste_status_dic["content"], "lxml")
    for link in soup.find_all("a"):
        if "@" in link.text:
            return link.text
    return None


def addFacebookUrlToUrl(urls):
    """
    adds string to first index of list

    para -> list: list of primitive data types

    return -> str: concatentated string
    """
    try:
        return "https://facebook.com/pg" + str(urls[0])
    except IndexError:
        return None
