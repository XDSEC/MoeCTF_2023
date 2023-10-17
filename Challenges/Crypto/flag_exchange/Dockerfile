FROM python:3.11-alpine
COPY chall /chall
WORKDIR /chall
RUN ["pip", "install", "pycryptodome"]
CMD ["python","main.py"]
EXPOSE 9999