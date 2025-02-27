pipeline {
 agent {
  docker {
   image 'np90/dbconnect:version-5.5.3'
   args '--entrypoint=\'\''
  }
 }
  environment {
   SHARD = credentials('PROD_DATABRICKS_SHARD')
   TOKEN = credentials('PROD_DATABRICKS_TOKEN')

}
 stages {
  stage('Set ~/databricks-connect file') {
   steps {
    sh '''
        cat << EOF > ~/.databricks-connect
        {
            "host": "$SHARD",
            "cluster_id": "1110-025932-gases1",
            "port": "15001",
            "ord_id": "0",
            "token": "$TOKEN"
        }
        EOF
    '''
   }
  }
  stage('Install PyTest and Run Tests') {
   steps {
    sh 'pip install pytest'   
    sh 'python -m pytest tests/'
   }
  }
  stage('Build Python Wheel') {
   steps {
    sh 'echo $JOB_NAME'
    sh 'python setup.py sdist bdist_wheel'
   }
  }
  stage('Upload') {
   steps {
    withAWS(region: 'us-west-2', credentials: 'ArtifactServiceAcct') {
     // Upload files from working directory 'dist' in your project workspace
     s3Upload(bucket: 'foobar.artifacts', path: 'modules/python/sampleproject/', workingDir: 'dist', includePathPattern: '**/*.whl')
    }
   }
  }
 }
}