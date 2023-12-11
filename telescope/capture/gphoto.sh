#!/bin/bash

set -exo pipefail

lib=1 # libphoto2
bin=1 # gphoto2

# note: these apply to each of lib and bin (whichever are enabled above)
download=1
configure=1
make=1
install=1
initial_directory=$PWD

trap 'cd "$initial_directory"' SIGINT

apt update
apt install -y curl build-essential libtool pkg-config
if [ "$lib" -eq 1 ]; then
    if [ "$download" -eq 1 ]; then
        curl -OL https://github.com/gphoto/libgphoto2/releases/download/v2.5.31/libgphoto2-2.5.31.tar.gz
        tar -xzf libgphoto2-2.5.31.tar.gz 
    fi
    cd libgphoto2-2.5.31/
    [ "$configure" -eq 1 ] && ./configure --prefix=/usr/local --with-camlibs=ptp2
    [ "$make" -eq 1 ] && make -j$(nproc)
    [ "$install" -eq 1 ] && make install -j$(nproc)
    ls -al /usr/local/lib/libgphoto2
    ldconfig
fi

cd $initial_directory

if [ "$bin" -eq 1 ]; then
    if [ "$download" -eq 1 ]; then
    curl -OL https://github.com/gphoto/gphoto2/releases/download/v2.5.28/gphoto2-2.5.28.tar.gz
    tar -xzf gphoto2-2.5.28.tar.gz 
    fi
    cd gphoto2-2.5.28/
    apt install -y libpopt-dev libexif-dev
    [ "$configure" -eq 1 ] && ./configure --prefix=/usr/local
    [ "$make" -eq 1 ] && make -j$(nproc)
    [ "$install" -eq 1 ] && make install -j$(nproc)
    gphoto2 -v
fi

cd $initial_directory
