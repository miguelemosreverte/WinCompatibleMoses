import os, subprocess

def startMosesAPI():
    directory = os.path.abspath("./Moses-API/")

    commands_to_run_inside_of_docker = "";
    #eval docker machine
    commands_to_run_inside_of_docker += "eval \"$(docker-machine env acrazymachineforacrazyidea)\";";
    #and build the moses image
    commands_to_run_inside_of_docker += " docker run -t -p 5000:5000 test1"
    #and remain open
    #commands_to_run_inside_of_docker += ";bash";

    os.chdir("C:\Program Files\Docker Toolbox")
    p = subprocess.Popen(['start.sh', commands_to_run_inside_of_docker], shell=True)


if __name__ == "__main__":
    startMosesAPI()

