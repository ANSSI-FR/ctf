FROM alpine

RUN apk update && apk add s6-networking python3
RUN adduser ctf -D
COPY chall.py flag.py /app/
WORKDIR /app/

EXPOSE 2000
USER ctf
CMD s6-tcpserver 0.0.0.0 2000 python3 chall.py
