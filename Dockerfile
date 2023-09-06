FROM python:3-alpine3.15
LABEL authors="siddhant vijay singh"

RUN pip install Flask==2.2.3 Cython==0.29.35

WORKDIR /app
COPY . .
EXPOSE 5000

CMD python ./run.py