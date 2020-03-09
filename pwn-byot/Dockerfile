FROM debian:stretch-slim AS builder
RUN apt update && apt install -y make build-essential
WORKDIR /build/
COPY byot.c byot.h Makefile ./
RUN make all
RUN strip byot

FROM debian:stretch-slim
RUN apt update && apt install -y socat
RUN useradd ctf
WORKDIR /app/
COPY --from=builder /build/byot ./
COPY flag ./
EXPOSE 4002
USER ctf
CMD socat tcp-listen:4002,reuseaddr,fork exec:./byot
