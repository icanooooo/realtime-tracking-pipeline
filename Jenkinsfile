pipeline {
	agent any

	environment {
		PGPASSWORD = 'thisisapassword'
	}

	stages {
		stage('Create Table') {
			steps {
				sh '''
					psql -h application_postgres -U icanooo -d historical_db -f /var/jenkins_home/sql/create_tables.sql
				'''
			}
		}
	}
}

