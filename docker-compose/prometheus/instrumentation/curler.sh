#!/bin/bash
while :
do
	curl http://localhost:5000
	sleep $((RANDOM % 300 ))

done