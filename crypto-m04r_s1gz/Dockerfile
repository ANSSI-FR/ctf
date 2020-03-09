FROM alpine

RUN apk update && apk add socat py3-crypto
RUN adduser ctf -D
COPY * /app/
WORKDIR /app/

EXPOSE 2000
USER ctf
CMD socat tcp-listen:2000,reuseaddr,fork exec:"python3 m04r_s1gz.py"
