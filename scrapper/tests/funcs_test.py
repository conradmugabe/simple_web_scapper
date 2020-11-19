import pytest

from scrapper import funcs


def test_readTextFile():
    print("Started readTextFile")
    test = funcs.readTextFile("./scrapper/tests/test_data/test_readtext.txt")

    prepare = ["new vision", "daily monitor", "cafe javas"]

    assert test == prepare
    print("Finished testing readTextFile")


def test_readtextException():
    print("Started readTextFile")
    path = "./test_data/something.txt"

    test = funcs.readTextFile(path)

    assert test is None
    print("Finished testing readTextFile")


def test_writeTextFile():
    print("Started writeTextFile")
    content = "hello world how are you?"
    path = "./scrapper/tests/test_data/test_writetextfile.txt"
    test = funcs.writeTextFile(path, content)

    assert test is True
    print("Finished testing writeTextFile")


def test_writeTextFileException():
    print("started writeTextFile")
    content = "hello world how are you?"
    path = "./scrapper/test_test_data/test_writetextfile.txt"

    test = funcs.writeTextFile(path, content)

    assert test is None
    print("finished tetsing writeTextFile")


def test_appendFile():
    print("started appendFile")
    path = "./scrapper/tests/test_data/test_appendtextfile"
    company_name = "company name"
    email = "company email"

    test = funcs.appendFile(path, company_name, email)

    assert test is True
    print("Finished testing appendFile")


def test_appendFileException():
    print("Started appendFile")
    path = "./scrapper/tests_test_data/test_appendtextfile"
    company_name = "company name"
    email = "company email"

    test = funcs.appendFile(path, company_name, email)

    assert test is None
    print("Finished testing appendFile")


def test_mapTwoListsToDic():
    print("started mapTwoListsToDic")
    list_one = [1, 2, 3, 4]
    list_two = ["hey", "how", "them", "user"]

    answer_one = funcs.mapTwoListsToDic(list_one, list_two)

    assert answer_one == {1: "hey", 2: "how", 3: "them", 4: "user"}
    print("Finished testing mapTwoListsToDic")


def test_mapTwoListsToDicFail():
    print("started mapTwoListsToDic")
    list_one = [1, 2, 3, 4]
    list_three = ["user", "other", "james"]

    answer_two = funcs.mapTwoListsToDic(list_one, list_three)

    assert answer_two is False
    print("Finished testing mapTwoListsToDic")


def test_getWebsiteStatus():
    print("started testing getWebisteStatus")
    print("finished testing getWebsiteStatus")
    pass


def test_linksOnWebsite():
    print("started testing linksOnWebsite")
    html_string = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>
        <a href="./login.html">log in</a>
        <a href="./logout.html">log out</a>
        </body>
        </html>
    """
    content_dict = {"content": html_string}
    urls = funcs.linksOnWebsite(content_dict)
    expected_result = ["./login.html", "./logout.html"]
    assert urls == expected_result
    print("finished testing linksOnWebiste")


def test_getUrlWithRegex():
    print("started getUrlWithRegex")

    url_list = ["heli1q=httpjjknrkjz"]
    answer = funcs.getUrlWithRegex(url_list)

    assert answer == ["httpjjknrkjz"]
    print("started testing getUrlWithRegex")


def test_getFacebookUrlInList():
    print("started getFacebookUrlInLists")
    facebook_url = "https://www.facebook.com"
    twitter_url = "https://www.twitter.com"
    url_list = [
        twitter_url + "/doe",
        facebook_url + "/user-one",
        facebook_url + "/user-two",
        twitter_url + "/james",
    ]
    url_list_empty = [twitter_url + "james", twitter_url + "doe"]
    answer = [facebook_url, facebook_url]

    fb_url_list_one = funcs.getFacebookUrlInList(url_list)
    fb_url_list_two = funcs.getFacebookUrlInList(url_list_empty)

    assert fb_url_list_two == list()
    assert fb_url_list_one == answer
    print("finished testing getFacebookUrlInLists")


def test_facebookAboutPageUrl():
    print("started testing facebookAboutPageUrl")
    html_string = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>
        <a href="./login.html">log in</a>
        <a href="./logout.html">log out</a>
        <a href="./about.html">About</a>
        </body>
        </html>
    """
    content_dict = {"content": html_string}
    urls = funcs.facebookAboutPageUrl(content_dict)
    assert urls == ["./about.html"]
    print("finished testing facebookAboutPageUrl")


def test_getEmailFromFacebookAboutPage():
    print("started finishing getEmailFromFacebookAboutPage")
    html_string = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>
        <a href="./login.html">log in</a>
        <a href="./logout.html">log out</a>
        <a href="">someone@email.com</a>
        </body>
        </html>
    """
    content_dict = {"content": html_string}
    expected_result_one = funcs.getEmailFromFacebookAboutPage(content_dict)

    assert expected_result_one == "someone@email.com"
    print("finished testing getEmailFromFacebookAboutPage")


def test_getEmailFromFacebookAboutPageFail():
    print("started testing getEmailFromFacebookAboutPageFail")
    html_string = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>
        <a href="./login.html">log in</a>
        <a href="./logout.html">log out</a>
        </body>
        </html>
    """
    content_dict = {"content": html_string}
    expected_result = funcs.getEmailFromFacebookAboutPage(content_dict)

    assert expected_result is None
    print("finished testing getEmailFromFacebookAboutPageFail")


def test_addFacebookUrlToUrl():
    print("started addFacebookUrlToUrl")

    test_one = funcs.addFacebookUrlToUrl(
        [
            1,
            2,
            10,
            34,
        ]
    )
    test_two = funcs.addFacebookUrlToUrl(["heyy", "user"])

    answer_one = "https://facebook.com/pg1"
    answer_two = "https://facebook.com/pgheyy"

    assert test_one == answer_one
    assert test_two == answer_two
    print("finised testing addFacebookUrlToUrl")


def test_addFacebookUrlToUrlException():
    print("started addFacebookUrlToUrl")
    test = []

    test = funcs.addFacebookUrlToUrl(test)

    assert test is None
    print("finsihed testing addFacebookUrlToUrl")


def test_parseSiteContent():
    print("started testing parseSiteContent")
    html_string = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>

        </body>
        </html>
    """
    test_dict = {"content": html_string}
    soup_result = funcs.parseSiteConent(test_dict)
    expected_result = "<h1>This is a Heading</h1>"
    soup_result = list(soup_result.find_all("h1"))
    soup_result = str(soup_result[0])

    assert soup_result == expected_result
    print("finished tesing parseSiteContent")
