FROM debian:stable-slim
RUN apt update
RUN apt install -y python3-dev python3-pip
WORKDIR /app
COPY content.json flag.txt jajaja.py requirements.txt ./
COPY static /app/static
COPY templates /app/templates
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

RUN useradd ctf
USER ctf
EXPOSE 5000
CMD python3 jajaja.py
