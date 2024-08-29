import dao.file.struct
import logging

from dao.db.util import getConn


def init():
    """初始化数据库表"""
    with getConn() as conn:
        sensorList = dao.file.struct.getSensorList()
        for sensor in sensorList:
            keyList = []
            if dao.file.struct.needTimestamp(sensor[1]): # 添加时间戳
                keyList = [["timestamp",'int']]
            keyList += dao.file.struct.getSensorKey(sensor[1])
            sql = "CREATE TABLE IF NOT EXISTS '" + sensor[1] + "' ("
            for key in keyList:
                sql += key[0] + " INT,"
            sql = sql[:-1]
            sql += ")"
            conn.execute(sql)
            conn.commit()
            logging.info("init " + sensor[1] + " success")


def writeData(id: str, data: dict):
    """写入单条数据"""
    with getConn() as conn:
        keyList = data.keys()
        sql = "INSERT INTO '" + id + "' ("
        for key in keyList:
            sql += key + ","
        sql = sql[:-1]
        sql += ") VALUES ("
        for key in keyList:
            sql += str(data[key]) + ","
        sql = sql[:-1]
        sql += ")"
        conn.execute(sql)
        conn.commit()
        logging.info("writeData " + id + " success")


def readData(id: str, start: int, end: int):
    """通过时间戳读取数据"""
    with getConn() as conn:
        sql = "SELECT * FROM '" + id + "' WHERE timestamp >= " + str(start) + " AND timestamp <= " + str(end)
        cursor = conn.execute(sql)
        data = cursor.fetchall()
        logging.info("readData " + id + " success")
        return data
    

def readNewData(id: str, num: int):
    """读取最新数据"""
    with getConn() as conn:
        sql = "SELECT * FROM '" + id + "' ORDER BY timestamp DESC LIMIT " + str(num)
        cursor = conn.execute(sql)
        data = cursor.fetchall()
        logging.info("readNewData " + id + " success")
        return data
    

def readrealTimeData(id: str):
    """读取实时数据"""
    with getConn() as conn:
        sql = "SELECT * FROM '" + id + "' ORDER BY timestamp DESC LIMIT 1"
        cursor = conn.execute(sql)
        data = cursor.fetchone()
        logging.info("readrealTimeData " + id + " success")
        return data
