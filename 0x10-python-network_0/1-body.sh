#!/bin/bash
# Script to implement Get request
curl -sX -G $1 | grep "200"
