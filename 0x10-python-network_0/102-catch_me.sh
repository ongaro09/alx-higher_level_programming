#!/bin/bash
# Script to send a request to 0.0.0.0:5000/catch_me that results in a "You got me!" response.

curl -sX PUT 0.0.0.0:5000/catch_me -H "Origin: School" -d "user_id=98" -L
