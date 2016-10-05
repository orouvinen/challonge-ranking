# import random
from challongeranking import challongeranking
import sqlite3
import os.path


def main():
    dbName = 'db_noobcups'

    # Gather a ranking from a series of tournaments named 'dnfnoobcup'.
    # The naming convention is with an increasing counter, EXCEPT for the
    # first tournament in the series, which DOES NOT have a number.
    cups = ['dnfnoobcup']
    cups += ['dnfnoobcup' + str(i) for i in range(2, 11)]
    cups += ['duelnoobcup11', 'duelnoobcup12', 'duelnoobcup13']

    # Replace you challonge API credentials
    challongeranking.setCredentials('your_challonge_username',
                                    'your_challonge_apikey')
    freshDb = False
    if not os.path.exists(dbName):
        freshDb = True

    db = sqlite3.connect(dbName)

    if freshDb is True:
        challongeranking.createDatabase(db)

    for cup in cups:
        print("Processing " + cup)
        challongeranking.processTournament(cup, db)

    db.close()

if __name__ == '__main__':
    main()
