def createFiles(fileNames):
    for fileName in fileNames:
        createCpp(fileName)
        createHpp(fileName)


def createHpp(fileName):
    data=readTemplate("hppTemplate")
    fileName+="_HPP\n"
    data[0]=data[0][:8]+fileName
    data[1]=data[1][:8]+fileName
    writeInFile(fileName + ".hpp", data)


def createCpp(fileName):
    data = readTemplate("cppTemplate")
    writeInFile(fileName+".cpp", data)


def writeInFile(fileName, data):
    toWrite = open(fileName, "w")
    for line in data:
        line += "\n"
        toWrite.write(line)
    toWrite.close()
