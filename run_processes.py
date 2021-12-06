from subprocess import Popen, PIPE

commands = ['python -m debugpy --listen 127.0.0.1:5678 --wait-for-client $WORKSPACE/train.py', 'basis host $TUNNEL_ID --access-token $HOST_ACCESS_TOKEN']

procs = [ Popen(i, stdout=PIPE, stderr=PIPE, shell=True) for i in commands ]

for p in procs:
   p.communicate()