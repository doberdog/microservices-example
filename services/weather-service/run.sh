#!/usr/bin/env bash
pip install -e .

pip install -r local_packages.txt --extra-index-url http://pypi-server:8081/ --trusted-host pypi-server
python -u ./petrichor_weather_service/weather_service.py
