#!/bin/bash
# Script to post JSON request
cat "$2" | curl -s  "$1" -d 
