# quote command of antaytheist
# python standard imports
import re

# antaytheist imports
from . import quotebible

second2func = {
    "bible": quotebible.quote
}

def quote(args):
    if args[0] not in second2func:
        return {"success": False, "error": 'Invalid second argument "' + args[0] + '"'}

    return second2func[args[0]](args[1:])
