FROM debian:stable-slim
RUN apt-get update && apt-get install -y build-essential socat make libc6-dev gcc-multilib

## Copy challenge files
WORKDIR /app
COPY source/script_flag.pdf ./
COPY source/Makefile ./
COPY source/alfred.c ./

## Compile the challenge
RUN make

## Run the challenge
RUN useradd ctf

EXPOSE 4000
USER ctf
CMD socat tcp-listen:4000,reuseaddr,fork exec:"./alfred",stderr
