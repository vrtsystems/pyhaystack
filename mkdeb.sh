#!/bin/bash
# Build a Debian package of pyhaystack.
set -e

: ${MY_DIR:=$( dirname "$0" )}
: ${PYTHON:=$( which python2 )}

: ${BUILD_PY2:=True}
: ${BUILD_PY3:=True}

# Set the output directory if not already given
: ${OUT_DIR:=${MY_DIR}/out}

cd "${MY_DIR}"

# Clean up
[ ! -d deb_dist ] || rm -fr deb_dist
[ ! -d dist ] || rm -fr dist

# Build
"${PYTHON}" setup.py \
	--command-package stdeb.command sdist_dsc \
	--with-python2=${BUILD_PY2} --with-python3=${BUILD_PY3} \
	${DEBIAN_VERSION:+--debian-version=}${DEBIAN_VERSION} \
	--depends python-hszinc --depends3 python3-hszinc \
	--depends python-signalslot --depends3 python3-signalslot \
	--build-depends python-hszinc --build-depends python3-hszinc \
	--build-depends python-signalslot --build-depends python3-signalslot \
	bdist_deb

# Clean up source tree
find deb_dist -mindepth 1 -maxdepth 1 -type d | xargs rm -fr

# Move out the resultant files
[ -d ${OUT_DIR} ] || mkdir ${OUT_DIR}
mv deb_dist/* ${OUT_DIR}
