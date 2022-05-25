def getStatus(id):
    file = open('config')
    config = file.readlines()
    file.close()
    return config[id]
