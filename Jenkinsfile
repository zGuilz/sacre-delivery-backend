@Library('agro-mais-pipeline@master')_

pipeline{
    agent { label 'master || docker'}
    stages{
        stage("Checkout Project"){
            steps{    
                git url: "https://github.com/zGuilz/agro_plus-backend",
                    branch: 'main'
                sh "ls"
                
                sh "curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-338.0.0-linux-x86_64.tar.gz"
                sh "./google-cloud-sdk/install.sh"
                sh "./google-cloud-sdk/bin/gcloud init"
            } 
        }
    }
}



