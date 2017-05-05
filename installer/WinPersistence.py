import os,sys

def install(package):
    """@brief     Imports modules and installs them if they are not."""
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        try:
            import pip
        except ImportError:
            print "no pip"
            os.system('python get_pip.py')
        finally:
            import pip
        pip.main(['install', package])

install("_winreg")
from _winreg import *

def preReboot():
    step_one_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"main.py")
    python_path = sys.executable
    run_step_one_path = python_path + " " + step_one_path
    key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run",0, KEY_ALL_ACCESS)
    SetValueEx(key, "DockerizingMosesInstallationPhaseTwo", 0, REG_SZ, step_one_path)

def postReboot():
    key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run",0, KEY_ALL_ACCESS)    
    DeleteValue(key, "DockerizingMosesInstallationPhaseTwo")