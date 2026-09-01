class Notification:
    def send(self):
        print("You 1 unread message")

class Email(Notification):
    def send(self):
        print("You have 1 email")

class SMS(Notification):
    def send(self):
        print("You have 1 SMS")

n = Notification()
n.send()
e = Email()
e.send()
s = SMS()
s.send()

#Im my example the method is overloading the actual print statement fromt he notification class in email and in sms as you see in the output