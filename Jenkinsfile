pipeline {
	agent any

	environment {
		VENV_PATH = "/opt/venv"
		PATH = "${VENV_PATH}/bin:${env.PATH}"
	}

	stages {
		stage('Create Table') {
			steps {
				sh '''
					python3 /var/jenkins_home/scripts/generate_data.py
				'''
			}
		}
	}
}

