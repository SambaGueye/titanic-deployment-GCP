FROM python:3

# pip install 
WORKDIR /code
COPY main.py /code/
# COPY requirements.txt

RUN pip install --upgrade google-cloud-bigquery
# RUN pip install -r requirements.txt

CMD ["python", "main.py"]