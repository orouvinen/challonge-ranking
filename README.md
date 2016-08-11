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

As of now, the database is very simple.

The columns of each table should be pretty self-explanatory, but here's quick run-down of the tables
that are most likely to be used.

#### Table PLAYERS
| Column | Description | 
| ------ |:-----------:|
| id     | unique identifier for a player |
| nick   | player nickname |
| rating | player Elo rating |

#### Table ALIASES
The table provides mapping from player's possible aliases to the player.

| Column | Description |
| ------ |:-----------:|
| alias  | alias nick  |
| player_id | References player id in `players` who used this alias |
