FROM debian:stable-slim AS builder
RUN apt-get update && apt-get install -y gcc-aarch64-linux-gnu make
WORKDIR /build/
COPY aarchibald.c Makefile ./
RUN make

FROM debian:stable-slim
RUN apt-get update && apt-get install -y socat qemu-user libc6-arm64-cross
RUN useradd ctf
WORKDIR /app/
COPY --from=builder /build/aarchibald ./
COPY flag run.sh ./
EXPOSE 4000
USER ctf
CMD socat tcp-listen:4000,reuseaddr,fork exec:./run.sh
