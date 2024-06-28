#!/bin/bash

# GitHub repository information
repo_owner="llvm"
repo_name="llvm-project"
api_url="https://api.github.com/repos/${repo_owner}/${repo_name}/releases/latest"

# Function to log messages
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') $1"
}

# Fetch latest release tag
log "Fetching latest release tag from $api_url..."
latest_tag=$(curl -sSL "$api_url" | grep -o '"tag_name": "[^"]*' | sed 's/"tag_name": "//')

if [ -z "$latest_tag" ]; then
    log "Failed to fetch latest release tag. Exiting."
    exit 1
fi

log "Latest release tag: $latest_tag"

# Construct download URL
llvm_url="https://github.com/${repo_owner}/${repo_name}/releases/download/${latest_tag}/llvm-${latest_tag/llvmorg-/}.src.tar.xz"

log "Constructed LLVM download URL: $llvm_url"

# Download LLVM archive
llvm_archive=$(basename "$llvm_url")
log "Downloading LLVM archive from $llvm_url to $llvm_archive..."
curl -sSL -o "$llvm_archive" "$llvm_url"

if [ $? -ne 0 ]; then
    log "Failed to download LLVM archive. Exiting."
    exit 1
fi

log "LLVM archive downloaded successfully."

# Extract LLVM archive
log "Extracting LLVM archive..."
tar -xJf "$llvm_archive"

if [ $? -ne 0 ]; then
    log "Failed to extract LLVM archive. Exiting."
    exit 1
fi

log "LLVM archive extracted successfully."

# Extracted folder name
llvm_folder=$(tar -tJf "$llvm_archive" | head -n 1 | cut -f 1 -d '/')

# Rename extracted folder to 'llvm'
mv "$llvm_folder" llvm

# Clean up downloaded archive
rm "$llvm_archive"

log "Setup completed successfully. LLVM is ready for use."
