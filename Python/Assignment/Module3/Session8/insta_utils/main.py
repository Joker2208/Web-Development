import likes, comments

current = int(input("Enter your current likes:"))
increment = int(input("Enter extra likes:"))

comment = input("Enter your comments:")
new_comments = input("Enter new comments:")

total_likes = likes.like_count(current,increment)
total_com = comments.comment_count(comment,new_comments)

