# users-api


## Setup (relevant for developers)
### Create virtualenv
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Install dependencies
```bash
(.venv) $ pip install -r requirements.txt
```


## Run
```bash
docker build -t users-api .
docker run -d -p 80:80 users-api
```