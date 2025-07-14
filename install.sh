#!/bin/bash
pkg update -y && pkg upgrade -y
pkg install -y python git
pip install --upgrade pip
pip install -r requirements.txt
python royalharvester.py
