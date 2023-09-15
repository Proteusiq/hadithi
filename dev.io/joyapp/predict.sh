#!/bin/bash

# Prediction
# Replace this with your new FastAPI endpoint URL
API_URL="http://localhost:8000/predict"

# Loop through each record in the JSON file
cat data/validation.json | jq -c '.[]' | while read record; do

  # Extract the original species
  original_species=$(echo $record | jq -r '.species')

  # Format the payload excluding the 'species' attribute
  payload=$(echo $record | jq '{ island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex }')

  # Send the payload using curl and capture the output
  response=$(curl -s -X POST "$API_URL" -H "Content-Type: application/json" -d "$payload")

  # Extract the species from the response
  returned_species=$(echo $response | jq -r '.species')

  # Compare the original species with the returned species
  if [ "$original_species" == "$returned_species" ]; then
    echo "Correct prediction for $original_species"
  else
    echo "Incorrect prediction. Original: $original_species, Returned: $returned_species"
  fi
  
done
