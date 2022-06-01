FROM python:3.9

WORKDIR /Biometry_with_PyTorch

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP add.py

COPY . .

EXPOSE 5000 
