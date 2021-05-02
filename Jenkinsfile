@Library('agro-mais-pipeline@master')_

pipeline{
    agent { label 'master || docker'}
    stages{
        stage("Checkout Project"){
            steps{    
                git url: "https://github.com/zGuilz/agro_plus-backend",
                    branch: 'main'
                sh "ls"
                
                sh "sudo apt-get install apt-transport-https ca-certificates gnupg"
                //sh "./google-cloud-sdk/install.sh"
                sh "./google-cloud-sdk/bin/gcloud init"
            } 
        }
    }
}



