FROM python:3.10
WORKDIR /app

RUN pip install flask
COPY app.py /app/

EXPOSE 80

CMD [ "python", "app.py" ]