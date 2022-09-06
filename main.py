import os
import shutil
from sys import argv

def main():
    if len(argv) < 3:
        print("Usage: \n\t[decompiler] sourcePath dstPath [jarPath]")
        exit(0)
    sourcePath, dstPath = argv[1], argv[2]
    if len(argv) == 4:
        jarPath = argv[3]
    else:
        jarPath = "/home/java/Desktop/tool/Jetbrains/idea-IU-222.3739.54/plugins/java-decompiler/lib/java-decompiler.jar"


    if os.path.exists(dstPath) :
        shutil.rmtree(dstPath)
    os.mkdir(dstPath)
    uncompressWar(sourcePath)
    decompile(sourcePath, dstPath, jarPath)
    uncompressJarResult(dstPath)
    collectAllJarToStoreLib(sourcePath, dstPath)
    removeSoureWar(sourcePath)


def uncompressWar(sourcePath):
    commandFmt = "find {} -name \"*.war\" -type f | xargs -I xx unzip xx -d xx.folder"
    command = commandFmt.format(sourcePath)
    os.system(command)

def decompile(sourcePath, dstPath, jarPath):
    print(jarPath)
    commandFmt = "java -cp \"{}\" org.jetbrains.java.decompiler.main.decompiler.ConsoleDecompiler -dgs=true {} {}"
    command = commandFmt.format(jarPath, sourcePath, dstPath)
    print(command)
    os.system(command)

def uncompressJarResult(dstPath):
    commandFmt = "find {} -name \"*.jar\" -type f | xargs -I xx unzip xx -d xx.folder "
    command = commandFmt.format(dstPath)
    os.system(command)
    # clean jar
    commandFmt = "find {} -name \"*.jar\" -type f | xargs -I xx rm -f xx "
    command = commandFmt.format(dstPath)
    os.system(command)

def collectAllJarToStoreLib(sourcePath, dstPath):
    storeLibPath = "{}/storelib".format(dstPath)
    if os.path.exists(storeLibPath) == False:
        os.mkdir(storeLibPath)
    commandFmt = "find {} -name \"*.jar\" -type f | xargs -I xx cp xx {}/"
    command = commandFmt.format(sourcePath , storeLibPath)
    os.system(command)

def removeSoureWar(sourcePath):
    commandFmt = "find {} -name \"*.war\" -type f | xargs -I xx rm -rf xx.folder"
    command = commandFmt.format(sourcePath)
    os.system(command)

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
