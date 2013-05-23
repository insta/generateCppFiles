def createFile(fileNames):
	for fileName in fileNames:
		createCpp(fileName)
		createHpp(fileName)

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

def createClass(fileNames):

	for fileName in fileNames:
		createCppClass(fileName)
		createHppClass(fileName)

def createHppClass(fileName):
	
	data=["#IFNDEF "+fileName.upper()+"_HPP","#DEFINE "+fileName.upper()+"_HPP","#include <iostream> "]
	data.append("class "+fileName+":")
	data.append("{")
	data.append("	public :")
	data.append("		"+fileName+"();")
	data.append("		~"+fileName+"();")
	data.append("	private :")
	data.append("};")
	
	writeInFile(fileName+".hpp",data)

def createCppClass(fileName):
	
		
