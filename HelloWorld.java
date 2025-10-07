pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                bat 'javac HelloWorld.java'
            }
        }

        stage('Test') {
            steps {
                echo 'Running the program...'
                bat 'java HelloWorld'
            }
        }

        stage('Archive') {
            steps {
                echo 'Archiving artifacts...'
                archiveArtifacts artifacts: '**/*.class', fingerprint: true
            }
        }
    }
}

