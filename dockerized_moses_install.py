import os, shutil, subprocess

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

def download_my_repo():
    install("gitpython")
    import git

    DIR_NAME = "Moses-API"
    REMOTE_URL = "https://github.com/miguelemosreverte/Moses-API.git"

    if os.path.isdir(DIR_NAME):
        shutil.rmtree(DIR_NAME)

    os.mkdir(DIR_NAME)

    repo = git.Repo.init(DIR_NAME)
    origin = repo.create_remote('origin',REMOTE_URL)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)

    print "---- DONE ----"

def download_and_run_docker_toolset():
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
    #now run the installer
    os.system("DockerToolbox.exe")

#download_my_repo()
#download_and_run_docker_toolset()
directory = os.path.abspath("./Moses-API/")

commands_to_run_inside_of_docker = "";
#create a good docker machine
commands_to_run_inside_of_docker += "docker-machine create --driver virtualbox --virtualbox-cpu-count 4 --virtualbox-memory \"7900\" --virtualbox-disk-size \"40000\" acrazymachineforacrazyidea; ";
#eval docker machine
commands_to_run_inside_of_docker += "eval \"$(docker-machine env acrazymachineforacrazyidea)\";";
#and build the moses image
commands_to_run_inside_of_docker += " docker build -t test1 \"" + directory + "\""
#and remain open
commands_to_run_inside_of_docker += ";bash";

os.chdir("C:\Program Files\Docker Toolbox")
p = subprocess.Popen(['start.sh', commands_to_run_inside_of_docker], shell=True)


