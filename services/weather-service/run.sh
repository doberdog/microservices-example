#!/usr/bin/env bash
pip install -e .
pip install -r local_packages.txt --extra-index-url http://layers:8081/ --trusted-host layers

python -u ./weather-service/weather-service.py
