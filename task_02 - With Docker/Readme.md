## How to run
In VS Code terminal, type following command to build a new docker image

```
docker build -t rest-apis-flask-python .
```
Note: Make sure in your current path `Dockerfile` is present.

Once a docker image is built run the container using

```
docker run -dp 5005:5000 rest-apis-flask-python 
```

### Other Notes
--- 
I am on Windows 10 running this under Ubuntu 18.08 environment using WSL.
Here, While building from the dockerfile, it asked me:

```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

One way here is to start the docker service..usually in linux we can start this using `systemctl start docker` but since we are in WSL, this gave me following message:

```
System has not been booted with systemd as init system (PID 1). Can't operate.
```

One way is to use other command `sudo service docker start`. (It worked!)

Well..life is not easy it gave me another error

```
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/build?buildargs=%7B%7D&cachefrom=%5B%5D&cgroupparent=&cpuperiod=0&cpuquota=0&cpusetcpus=&cpusetmems=&cpushares=0&dockerfile=Dockerfile&labels=%7B%7D&memory=0&memswap=0&networkmode=default&rm=1&shmsize=0&t=rest-apis-flask-python&target=&ulimits=null&version=1": dial unix /var/run/docker.sock: connect: permission denied
```

I think we need to add user to the docker group or some other hacks 
Ref: https://stackoverflow.com/questions/51342810/how-to-fix-dial-unix-var-run-docker-sock-connect-permission-denied-when-gro

I choose the following:

```
sudo chmod 666 /var/run/docker.sock
```


