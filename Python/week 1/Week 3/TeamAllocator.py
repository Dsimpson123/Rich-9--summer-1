#This program will allocate teams randomly from a list 



import random

players =["Darren", "Devon", "Walter",
           "Ollie", "Xavier", "Carl",
           "EJ", "Nahum", "Joaquin",
           "Marshawn", "Ja'Den", "Isiah",
           "Nishad", "Kauri", "Semaj",
           "Joseph", "Taquari", "Jarmauri",
           "Tay", "Braylen", "Avery",
           "Kenyon" "kriss", "Kamari"]

def PickTeams(players):
    random.shuffle(players)
    team1 = players[:len(players) //2]
    teamCaptain1 = team1[random.randrange(0, 12)]

    print("Team 1:")
    print("Team 1 Captain: "+ teamCaptain1)
    for player in team1:
        print(player)

    team2= players[len(players) //2:]
    teamCaptain2 = team2[ random.randrange(0,12)]

    print("Team 2:")
    print("Team 2 Captain: "+ teamCaptain2)
    for player in team2:
        print(player)

PickTeams(players)


    