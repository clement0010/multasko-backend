FROM python:3.8.3

RUN mkdir /flask-backend

WORKDIR /flask-backend

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python main.py