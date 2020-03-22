#!/bin/sh
# Usage: ./write-pastey filename

# username and password for Pastey
USERNAME="user"
PASSWORD="pass"

# URL Pastey is being hosted at
PASTEY_URL="http://localhost:5000/"


AUTH_HEADER=$(echo -n "$USERNAME:$PASSWORD" | base64)

# POST chosen file to the server
curl -X POST -H "Authorization: Basic $AUTH_HEADER" --data-binary @$1 "$PASTEY_URL$1"


