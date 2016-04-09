# bible module for contra in antaytheist
import re
import requests
from bs4 import BeautifulSoup

from ..util.bible import bibfullref
from ..util.scripture import chapterverseregex
from ..util.sab import book2url
from .aliasbible import aliases

# Screw fancy output, just give them a link

def contra(args):
    if args[0].lower() in aliases:
        ref = bibfullref(aliases[args[0]])
    else:
        ref = bibfullref(args[0])

    if ref["success"] == False:
        return ref

    contralisturl = "http://skepticsannotatedbible.com/" + book2url[ref["book"]] + "/contra_list.html"

    try:
        sabget = requests.get(contralisturl, timeout=15)
    except requests.exceptions.RequestException:
        return {"success": False, "error": "Could not connect to SAB"}

    # a stray tag must be removed, otherwise parser/bs gets confused
    finaltext = re.sub(r"manger\?</b>", "manger?", sabget.text)
    if ref["book"] == "Genesis":
        # yet another stray tag
        finaltext = re.sub(r"1:29</a>, </A>", "1:29</a>, ", finaltext)
    soup = BeautifulSoup(finaltext, "html.parser")

    if "versestart" in ref:
        # ensure that we only get an exact match for the chapter:verse we are looking for
        # but also ensuring that there can be more chapter:verse pairs after it
        searchref = ref["chapter"] + ":" + ref["versestart"] + r"(?!\d)"
    else:
        searchref = ref["chapter"] + r":\d{1,3}"

    foundref = soup.find("ol").find("a", string=re.compile(searchref))
    if foundref == None:
        return {"success": False, "error": "Could not find a relevant contradiction"}

    finalelem = foundref.previous_element

    while True:
        if str(type(finalelem)) == "<class 'bs4.element.Tag'>":
            if "contra/" in finalelem["href"]:
                break;
        finalelem = finalelem.previous_element

    return {"success": True, "contra": {"link": "http://skepticsannotatedbible.com/" + finalelem["href"][3:], "source": {"url": contralisturl, "name": "Skeptic's Annotated Bible"}}}
