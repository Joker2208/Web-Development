import re
text = "#Have #nice day nice #guy"

def extract_hashtags(text):
    hash = re.findall("#\w*",text)
    print(hash)

extract_hashtags(text)

