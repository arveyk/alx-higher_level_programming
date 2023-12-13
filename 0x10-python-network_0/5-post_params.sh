#!/bin/bash
# Script to send post request
curl -s -d "email:test@gmail.com&subject:I will always be here for PLD" "$1"
