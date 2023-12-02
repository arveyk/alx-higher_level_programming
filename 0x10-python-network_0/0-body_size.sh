#!/usr/bin/env bash
# Script to request to a commandline given URL
curl -so /dev/null  $1 -w '%{size_download}'
