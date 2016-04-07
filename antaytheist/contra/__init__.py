# main contradiction finder
# python standard imports
import re

# antaytheist imports
from . import contrabible

second2func = {
    "bible": contrabible.contra
}

def contra(args):
    if args[0] not in second2func:
        return {"success": False, "error": 'Invalid second argument "' + args[0] + '"'}

    return second2func[args[0]](args[1:])
