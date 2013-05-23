import sys
from createFile import *


def getArgs():
    mainName = "main.cpp"
    classNames = []
    fileNames = []
    flag = ""
    boolName = False
    data = True
    for arg in sys.argv[1:]:
        if "-" in arg:
            if arg == "-c" or arg == "-C":
                flag = "c"
                data = False
            elif arg == "-f" or arg == "-F":
                flag = "f"
                data = False
            else:
                warning(3)
        else:
            if flag == "c":
                if arg in classNames or arg in fileNames:
                    warning(2)
                else:
                    arg = arg[0].upper() + arg[1:]
                    classNames.append(arg)
                    data = True
            elif flag == "f":
                if arg in fileNames or arg in classNames:
                    warning(2)
                else:
                    arg = arg[0].upper() + arg[1:]
                    fileNames.append(arg)
                    data = True
            else:
                if boolName:
                    warning(0)
                else:
                    mainName = arg
                    boolName = True
    if not data:
        warning(1)
    return mainName, classNames, fileNames


def createMain(name, fileName, className):
    name += ".cpp"
    fileOpen = open(name, 'w')
    fileOpen.write('#include <iostream>\n')
    fileOpen.write('\n')
    for i in fileName:
        data = '#include "' + i + '.hpp"\n'
        fileOpen.write(data)
    for i in className:
        data = '#include "' + i + '.hpp"\n'
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
    sys.exit(0)


def main():
    mainName, classNames, fileNames = getArgs()
    print(fileNames)
    print(classNames)
    print(mainName)
    createMain(mainName, fileNames, classNames)
    createFile(fileNames)
    createClass(classNames)

if __name__ == '__main__':
    main()
