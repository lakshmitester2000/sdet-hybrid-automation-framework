pipeline {
    agent any

    environment {
        // Define your Docker image name
        DOCKER_IMAGE = "my-selenium-tests"
    }

    stages {
        stage('Checkout') {
            steps {
                // This pulls the code from your remote repo
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Rebuilds the test-runner image
                    sh "docker compose build tests"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        // Run the grid and the tests
                        sh "docker compose up --abort-on-container-exit --exit-code-from tests"
                    } finally {
                        // Always shut down the grid, even if tests fail
                        sh "docker compose down"
                    }
                }
            }
        }

        stage('Archive Reports') {
            steps {
                // This saves your Allure results inside Jenkins
                allure includeProperties: false, results: [[path: 'reports/allure-results']]
            }
        }
    }
}