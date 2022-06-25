FROM python:3.10
WORKDIR /app
COPY ./requirements/prod.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt
copy . .

RUN chmod +x /app/docker/prod/start.sh
CMD ["/app/docker/prod/start.sh"]
