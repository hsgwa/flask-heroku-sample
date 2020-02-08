Joy-Tan Resevation Manage Application
====================

A reservation management application which uses google spread sheet as data base.

## Development Setup

### Google Spread sheet setup

* Create Google Cloud Platform Project

* Setup Service Account and download certificate.json

* Enable Google Sheets API

* Create Spread sheet


### Local environment setup
* `heroku create`

* `pipenv install`

* `pipenv shell`



## Setup environment variables

* Create environment variables to .env

```
$ cat .env
TYPE="service_account"
PROJECT_ID="****"
PRIVATE_KEY_ID="****"
PRIVATE_KEY="****"
CLIENT_EMAIL="****"
CLIENT_ID="****"
AUTH_URI="https://accounts.google.com/o/oauth2/auth"
TOKEN_URI="https://oauth2.googleapis.com/token"
AUTH_PROVIDER_X509_CERT_URL="https://www.googleapis.com/oauth2/v1/certs"
CLIENT_X509_CERT_URL="****"
RANGE="B2:C1000"
SPREADSHEET_ID="****"
```
See certificate.json, spread sheet uri and spread sheet api.

* push .env to heroku

```
heroku plugins:install heroku-config
heroku config:push
```
## Deploy

* `git push heroku master`

## Debug

* `pipenv install`

* `python app.py`