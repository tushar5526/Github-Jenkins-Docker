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




