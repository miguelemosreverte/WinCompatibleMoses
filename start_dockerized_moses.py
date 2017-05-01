
import os, subprocess


pepe = os.path.abspath("docker-ip.txt");
commands_to_run_inside_of_docker = "docker-machine ip;";
commands_to_run_inside_of_docker += "docker-machine ip > \"" + pepe + "\";";

os.chdir("C:\Program Files\Docker Toolbox")

p = subprocess.Popen(['start.sh', commands_to_run_inside_of_docker], shell=True)
