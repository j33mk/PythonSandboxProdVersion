import re

# self discipline is the key to success

# download the website from the internet and return html to the user



# but hey wait you remembered what if the user entered the website in wrong format or empty or it doesn't makes any sense what you should do

# list down what the user can go wrong
#  1. The user can input empty website
#  2. The user can input wrong website with wrong domain names
# 3. The user can input a website which doesnot exists
# 4. There are many possibilities sky is the limit but you can handle few ones as such like empty websites and wrong format of website


def check_website(website):
    if not website.strip():
        raise Exception("The website name cannot be empty")
    else:
        # check for regex expression if the wesbite is valid :)
        if isValidURL(website) == True:
            return True
        else:
            raise Exception("The url provided is not in a valid format please fix the url")


def isValidURL(str):

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
try:
    result = check_website("   ")
    print(result)
except Exception as ex:
    print(ex)

