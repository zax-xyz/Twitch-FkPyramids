import socket
import datetime


Host = "irc.twitch.tv"
Port = 6667
Nick = ""  # Twitch username
Pass = ""  # Oauth key (twitchapps.com/tmi)
Channel = input("Channel: ")

s = socket.socket()
s.connect((Host, Port))
s.send(bytes("PASS " + Pass + "\r\n", "UTF-8"))
s.send(bytes("NICK " + Nick + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + Channel + " \r\n", "UTF-8"))


def send_message(message):
    s.send(bytes("PRIVMSG #" + Channel + " :" + message + "\r\n", "UTF-8"))

length = 0
x = 0
y = 0


while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        print("Joined " + Channel)
        break

while True:
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) > 2:
            message = ':'.join(parts[2:])
            username = parts[1].split("!")[0]
            msg_parts = message.split()

            current_time = datetime.datetime.now()
            print("{:%H:%M:%S} ".format(current_time) + username + ": " + message)

            if username != "zaxutic" and username != "fkpyramids":
                if len(msg_parts) == 1 + length:
                    length += 1
                    print(length)

                    if len(msg_parts) == 1:
                        p_part = message
                        x = 1
                    elif x == 1:
                        for part in msg_parts:
                            if part != p_part:
                                length = 0
                                x = 0
                    else:
                        length = 0

                    if length == 3:
                        for i in [1, 2, 3, 2, 1]:
                            send_message("no " * i)
                        length = 0
                        x = 0
                        y +=1
                else:
                    if len(msg_parts) == 1:
                        p_part = message
                        length = 1
                    else:
                        length = 0
                    print(length)
            else:
                length = 0
                print(length)
