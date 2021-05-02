@Library('agro-mais-pipeline@master')_

/*pipeline{
    agent {
        label 'master'
    }
    stages{
        stage("Checkout Project"){
            agent {         
               label 'docker'
             } 
            steps{    
                git url: "https://github.com/zGuilz/agro_plus-backend",
                    branch: 'main'
                sh "ls"
                
                sh "docker pull google/cloud-sdk:latest"
                sh "docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login"
          
                //sh "./google-cloud-sdk/install.sh"
                //sh "./google-cloud-sdk/bin/gcloud init"
            } 
        }
    }
}*/

node {  
    stage('Build') { 
        echo "test"
    }
    stage('Test') { 
        // 
    }
    stage('Deploy') { 
        // 
    }
}



