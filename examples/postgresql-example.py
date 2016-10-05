from challongeranking import challongeranking
import psycopg2


# Example using PostgreSQL.
# You will need to create the database (named "noobcups" in this example)
# before running this.


def main():
    # Gather a ranking from a series of tournaments named 'dnfnoobcup'.
    # The naming convention is with an increasing counter, EXCEPT for the
    # first tournament in the series, which DOES NOT have a number.
    cups = ['dnfnoobcup']
    cups += ['dnfnoobcup' + str(i) for i in range(2, 11)]
    cups += ['duelnoobcup11', 'duelnoobcup12', 'duelnoobcup13']
    # Replace you challonge API credentials
    challongeranking.setCredentials('your_challonge_username',
                                    'your_challonge_apikey')

    # Connect to the postgresql that has been previously created with
    # createdb.
    db = psycopg2.connect(database="noobcups")

    # see if the tables exists already (just check for presence of
    # table 'tournaments')
    # If not, then create them.
    cur = db.cursor()
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE "
                "table_name='tournaments')")

    if cur.fetchone()[0] is False:
        challongeranking.createDatabase(db)

    for cup in cups:
        print("Processing " + cup)
        challongeranking.processTournament(cup, db)

    db.close()

if __name__ == '__main__':
    main()
