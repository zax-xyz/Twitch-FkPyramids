import socket
import datetime
import time
import itertools


Host = "irc.twitch.tv"
Port = 6667
Nick = ""  # Twitch username
Pass = ""  # Oauth key (twitchapps.com/tmi)
Channel = ""  # Twitch channel's chat you want to join

def connect():
    global s
    global line
    print("CONNECTING")
    s = socket.socket()
    s.connect((Host, Port))
    s.send(bytes("PASS " + Pass + "\r\n", "UTF-8"))
    s.send(bytes("NICK " + Nick + "\r\n", "UTF-8"))
    s.send(bytes("JOIN #" + Channel + " \r\n", "UTF-8"))
    print("CONNECTED")
    while True:
        line = str(s.recv(1024))
        if "End of /NAMES list" in line:
            print("Entered " + Channel + "'s chat")
            break


def send_message(message):
    s.send(bytes("PRIVMSG #" + Channel + " :" + message + "\r\n", "UTF-8"))

length = 0

connect()

while True:
    line = s.recv(1024).decode("utf-8")
    if len(line) == 0:
        sec = 2
        while True:
            for i in itertools.count():
                try:
                    sys_print_write("Reconnecting in " + str(sec) + " seconds...")
                    s.close()
                    time.sleep(sec * 1000)
                    if sec != 16 and i % 2 == 1:
                        sec *= 2
                    connect()
                    break
                except:
                    pass
    parts = line.split(':')
    if line.startswith('PING'):
        print("RECEIVED PONG")
        s.send(bytes("PONG\r\n", "UTF-8"))
        print("SENT PONG")
    elif len(parts) > 2:
        message = ':'.join(parts[2:])
        username = parts[1].split("!")[0]
        msg_parts = message.split()

        current_time = datetime.datetime.now()
        print("{:%H:%M:%S} ".format(current_time) + username + ": " + message[:-1])

        if msg_parts[0] == '!channel':
            if len(msg_parts) == 2:
                send_message("Switching channel to " + Channel + "\r\n", "UTF-8")
                print("Switching channel to " + Channel)
                Channel = m_parts[1]
                s.close()
                connect()
            else:
                send_message('Syntax: ' + m_parts[0] + ' [channel]')

        if username != "fkpyramids":  # Put the username of the bot here
            if len(m_parts) == 1:
                py_part = message
                length = 1
            elif len(m_parts) == 1 + length:
                length += 1

                for part in m_parts:
                    if part != py_part:
                        length = 0

                if length == 3:
                    for i in [1, 2, 3, 2, 1]:
                        send_message("no " * i)
                    length = 0
            else:
                length = 0
        else:
            length = 0
