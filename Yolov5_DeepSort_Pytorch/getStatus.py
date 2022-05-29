def getStatus(id):
    file = open('config.py')
    config = file.readlines()
    file.close()
    return config[id]
print(getStatus(4))