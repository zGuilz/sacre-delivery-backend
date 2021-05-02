@Library('agro-mais-pipeline@master')_

pipeline{
    agent { label 'master || dockerfile'}
    stages{
        stage("Checkout Project"){
            steps{    
                git url: "https://github.com/zGuilz/agro_plus-backend",
                    branch: 'main'
                sh "ls"
                
          
                //sh "./google-cloud-sdk/install.sh"
                sh "./google-cloud-sdk/bin/gcloud init"
            } 
        }
    }
}



