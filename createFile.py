def createFile(fileNames):
    for fileName in fileNames:
        createCpp(fileName)
        createHpp(fileName)


def createCpp(fileName):
    data = ["using namespace std;", ""]
    writeInFile(fileName + ".cpp", data)


def createHpp(fileName):
    data = ["#IFNDEF "+fileName.upper()+"_HPP", "#DEFINE "+fileName.upper()+"_HPP", "#include <iostream> ", "", "#ENDIF"]
    writeInFile(fileName+".hpp", data)


def writeInFile(fileName, data):
    toWrite = open(fileName, "w")
    for line in data:
        line += "\n"
        toWrite.write(line)
    toWrite.close()


def createClass(fileNames):

    for fileName in fileNames:
        createCppClass(fileName)
        createHppClass(fileName)


def createHppClass(fileName):
    data = ["#IFNDEF "+fileName.upper()+"_HPP", "#DEFINE "+fileName.upper()+"_HPP", "#include <iostream> ", ""]
    data.append("class "+fileName)
    data.append("{")
    data.append("   public :")
    data.append("       "+fileName+"();")
    data.append("       ~"+fileName+"();")
    data.append("")
    data.append("   private :")
    data.append("};")
    data.extend(["", "#ENDIF"])

    writeInFile(fileName+".hpp", data)


def createCppClass(fileName):
    data = ["using namespace std;", fileName+"::"+fileName+"()", "{\n", "}\n", fileName+"::~"+fileName+"()", "{\n", "}"]
    writeInFile(fileName+".cpp", data)
