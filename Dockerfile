FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
#RUN python manage.py flush --no-input
#RUN python manage.py loaddata initial_data.json
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]
