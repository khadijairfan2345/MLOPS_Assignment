// Jenkinsfile
pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Logging into Docker hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo "$DOCKERHUB_PASS" | docker login -u $DOCKERHUB_USER --password-stdin'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my_app:latest .'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh '''
                    docker tag my_app:latest $DOCKERHUB_USER/my_app:latest
                    docker push $DOCKERHUB_USER/my_app:latest
                '''
            }
        }
        stage('Notify Admin') {
            steps {
                mail to: 'khadijairfan2345@email.com',
                     subject: "Jenkins Job Successful",
                     body: "Jenkins job was completed successfully and the Docker image is pushed to Docker Hub."
            }
        }
    }
}
