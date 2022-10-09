#!/bin/bash


set -euo pipefail

FULL_CSV=verra.csv

PARAMS='{"program":"VCS","protocolCategories":["14"],"countries":["KE"],"issuanceStartInclusive":"2022-04-01","issuanceTypeCodes":["ISSUE"]}'

fetch_data() {
  curl 'https://registry.verra.org/uiapi/asset/asset/search?$skip=0&count=true&$format=csv' \
    -X POST \
    -H 'Content-Type: application/json' \
    --compressed \
    --data-raw '{"program":"VCS","issuanceTypeCodes":["ISSUE"]}'
}

fetch_data > ${FULL_CSV}