# Challenge - 02

Files provided:
```
├── challenge-02
│   ├── README.md
│   └── golang
│       ├── file.txt
│       └── server.go
```

## Ask
- Please find `golang` folder which has simple web server implementation in go. Server reads file.txt and displays the contents as home page.

- Server can be built with CLI command. This will provide executable file `server`
```
#cd golang 
#go build server.go
```
- Server can be started by CLI command
```
#./server 
```
- You will also find two files, which should be read based on the Deployment environment instead of file.txt content by server.
```
file-dev.txt --> file read for DEV environment
file-prood.txt --> file read for PROD environment
```
- Your task is to work on Deployment files for this server. Start with containerizing the app and then use `docker-compose` to deploy.
- As stretch goal, think about observability and what can be done.

- Make sure at deployment time, you can pass Environment as parameter to select value DEV/PROD. Based on Environment server should display contents of either file-dev.txt or file-prod.txt

- Hints:
  1) you can't change server.go but can manipulate file*.* files in your deployment.
  2) make sure your process includes golang build, run, deploy steps accordingly.
  
- Submit/commit your code as a new file/s to your personal repo folder named challenge-02

- Please provide complete written instructions on how to use your solution files. Like how to run, build, deploy.

## Solution 
- I've created a Docker file "Dockerfile" and Docker compose file "docker-compose.yaml" to achieve the ask.

### Prerequisites
- We need Docker to be installed in our environment and Docker service to be in running state to execute the above Docker resource files.
```
curl -fsSL https://get.docker.com/ | sh
sudo systemctl start docker
```

### Steps to execute Script
- Navigate inside "challenge-02/golang" directory.
- To execute the web server for "dev" with environment vairable.
```
vi docker-compose.yaml # update the ENV: dev
docker-compose build
docker-compose up -d
```

- To execute the web server for "prod" with environment vairable.
```
vi docker-compose.yaml # update the ENV: prod
docker-compose stop
docker-compose build
docker-compose up -d
```

### Result
- On executing the docker compose with Dev environment variable.
<img width="369" alt="challenge02-dev" src="https://user-images.githubusercontent.com/54766634/164445563-495cab05-ffed-4348-afbf-f682504649e3.png">

- On executing the docker compose with Prod environment variable.
<img width="394" alt="challenge02-prod" src="https://user-images.githubusercontent.com/54766634/164445627-c430538d-513e-4881-8310-c3ab515fb9de.png">
