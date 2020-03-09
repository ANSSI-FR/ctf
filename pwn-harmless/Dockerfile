FROM debian:stable-slim AS builder
RUN apt-get update && apt-get install -y gcc-arm-linux-gnueabi make
WORKDIR /build/
COPY harmless.c Makefile ./
RUN make

FROM debian:stable-slim
RUN apt update \
    && apt install -y socat libc6-armel-cross libpixman-1-dev libfdt-dev wget patch \
    && apt install -y build-essential zlib1g-dev pkg-config libglib2.0-dev binutils-dev libboost-all-dev autoconf libtool libssl-dev libpixman-1-dev libpython-dev python-pip python-capstone virtualenv

## Compile patched QEMU with ASLR support
RUN wget https://github.com/qemu/qemu/archive/v2.7.0.tar.gz \
    && tar xzf v2.7.0.tar.gz \
    && mv qemu-2.7.0 qemu-2.7.0.orig
COPY qemu-2.7.0-aslr_heap_pie_nx_wxorx_mmap.patch .
RUN patch -s -p0 < qemu-2.7.0-aslr_heap_pie_nx_wxorx_mmap.patch
RUN mv qemu-2.7.0.orig qemu-2.7.0 \
    && cd qemu-2.7.0 \
    && ./configure --target-list="arm-linux-user" \
    && make all
RUN cd /qemu-2.7.0 && make install
RUN rm -rf qemu-2.7.0/ qemu-2.7.0-aslr_heap_pie_nx_wxorx_mmap.patch v2.7.0.tar.gz
##
RUN useradd ctf
WORKDIR /app/
COPY --from=builder /build/harmless ./
COPY flag run.sh ./
EXPOSE 4001
USER ctf
CMD socat tcp-listen:4001,reuseaddr,fork exec:./run.sh
