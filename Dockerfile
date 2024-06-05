# python base image
FROM python:3.11.0

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

#COPY requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# run db migrations
RUN python manage.py migrate

# collect statics
RUN pyhton manage.py collectstatic --noinput

# expose the django port 8000
EXPOSE 8000

# start the server
CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
