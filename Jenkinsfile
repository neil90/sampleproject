pipeline {
  environment {
   SHARD = credentials('PROD_DATABRICKS_SHARD')
   TOKEN = credentials('PROD_DATABRICKS_TOKEN')

}    
 agent {
  docker {
   image 'np90/dbconnect:version-5.5.3'
   args '-e SHARD=$SHARD -e TOKEN=$TOKEN -e CLUSTERID=1110-025932-gases1'
  }
 }

 stages {
  stage('Install PyTest and Run Tests') {
   steps {
    sh 'pip install pytest'   
    sh 'cat ~/.databricks-connect #python -m pytest tests/'
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