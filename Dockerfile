FROM python:3.10-slim-bookworm
USER root
RUN mkdir /app
WORKDIR /app/

# Install system dependencies required by Airflow and other packages
RUN apt-get update -y && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
RUN pip3 install --no-cache-dir -r requirements.txt

ENV AWS_DEFAULT_REGION="us-east-1"
ENV BUCKET_NAME="mynetworksecurity-1"
ENV PREDICTION_BUCKET_NAME="my-network-datasource"
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True

RUN airflow db init
RUN airflow users create -e patilsunda14@gmail.com -f sunda -l patil -p admin -r Admin -u admin
RUN chmod 777 start.sh

ENTRYPOINT ["/bin/sh"]
CMD ["start.sh"]