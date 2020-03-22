#!/bin/sh
# Usage: ./read-pastey paste-id

# username and password for Pastey
USERNAME="user"
PASSWORD="pass"

# URL Pastey is being hosted at
PASTEY_URL="http://localhost:5000/"


AUTH_HEADER=$(echo -n "$USERNAME:$PASSWORD" | base64)

curl -H "Authorization: Basic $AUTH_HEADER" "$PASTEY_URL$1"

# add newlien
echo ''
