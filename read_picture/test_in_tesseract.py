from PIL import Image
import subprocess

def clearFile (filePath ,newFilePath):
    image = Image.open(filePath)

    #对图片进行阀值过滤
    image = image.point(lambda x:0 if x<240 else 255)
    image.save(newFilePath)

    # 调用系统的tesseract 识别图片
    subprocess.call(['tesseract',newFilePath,'output'])

    # open file and read it
    outputFile = open('output.txt','r')

    print(outputFile.read())

    outputFile.close()

clearFile('keep-me-informed_20171114.png','keep-me-informed_clean.png')