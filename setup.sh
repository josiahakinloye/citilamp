#!/usr/bin/sh
sudo apt install git
git clone git@github.com:Ilozuluchris/apixu-python.git
python apixu-python/setup.py install
pip install -r requirements.txt
