FROM python:3.11.2-bullseye

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN python manage.py collectstatic

ENTRYPOINT ["./run.sh"]