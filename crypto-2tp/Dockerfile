FROM alpine

RUN apk update && apk add s6-networking py3-cryptography
RUN adduser ctf -D
COPY 2tp.py flag key /app/
WORKDIR /app/

EXPOSE 2000
USER ctf
CMD s6-tcpserver 0.0.0.0 2000 python3 2tp.py
