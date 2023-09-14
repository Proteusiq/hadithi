#!/bin/bash

# chmod +x learn.sh

# Replace this with your FastAPI endpoint URL
API_URL="http://localhost:8000/learn"

# Loop through each record in the JSON file
cat data/penguins.json | jq -c '.[]' | while read record; do

  # Extract attributes and species from the record and format the payload
  payload=$(echo $record | jq '{ attributes: { island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex }, species }')

  # Send the payload using curl
  curl -X POST "$API_URL" -H "Content-Type: application/json" -d "$payload"
  
done
