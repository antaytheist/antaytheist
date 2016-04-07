# bible related utilities for antaytheist
import re

bibrefregex = re.compile("(.*?)\s(\d{1,2})(?::(\d{1,2})(?:-(\d{1,2})?)?)?")

booknames = {
    # OT
    "gen(esis)?": "Genesis",
    "ex(odus)?": "Exodus",
    "lev(iticus)?": "Leviticus",
    "num(bers)?": "Numbers",
    "deut(eronomy)?": "Deuteronomy",
    "jos(hua)?": "Joshua",
    "j(ud)?g(es)?": "Judges",
    "ru(th)?": "Ruth",
    "(1|I)\s?sam(uel)?": "1 Samuel",
    "(2|II)\s?sam(uel)?": "2 Samuel",
    "(1|I)\s?ki(ngs)?": "1 Kings",
    "(2|II)\s?ki(ngs)?": "2 Kings",
    "(1|I)\s?chr(onicles)?": "1 Chronicles",
    "(2|II)\s?chr(onicles)?": "2 Chronicles",
    "ezra?": "Ezra",
    "neh(emiah)?": "Nehemiah",
    "est(her)?": "Esther",
    "job": "Job",
    "ps(alms)?": "Psalms",
    "pr(overbs)?": "Proverbs",
    "ec(clesiastes)?": "Ecclesiastes",
    "song( of solomon)?": "Song of Solomom",
    "is(aiah)?": "Isaiah",
    "jer(emiah)?": "Jeremiah",
    "lam(entations)?": "Lamentations",
    "ezek(iel)?": "Ezekiel",
    "dan(iel)?": "Daniel",
    "hos(ea)?": "Hosea",
    "j(oe)?l": "Joel",
    "am(os)?": "Amos",
    "ob(adiah)?": "Obadiah",
    "jon(ah)?": "Jonah",
    "mic(ah)?": "Micah",
    "nah(um)?": "Nahum",
    "hab(akkuk)?": "Habakkuk",
    "zeph(aniah)?": "Zephaniah",
    "hag(gai)?": "Haggai",
    "zech(ariah)?": "Zechariah",
    "mal(achi)?": "Malachi",
    #NT
    "ma?t(thew)?": "Matthew",
    "m(ar)?k": "Mark",
    "lu?ke?": "Luke",
    "j(oh)?n": "John",
    "acts": "Acts",
    "rom(ans)?": "Romans",
    "(1|I)\s?cor(inthians)?": "1 Corinthians",
    "(2|II)\s?cor(inthians)?": "2 Corinthians",
    "gal(atians)": "Galatians",
    "eph(esians)?": "Ephesians",
    "phil(ippians)?": "Philippians",
    "col(ossians)": "Collosians",
    "(1|I)\s?th(essalonians)?": "1 Thessalonians",
    "(2|II)\s?th(essalonians)?": "2 Thessalonians",
    "(1|I)\s?tim(othy)?": "1 Timothy",
    "(2|II)\s?tim(othy)?": "2 Timothy",
    "tit(us)?": "Titus",
    "philem(on)?": "Philemon",
    "heb(rews)?": "Hebrews",
    "ja(me)?s": "James",
    "(1|I)\s?pet(er)?": "1 Peter",
    "(2|II)\s?pet(er)?": "2 Peter",
    "(1|I)\s?j(oh)?n": "1 John",
    "(2|II)\s?j(oh)?n": "2 John",
    "(3|III)\s?j(oh)?n": "3 John",
    "jude?": "Jude",
    "rev(elation)?": "Revelation",
}

booknameregexes = {}
for key, item in booknames.items():
    booknameregexes[re.compile(key)] = item

def bibfullref(bibref):
    response = {}
    askmatch = bibrefregex.fullmatch(bibref)
    if not askmatch:
        return {"success": False, "error": 'Bible reference "' + bibref + '" is invalid (invalid structure)'}

    captures = askmatch.groups()
    bookname = captures[0]
    chapter = captures[1]
    versestart = captures[2]
    verseend = captures[3]
    if versestart != None:
        if verseend != None:
            if int(versestart) >= int(verseend):
                return {"success": False, "error": 'Ending verse "' + verseend + '" is greater than or equal to the starting verse "' + versestart + '"'}
            response["verseend"] = verseend
        response["versestart"] = versestart

    lowerbookname = bookname.lower()
    finalbookname = None
    for key, item in booknameregexes.items():
        if key.fullmatch(lowerbookname):
            finalbookname = item
            break

    if finalbookname == None:
        return {"success": False, "error": 'Bible reference "' + bibref + '" is invalid (invalid book name)'}

    response["success"] = True
    response["book"] = finalbookname
    response["chapter"] = chapter
    return response
