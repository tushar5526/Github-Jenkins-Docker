# Github-Jenkins-Docker

![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/9.png)


- [ ]	Create container image that has Jenkins installed  using dockerfile, when we launch this image, it should automatically start Jenkins service in the container.

- [ ]	Create a job chain of job1, job2, job3 and  job4 using build pipeline plugin in Jenkins 

- [ ]	 ***Job1*** : Pull  the Github repo automatically when some developers push repo to Github.

- [ ]	 ***Job2*** : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image container to deploy code ( eg. If code is of  PHP, then Jenkins should start the container that has PHP already installed ).

- [ ]	***Job3*** : Test your app if it  is working or not.

- [ ]	***Job4*** : if app is not working , then send email to developer with error messages.

- [ ]	***Job5*** Create One extra job for monitoring : If container where app is running. fails due to any reson then this job should automatically start the container again.

## Pre-Requisites 

- RHEL 8 as Base OS (or you can try on other linux bases OS)
- Docker is installed (if not use the docker.repo in this repository to download it )
- Basics of Linux, Docker, Jenkins
- Docker Images : 
  - **php** named image, which has httpd and php installed
  - **py** named image, which has httpd and python installed
  - **httpd** named image, which has httpd installed

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

![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/1.PNG)

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



![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/2.PNG)



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

![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/8.PNG)


- You change the password of jenkins by clicking on **admin** in the left panel 

- Close windows to install plugins, we will do it later

- Go to ***Manage Jenkins** 
  - Scroll down and select ***Manage Plugins***
  - Go to ***Available*** tabs and install :
   - GitHub
   - Build Pipeline
   - Select ***Restart Jenkins when done***
 

 
# JOB 1 :

- [ ]	 ***Job1*** : Pull  the Github repo automatically when some developers push repo to Github.
  
  - Name this job : ***Job1***
  - You can refer to my Blog www.github.com/tushar5526/jenkinsTest to read about it in detail
  
![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/3.PNG)

  
  *You can ***GitHub WebHooks*** as described in my blog, but for simplicity I am using ***Poll SCM**, (POLL SCM will introduce some overhead)*
  
  - In  ***Post-Build-Actions*** select ***Build-Other-Projects*** and type ***Job2***, select ***save*** and ***apply***
  
![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/4.PNG)


# JOB 2:

- [ ]	 ***Job2*** : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image container to deploy code ( eg. If code is of  PHP, then Jenkins should start the container that has PHP already installed ).

### How will this work ?

- I have made a python file which goes into the current workspace and checks the extension of downloaded files and then run respective container ( this file is already placed in jenkins container )

Take a look at python file : launch.py 

```
import os

for file in os.listdir('/root/.jenkins/workspace/Job1'):
  ext = os.path.splitext(file[-1].lower()

  
  if ext == '.php':
    print('running httpd with php container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8082:8080 --name test php')
    break
    
  if ext == '.py':
    print('running httpd with python3 container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8082:8080 --name test python')
    break
    
  if ext == '.html':
    print('running httpd container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8082:8080 --name test httpd')
    break
```

- Create a job named ***Job2*** 
- Go to ***Build***
  - Select ***Execute Shell**
  - Type the following command
  ```
  cd /
  python3 launch.py
  ```
***This will launch the container at 8082 port***

- In  ***Post-Build-Actions*** select ***Build-Other-Projects*** and type ***Job34***, select ***save*** and ***apply***
  
![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/5.PNG)


![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/5-2.PNG)


# JOB 3 and JOB 4 :

*I will combine both these jobs as it was easy that way*

- [ ]	***Job3*** : Test your app if it  is working or not.

- [ ]	***Job4*** : if app is not working , then send email to developer with error messages.

- Make a new job named ***JOB34*** 
- Go to ***Build***
  - Select ***Execute Shell**
  - Type the following command
  
  ```
  status=$(curl -o /dev/null -sw "%{http_code}" 192.168.43.64:8082)
  if [[ status==200 ]]; then echo "good";
  else python3 /mail.py;
  fi
  ```
  
![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/6.PNG)
+
  
# JOB 5 : 
  
  - For this we will check ***test*** container is working or not every minute and launch a new one if it is not working
  
![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/7.PNG)

![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/7-2.PNG)

  
  
# PHEW ! Now you can AUTOMATE your development process easily

![Image description](https://github.com/tushar5526/Github-Jenkins-Docker/blob/master/images/10.PNG)

- [x]	Create container image that has Jenkins installed  using dockerfile, when we launch this image, it should automatically starts Jenkins service in the container.

- [x]	Create a job chain of job1, job2, job3 and  job4 using build pipeline plugin in Jenkins 

- [x]	 ***Job1*** : Pull  the Github repo automatically when some developers push repo to Github.

- [x]	 ***Job2*** : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image container to deploy code ( eg. If code is of  PHP, then Jenkins should start the container that has PHP already installed ).

- [x]	***Job3*** : Test your app if it  is working or not.

- [x]	***Job4*** : if app is not working , then send email to developer with error messages.

- [x]	***Job5*** Create One extra job for monitoring : If container where app is running. fails due to any reson then this job should automatically start the container again.


# Future Scope : 
- Support for backends like node.js
- Integration of Jenkins
