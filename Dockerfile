FROM python:3.12-slim

# Chrome
RUN apt-get update &&  \
    apt-get install -y -q wget && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y -q ./google-chrome-stable_current_amd64.deb  && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# JDK + Allure
RUN apt-get update &&  \
    apt-get install -y -q openjdk-17-jdk && \
    wget -q https://github.com/allure-framework/allure2/releases/download/2.34.1/allure_2.34.1-1_all.deb && \
    apt-get install -y -q ./allure_2.34.1-1_all.deb && \
    rm allure_2.34.1-1_all.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/workspace

COPY ./requirements.txt /usr/workspace

RUN pip install --no-cache-dir -r requirements.txt