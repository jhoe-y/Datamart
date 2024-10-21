#!/bin/bash

npm install -r requirements.txt

python main.py

cd datamart

npm install

node server.js
