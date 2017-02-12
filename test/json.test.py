import json

class logelement():
    pass


element = logelement()

element.err = "no disk"

element.des = "python"

element.id = 200


print  json.dumps(element.__dict__)