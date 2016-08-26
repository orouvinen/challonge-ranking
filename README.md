# challongeranking

challongeranking is a Python-module for ranking players in tournaments hosted in [Challonge](https://www.challonge.com). The rating algorithm is a basic Elo rating with a constant K value of 32.

Players are identified by an email hash provided by the Challonge API. This means that in order for a match to be
ranked, **both players must have been registered to the processed tournament(s) with their Challonge-accounts**.

## Installing
```
pip install iso8601
pip install -e git+http://github.com/russ-/pychallonge#egg=pychallonge
pip install challongeranking
```

## Usage
To import, use `from challongeranking import challongeranking`.
Please see the examples directory for example code.

## Using the stored data
challongeranking stores ratings in a **sqlite3 database**.
Please see [README-database](README-database.md) for details.
