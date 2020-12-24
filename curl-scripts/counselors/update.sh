#!/bin/bash

curl "http://localhost:8000/counselors/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "counselor": {
      "name": "'"${NAME}"'",
      "location": "'"${COLOR}"'",
      "ripe": "'"${RIPE}"'"
    }
  }'

echo
