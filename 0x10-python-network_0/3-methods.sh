#!/bin/bash
# display all HTTP methods the server can accept using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
