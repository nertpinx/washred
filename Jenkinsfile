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
            sleep 20
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
      steps {
        sh 'python setup.py pylint'
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
        stage('') {
          steps {
            echo 'aaaaaa'
          }
        }
      }
    }
    stage('') {
      steps {
        echo 'asdf'
        isUnix()
      }
    }
  }
}