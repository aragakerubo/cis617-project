#!/bin/bash

for profile in alice-invalid bob-invalid charlie-invalid diana-invalid; do
  echo "Simulating for $profile"
  for i in {1..15}; do
    echo "Attempt $i"
    aws sts get-caller-identity --profile $profile 2>/dev/null
    sleep 1
  done
done

