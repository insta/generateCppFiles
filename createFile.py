def createFile(fileNames):
	for fileName in fileNames:
		createCpp(fileName)
		createHpp(fileName)
	return 0

def createCpp(fileName):
	data=["using namespace std;"]
	writeInFile(fileName+".cpp",data)

def createHpp(fileName):
	data=["#IFNDEF "+fileName.upper()+"_HPP","#DEFINE "+fileName.upper()+"_HPP","#ENDIF"]
	writeInFile(filename+".hpp",data)

def writeInFile(fileName,data):	
	
	toWrite=open(fileName,"w")
	for line in data:
		toWrite.write(data)
	toWrite.close()
