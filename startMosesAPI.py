import os, subprocess

def startMosesAPI():
    directory = os.path.abspath("./WinCompatibleMoses/")
    os.chdir("C:\Program Files\Docker Toolbox")
    commands_to_run_inside_of_docker = "";
    #get docker ip
    docker_ip_file = directory.replace('\\','/') + "/docker-ip.txt";
    commands_to_run_inside_of_docker += "docker-machine ip acrazymachineforacrazyidea > "+docker_ip_file+";";
    #eval docker machine
    commands_to_run_inside_of_docker += "eval \"$(docker-machine env acrazymachineforacrazyidea)\";";    
    #and build the moses image
    commands_to_run_inside_of_docker += " docker run -d -p 5000:5000 test1"
    #and remain open
    #commands_to_run_inside_of_docker += ";bash";

    p = subprocess.Popen(['start.sh', commands_to_run_inside_of_docker], shell=True)


if __name__ == "__main__":
    startMosesAPI()

