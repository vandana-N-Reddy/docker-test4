pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'echo "Build successful!"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 app.py'
            }
        }

        stage('Archive') {
            steps {
                echo 'Archiving results...'
                archiveArtifacts artifacts: '/*.txt', fingerprint: true
            }
        }
    }
}


