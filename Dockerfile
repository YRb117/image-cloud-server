FROM python:3.8-slim-buster

# Allow statements and log messages to immediately appear in the  logs
ENV PYTHONUNBUFFERED True

RUN pip install --upgrade pip

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install  dependencies.
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py","makemigration"]
CMD ["python", "manage.py","migrate"]

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
