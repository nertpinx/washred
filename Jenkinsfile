pipeline {
  agent any
  stages {
    stage('pre') {
      steps {
        echo 'Pre-ing'
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