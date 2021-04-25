import os


def main():
    oldLine=''
    print("Hello User")
    print("Welcome to the Text Replacement")
    print("Pleace place the text file under the same directory as this <textRepla.py>")
    print("|||||||||||||||||||||||||||||||||||||||||")
    fileName=input("pleace enter the <text file> ===>: ")##gitCommandLineBasics.txt
    originText=input("pleace enter the string which you want to be replaced ===>: ")##Tianchao
    newText=input("pleace enter the string which you want useing to replace the old oned ===>: ")##tianjingzhuo
    try: 
        with open(fileName,'r') as f:
            fN=open("newFile",'w')
            for line in f:
                oldLine=line
                if originText in oldLine:
                    newLine = oldLine.replace(originText, newText+" ")
                    # print(newLine)
                    fN.write(newLine+"")
                else:
                    # print(oldLine)
                    fN.write(oldLine+"")
        fN.close()
        os.remove(fileName)
        os.rename('newFile', fileName)
    except OSError as e:
        print("This file does not exit under this directory")
    
if __name__ == "__main__":
    main()