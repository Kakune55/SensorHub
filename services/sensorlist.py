import dao.db.sdata as sdata
import dao.file.struct as struct

import time, json

def getSensorList() -> list:
    sensorList = []
    sensorIDList =  struct.getSensorList()
    for sensor in sensorIDList:
        util = {}
        util["name"] = sensor[0]
        util["id"] = sensor[1] 
        realTimeData = sdata.readrealTimeData(sensor[1])
        if len(realTimeData) == 0:
            util["lastUpdate"] = "Never"
        else:
            util["lastUpdate"] = time.ctime(realTimeData[0])
        sensorList.append(util)
    return sensorList


def getSensorData(id: str, start: int, end: int) -> list:
    if struct.haveSensor(id):
        rawData = sdata.readData(id, start, end)
        if len(rawData) > 0:
            data = []
            for i in range(len(rawData)):
                data.append({
                    "time": time.ctime(rawData[i][0]),
                    "data": json.loads(rawData[i][1])
                })
            return data
    else:
        return []
    

def getSensorNewData(id: str, num: int) -> list:
    if struct.haveSensor(id):
        rawData = sdata.readNewData(id, num)
        if len(rawData) > 0:
            allData = []
            for i in rawData:
                data = {}
                keyList = struct.getSensorKey(id)
                for j in range(1, len(i)):
                    data[keyList[j-1][0]] = i[j]
                allData.append({
                    "time": time.ctime(i[0]),
                    "data": data
                })
            return allData
    else:
        return []

