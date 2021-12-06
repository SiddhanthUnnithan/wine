import threading
import subprocess

def setup_environment():
    print("Setting up environment and installing dependencies for Basis...")
    cmd = 'apt update && apt upgrade && apt install -y curl wget libicu-dev'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in result.stdout:
        print(line)

def install_basis():
    print("Installing Basis...")
    cmd = 'curl -sL https://aka.ms/BasisCliInstall | bash'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in result.stdout:
        print(line)

def connect_basis_host():
    cmd = '$HOME/bin/basis host $TUNNEL_ID --access-token $HOST_ACCESS_TOKEN'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in result.stdout:
        print(line)

def run_python_debug_server():
    cmd = 'python -m debugpy --listen 127.0.0.1:5678 --wait-for-client ./train.py'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in result.stdout:
        print(line)

# synchronous
setup_environment()
install_basis()

# async threading
basis_thread = threading.Thread(target=connect_basis_host)
python_debug_thread = threading.Thread(target=run_python_debug_server)

# making a thread a `daemon` means that when the main process
# ends the thread will end too
basis_thread.daemon = True
python_debug_thread.daemon = True

# start the threads running
print("Starting thread connecting Basis host to tunnel...")
basis_thread.start()
print("Starting debug server thread...")
python_debug_thread.start()

# wait for all the child threads to terminate before ending
basis_thread.join()
python_debug_thread.join()