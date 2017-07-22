import socket
import datetime
import time


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
sec = 2
a = 0

while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        print("Sucessfully joined " + Channel)
        break

while True:
    line = s.recv(1024).decode("utf-8")
    if len(line) == 0:
        while True:
            try:
                print("Reconnecting in" + str(sec) + "seconds...")
                s.close
                time.sleep(sec * 1000)
                if sec != 16 and a % 2 == 1:
                     sec * 2
                a += 1
                s = socket.socket()
                s.connect((Host, Port))
                s.send(bytes("PASS " + Pass + "\r\n", "UTF-8"))
                s.send(bytes("NICK " + Nick + "\r\n", "UTF-8"))
                s.send(bytes("JOIN #" + Channel + " \r\n", "UTF-8"))
                break
            except:
                pass
    else:
        sec = 2
        a = 1
    parts = line.split(':')
    if line.startswith('PING'):
        print("---RECEIVED PONG---")
        s.send(bytes("PONG\r\n", "UTF-8"))
        print("---SENT PONG---")
    elif len(parts) > 2:
        message = ':'.join(parts[2:])
        username = parts[1].split("!")[0]
        msg_parts = message.split()

        current_time = datetime.datetime.now()
        print("{:%H:%M:%S} ".format(current_time) + username + ": " + message[:-1])

        if msg_parts[0] == '!pyblockchan' or msg_parts[0] == '!channel':
            if len(msg_parts) == 2:
                Channel = msg_parts[1]
                s.close
                s = socket.socket()
                s.connect((Host, Port))
                s.send(bytes("PASS " + Pass + "\r\n", "UTF-8"))
                s.send(bytes("NICK " + Nick + "\r\n", "UTF-8"))
                s.send(bytes("JOIN #" + Channel + " \r\n", "UTF-8"))
            else:
                send_message('Syntax: ' + msg_parts[0] + ' [channel]')

        if username != "zaxutic" and username != "fkpyramids":
            if len(msg_parts) == 1 + length:
                length += 1

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
            else:
                if len(msg_parts) == 1:
                    p_part = message
                    length = 1
                else:
                    length = 0
        else:
            length = 0

