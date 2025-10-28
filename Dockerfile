FROM python:3.13

#Unbuffered output gives real-time logs in containerized 
#environments, crucial for debugging production issues.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev gcc

RUN pip install --upgrade pip && pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system 

COPY . .

EXPOSE 8000 

CMD ["gunicorn", "storefront.wsgi:application", "--bind", "0.0.0.0:8000"]