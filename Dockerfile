FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    postgresql-client \
    python3 \
    python3-venv \
    python3-pip \
    && apt-get clean

# Using virtualenv in this image to run python script 
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install pandas psycopg2-binary sqlalchemy Faker

ENV PATH="/opt/venv/bin:$PATH"

USER jenkins

