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
