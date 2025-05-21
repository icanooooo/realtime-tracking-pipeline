pipeline {
	agent any

	environment {
		PGPASSWORD = 'thisisapassword'
	}

	stages {
		stage('Create Table') {
			steps {
				sh '''
					psql -h localhost -U icanooo -d historical_db -f createdb/create_tables.sql
				'''
			}
		}
	}
}

