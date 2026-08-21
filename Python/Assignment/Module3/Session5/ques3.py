class InstagramPost:
    def __init__(self,caption,likes,comments):
        self.caption = caption
        self.likes = likes 
        self.comments = comments

    def add_comment(self,comment_text):
        self.comments.append(comment_text)
        self.likes += 1

i = InstagramPost("Wow",25,["a","b","c"])
i.add_comment("hello")
print(i.likes)
print(i.comments)