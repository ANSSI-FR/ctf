FROM alpine

RUN apk update && apk add s6-networking python
RUN adduser ctf -D
COPY chall.py flag.py /app/
WORKDIR /app/

EXPOSE 3000
USER ctf
CMD s6-tcpserver 0.0.0.0 3000 python chall.py
