@Library('agro-mais-pipeline@master')_

pipeline{
    agent { label 'master', docker { image 'python:3.5.1' } }
    stages{
        stage("Checkout Project"){
            steps{
                git url: "https://github.com/zGuilz/agro_plus-backend",
                    branch: 'main'
                sh "ls"
                sh "python --version"
                sh "curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-338.0.0-linux-x86_64.tar.gz"
                sh "./google-cloud-sdk/install.sh"
                sh "./google-cloud-sdk/bin/gcloud init"
            }
            post{
                success{
                    echo "Consegui efetuar o deploy"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}



