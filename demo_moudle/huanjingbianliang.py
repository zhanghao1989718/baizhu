import os,sys

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
print("=" * 50)
rootPath = os.path.split(curPath)[0]
print(rootPath)
print("+" * 50)
sys.path.append(rootPath)
print(sys.path.append(rootPath))

