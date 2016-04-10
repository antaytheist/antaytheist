# misc quote (from people) for antaytheist

peoplequotes = {
    "contend": {
        "text": "I contend that we are both atheists. I just believe in one fewer god than you do. When you understand why you dismiss all the other possible gods, you will understand why I dismiss yours",
        "source":{
            "name": "Stephen Roberts",
            "url": "http://www.askatheists.com/4599"
        }
    },

    "epicurus": {
        "text": "Is God willing to prevent evil, but not able? Then he is not omnipotent. Is he able, but not willing? Then he is malevolent. Is he both able and willing? Then whence cometh evil? Is he neither able nor willing? Then why call him God?",
        "source": {
            "name": "Epicurus",
            "url": "http://www.askatheists.com/7256"
        }
    },

    "hitchrazor": {
        "text": "What can be asserted without evidence can be dismissed without evidence.",
        "source": {
            "name": "Christopher Hitchens",
            "url": "https://en.wikipedia.org/wiki/Hitchens's_razor"
        }
    },

    "godlove": {
        "text": "Religion has actually convinced people that there's an invisible man -- living in the sky -- who watches everything you do, every minute of every day. And the invisible man has a special list of ten things he does not want you to do.. And if you do any of these ten things, he has a special place, full of fire and smoke and burning and torture and anguish, where he will send you to live and suffer and burn and choke and scream and cry forever and ever 'til the end of time! ...But He loves you... and HE NEEDS MONEY!",
        "source": {
            "name": "George Carlin",
            "url": "http://www.askatheists.com/16940"
        }
    }
}

def quote(args):
    if args[0].lower() not in peoplequotes:
        return {"success": False, "error": 'Invalid people quote "' + args[0] + '"'}

    quotedata = peoplequotes[args[0].lower()]
    return {"success": True, "output": {"text": quotedata["text"]}, "source": quotedata["source"]}
