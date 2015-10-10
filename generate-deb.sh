#! /bin/bash

BUILD_DIR=build/

rm -Rf $BUILD_DIR 

mkdir -p $BUILD_DIR $BUILD_DIR/usr/bin $BUILD_DIR/usr/lib/python3/dist-packages

cp backup.py $BUILD_DIR/usr/bin
cp -R backend/ fs/ $BUILD_DIR/usr/lib/python3/dist-packages
cp -R DEBIAN/ $BUILD_DIR/
cp LICENSE $BUILD_DIR/DEBIAN/copyright

dpkg-deb --build $BUILD_DIR allis-backup.deb
