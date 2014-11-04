#!/bin/bash

ROOT_DIR="$(readlink -m $(dirname ${BASH_SOURCE[0]})/..)"
TARGET=${1-"x86"}
SDK="/opt/OpenWrt-SDK-${TARGET}"

echo "Building in ${SDK}"

echo "Cleaning"
mkdir -p ${SDK}/dl
mkdir -p ${SDK}/package
rm -r ${SDK}/package/*/

echo "Copying source"
cp -r ${ROOT_DIR}/packages/* ${SDK}/package

#echo "Downloading dependencies"
#svn export https://github.com/openwrt-es/barrier-breaker-openwrt-packages/trunk/lang/python ${SDK}/package/python


echo "Building"
cd ${SDK}
make clean
make