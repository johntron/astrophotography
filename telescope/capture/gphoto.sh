apt update
apt upgrade -y
apt install -y curl
curl -OL https://github.com/gphoto/libgphoto2/releases/download/v2.5.31/libgphoto2-2.5.31.tar.gz
tar -xzf libgphoto2-2.5.31.tar.gz 
cd libgphoto2-2.5.31/
apt install -y libtool
./configure --prefix=/usr/local --with-camlibs=ptp2
make
make install
ls -al /usr/local/lib/libgphoto2
curl -OL https://github.com/gphoto/gphoto2/releases/download/v2.5.28/gphoto2-2.5.28.tar.gz
tar -xzf gphoto2-2.5.28.tar.gz 
cd gphoto2-2.5.28/
apt install -y libpopt-devel libexif-dev
./configure --prefix=/usr/local
make
make install
ldconfig
gphoto2 -v
