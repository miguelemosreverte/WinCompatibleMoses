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
    #create a good docker machine
    commands_to_run_inside_of_docker = "docker-machine rm acrazymachineforacrazyidea -y; ";
    commands_to_run_inside_of_docker +=  "docker-machine create --driver virtualbox --virtualbox-cpu-count "+get_the_system_cores()+" --virtualbox-memory "\
        + '"' + get_half_the_system_memory() + '"' + " --virtualbox-disk-size \"40000\" acrazymachineforacrazyidea; ";
    #eval docker machine
    commands_to_run_inside_of_docker += "eval \"$(docker-machine env acrazymachineforacrazyidea)\";";
    #and build the moses image
    commands_to_run_inside_of_docker += " docker build -t test1 \"" + os.path.abspath("../Moses-API/").replace("\\","/") + "/\"" + ";"
    #and remain open
    #commands_to_run_inside_of_docker += ";bash";

    os.chdir("C:\Program Files\Docker Toolbox")
    p = subprocess.Popen(['start.sh', commands_to_run_inside_of_docker], shell=True)

if __name__ == "__main__":
    create_MosesAPI_docker_image()


