COUNTClient = 0
def incrementUser():
    global COUNTClient
    COUNTClient = COUNTClient + 1
    return COUNTClient

def resetUserCount():
    global COUNTClient
    COUNTClient = 0