#!/bin/bash
# Script to send a url request and display the status code
culr "$1" | grep '^HTTP' | cut -f 2
