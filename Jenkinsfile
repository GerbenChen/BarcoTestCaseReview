pipeline {
  agent none
  stages {
    stage('build and test') {
      agent { docker { image 'python:3.6.9-alpine' } }
      stages {
        stage('build'){
          steps {
            sh 'pip install --no-cache-dir -r requirements.txt'
          }
        }
        stage('test') {
          steps {
            sh 'python warrantyinfo_testcase.py -v'
          }
          post {
            always {
              junit 'Barco/warrantyinfo_testcase_results.xml'
            }
          }
        }
      }
    }
    stage('build docker image'){
      agent any
      steps{
        sh 'docker build -t warrantyinfo:latest .'
        sh 'a=`docker images -f "dangling=true" -q | wc -l`'
        sh 'if [ $a -ge 0 ];then docker rmi $(docker images -f "dangling=true" -q);fi'
      }
    }
  }
}