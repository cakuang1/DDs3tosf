FROM python:3.9



COPY requirements.txt /
RUN pip install -r /requirements.txt


COPY utils /utils
COPY setup.py /
COPY cleaning.py /etl/cleaning.py
COPY fe.py /etl/fe.py
COPY push.py /etl/push.py



