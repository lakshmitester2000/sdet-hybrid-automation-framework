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

        stage('Cleanup Environment') {
            steps {
                script {
                    // Ensures any hanging containers are stopped before we start
                    bat "docker compose down"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // 'bat' is the Windows equivalent of 'sh'
                    bat "docker compose build tests"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        // Run the grid and the tests
                        // --abort-on-container-exit stops the grid when tests finish
                        bat "docker compose up --abort-on-container-exit --exit-code-from tests"
                    } finally {
                        // Always shut down the grid to free up RAM/CPU
                        bat "docker compose down"
                    }
                }
            }
        }

        stage('Archive Reports') {
            steps {
                // This saves your Allure results inside Jenkins
                // Ensure the path matches where your code saves the JSON results
                allure includeProperties: false, results: [[path: 'reports/allure-results']]
            }
        }
    }
}