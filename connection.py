import pyodbc
import json

with open("dadosDatabase.json", "r", encoding="utf-8") as jsonFile:
    dadosDatabase = json.load(jsonFile)



# f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trustedConnection}"
connection = pyodbc.connect(f"DRIVER={dadosDatabase["driver"]};SERVER={dadosDatabase["server"]};DATABASE={dadosDatabase["database"]};UID={dadosDatabase["userid"]};PWD={dadosDatabase["password"]};TRUSTED_CONNECTION={dadosDatabase["trusteconnection"]}")
cursor = connection.cursor()
