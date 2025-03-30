#!/bin/bash

# Set pip config file to use local configuration
export PIP_CONFIG_FILE=".pip/pip.conf"

# Install dependencies
pip install -r requirements.txt 