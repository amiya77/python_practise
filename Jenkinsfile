ipeline {
    agent {label 'master'}

    stages {
        stage('Hello') {
            steps {
                sshagent(credentials:["installer_pem"]){
                    sh  "ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 'hostname'"
          }
            }
        }
        stage('AWS Login') {
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'AWS_CREDS', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh '''
                        date=$(date '+%d-%m-%y-%s')
                        aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 086272791573.dkr.ecr.ap-south-1.amazonaws.com
                        docker pull 086272791573.dkr.ecr.ap-south-1.amazonaws.com/4500-k8s-qa:backend-cicdpipeline
                        docker tag 086272791573.dkr.ecr.ap-south-1.amazonaws.com/4500-k8s-qa:backend-cicdpipeline 086272791573.dkr.ecr.ap-south-1.amazonaws.com/4500-k8s-qa:backend-$date
                        docker push 086272791573.dkr.ecr.ap-south-1.amazonaws.com/4500-k8s-qa:backend-$date
                        docker pull $image_name
                        docker tag $image_name 086272791573.dkr.ecr.ap-south-1.amazonaws.com/4500-k8s-qa:backend-cicdpipeline
                        docker push 086272791573.dkr.ecr.ap-south-1.amazonaws.com/4500-k8s-qa:backend-cicdpipeline
                    '''
                }
            }
        }
        stage('DB Backup') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'MARIADB_CREDS', passwordVariable: 'PASSWORD', usernameVariable: 'USER')]){
                    sshagent(credentials:["installer_pem"]){
                        sh '''
                            ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 "sudo kubectl exec -it mariadb-sts-0 -- mysqldump --routines -u${USER} -p${PASSWORD} mcube > /home/appadmin/jenkins/mcube_dump-$(date '+%d-%m-%y-%s').sql"
                        '''
                    }
                }
            }
        }
        stage('ES Backup') {
            steps {
                withCredentials([usernameColonPassword(credentialsId: 'es_key', variable: 'ELASTIC_CREDS')]) {
                    sshagent(credentials:["installer_pem"]){
                        sh '''
                            ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 "sudo docker run -v /opt/mcube/mcube-es-server/import/:/tmp/ --rm -i elasticdump/elasticsearch-dump --input=http://${ELASTIC_CREDS}@100.112.1.140:9200/.nxtgen --output=/tmp/nxtgen_bak_test-$(date '+%d-%m-%y-%s')-settings.json --type=settings"
                            ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 "sudo docker run -v /opt/mcube/mcube-es-server/import/:/tmp/ --rm -i elasticdump/elasticsearch-dump --input=http://${ELASTIC_CREDS}@100.112.1.140:9200/.nxtgen --output=/tmp/nxtgen_bak_test-$(date '+%d-%m-%y-%s')-mapping.json --type=mapping"
                            ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 "sudo docker run -v /opt/mcube/mcube-es-server/import/:/tmp/ --rm -i elasticdump/elasticsearch-dump --input=http://${ELASTIC_CREDS}@100.112.1.140:9200/.nxtgen --output=/tmp/nxtgen_bak_test-$(date '+%d-%m-%y-%s')-data.json --type=data"
                          '''
                    }
                }
            }
        }
        stage('Run SQL Script If Any') {
                when {
                    expression {
                        return params.test != null && params.test != ''
                    }
                }
                steps {
                    script {
                        // Use withFileParameter to handle the uploaded file
                        withFileParameter('test') {
                            withCredentials([usernamePassword(credentialsId: 'MARIADB_CREDS', passwordVariable: 'PASSWORD', usernameVariable: 'USER')]){
                                sshagent(credentials:["installer_pem"]){
                                    sh """
                                        scp -o StrictHostKeyChecking=no ${test} appadmin@100.112.1.140:/home/appadmin/jenkins/test.sql
                                        ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 "sudo kubectl exec -it mariadb-sts-0 -- mysql -u${USER} -p${PASSWORD} mcube < /home/appadmin/jenkins/test.sql"
                                        echo "Done"
                                    """
                                }
                            }
                        }
                    }
                }
            }
        stage('Deployment') {
            steps {
                sshagent(credentials:["installer_pem"]){
                    sh '''
                        ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 "cd /home/appadmin/jenkins && sudo kubectl delete -f backend-dep-svc-conf.yml"
                        ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 "cd /home/appadmin/jenkins && sudo kubectl apply -f backend-dep-svc-conf.yml"
                        ssh -t -t -o StrictHostKeyChecking=no appadmin@100.112.1.140 "sudo kubectl rollout restart deployment openresty"
                    '''
                }
            }
        }
    }
     post {
          success {
            emailext attachLog: false, attachmentsPattern: 'log.txt', body: "Hi Team,\n\nYour deployment for backend in 5.1 QA environment has been done successfully.\n\nThanks and Regards,\nMcube Team", from: "tcgmcube.support@tcgdigital.com", replyTo: "rupam.bose@tcgdigital.com", recipientProviders: [requestor()], subject: "5.1 QA deployment status", to: '''cc:sheikh.ashir@tcgdigital.com, bcc:sourav.sen@tcgdigital.com'''
          }
          failure {
            emailext attachLog: true, attachmentsPattern: 'log.txt', body: "Hi Team,\n\nYour deployment for backend in 5.1 QA environment has failed. Please find attached logs for details.\n\nThanks and Regards,\nMcube Team", from: "tcgmcube.support@tcgdigital.com", replyTo: "rupam.bose@tcgdigital.com", recipientProviders: [requestor()], subject: "5.1 QA deployment status", to: '''cc:sheikh.ashir@tcgdigital.com, bcc:sourav.kundu@tcgdigital.com'''
          }
     }   
}
