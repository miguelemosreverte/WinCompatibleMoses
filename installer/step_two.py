import os, subprocess



def create_MosesAPI_docker_image():
    commands = ""
    #first create the default docker machine if it does not exists
    commands += "start.sh docker-machine create --driver virtualbox default; "  
    #then run the third and last part of the installation
    commands += "python \"" + (os.path.join(os.path.dirname(os.path.abspath(__file__)), "step_three.py")) + "\";bash;"
    
    os.chdir("C:\Program Files\Docker Toolbox")
    p = subprocess.check_call(['start.sh', commands], shell=True)
    
if __name__ == "__main__":
    create_MosesAPI_docker_image()

