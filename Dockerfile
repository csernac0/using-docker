FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
CMD ["test.py"]
ENTRYPOINT ["python3"]