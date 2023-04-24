FROM python:3.9.11-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
COPY database.py database.py
COPY app.py app.py
COPY static statc
COPY templates templates
RUN pip3 install -r requirements.txt


CMD ["python3", "database.py"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
