pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                bat 'echo Hello from Jenkins Build Stage'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'java HelloWorld'
            }
        }

        stage('Archive') {
            steps {
                echo 'Archiving artifacts...'
                bat 'echo Done!'
            }
        }
    }
}

