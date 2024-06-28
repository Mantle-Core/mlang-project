#!/bin/bash

# Path to Python script for generating xmacro header
GENERATE_XMACRO_HEADER_PY="scripts/GenerateXMacroHeader.py"
GENERATE_TOKENTYPE_HEADER_PY="scripts/GenerateTokenTypeHeader.py"

# xmacro header file
XMACRO_HEADER="TokenType.def"
ENUM_HEADER="TokenType.h"

# Generate xmacro header and enum header
generate_headers() {
    generate_xmacro_header
    generate_enum_header
}

# Generate xmacro header
generate_xmacro_header() {
    if [ -f "$GENERATE_XMACRO_HEADER_PY" ]; then
        python "$GENERATE_XMACRO_HEADER_PY" > "$XMACRO_HEADER"
        echo "Generated $XMACRO_HEADER"
    else
        echo "Error: $GENERATE_XMACRO_HEADER_PY not found!"
        exit 1
    fi
}

# Generate enum header
generate_enum_header() {
    if [ -f "$GENERATE_TOKENTYPE_HEADER_PY" ]; then
        python "$GENERATE_TOKENTYPE_HEADER_PY" > "$ENUM_HEADER"
        echo "Generated $ENUM_HEADER"
    else
        echo "Error: $GENERATE_TOKENTYPE_HEADER_PY not found!"
        exit 1
    fi
}

# Clean up generated files
clean() {
    rm -f "$XMACRO_HEADER" "$ENUM_HEADER"
    echo "Cleaned up generated files"
}

# Main script execution
case "$1" in
    all)
        generate_headers
        ;;
    clean)
        clean
        ;;
    *)
        echo "Usage: $0 {all|clean}"
        exit 1
        ;;
esac
