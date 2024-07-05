#!/bin/bash
# GET request to the URL using curl, and display the body of the response
curl -s -X GET "$1" -H "X-School-User-Id: 98"
