from os import walk


def importFolder(path):

    for information in walk(path):
        print(information)


importFolder('../graphics/character/run')
