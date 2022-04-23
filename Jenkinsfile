properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/Datsent/WorldOfGames.git/')])
pipeline{
    agent any
    	environment {
		DOCKERHUB_CREDENTIALS = credentials('test')
	    }

    stages{
        stage('Checkout git repository'){
            steps{
                git 'https://github.com/Datsent/WorldOfGames.git/'
                //script {
                //    //git 'https://github.com/Datsent/WorldOfGames.git'
                //    if (isUnix()==true){
                //        sh 'type README.md'
                //    }
                //    else{
                //        bat 'type README.md'  
                //    }
                //}
                echo 'Clone Git Project Done'
            }
        }
        stage('Build Docker Image'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker-compose build'
                        echo "Build Docker Image completed"
                    }
                    else{
                        bat 'docker-compose build'
                        echo "Build Docker Image completed"
                    }
                }
                
            }
        }
        stage('Docker Run'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker-compose up -d'
                        echo "Container Running"
                    }
                    else{
                        bat 'docker-compose up -d'
                        echo "Container Running"
                    }
                }
            }
        }
        stage('Test'){
                steps{
                  catchError(message: 'The Build is FAILED. No Push', stageResult: 'FAILURE') {
                    script {
                        try{
                            if (isUnix()==true){
                                sh 'pip install -r Utils\\requirements.txt'
                                sh 'python Utils\\e2e.py'
                                echo "Test PASSED"
                            }
                            else{
                                bat 'pip install -r Utils\\requirements.txt'
                                bat 'python Utils\\e2e.py'
                                echo "Test PASSED"
                            }
                        }
                        catch (e) {
                            echo "Test FAILED"
                            currentBuild.result = "FAILURE"
                            currentStage.result = "FAILURE"
                        } 
                    }
                  }
                }
        }
        stage('Terminate Container'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker stop WoG_WEB'
                        echo "Container Stopped"
                    }
                    else{
                        bat 'docker stop WoG_WEB'
                        echo "Container Stopped"
                    }
                }
            }
        }
        stage('Delete Container'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker rm WoG_WEB'
                        echo "Container Removed"
                    }
                    else{
                        bat 'docker rm WoG_WEB'
                        echo "Container Removed"
                    }
                }
            }
        }
        stage('Docker Login'){
            steps{
              catchError(message: 'The Build is FAILED. No Push', stageResult: 'FAILURE') {
                script {
                    if (isUnix()==true){
                        if (currentBuild.result == "FAILURE"){
                            echo "The Test stage is fail. No need Login"
                            currentStage.result = "FAILURE"
                        }
                        else{
                            sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'                            
                        }
                    }
                    else{
                        if (currentBuild.result == "FAILURE"){
                            echo "The Test stage is fail. No need Login"
                            currentStage.result = "FAILURE"
                        }
                        else{
                            bat 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'                            
                        }
                    }
                }
              }
            }    
        }
        stage('Push Image to DockerHub'){
            steps{
              catchError(message: 'The Build is FAILED. No Push', stageResult: 'FAILURE') {
                script {
                    if (isUnix()==true){
                        if (currentBuild.result == "FAILURE"){
                            echo "The Test stage is fail. The Image didn`t pushed"
                            currentStage.result = "FAILURE"
                        }
                        else{
                            sh 'docker push datsent/worldofgames'                            
                        }
                    }
                    else{
                        if (currentBuild.result == "FAILURE"){
                            echo "The Test stage is fail. The Image didn`t pushed"
                            currentStage.result = "FAILURE"
                        }
                        else{
                            bat 'docker push datsent/worldofgames'                            
                        }
                    }
                }
              }
            }
        }
        stage('Delete Image'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker rmi datsent/worldofgames'
                        echo "Local Image removed"
                    }
                    else{
                        bat 'docker rmi datsent/worldofgames'
                        echo "Local Image removed"
                    }
                }
            }
        }
        stage('Docker Logout'){
            steps{
                script {
                    if (isUnix()==true){
                        sh 'docker logout'
                        echo "Logout"
                    }
                    else{
                        bat 'docker logout'
                        echo "Logout"
                    }
                }
            }
        }
    }
}
