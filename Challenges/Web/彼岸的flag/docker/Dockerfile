FROM python:latest

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/templates/
COPY htmlhead /app/templates/
COPY htmltail /app/templates/
COPY gen.py /app/templates/
COPY app.py /app/

RUN chmod +w /app/templates/gen.py

RUN pip install flask

EXPOSE 80
CMD [ "python", "app.py" ]