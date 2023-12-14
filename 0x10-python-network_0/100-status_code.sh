#!/bin/bash
# Script to send a url request and display the status code
curl -o /dev/null -s -w "%{http_code}\n"  "$1"
