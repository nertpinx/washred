pipeline {
  agent any
  stages {
    stage('pre') {
      steps {
        echo 'Preing'
      }
    }
    stage('almost') {
      parallel {
        stage('almost') {
          steps {
            sleep 5
            sh 'pwd'
          }
        }
        stage('second almost') {
          steps {
            echo 'dunno'
          }
        }
      }
    }
    stage('during') {
      agent {
        docker {
          image 'python:3-alpine'
        }

      }
      steps {
        sh './setup.py pylint'
      }
    }
    stage('post') {
      parallel {
        stage('post') {
          steps {
            build(job: 'asdf', quietPeriod: 5)
          }
        }
        stage('popost') {
          steps {
            node(label: 'meh')
          }
        }
        stage('error') {
          steps {
            echo 'aaaaaa'
          }
        }
      }
    }
    stage('error') {
      steps {
        echo 'asdf'
        isUnix()
      }
    }
  }
}