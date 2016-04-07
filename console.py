# console interface for antaytheist
import json

import antaytheist

while True:
    print(json.dumps(antaytheist.do(input("antaytheist > ")), sort_keys=True, indent=4))
