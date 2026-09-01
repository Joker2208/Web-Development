class InstaStory:
    def share(self):
        print("Sharing an image story")

class WhatsAppStory(InstaStory):
    def share(self):
        print("Sharing a text status")

i = InstaStory()
i.share()
w = WhatsAppStory()
w.share()