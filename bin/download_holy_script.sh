#!/bin/bash
# Usage: ./download.sh <URL> <output_file>
URL=$1
OUTPUT=$2

curl -sS "$URL" > "$OUTPUT" || { echo "Download failed"; exit 1; }