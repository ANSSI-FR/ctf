FROM alpine

RUN apk update && apk add socat python py2-pip zlib-dev jpeg-dev gcc python2-dev musl-dev
RUN pip install qrcode Pillow
RUN adduser ctf -D
COPY chall.py flag.py /app/
RUN chown ctf /app
WORKDIR /app/

EXPOSE 3000
USER ctf
CMD socat TCP-LISTEN:3000,reuseaddr,fork EXEC:"python chall.py"
