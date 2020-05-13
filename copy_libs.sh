#!/bin/bash
# -- ----------------------------------------------------------------------- --
# -- copy_libs.sh - copy libraries into the c0rv1 package
# -- ----------------------------------------------------------------------- --
LIBS_DIR="./libs"
PACKAGE_DIR="./c0rv1"

echo "Copying libraries"

# -- Encryption chip
echo " - Crypto (ATECx08A)"
cp -r "${LIBS_DIR}/ucryptoauthlib/cryptoauthlib" "${PACKAGE_DIR}/cryptoauthlib"

# -- Accelero
echo " - Accelerometer (LIS2DH12)"
cp -r "${LIBS_DIR}/micropython-lis2hh12/lis2hh12.py" "${PACKAGE_DIR}/lis2hh12.py"