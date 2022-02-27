pipeline{
    agent any
    stages{
        stage('Checkout git repository'){
            steps{
                script {
                    git 'https://github.com/Datsent/WorldOfGames.git'
                    if (isUnix()==true){
                        sh 'type README.md'
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
                        sh 'cd Utils'
                        sh 'python e2e.py'
                    }
                    else{
                        bat 'pip install -r Utils\\requirements.txt'
                        bat 'python Utils\\e2e.py'
                    }
                }
            }
            
        }
    }
}
