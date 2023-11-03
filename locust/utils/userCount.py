import uuid

myuuid = uuid.uuid4()

COUNTClient = 0
def incrementUser():
    # global COUNTClient
    # COUNTClient = COUNTClient + 1
    return uuid.uuid4()

def resetUserCount():
    global COUNTClient
    COUNTClient = 0