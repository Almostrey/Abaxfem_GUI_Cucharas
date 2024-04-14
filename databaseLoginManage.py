import sqlite3 as sql
from datetime import datetime
nameDB = "dataL.db"

def createDB():
    conn = sql.connect(nameDB)
    conn.commit()
    conn.close()

def createTable(nameTable, columns):
    try:
        conn = sql.connect(nameDB)
        instruction = f"CREATE TABLE {nameTable} ({columns})"
        conn.execute(instruction)
        conn.commit()
        conn.close()
    except:
        pass

def insertLoginRow(nameTable, user, password, function, name):
    if isDuplicated(nameTable, "User", user):
        return False
    else:
        date = datetime.strftime(datetime.now(), '%d/%m/%Y')
        conn = sql.connect(nameDB)
        cursor = conn.cursor()
        instruccion = f"INSERT INTO {nameTable} VALUES ('{user}', '{password}', '{function}', '{name}', '{date}')"
        conn.execute(instruccion)
        conn.commit()
        conn.close()
        return True

def readRows(nameTable):
    conn = sql.connect(nameDB)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM {nameTable}"
    cursor.execute(instruccion)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data

def searchDB(nameTable, column, value):
    conn = sql.connect(nameDB)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM {nameTable} WHERE {column} = {value}"
    cursor.execute(instruccion)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data

def updateFields(nameTable, columnRef, valueRef, column, value):
    date = datetime.strftime(datetime.now(), '%d/%m/%Y')
    conn = sql.connect(nameDB)
    cursor = conn.cursor()
    instruccion = f"UPDATE {nameTable} SET Date = '{date}' WHERE {columnRef}={valueRef}"
    cursor.execute(instruccion)
    conn.commit()
    instruccion = f"UPDATE {nameTable} SET {column} = {value} WHERE {columnRef}={valueRef}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    return True

def deleteRow(nameTable, column, value):
    try:
        conn = sql.connect(nameDB)
        cursor = conn.cursor()
        instruccion = f"DELETE FROM {nameTable} WHERE {column} = {value}"
        cursor.execute(instruccion)
        conn.commit()
        conn.close()
    except:
        pass

def deleteTable(nameTable):
    try:
        conn = sql.connect(nameDB)
        cursor = conn.cursor()
        instruccion = f"DROP TABLE {nameTable}"
        cursor.execute(instruccion)
        conn.commit()
        conn.close()
    except:
        pass

def login(user, password):
    try:
        row = searchDB("LoginTable", "User", f"'{user}'")
        if row[0][0] == '':
            return False
        else:
            if user == row[0][0] and password == row[0][1]:
                return row[0][2]
    except:
        return False

def isDuplicated(nameTable, column, value):
    try:
        row = searchDB(nameTable, column, f"'{value}'")
        if row != []:
            return True
        else: 
            return False
    except:
        return True

def addHistory(user):
    try:
        data = searchDB("LoginTable", "User", f"'{user}'")
        date = datetime.strftime(datetime.now(), '%d/%m/%Y')
        time = datetime.strftime(datetime.now(), '%H:%M:%S')
        conn = sql.connect(nameDB)
        cursor = conn.cursor()
        instruccion = f"INSERT INTO HistoryLoginTable VALUES ('{data[0][0]}', '{data[0][2]}', '{data[0][3]}', '{date}', '{time}')"
        conn.execute(instruccion)
        conn.commit()
        conn.close()
    except:
        pass

def restore():
    insertLoginRow("LoginTable", 'ADMIN', '123456', 'ADMINISTRADOR', 'Administrador')
    insertLoginRow("LoginTable", 'OPERADOR', '123456', 'OPERADOR', 'Operario 1')

def getBriefHistory(number: int):
    conn = sql.connect(nameDB)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM HistoryLoginTable"
    cursor.execute(instruccion)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    if len(data) >= 5:
        return data[len(data)-number:len(data)]
    else:
        return data[0:number]

if __name__ == "__main__":
    nameTable = "LoginTable"
    #createTable("HistoryLoginTable", "User text, Function text, Name text, Date text, Time Text")
    #print(insertLoginRow("LoginTable", 'ADMIN', '123456', 'ADMINISTRADOR', 'Diego Guevara B.'))
    #print(insertLoginRow("LoginTable", 'OPERADOR', '123456', 'OPERADOR', 'Usuario 1'))
    #data = readRows(nameTable)
    #data = searchDB(nameTable, "User", f"'Almostrey'")
    #updateFields(nameTable, "User", f"'Jauniman'", 'Name', f"'Juan Guevara B.'")
    #deleteRow("HistoryLoginTable", "User", f"'Diego'")
    #deleteTable(nameTable)
    #print(login("Jauniman", "1725248767"))
    #deleteTable(nameTable)
    #addHistory("OPERADOR")