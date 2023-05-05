FROM python:3.9



COPY requirements.txt /
RUN pip install -r /requirements.txt


COPY utils /utils
COPY setup.py /
COPY script1.py /etl/cleaning.py
COPY script2.py /etl/fe.py
COPY script2.py /etl/push.py



