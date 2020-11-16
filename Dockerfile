FROM bde2020/spark-python-template:2.4.0-hadoop2.7

COPY arquivo*.txt /tmp/

ENV SPARK_APPLICATION_PYTHON_LOCATION=/app/entrypoint.py
