from main import *


def createFiles(fileNames):
    include = []
    for fileName in fileNames[1:]:
        if fileNames[0].upper() == "C":
            createCpp(fileName, "cppClassTemplate")
            createHpp(fileName, "hppClassTemplate")
            include.append(fileName)
        else:
            createCpp(fileName, "cppTemplate")
            createHpp(fileName, "hppTemplate")
            include.append(fileName)
    return include


def createHpp(fileName, template):
    data = readTemplate(template)
    data[0] = data[0][:8]+fileName+"_HPP\n"
    data[1] = data[1][:8]+fileName+"_HPP"
    writeInFile(fileName + ".hpp", data)


def createCpp(fileName, template):
    data = readTemplate(template)
    writeInFile(fileName+".cpp", data)


def createMain(fileName, include, template):
    data = readTemplate(template)
    for i in include:
        header = '#include "' + i + '.hpp"\n'
        data.insert(2, header)
    writeInFile(fileName+".cpp", data)


def writeInFile(fileName, data):
    toWrite = open(fileName, "w")
    for line in data:
        # line += "\n"
        toWrite.write(line)
    toWrite.close()
