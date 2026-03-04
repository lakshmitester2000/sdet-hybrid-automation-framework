#!/bin/bash

# Function to check if Selenium Hub is ready
echo "Waiting for Selenium Hub to be ready at http://selenium-hub:4444/wd/hub..."

# Loop until the Hub returns a 200 OK or we timeout
while ! curl -s http://selenium-hub:4444/wd/hub/status | grep -q '"ready": true'; do
  echo "Selenium Hub is not ready yet - sleeping..."
  sleep 2
done

echo "Selenium Hub is UP and Ready! Starting tests..."

# Execute the command passed from Docker (which is 'pytest')
exec "$@"
