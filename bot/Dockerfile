# 
FROM python:3.11

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod 777 /usr/src/app/entrypoint.sh

# copy project
COPY . .
ENV PYTHONPATH /usr/src/app/src
# ENTRYPOINT ["sh", "entrypoint.sh"]
# 