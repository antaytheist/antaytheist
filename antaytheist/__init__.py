# import everything
# standard python libs
import shlex

# antaytheist libs
from . import contra
from . import quote

def antayprint(args):
    return {"text": str(args), "success": True}

command2func = {
    "contra": contra.contra,
    "contradict": contra.contra,
    "quote": quote.quote,
    "print": antayprint,
}

def do(command):
    try:
        lexcmd = shlex.split(command)
    except Exception as e:
        return {"success": False, "error": str(e)}

    response = {}

    if lexcmd[0] not in command2func:
        return {"success": False, "error": 'Invalid function "' + lexcmd[0] + '"'}

    if lexcmd[0] != "print":
        if len(lexcmd) < 3:
            return {"success": False, "error": "Too few arguments given"}

    response["main"] = command2func[lexcmd[0]](lexcmd[1:])
    response["finalsuccess"] = response["main"]["success"]
    response["command"] = lexcmd[0]
    return response
