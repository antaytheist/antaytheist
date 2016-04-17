import antaytheist
import re

import praw

commandregex = re.compile("u/antaytheist (.*)")
footer = "\n\n*****\n\nI am just a bot | [Source](https://github.com/antaytheist/antaytheist)"

r = praw.Reddit(user_agent="antaytheist testing version", site_name="antaytheist")

r.refresh_access_information()

for message in r.get_unread():
    cmdmatch = commandregex.search(message.body)
    print("See message with body " + message.body)
    if cmdmatch:
        antayoutput = antaytheist.do(cmdmatch.group(1))
        print("Matched!")
        if antayoutput["finalsuccess"]:
            if antayoutput["command"] == "quote":
                message.reply(antayoutput["main"]["output"]["text"] + "\n\n -- [" + antayoutput["main"]["source"]["name"] + "](" + antayoutput["main"]["source"]["url"] + ")" + footer)
            elif antayoutput["command"] == "contra":
                message.reply(antayoutput["main"]["contra"]["link"] + "\n\n -- [" + antayoutput["main"]["contra"]["source"]["name"] + "](" + antayoutput["main"]["contra"]["source"]["url"] + ")" + footer)
        else:
            message.reply("Uh oh! Something went wrong!\n\nError: " + antayoutput["main"]["error"] + footer)

    message.mark_as_read()
