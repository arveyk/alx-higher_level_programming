#!/bin/bash
# Script to send a url request and display the status code
curl -s -i "$1" | grep HTTP | cut -c 10-12  
