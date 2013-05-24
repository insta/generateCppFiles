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
            elif arg=="-h" or arg=="-H":
                helpFile()
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

def genMakeFile(name,fileNames,classNames):
    data=readTemplate("makeFileTemplate")
    tmp=""
    for fileName in fileNames:
        tmp+=fileName+" "
    for fileName in classNames:
	tmp+=fileName+" "
    data[3]="SOURCES="+tmp 
    output=open(name+"MakeFile","w")
    for line in data:
        output.write(line)
    output.close()

def readTemplate(location):
    template=open(location)
    data=[]
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
    mainName, classNames, fileNames = getArgs()
    print(fileNames)
    print(classNames)
    print(mainName)
    createMain(mainName, fileNames, classNames)
    createFiles(fileNames)
    createFiles(classNames)
    genMakeFile(mainName,fileNames,classNames)

if __name__ == '__main__':
    main()
