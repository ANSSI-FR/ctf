FROM alpine
#RUN apk update && apk add s6-networking python3
RUN apk update
RUN apk add socat python3

RUN adduser ctf -D
COPY petitpoucet.py puzzles.txt flag.py /app/
WORKDIR /app/

EXPOSE 2000
USER ctf
CMD socat TCP-LISTEN:2000,reuseaddr,fork EXEC:"python3 petitpoucet.py 2>log.txt"
