FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y postgresql-client

USER jenkins
