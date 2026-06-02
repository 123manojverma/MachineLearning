FROM python:3.14.5
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask","run"]
