def display_friend( users):
    for username, followers in users.items():
        followers= followers / 1000
        k = str(followers) + "K"
        print(username,":",k,"followers")

friends = {
    "Dipesh" : 100000,
    "Rutu"  : 1909090909090
}

display_friend(friends)
