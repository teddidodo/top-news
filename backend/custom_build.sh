#!/bin/bash

# Install pygooglenews
pip install pygooglenews --no-deps

# Install other requirements from requirements.txt
pip install -r requirements.txt

# Build or deploy your application (if needed)
# Example: python build.py
python -m uvicorn main:app
# chmod +x custom-build.sh