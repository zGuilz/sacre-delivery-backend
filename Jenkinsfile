@Library('agro-mais-pipeline@master')_

pipeline{
    agent { label 'master' }
    stages{
        stage("Checkout Project"){
            steps{
                git url: "https://github.com/zGuilz/agro_plus-backend",
                    branch: 'master'
            }
            post{
                success{
                    echo "Projeto OK"
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



