# Ookma-Kyi

> A Python implementation of the now defunct Battlemail game

Battlemail was an email game originally written by Paul Gouge. The concept is
fairly simple: Players pick 6 attack and 6 defense moves which are sent to their
opponent. The opponent then picks 6 attack and 6 defense moves. Once submitted,
both players are then treated to a display of martial arts based on the moves
both players picked.

This project hopes to reproduce the game in Python, providing a server and MySQL
persistence. If successful, it will allow for a new Battlemail player community
to arise.

## Prerequisites

* [Python 3.7+](https://www.python.org)
* [Django 2.2+](https://www.djangoproject.com)

## Install

```sh
pip install ookma-kyi
```

## Configuration

Before running the application, you will need to configure the following
environment variables:

```sh
export OOKMA_DATABASE_HOST=localhost
export OOKMA_DATABASE_PORT=<port>
export OOKMA_DATABASE_USER=<username>
export OOKMA_DATABASE_PASS=<password>
export OOKMA_DATABASE_NAME=<databasename>
```

## Usage

start the server and access your site or localhost to access the app.


```
http://www.your-domain-here.tld
-or-
127.0.0.1
```

## License

[MIT]: https://opensource.org/licenses/MIT

`ookma-kyi` is open source software released under the [MIT license][MIT].

## Sponsored by

