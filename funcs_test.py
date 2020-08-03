import funcs


def test_readTextFile():
    print("Started readTextFile")
    test = funcs.readTextFile("./test_readtext.txt")

    prepare = ['new vision', 'daily monitor', 'cafe javas']

    assert test == prepare
    print("Ended readTextFile")


def test_readTextFileException():
    print("Started readTextFileException")
    test = funcs.readTextFile("./assets/companies.txt")

    prepare = FileNotFoundError("./assets/companies.txt")

    assert test == prepare
    print("Ended readTextFileException")


def test_getWebsite():
    print("started getWebsite")
    test = funcs.getWebsiteStatus("https://www.google.com")

    prepare = {"succedded": True}

    assert test == prepare
    print("Ended getWebsite")


def test_getWebsite_withSearch():
    print("started getWebsiteStatus")
    test = funcs.getWebsiteStatus("https://www.google.com", "new vision")

    prepare = {"succedded": True}

    assert test == prepare
    print("Ended getWebsiteStatus")
