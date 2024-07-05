#!/bin/bash
# POST request to the passed URL using curl, and display the body of the response
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
