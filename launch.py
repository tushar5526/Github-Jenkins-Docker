import os

for file in os.listdir('/root/.jenkins/workspace/job1'):
  ext = os.path.splitext(file0[-1].lower()

  
  if ext == '.php':
    print('running httpd with php container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8082:8080 php')
    break
    
  if ext == '.py':
    print('running httpd with python3 container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8082:8080 python')
    break
    
  if ext == '.html':
    print('running httpd container')
    os.system('docker run -it -v /root/.jenkins/workspace/job1/:/var/www/html -p 8082:8080 httpd')
    break
