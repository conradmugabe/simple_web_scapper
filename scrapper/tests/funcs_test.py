import pytest

from scrapper import funcs


def test_readTextFile():
    print("Started readTextFile")
    test = funcs.readTextFile("./scrapper/tests/test_data/test_readtext.txt")

    prepare = ["new vision", "daily monitor", "cafe javas"]

    assert test == prepare
    print("Ended readTextFile")


def test_readTextFileException():
    print("Started readTextFileException")

    with pytest.raises(FileNotFoundError):
        funcs.readTextFile("./some_test_data/companies.txt")

    print("Ended readTextFileException")


# def test_getWebsite():
#     pass


# def test_getWebsite_withSearch():
#     pass


def test_mapTwoListsToDic():
    print("started mapTwoListsToDic")
    list_one = [1, 2, 3, 4]
    list_two = ["hey", "how", "them", "user"]
    list_three = ["user", "other", "james"]

    answer_one = funcs.mapTwoListsToDic(list_one, list_two)
    answer_two = funcs.mapTwoListsToDic(list_one, list_three)

    assert answer_two is False
    assert answer_one == {1: "hey", 2: "how", 3: "them", 4: "user"}


def test_getUrlWithRegex():
    print("started getUrlWithRegex")

    url_list = ["heli1q=httpjjknrkjz"]
    answer = funcs.getUrlWithRegex(url_list)

    assert answer == ["httpjjknrkjz"]
    print("started getUrlWithRegex")


def test_getFacebookUrlInLists():
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
    print("finished getFacebookUrlInLists")


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
    print("finised addFacebookUrlToUrl")
