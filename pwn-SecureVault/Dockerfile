FROM debian:stable-slim AS builder
RUN apt-get update && apt-get install -y gcc-arm-linux-gnueabi make
WORKDIR /build/
COPY SecureVault.s Makefile ./
RUN make

FROM debian:stable-slim
RUN apt-get update && apt-get install -y socat qemu-user libc6-armel-cross 
RUN useradd ctf
WORKDIR /app/
COPY --from=builder /build/SecureVault ./
RUN mkdir -p .mysecretdir
COPY run.sh ./
COPY flag ./.mysecretdir
EXPOSE 4000
USER ctf
CMD socat tcp-listen:4000,reuseaddr,fork exec:./run.sh
