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

The columns of each table should be pretty self-explanatory, but here's quick run-down of the tables.


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

#### Table TOURNAMENTS
Contains record of all the tournaments that have been processed so far.

| Column | 
| ------ |
| id |

#### Table PARTICIPATIONS
Keeps track of player participation in tournaments. Each row tells a
player_id who participated in a tournament with tournament_id.
I.e. for all tournaments, contains a player_id of each player who took part in
the tournament.

| Column | Description |
| ------ |:-----------:|
| player_id | foreign key (players.id) |
| tournament_id | foreign key (tournaments.id) |

#### Table MATCHES
Match and Elo history for players.

| Column | Description | Notes |
| ------ |:-----------:| ----- |
| id     | match unique id | Formed by prefixing tournament ID with match ID |
| tournament_id | foreign key (tournaments.id) |
| player1_id | foreign key (players.id) |
| player2_id | foreign key (players.id) |
| winner_id  | Winner of the match, foreign key (players.id) |
| player1_elo | Player 1 Elo rating before the match was played |
| player2_elo | Player 2 Elo rating before the match was played |
| player1_elo_change | Match Elo change for player 1 |
| player2_elo_change | Match Elo change for player 2 |
