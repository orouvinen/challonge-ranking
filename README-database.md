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

| Column | Description |
| ------ |:-----------:|
| id | Challonge id for tournament |
| name | Name of tournament as string |
| winner | foreign key (players.id) |

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
| id     | match unique id | Composite key (match_id & tournament_id) |
| tournament_id | foreign key (tournaments.id) |
| date | match date | Date of match update (time of score report?) |
| player1_id | foreign key (players.id) |
| player2_id | foreign key (players.id) |
| winner_id  | Winner of the match, foreign key (players.id) |
| player1_elo | Player 1 Elo rating before the match was played |
| player2_elo | Player 2 Elo rating before the match was played |
| player1_elo_change | Match Elo change for player 1 |
| player2_elo_change | Match Elo change for player 2 |
