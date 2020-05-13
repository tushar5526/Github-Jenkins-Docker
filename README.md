# Github-Jenkins-Docker

- [ ]	Create container image that has Jenkins installed  using dockerfile, when we launch this image, it should automatically starts Jenkins service in the container.

- [ ]	Create a job chain of job1, job2, job3 and  job4 using build pipeline plugin in Jenkins 

- [ ]	 ***Job1*** : Pull  the Github repo automatically when some developers push repo to Github.

- [ ]	 ***Job2*** : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image container to deploy code ( eg. If code is of  PHP, then Jenkins should start the container that has PHP already installed ).

- [ ]	***Job3*** : Test your app if it  is working or not.

- [ ]	***Job4*** : if app is not working , then send email to developer with error messages.

- [ ]	Create One extra job j***Job5*** for monitor : If container where app is running. fails due to any reson then this job should automatically start the container again.

## Pre-Requisites 

- RHEL 8 as Base OS (or you can try on other linux bases OS)
- Docker is installed (if not use the docker.repo in this repository to download it )
- Basics of Linux, Docker, Jenkins


# Let's Start !

- [ ] Create container image that has Jenkins installed  using dockerfile, when we launch this image, it should automatically starts Jenkins service in the container.

- First clone this repo somewhere in your RHEL 8 base OS 
- Navigate to the cloned repo

```
git clone https://github.com/tushar5526/Github-Jenkins-Docker
cd Github-Jenkins-Docker

```

### Now we will build the image, that will run the Jenkins as soon as a container is deployed with this image (see Dockerfile RUN java -jar ... command)

```
docker build -t jenkins .
```

***IMAGE here***


- [x] ***Create container image that has Jenkins installed  using dockerfile, when we launch this image, it should automatically starts Jenkins service in the container.****

### This is done now, let's move to next step

- First launch a jenkins container

```
docker run -it -p 8081:8080 -v /var/run/docker.sock:/var/run/docker.sock --name jenkins jenkins
```


* This launches a jenkins conatainer that has docker installed already, but docker in docker is pretty difficult to manage and handle as well, using --privileged will expose our BASE OS to vulnerabilities as it gives the docker conatiner total access to BASE OS * 

***THE TRICK***

*docker runs on docker-daemon which runs in /var/run/docker.sock , so in the line* 
` -v /var/run/docker.sock:/var/run/docker.sock ` *we making the docker installed in jenkins container  to use daemon of BASE OS, we can still use all the docker commands like launching image and docker ps from the docker in jenkins container*

**You would get something like this, copy the admin password***



***Image here***


- [ ]	Create a job chain of job1, job2, job3 and  job4 using build pipeline plugin in Jenkins 

- If have RHEL on some virtual box, then you can login to jenkins by going to 

```
(base OS IP Address):8081
eg : 192.168.43.64:8081
```

- If RHEL is your main operating system, then do the following

```
docker inspect jenkins
```

- See the IP Address of the docker container

```
(IP Address of Container):8080

eg : 172.17.0.2:8080
```

- Now Enter the **password** you copied earlier and it will login you inside the jenkins

- You change the password of jenkins by clicking on **admin** in the left panel 

- Close windows to install plugins, we will do it later

- Go to ***Manage Jenkins** 
  - Scroll down and select ***Manage Plugins***
  - Go to ***Available*** tabs and install :
   - GitHub
   - Build Pipeline
   - Select ***Restart Jenkins when done***
 
 - [x]	***Create a job chain of job1, job2, job3 and  job4 using build pipeline plugin in Jenkins*** 
 
# JOB 1 :

- [ ]	 ***Job1*** : Pull  the Github repo automatically when some developers push repo to Github.
  
  - Name this job : ***Job1***
  - You can refer to my Blog www.github.com/tushar5526/jenkinsTest to read about it in detail
  
  **Image here***
  
  *You can ***GitHub WebHooks*** as described in my blog, but for simplicity I am using ***Poll SCM**, (POLL SCM will introduce some overhead)*
  
  - In  ***Post-Build-Actions*** select ***Build-Other-Projects*** and type ***Job2***, select ***save*** and ***apply***
  
  ***image here***
  
- [x]	 ***Job1*** : Pull  the Github repo automatically when some developers push repo to Github.


# JOB 2:

- [ ]	 ***Job2*** : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image container to deploy code ( eg. If code is of  PHP, then Jenkins should start the container that has PHP already installed ).

### How this will work ?

- I have made a python file which goes into the current workspace and checks the extension of downloaded files and then run respective container ( this file is already placed in jenkins container )

Take a look at python file : launch.py 

```
import os

for file in os.listdir('/root/.jenkins/workspace/Job1'):
  ext = os.path.splitext(file0[-1].lower()

  
  if ext == '.php':
    print('running httpd with php container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8081:8080 php')
    break
    
  if ext == '.py':
    print('running httpd with python3 container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8081:8080 python')
    break
    
  if ext == '.html':
    print('running httpd container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8081:8080 httpd')
    break
```



