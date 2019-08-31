# Cykel

Basic backend for a mobility sharing service. Used on [CCCamp2019](https://events.ccc.de/camp/2019/wiki/Main_Page).

## Prerequisites

* Python (≥3.7)
* A database that supports GIS extensions, for example PostGIS or SpatiaLite

Create a file `.env` in the `cykel` subdirectory, with the following contents:

```
# insert your own random string here
SECRET_KEY=f2bf0a4e621a16d9eb8253aa7a540f75ed8787b5
# set to 1 to enable DEBUG output, or 0 to disable
DEBUG=1
# configure your database in a format supported by https://github.com/jacobian/dj-database-url
DATABASE_URL=spatialite:///cykel.sqlite
# it is recommended to use a DNS alias for localhost, instead of "localhost", for CORS reasons
ALLOWED_HOSTS=lvh.me,localhost
# set the full URL to the frontend
UI_SITE_URL=http://lvh.me:1234/
# CORS origins to whitelist, i.e. the frontend URL (with scheme, without path)
CORS_ORIGIN_WHITELIST=http://lvh.me:1234
```

Install the required packages using `pip install -r requirements.txt`. It is recommended to use a virtualenv with your choice of tool, e.g. `pipenv`, in which case you can run `pipenv install` (and `pipenv shell` or prefix `pipenv run` to run commands).

Then run `manage.py migrate` to create the database tables.

### Database configuration for PostgreSQL/PostGIS

You need to enable the following extensions in the cykel database after installing PostGIS:

```
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
```

The DB migration will fail otherwise.

## Running the local server

Run `manage.py runserver`.

### Configuring authentication

For the administration interface you can run `manage.py createsuperuser` to create an user with administrative rights and access the interface at `http://localhost:8080/admin`.

Then, visit `/admin/` and edit the URL of the first Website (`/admin/sites/site/1/change/`).

### Configuring OAuth

Visit `/admin/socialaccount/socialapp/add/` (Add Social Application).

For example, for GitHub select "Provider: GitHub", "Name: github", the Client-Id and Secret are shown in the OAuth application creation process at GitHub.

When you create an OAuth2-Application at a provider, you need to enter a callback URL. This URL is in the format `https://<host>/auth/<name>/login/callback/`.

## Update bike location

For updating the current bike location we provide the `/api/bike/updatelocation` endpoint.

One project which can use this together with TheThingsNetwork is the [`cykel-ttn`](https://github.com/stadtulm/cykel-ttn) adapter. Read the readme in the repository on how to use it - for authentication you need to add a new api key at `/admin/rest_framework_api_key/apikey/`.

