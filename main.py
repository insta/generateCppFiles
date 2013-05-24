import sys
from createFile import *


def getArgs(knownFlags):
    inputData = [["m"]]

    for arg in sys.argv[1:]:
        if "-" in arg:
            if arg == "-h" or arg == "-H":
                helpFile()
            else:
                inputData.append([arg[1:]])
        else:
            inputData[len(inputData)-1].append(arg)
    if len(inputData[0]) > 2:
            warning(0)

    tmp = []
    if len(inputData) > 1:
        for dataType in inputData[1:]:
            if dataType[0].upper() in knownFlags:
                if len(dataType) > 1:
                    for name in dataType[1:]:
                        if name in tmp:
                            warning(2)
                        else:
                            tmp.append(name)
                else:
                    warning(1)
            else:
                warning(3)

    return inputData


def genMakeFile(inputData):
    data = readTemplate("makeFileTemplate")
    tmp = ""
    for typeData in inputData:
        for fileName in typeData[1:]:
            tmp += fileName+" "
    data[3] = "SOURCES="+tmp
    output = open("GCC"+"MakeFile", "w")
    for line in data:
        output.write(line)
    output.close()


def readTemplate(location):
    template = open(location)
    data = []
    for lines in template.readlines():
        data.append(lines)
    template.close()
    return data


def warning(errNum):
    if errNum == 0:
        print("Flag missing")
    elif errNum == 1:
        print("Missing arguments after flag delaration")
    elif errNum == 2:
        print("Double occurence of file")
    elif errNum == 3:
        print("Unknown flag occurence")
    else:
        print("I'm a teapot")
    helpFile()


def helpFile():
    print("This command is used to generate basic cpp and hpp files with all #includes pre-configure")
    print("Command Arg1 -f Args1 -c Args2")
    print("Arg1 : Name used for main.cpp file, default : main.cpp")
    print("-f Args1 : generates basic cpp and hpp files for specified names")
    print("-c Args2 : generates basic cpp and hpp class files")
    sys.exit(0)


def main():
    data = getArgs(["C", "F"])
    print(data)
    include = []
    for fileType in data[1:]:
        include.extend(createFiles(fileType))
    createMain(data[0][1], include, "mainTemplate")

    genMakeFile(data)

if __name__ == '__main__':
    main()
