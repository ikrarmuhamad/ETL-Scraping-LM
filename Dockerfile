FROM apache/airflow:2.10.4

# Salin file requirements.txt
COPY requirements.txt /

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt