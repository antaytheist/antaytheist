# bible quoter for antaytheist
import requests
from bs4 import BeautifulSoup

from ..util.bible import bibfullref

def quote(args):
    ref = bibfullref(args[0])
    if ref["success"] == False:
        return ref

    searchstr = ref["book"] + " " + ref["chapter"]
    if "versestart" in ref:
        searchstr += ":" + ref["versestart"]
    if "verseend" in ref:
        searchstr += "-" + ref["verseend"]

    if len(args) == 2:
        bibversion = args[1]
    else:
        bibversion = "KJV"

    try:
        gatewayget = requests.get("https://www.biblegateway.com/passage/", params={"search": searchstr, "version": bibversion}, timeout=15)
    except requests.exceptions.RequestException:
        return {"success": False, "error": "Could not connect to BibleGateway"}

    soup = BeautifulSoup(gatewayget.text, "html.parser")
    datacontainer = soup.find(class_="text-html")
    if datacontainer == None:
        return {"success": False, "error": "Passage not found"}

    output = {
        "ref": datacontainer.find(class_="passage-display-version").string,
        "version": datacontainer.find(class_="passage-display-bcv").string,
        "text": ""
    }

    for verse in datacontainer.find_all(class_="text"):
        for string in verse.strings:
            output["text"] += string

    return {"success": True, "refdata": ref, "output": output}
