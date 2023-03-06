FROM python:3.11.2-bullseye

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./

ENTRYPOINT ["./run.sh"]