#!/bin/bash

curl "http://localhost:8000/counselors/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
