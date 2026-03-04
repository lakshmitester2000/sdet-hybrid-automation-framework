pipeline {
    agent any

    // ADDED: This tells Jenkins to use the 'allure' tool you configured in Global Tool Configuration
    tools {
        allure 'allure'
    }

    environment {
        DOCKER_IMAGE = "my-selenium-tests"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Cleanup Environment') {
            steps {
                script {
                    bat "docker compose down"
                    bat "docker rm -f selenium-hub test-runner || ver > nul"
                    bat "docker network prune -f"
                    bat "docker volume prune -f"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker compose build tests"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        // The exit code from the 'tests' container will determine if this stage passes or fails
                        bat "docker compose up --abort-on-container-exit --exit-code-from tests"
                    } finally {
                        bat "docker compose down"
                    }
                }
            }
        }

        stage('Archive Reports') {
            steps {
                // IMPORTANT: Ensure 'allure-results' matches the folder name created by pytest in your project
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }
    }

    // Optional: Keep your workspace clean after every run
    post {
        always {
            script {
                bat "docker image prune -f"
            }
        }
    }
}