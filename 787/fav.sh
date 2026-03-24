#!/bin/sh
URL="https://habr.com"
FAVICON="$URL/favicon.ico"
NAME=$(echo "$URL" | awk -F'[/.]' '{print $3}')
mkdir -p favicons
cd favicons
curl -o "$NAME" "$FAVICON"

