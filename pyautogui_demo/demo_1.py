import pywinauto
from pywinauto import application
import os


os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"})
pywinauto.Application(backend="uia").start("C:\\Users\\80649.LAPTOP-T3EKEB7M\\Desktop\\软媒清理大师@133_39990.exe")

