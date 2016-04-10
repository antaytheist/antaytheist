# fallacy quoter for antaytheist
import json
import re
import requests

fallaciesjson = requests.get("https://yourlogicalfallacyis.com/js/data/fallacies.json", timeout=15)
fallaciesjson.raise_for_status()
fallacies = json.loads(fallaciesjson.text)
fallacynames = []

for fallacyitem in fallacies:
    fallacynames.append(fallacyitem["title"])

def quote(args):
    if args[0].lower() not in fallacynames:
        return {"success": False, "error": 'Invalid fallacy "' + args[0] + '"'}

    for fallacyitem in fallacies:
        if fallacyitem["title"] == args[0].lower():
            myfallacy = fallacyitem
            break

    return {
        "success": True,
        "output": {
            "text": re.sub("&nbsp;", " ", myfallacy["description"]) + "\n\n" + myfallacy["exampleText"]
        },
        "source": {
            "name": "your logical fallacy is", "src": "https://yourlogicalfallacyis.com/"
        }
    }
