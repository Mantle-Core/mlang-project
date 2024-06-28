#!/bin/bash

# List of subdirectories
SUBDIRS=(
    "mlang/lib/tokenize"
    "mlang/lib"
    #"mlang" This is a special makefile
)

# Base content for the subdirectory Makefile
BASE_MAKEFILE_CONTENT="
# Compiler
CC = clang++

# Compiler flags
CFLAGS = -std=c++20 -Wall -Wextra
CFLAGS_DEBUG = \$(CFLAGS) -g

OBJ_DIR = obj
OBJ_DEBUG_DIR = \$(OBJ_DIR)/debug
OBJ_RELEASE_DIR = \$(OBJ_DIR)/release

SRCS = # Add source files here

OBJ_SRCS_RELEASE = \$(addprefix \$(OBJ_RELEASE_DIR)/,\$(SRCS:.cpp=.o))
OBJ_SRCS_DEBUG = \$(addprefix \$(OBJ_DEBUG_DIR)/,\$(SRCS:.cpp=.o))

# Create object directories if they don't exist before any target
.PHONY: all
all: \$(OBJ_RELEASE_DIR) \$(OBJ_DEBUG_DIR)

\$(OBJ_RELEASE_DIR):
\tmkdir -p \$(OBJ_RELEASE_DIR)

\$(OBJ_DEBUG_DIR):
\tmkdir -p \$(OBJ_DEBUG_DIR)

# Release build
release: \$(OBJ_RELEASE_DIR) \$(OBJ_SRCS_RELEASE)
\t\$(MAKE) \$(OBJ_SRCS_RELEASE)

\$(OBJ_RELEASE_DIR)/%.o: %.cpp | \$(OBJ_RELEASE_DIR)
\t\$(CC) \$(CFLAGS) -c \$< -o \$@

# Debug build
debug: \$(OBJ_DEBUG_DIR) \$(OBJ_SRCS_DEBUG)
\t\$(MAKE) \$(OBJ_SRCS_DEBUG)

\$(OBJ_DEBUG_DIR)/%.o: %.cpp | \$(OBJ_DEBUG_DIR)
\t\$(CC) \$(CFLAGS_DEBUG) -c \$< -o \$@

# Clean up generated files
clean:
\trm -rf \$(OBJ_DIR)

.PHONY: release debug clean
"

# Function to create or update Makefile in subdirectory
setup_makefile() {
    local dir=$1
    local file="$dir/Makefile"

    # Create the base Makefile if it doesn't exist
    if [ ! -f "$file" ]; then
        echo -e "$BASE_MAKEFILE_CONTENT" > "$file"
        echo "Created base Makefile in $dir"
    fi
}

# Function to remove Makefile in subdirectory
clean_makefile() {
    local dir=$1
    local file="$dir/Makefile"

    # Remove the Makefile if it exists
    if [ -f "$file" ]; then
        rm -f "$file"
        echo "Removed Makefile in $dir"
    fi
}

# Main script execution
case "$1" in
    setup)
        for dir in "${SUBDIRS[@]}"; do
            mkdir -p "$dir" # Ensure the subdirectory exists
            setup_makefile "$dir"
        done
        ;;
    clean)
        for dir in "${SUBDIRS[@]}"; do
            clean_makefile "$dir"
        done
        ;;
    *)
        echo "Usage: $0 {setup|clean}"
        exit 1
        ;;
esac
