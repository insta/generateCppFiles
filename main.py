import sys
from createFile import *


def getArgs(knownFlags):
    mainName = "main.cpp"
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


def createMain(data):
    data[0][1] += ".cpp"
    fileOpen = open(data[0][1], 'w')
    fileOpen.write('#include <iostream>\n')
    fileOpen.write('\n')
    for i in data[1:]:
        for j in i[1:]:
            output = '#include "' + j + '.hpp"\n'
        fileOpen.write(data)

    fileOpen.write('\n')
    fileOpen.write('using namespace std;\n')
    fileOpen.write('\n')
    fileOpen.write('int main(int argc, char *argv[])\n')
    fileOpen.write('{\n')
    fileOpen.write('    cout << "Hello world!" << endl;\n')
    fileOpen.write('    return 0;\n')
    fileOpen.write('}\n')
    fileOpen.close()


def genMakeFile(name, fileNames, classNames):
    data = readTemplate("makeFileTemplate")
    tmp = ""
    for fileName in fileNames:
        tmp += fileName+" "
    for fileName in classNames:
        tmp += fileName+" "
    data[3] = "SOURCES="+tmp
    output = open(name+"MakeFile", "w")
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
    print(fileNames)
    print(classNames)
    print(mainName)
    createMain(data)
    for fileType in data[1:]:
        createFiles(fileType)

    genMakeFile(mainName, fileNames, classNames)

if __name__ == '__main__':
    main()
