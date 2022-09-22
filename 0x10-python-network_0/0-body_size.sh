#!/bin/bash
#!/usr/bin/python3
# This script sends a request to that URL, and displays the size of the body of the response
curl -s "$1" -w '%{size_request}'
