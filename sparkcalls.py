import requests
import json
#Esta funcion crea el encabezado para la autenticacion de Spark
def setHeaders(token):
    accessToken_hdr = 'Bearer ' + token
    spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
    return spark_header
# Esta funcion obtiene los mensajes que le escriben al Bot
def SparkGET(uri, theHeader):
    resp = requests.get(uri, headers=theHeader)
    return resp.json()
# Esta funcion envia mensajes a Spark
def SparkPOST(theHeader, uri, payload):
    resp = requests.post(uri, data=json.dumps(payload), headers=theHeader)
    return resp.json()
# Esta funcion consulta y devuelve el lista de rooms del usuario
def getRooms(theHeader):
    uri = 'https://api.ciscospark.com/v1/rooms'
    resp = requests.get(uri, headers=theHeader)
    return resp.json()
# Esta funcion busca un room especifico y devuelve su id
def findRoom(roomList, name):
    roomId = 0
    for room in roomList["items"]:
        if room["title"] == name:
            roomId = room["id"]
            break
    return roomId