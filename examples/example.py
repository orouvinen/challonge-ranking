from challongeranking import challongeranking

def main():
    # Gather a ranking from a series of tournaments named 'dnfnoobcup'.
    # The naming convention is with an increasing counter, EXCEPT for the
    # first tournament in the series, which DOES NOT have a number.
    cups = ['dnfnoobcup']
    cups += ['dnfnoobcup' + str(i) for i in range(2, 11)]

    # Replace you challonge API credentials
    challongeranking.setCredentials('your_challonge_username',
                           'your_challonge_api_key')

    for cup in cups:
        challongeranking.processTournament(cup, 'dnfnoobcup_database')


if __name__ == '__main__':
    main()
