FROM python:latest

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/templates/
COPY index.html /app/templates
COPY htmlhead /app/
COPY htmltail /app/
COPY gen.py /app/
COPY app.py /app/

RUN chmod +w /app/gen.py

RUN pip install flask

EXPOSE 80
CMD [ "python", "app.py" ]