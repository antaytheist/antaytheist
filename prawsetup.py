# initial praw setup automation
import praw
import configparser
import webbrowser

r = praw.Reddit(user_agent="Initial OAuth setup for antaytheist", site_name="antaytheist")

config = configparser.ConfigParser()
config.read("praw.ini")

url = r.get_authorize_url("antaytheistbot", "identity read submit privatemessages", True)

webbrowser.open(url)

accessinfo = r.get_access_information(input("Paste in the code: "))

config["antaytheist"]["oauth_refresh_token"] = accessinfo["refresh_token"]

with open("praw.ini", "w") as f:
    config.write(f)

print("All setup! You should now be able to run antaytheist!")
