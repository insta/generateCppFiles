import sys
def createMain(name, fileName, className):
	fileOpen = open(name, w)
	fileOpen.write('#include <iostream>')
    fileOpen.write('\n')
	for i in fileName:
        fileOpen.write('#include "'+ i+ '.hpp"')
    for i in className:
        fileOpen.write('#include "'+ i +'i.hpp"')
    fileOpen.write('\n')
    fileOpen.write('using namespace std;')
    fileOpen.write('\n')
    fileOpen.write('int main(int argc, char *argv[])')
    fileOpen.write('{')
    fileOpen.write('    cout << "Hello world!" << endl;')
    fileOpen.write('    return 0;')
    fileOpen.write('}')
    fileOpen.close()

def warning(errNum):
	if errNum==0:
		print("Flag missing")
	elif errNum==1:
		print("Missing arguments after flag delaration")
	else:
		print("I'm a teapot")

def main()
    main="main.cpp"
    classNames=[]
    fileNames=[]
    flag=""
    counter=1
    data=True
    for arg in sys.argv[0:]:
        if arg=="-c" or argv=="-C":
            flag="c"
            data=False
        elif arg=="-f" or arg=="-F":
            flag="f"
            data=False
        else:
            if flag=="c":
                classNames.append(arg)
                data=True
            elif flag=="f":
                fileNames.append(arg)
                data=True
            else:
                if counter>1:
                    warning(0)
                else:
                    main=arg
        counter+=1
    if not data:
        warning(1)

