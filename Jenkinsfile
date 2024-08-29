pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Клонування репозиторію з гілки main
                git branch: 'main', url: 'https://github.com/Shava173/Weather_Exam.git'
            }
        }
        
        stage('Test') {
            steps {
                // Команди для тестування
                sh 'htmlhint *.html'
                sh 'csslint *.css'
                sh 'jshint *.js'
            }
        }
        
        stage('Deploy') {
            steps {
                // Команди для деплою
                sh 'rsync -avz --delete-after $WORKSPACE/ /var/www/html/'
                sh 'sudo systemctl restart apache2'
            }
        }
        
        stage('Verify') {
            steps {
                // Перевірка роботи веб-сайту
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
