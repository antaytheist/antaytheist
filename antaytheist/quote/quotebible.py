# bible quoter for antaytheist
import json
import requests
from bs4 import BeautifulSoup

from ..util.bible import bibfullref

def biblegateway(ref):
    searchstr = ref["book"] + " " + ref["chapter"]
    if "versestart" in ref:
        searchstr += ":" + ref["versestart"]
    if "verseend" in ref:
        searchstr += "-" + ref["verseend"]

    try:
        gatewayget = requests.get("https://www.biblegateway.com/passage/", params={"search": searchstr, "version": ref["version"]}, timeout=15)
    except requests.exceptions.RequestException:
        return {"success": False, "error": "Could not connect to BibleGateway"}

    soup = BeautifulSoup(gatewayget.text, "html.parser")
    datacontainer = soup.find(class_="text-html")
    if datacontainer == None:
        return {"success": False, "error": "Passage not found"}

    output = {
        "version": datacontainer.find(class_="passage-display-version").string,
        "ref": datacontainer.find(class_="passage-display-bcv").string,
        "text": ""
    }

    for verse in datacontainer.find_all(class_="text"):
        for string in verse.strings:
            output["text"] += string

    return {"success": True, "refdata": ref, "output": output, "source": {"name": "BibleGateway", "url": gatewayget.url}}

def getbible(ref):
    searchstr = ref["book"] + " " + ref["chapter"]
    if "versestart" in ref:
        searchstr += ":" + ref["versestart"]
    if "verseend" in ref:
        searchstr += "-" + ref["verseend"]

    try:
        getbibleget = requests.get("https://getbible.net/json", params={"p": searchstr, "v": ref["version"]}, timeout=15)
    except requests.exceptions.RequestException:
        return {"success": False, "error": "Could not connect to GETBIBLE.net"}

    try:
        response = json.loads(getbibleget.text[1:-2])

        output = {
            "ref": searchstr,
            "version": response["version"],
            "text": ""
        }

        print(response["book"][0]["chapter"])
        for versenum, verseitem in response["book"][0]["chapter"].items():
            output["text"] += versenum + verseitem["verse"] + " "

    except Exception: # would be nice to narrow this down
        return {"success": False, "error": "Invalid data returned from GETBIBLE.net: possibly invalid passage given"}

    return {"success": True, "refdata": ref, "output": output, "source": {"name": "GETBIBLE.net", "url": getbibleget.url}}

biblesources = [
    getbible,
    biblegateway,
]

def quote(args):
    ref = bibfullref(args[0])
    if ref["success"] == False:
        return ref

    if len(args) == 2:
        ref["version"] = args[1]
    else:
        ref["version"] = "KJV"

    for source in biblesources:
        output = source(ref)
        if output["success"]:
            break

    return output
