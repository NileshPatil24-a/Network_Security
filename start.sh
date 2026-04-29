#!/bin/sh
nohup airflow scheduler &
nohup airflow webserver -p 8081 &
python main.py