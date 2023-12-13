#!/bin/bash
# Script to post JSON request
file="cat $2"
curl -s  "$1" -d "file" 
