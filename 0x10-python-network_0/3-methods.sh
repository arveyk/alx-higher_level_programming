#!/bin/bash
# Script to display HTTP options
curl -siLX OPTIONS $1 | grep 'Allow:' | cut -b 6
