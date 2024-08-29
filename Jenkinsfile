pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Shava173/Weather_Exam.git'
            }
        }
        
        stage('Test') {
            steps {
                // Тестування HTML файлів
                sh 'htmlhint index.html'
                sh 'htmlhint templates/*.html'

                // Тестування CSS файлів
                script {
                    def cssFiles = sh(script: "ls static/*.css 2>/dev/null", returnStatus: true)
                    if (cssFiles == 0) {
                        sh 'csslint static/*.css'
                    } else {
                        echo 'No CSS files found to lint.'
                    }
                }

                // Тестування JavaScript файлів (якщо вони у вас є)
                // sh 'jshint static/*.js'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'rsync -avz --delete-after $WORKSPACE/ /var/www/html/'
                sh 'sudo systemctl restart apache2'
            }
        }
        
        stage('Verify') {
            steps {
                script {
                    def response = sh(script: "curl -o /dev/null -s -w '%{http_code}' http://localhost", returnStdout: true).trim()
                    if (response != '200') {
                        error("Website is not reachable, received HTTP status: ${response}")
                    }
                }
            }
        }
    }
}
