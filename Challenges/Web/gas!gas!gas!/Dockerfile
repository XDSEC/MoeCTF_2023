FROM python:3.10
WORKDIR /app

RUN pip install flask

RUN mkdir /app/templates
COPY templates /app/templates
COPY app.py /app/


EXPOSE 80

CMD [ "python", "app.py" ]