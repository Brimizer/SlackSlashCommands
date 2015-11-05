# Slack Slash Command Server

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

A Python app, configured to respond to a variety of cool /commands in Slack

## Supported Commands
More to come soon!

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:brimizer/SlackSlashCommands.git
$ cd SlackSlashCommands
$ pip install -r requirements.txt
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku open
```

## Documentation

More to come
