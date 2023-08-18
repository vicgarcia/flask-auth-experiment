FROM python:3.10-bookworm

RUN apt-get -y clean && apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python3-dev python3-venv python3-pip

RUN useradd -s /bin/bash testuser && \
    echo 'testuser:testpassword' | chpasswd

RUN pip install flask flask-jwt-extended python-pam six

COPY app.py /

EXPOSE 3000

CMD ["python", "app.py"]