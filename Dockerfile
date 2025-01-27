FROM apache/airflow:2.10.4

USER root

# Tambahkan Google Chrome Repository dan install Google Chrome
RUN apt-get update && apt-get install -y wget gnupg && \
    wget -qO - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable unzip && \
    rm -rf /var/lib/apt/lists/*

# Set Chrome environment variables
ENV CHROME_BIN=/usr/bin/google-chrome
ENV CHROMEDRIVER_BIN=/usr/local/bin/chromedriver

# Beralih ke pengguna airflow untuk instalasi Python dependencies
USER airflow

# Salin file requirements.txt ke container
COPY requirements.txt /

# Install Python dependencies dari requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Kembali ke pengguna airflow
USER airflow