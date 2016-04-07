# bible module for contra in antaytheist
import re

from ..util.bible import bibrefregex

# Replace numbers with strings of the full reference!
# {"success": True,
#  "question": "What happened?",
#  "consistent": {
#      "msg": "Nice", "verses": [1, 2, 3]
#  },
#  "contras": [
#      {"msg": "Something different", "verses": [7, 8, 9]},
#      {"msg": "Yet another different message", "verses": [13, 15, 18]}
#  ],
#  "misc": {
#      "errancyrating": "na"
#      "sablink": "http://example.com/contra"
#  }


def contra(args):
    return {"success": True}
