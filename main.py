import sys
def createMain(name, fileName, className):
	fileOpen = open(name+".cpp", w)
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
	elif errNum==2:
		print("Double occurence of file")
	else:
		print("I'm a teapot")
	sys.exit(0)

def main():
	mainName="main.cpp"
	classNames=[]
	fileNames=[]
	flag=""
	counter=1
	data=True
	for arg in sys.argv[1:]:
		if arg=="-c" or arg=="-C":
			flag="c"
			data=False
		elif arg=="-f" or arg=="-F":
			flag="f"
			data=False
		else:
			if flag=="c":
				if arg in classNames or arg in fileNames:
					warning(2)
				else:
					classNames.append(arg)
					data=True
			elif flag=="f":
				if arg in fileNames or arg in classNames:
					warning(2)
				else:
					fileNames.append(arg)
					data=True
			else:
				if counter>1:
					warning(0)
				else:
					mainName=arg
					counter+=1
	if not data:
		warning(1)
	print(fileNames)
	print(classNames)
	print(mainName)

main()	
