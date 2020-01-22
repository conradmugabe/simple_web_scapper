def readFile(file_name):
    """Takes in a text file \n
        Returns a list of contents in the text file provided"""
    with open(file_name) as file_to_read:
        file_contents = file_to_read.readlines()
        return file_contents

def checkStatusCodeExistance(website_to_check):
    '''Takes in "response.get(https:...)" and checks if return message between 200 to 400 \n
            Returns True or False if otherwise'''
    if website_to_check:
        return True
    else:
        return False

def checkIfStatusCodeOk(website_to_check):
    '''Takes in "response.get(https:...)" and checks if the HTTP message is 200 (OK) \n
        Returns True or False if not a 200 message'''
    if website_to_check.status_code == 200:
        return True
    else:
        return False