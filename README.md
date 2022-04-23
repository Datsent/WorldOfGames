# World of Games

CLI gaming platform created during DevOps course using:
- **Python** code - using Flask, Selenium and HTML.
- **Docker** - docker-compose.
- **Jenkins** - using jenkinsfile.

## Compatible
Compatible with Windows, Linux, Mac operating systems.

## Requirements
 - [Phiton 3.8](https://www.python.org/downloads/) and [pip installer](https://pip.pypa.io/en/stable/getting-started/)
 - [Docker deamon](https://www.docker.com/get-started/)
 - [Jenkins](https://www.jenkins.io/)

## Deployment

To deploy this project on docker container, use command:

```bash
  docker-compose up -d
```
This will deploy container on local docker deamon.
To play - use command:
```bash
docker exec -it WoG_WEB sh
```
Run the Game:
```bash
python MainGame.py
```
For Score visit in browser: *127.0.0.1:8081*
## Demo
![ezgif com-gif-maker](https://user-images.githubusercontent.com/45486622/164917193-c3999554-369a-4555-9b51-8b8e5eb09470.gif)

## Testin - Jenkins - Pipeline
Runing the test using Jenkins pipeline by Jenkinsfile. For pushing the image to your docker hub - need to provide credentials and incorporate them in your own Jenkins system under the appropriate id 
