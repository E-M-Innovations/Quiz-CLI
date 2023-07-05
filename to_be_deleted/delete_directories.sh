#!/bin/bash

# Function to check if a directory contains a .toml file
directory_contains_toml() {
    for file in "$1"/*.toml; do
        [ -e "$file" ] && return 0
    done
    return 1
}

# Loop through directories and delete those without .toml files or named "docs"
for dir in */; do
    if [[ "$dir" == "docs/" ]] && ! directory_contains_toml "$dir"; then
        echo "Deleting directory: $dir"
        rm -rf "$dir"
    fi
done
