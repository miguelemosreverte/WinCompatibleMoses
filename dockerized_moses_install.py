import os, subprocess

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


def get_half_the_system_memory():
    install('psutil') 
    from psutil import virtual_memory
    mem = virtual_memory()
    return str((mem.total / 2) / 1000000)
def get_the_system_cores():
    install('psutil') 
    from psutil import cpu_count
    return str(cpu_count())

def create_MosesAPI_docker_image():
    commands_to_run_inside_of_docker = "docker-machine create --driver virtualbox default;";
    #create a good docker machine
    commands_to_run_inside_of_docker += "docker-machine rm acrazymachineforacrazyidea -y; ";
    commands_to_run_inside_of_docker +=  "docker-machine create --driver virtualbox --virtualbox-cpu-count "+get_the_system_cores()+" --virtualbox-memory "\
        + '"' + get_half_the_system_memory() + '"' + " --virtualbox-disk-size \"40000\" acrazymachineforacrazyidea; ";
    #eval docker machine
    commands_to_run_inside_of_docker += "eval \"$(docker-machine env acrazymachineforacrazyidea)\";";
    #and build the moses image
    commands_to_run_inside_of_docker += " docker build -t test1 \"" + os.path.abspath("./WinCompatibleMoses/Moses-API/") + "\""
    #and remain open
    #commands_to_run_inside_of_docker += ";bash";

    os.chdir("C:\Program Files\Docker Toolbox")
    p = subprocess.check_call(['start.sh', commands_to_run_inside_of_docker], shell=True)

if __name__ == "__main__":
    #first
    download_docker_toolset()
    #now run the installer
    os.system("DockerToolbox.exe")
    #then delete the installer
    os.remove("DockerToolbox.exe")
    #and finally
    create_MosesAPI_docker_image()


