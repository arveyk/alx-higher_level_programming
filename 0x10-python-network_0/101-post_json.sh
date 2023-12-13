#!/bin/bash
# Script to post JSON request
curl -s  "$1" -d cat "$2" 
