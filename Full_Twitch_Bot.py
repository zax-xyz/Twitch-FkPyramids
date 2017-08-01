import socket
import datetime
import time
import itertools

Host = "irc.twitch.tv"
Port = 6667
Nick = ""
Pass = ""
Channel = ""

log = open("logs.txt", 'a', encoding='utf8', errors='replace')


def current_time():
    t = datetime.datetime.now()
    return "{:%H:%M:%S} ".format(t)


def print_write(output):
    print(current_time() + output)
    log.write(current_time() + output + "\n")


def sys_print_write(output):
    print("[" + current_time() + output + "]")
    log.write("[" + current_time() + output + "\n" + "]")


def connect():
    global s
    global line
    sys_print_write("CONNECTING")
    s = socket.socket()
    s.connect((Host, Port))
    s.send(bytes("PASS " + Pass + "\r\n", "UTF-8"))
    s.send(bytes("NICK " + Nick + "\r\n", "UTF-8"))
    s.send(bytes("JOIN #" + Channel + " \r\n", "UTF-8"))
    sys_print_write("CONNECTED")
    while True:
        line = str(s.recv(1024))
        if "End of /NAMES list" in line:
            sys_print_write("Entered " + Channel + "'s chat")
            break

length = 0
sec = 2
global_com = 1
py_blocking = 1

connect()


def send_message(msg):
    s.send(bytes("PRIVMSG #" + Channel + " :" + msg + "\r\n", "UTF-8"))
    log.write(current_time() + Nick + ": " + msg + '\n')


def block():
    global length
    global py_part
    if username != "zaxutic" and username != "fkpyramids":
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


def zax_commands():
    global global_com
    global py_blocking
    global Channel
    if username == 'zaxutic':
        if m_parts[0] == "!pyramid":
            if len(m_parts) >= 3 and m_parts[1].isdigit():
                p_len = int(m_parts[1]) + 1
                p_part = ' '.join(m_parts[2:]) + " "
                for i in range(1, p_len):
                    send_message(p_part * i)
                for i in range(2, p_len):
                    send_message(p_part * (p_len - i))
            else:
                send_message("Syntax: !pyramid [length] [message]")
        elif m_parts[0] == "!speed":
            if len(m_parts) == 2 and m_parts[1].isdigit():
                s_len = int(m_parts[1])
                for i in range(s_len):
                    send_message("bl00dySpeed " + "bl00dySpeedy " * i)
                for i in range(2, s_len + 1):
                    send_message("bl00dySpeed " + "bl00dySpeedy " * (s_len - i))
            else:
                send_message("Syntax : !speed [length]")
        elif m_parts[0] == "!s":
            if len(m_parts) >= 3 and m_parts[1].isdigit():
                r = int(m_parts[1])
                for i in range(r):
                    if m_parts[2] == "/purge":
                        send_message("/timeout " + m_parts[3] + " 1")
                    else:
                        send_message(' '.join(m_parts[2:]))
            else:
                send_message("Syntax: !s [length] [message]")
        elif m_parts[0] == "!purge":
            if len(m_parts) == 2:
                send_message("/timeout " + m_parts[1] + " 1")
            else:
                send_message("Syntax: !purge [username]")
        elif m_parts[0] == "!bcp" and m_parts[1].isdigit():
            if len(m_parts) == 2:
                p_len = int(m_parts[1]) + 1
                for i in range(1, p_len):
                    send_message("catbag1 catbag2 " * i)
                    send_message("catbag3 catbag4 " * i)
                for i in range(2, p_len):
                    send_message("catbag1 catbag2 " * (p_len - i))
                    send_message("catbag3 catbag4 " * (p_len - i))
            else:
                send_message("Syntax: !bcp [length]")
        elif m_parts[0] == "!global":
            try:
                if m_parts[1] == "off" or m_parts[1] == "0":
                    global_com = 0
                elif m_parts[1] == "on" or m_parts[1] == "1":
                    global_com = 1
                else:
                    send_message("Syntax: !globals on/off/0/1")
            except IndexError:
                send_message("Syntax: !globals on/off/0/1")
                pass
        elif m_parts[0] == "!block":
            try:
                if m_parts[1] == "off" or m_parts[1] == "0":
                    py_blocking = 0
                elif m_parts[1] == "on" or m_parts[1] == "1":
                    py_blocking = 1
                else:
                    send_message("Syntax: !globals on/off/0/1")
            except IndexError:
                send_message("Syntax: !globals on/off/0/1")
                pass
        elif m_parts[0] == '!channel':
            if len(m_parts) == 2:
                send_message("Switching channel to " + Channel + "\r\n", "UTF-8")
                print("Switching channel to " + Channel)
                Channel = m_parts[1]
                s.close()
                connect()
            else:
                send_message('Syntax: ' + m_parts[0] + ' [channel]')


def global_commands():
    if m_parts[0] == "CatBag":
        send_message("CatBag")
    elif m_parts[0] == "!CatBag":
        send_message("CatBag CatBag CatBag CatBag CatBag CatBag")
    elif m_parts[0] == "!nani":
        send_message("なに？！")
    elif m_parts[0] == "!purgeme":
        send_message("/timeout " + username + "1")
        send_message(username.capitalize() + "has been purged.")


while True:
    line = s.recv(1024).decode("utf-8")
    if len(line) == 0:
        for i in itertools.count():
            try:
                sys_print_write("Reconnecting in " + str(sec) + " seconds...")
                s.close()
                time.sleep(sec * 1000)
                if sec != 16 and i % 2 == 1:
                    sec *= 2
                connect()
                sec = 2
                break
            except:
                pass
    parts = line.split(':')
    if line.startswith('PING'):
        print("---RECEIVED PONG---")
        s.send(bytes("PONG\r\n", "UTF-8"))
        print("---SENT PONG---")
    elif len(parts) > 2:
        message = ':'.join(parts[2:])
        username = parts[1].split("!")[0]
        m_parts = message.split()

        print_write(username + ": " + message[:-1])

        if py_blocking == 1:
            block()
        zax_commands()
        if global_com == 1:
            global_commands()
