# import everything
# standard python libs
import shlex

# antaytheist libs
from . import contra
from . import quote

command2func = {
    "contra": contra.contra,
    "contradict": contra.contra,
    "quote": quote.quote,
}

def do(command):
    try:
        lexcmd = shlex.split(command)
    except Exception as e:
        return {"finalsuccess": False, "main": {"error": str(e), "success": False}}

    response = {}

    if lexcmd[0] not in command2func:
        return {"finalsuccess": False, "main": {"error": 'Invalid function "' + lexcmd[0] + '"', "success": False}}

    if len(lexcmd) < 3:
        return {"finalsuccess": False, "main": {"error": "Too few arguments given", "success": False}}

    response["main"] = command2func[lexcmd[0]](lexcmd[1:])
    response["finalsuccess"] = response["main"]["success"]
    response["command"] = lexcmd[0]
    return response
