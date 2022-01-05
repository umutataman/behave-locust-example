#!/usr/bin/env bash
# Created by Umut Ataman at 05/01/2022

echo "Installing python and google-chrome-stable"
apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable python3 python3-pip allure
# Check if the virtual environment is already created.
if [[ ! -e venv ]]; then
	echo "---venv installing---" 1>&2
	export LC_ALL=C
    python3 -m pip install virtualenv
    virtualenv -p python3 venv
elif [[ ! -d venv ]]; then
    echo "---venv already exists but is not a directory---" 1>&2
else
    echo "---venv already exists---" 1>&2
fi
echo  "---Activate virtual environment---"
source "venv/bin/activate"
python3 -V
echo  "---Install requirements(dependencies) for test run---"
python3 -m pip install -U -r requirements.txt
echo  "---Run web tests ---"
python3 -m behave -D headless=true --tags=web