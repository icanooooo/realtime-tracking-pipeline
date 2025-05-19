#!/bin/bash

airflow db init

airflow users create \
	-- username airflow \
	-- password airflow \
	-- firstname Muhammad \
	-- lastname Ihsan \
	-- role Admin \
	-- email muhihsan0.jkt@gmail.com

tail -f /dev/null
