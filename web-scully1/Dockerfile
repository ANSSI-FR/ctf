FROM python:2.7-alpine
RUN apk update && apk add python py-pip 
RUN adduser -D ctf

WORKDIR /app

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app /app
RUN chmod +x /app/docker-entrypoint.sh
RUN chown -R ctf:ctf /app

USER ctf
EXPOSE 8000
ENTRYPOINT ["/app/docker-entrypoint.sh"]
