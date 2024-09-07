import json


def getSensorList() -> list:
    """Returns a list of sensors"""
    with open("data/struct.json") as f:
        fjson = json.load(f)
        out = []
        for i in fjson:
            out.append([i["name"], i["id"]])
    return out


def haveSensor(id: str) -> bool:
    """Returns if the sensor exists"""
    with open("data/struct.json") as f:
        fjson = json.load(f)
        for i in fjson:
            if i["id"] == id:
                return True
    return False


def getSensorKey(id: str) -> list:
    """Returns a Key and Type list of sensors"""
    with open("data/struct.json") as f:
        fjson = json.load(f)
        out = []
        for i in fjson:
            if i["id"] == id:
                for j in i["struct"]:
                    out.append([j["key"], j["type"]])
    return out

def needTimestamp(id: str) -> bool:
    """Returns if the sensor needs a timestamp"""
    with open("data/struct.json") as f:
        fjson = json.load(f)
        for i in fjson:
            if i["id"] == id:
                if "timestamp" in i: return True
    return False


def getSensorLimit(id: str) -> int:
    """Returns the limit of the sensor"""
    with open("data/struct.json") as f:
        fjson = json.load(f)
        for i in fjson:
            if i["id"] == id:
                return i["maxstore"]
        return 0

