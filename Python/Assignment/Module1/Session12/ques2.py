def  format_follower_count(followers):
    if followers < 1000000 and followers >= 1000:
        followers = followers / 1000
        k = str(followers) + "K"
        return k

    elif followers > 1000000:
        followers = followers / 1000000
        m = str(followers) + "M"
        return m
    else:
        return followers
    
followers = int(input("Enter your followers: "))
format_follower_count(followers)
print(format_follower_count(followers))
