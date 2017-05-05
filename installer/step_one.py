import os,sys, subprocess
from WinPersistence import preReboot

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


def download_docker_toolset():
    install("urllib2")
    import urllib2

    url = "https://download.docker.com/win/stable/DockerToolbox.exe"

    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()


if __name__ == "__main__":
    #first
    download_docker_toolset()
    #now run the installer
    os.system("DockerToolbox.exe")
    #then delete the installer
    os.remove("DockerToolbox.exe")
    #now reboot
    preReboot()
    open("current.txt", 'a').close()
