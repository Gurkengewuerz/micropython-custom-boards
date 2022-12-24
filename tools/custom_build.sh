#!/bin/bash

if which nproc > /dev/null; then
    MAKEOPTS="-j$(nproc)"
else
    MAKEOPTS="-j$(sysctl -n hw.ncpu)"
fi

function ci_build_esp32 {
    source esp-idf/export.sh
    make ${MAKEOPTS} -C mpy-cross
    make ${MAKEOPTS} -C ports/esp32 submodules

    # scan original repository for boards
    for f in ../builds/ports/esp32/boards/*; do
        name=$(basename $f)

        make ${MAKEOPTS} -C ports/esp32 BOARD=$name
    done
}
