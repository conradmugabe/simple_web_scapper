import funcs

GOOGLE_URL = "https://www.google.com"

for line in funcs.readTextFile('companies.txt'):
    website_status = funcs.getWebsiteStatus(GOOGLE_URL, line)
    links = funcs.linksOnWebsite(website_status)
    all_urls = funcs.getUrlWithRegex(links)
    facebook_urls = funcs.getFacebookUrlInList(all_urls)

    facebook_status = funcs.getWebsiteStatus(facebook_urls[0])
    facebook_links = funcs.facebookAboutPageUrl(facebook_status)
    about_page_url = funcs.addFacebookUrlToUrl(facebook_links)

    about_page_status = funcs.getWebsiteStatus(about_page_url)
    email = funcs.getEmailFromFacebookAboutPage(about_page_status)
    funcs.appendFile("companies_with_emails.txt", line, email)
