properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/Datsent/WorldOfGames.git/')])
pipeline{
    agent any
    stages{
        stage('Checkout git repository'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'cat README.md'
                    }
                    else{
                        bat 'type README.md'  
                    }
                }   
            }
        }
        stage('Build Docker Image'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker-compose build'
                    }
                    else{
                        bat 'docker-compose build'  
                    }
                }
                
            }
        }
        stage('Docker Run'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker-compose up -d'
                    }
                    else{
                        bat 'docker-compose up -d'  
                    }
                }
            }
        }
        stage('Test'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'pip install -r Utils\\requirements.txt'
                        sh 'python Utils\\e2e.py'
                    }
                    else{
                        bat 'pip install -r Utils\\requirements.txt'
                        bat 'python Utils\\e2e.py'
                    }
                }
            }
        }
        stage('Terminate Container'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker stop WoG_WEB'
                    }
                    else{
                        bat 'docker stop WoG_WEB'
                    }
                }
            }
        }
        stage('Delete Container'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker rm WoG_WEB'
                    }
                    else{
                        bat 'docker rm WoG_WEB'
                    }
                }
            }
        }
        stage('Push Image to DockerHub'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker push datsent/worldofgames'
                    }
                    else{
                        bat 'docker push datsent/worldofgames'
                    }
                }
            }
        }
        stage('Delete Image'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker rmi datsent/worldofgames'
                    }
                    else{
                        bat 'docker rmi datsent/worldofgames'
                    }
                }
            }
        }
    }
}
