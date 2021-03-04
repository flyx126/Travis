FROM python:latest
WORKDIR /code/
COPY ./src ./src
COPY ./config ./config
COPY ./application.py .
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python",  "application.py"]