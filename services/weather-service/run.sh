#!/usr/bin/env bash
pip install -e .

pip install -r local_packages.txt --extra-index-url http://petricnet:8081/ --trusted-host petricnet
python -u ./weather-service/weather-service.py
