import socket
import datetime
import time
import itertools
from random import randint
import sys
from termcolor import colored

Host = "irc.twitch.tv"
Port = 6667
Owner = 'zaxu__'
with open("auth", "r", encoding='utf-8') as auth_file:
    line = auth_file.readline().split()
    Nick = line[0]
    Pass = line[1]

Channel = sys.argv[1]
cooldown = 0

def current_time():
    t = datetime.datetime.now()
    return colored(t.strftime("%Y-%m-%d %H:%M:%S  "), 'green')

def print_write(output):
    out = current_time() + output
    print(out)

    with open("logs.txt", 'a', encoding='utf8', errors='replace') as log:
        log.write(out + '\n')

def sys_print_write(output):
    out = current_time() + colored(output, 'red', attrs=['bold'])
    print(out)

    with open("logs.txt", 'a', encoding='utf8', errors='replace') as log:
        log.write(out + '\n')

def connect():
    global s
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
            out = current_time() + colored(f"Entered {Channel}'s channel",
                                           'green', attrs=['bold'])
            print(out)

            with open("logs.txt", 'a', encoding='utf8', errors='replace') as log:
                log.write(out + '\n')

            break

length = 0
sec = 2
global_com = False
py_blocking = False
x = 0
NoBully = False
cd = 0

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if arg == 'all':
            global_com = True
            py_blocking = True
            NoBully = True
        elif arg == 'global':
            global_com = True
        elif arg == 'block':
            py_blocking = True
        elif arg == 'nobully':
            NoBully = True

mlst = ['yes', 'no']
mcd = 0

connect()

def send_message(msg):
    s.send(bytes("PRIVMSG #" + Channel + " :" + msg + "\r\n", "UTF-8"))
    print_write(
        current_time() + colored(Nick, 'cyan', attrs=['bold']) + ": " + msg
    )

def block():
    global length
    global py_part
    global x
    global cd
    if username not in [Owner, Nick]:
        if len(m_parts) == 1:
            if len(m_parts) == length - 1 and m_parts[0] == py_part:
                send_message(
                    f"@{username} Baby pyramids don't count, you degenerate."
                )

            py_part = m_parts[0]
            length = 1
        elif len(m_parts) == 1 + length:
            length += 1
            for part in m_parts:
                if part != py_part:
                    length = 0
                    break
            if length == 3:
                if x % 2 == 0 or (time.time() - cd) >= 30:
                    send_message("no")
                    cd = time.time()
                    x = 0
                else:
                    send_message("No")
                length = 0
                x += 1
        else:
            length = 0
    else:
        length = 0

def owner_commands():
    global global_com
    global py_blocking
    global Channel
    global NoBully
    com = m_parts[0]
    if username == Owner:
        if com == "!pyramid":
            if len(m_parts) >= 3 and m_parts[1].isdigit():
                p_len = int(m_parts[1]) + 1
                p_part = ' '.join(m_parts[2:]) + " "
                for i in range(1, p_len):
                    send_message(p_part * i)
                for i in range(2, p_len):
                    send_message(p_part * (p_len - i))
            else:
                send_message("Syntax: !pyramid [length] [message]")
        elif com == "!speed":
            if len(m_parts) == 2 and m_parts[1].isdigit():
                s_len = int(m_parts[1])
                for i in range(s_len):
                    send_message("bl00dySpeed " + "bl00dySpeedy " * i)
                for i in range(2, s_len + 1):
                    send_message("bl00dySpeed " + "bl00dySpeedy " * (s_len - i))
            else:
                send_message("Syntax : !speed [length]")
        elif com == "!s":
            if len(m_parts) >= 3 and m_parts[1].isdigit():
                r = int(m_parts[1])
                for i in range(r):
                    if m_parts[2] == "/purge":
                        send_message("/timeout " + m_parts[3] + " 1")
                    else:
                        send_message(' '.join(m_parts[2:]))
            else:
                send_message("Syntax: !s [length] [message]")
        elif com == "!purge":
            if len(m_parts) == 2:
                send_message("/timeout " + m_parts[1] + " 1")
            else:
                send_message("Syntax: !purge [username]")
        elif com == "!bcp" and m_parts[1].isdigit():
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
        elif com == "!fpglobals" or com == "!globals":
            try:
                if m_parts[1] == "off" or m_parts[1] == "0":
                    if global_com:
                        global_com = False
                        send_message("Turned off global commands")
                    else:
                        send_message("Global commands are already off")
                elif m_parts[1] == "on" or m_parts[1] == "1":
                    if not global_com:
                        global_com = True
                        send_message("Turned on global commands")
                    else:
                        send_message("Global commands are already on")
                else:
                    send_message("Syntax: !fpglobals on/off/0/1")
            except IndexError:
                send_message("Syntax: !fpglobals on/off/0/1")
                pass
        elif com == "!fpblocking" or com == "!blocking":
            try:
                if m_parts[1] == "off" or m_parts[1] == "0":
                    if py_blocking:
                        py_blocking = False
                        send_message("Turned off pyramid blocking")
                    else:
                        send_message("Pyramid blocking is already off")
                elif m_parts[1] == "on" or m_parts[1] == "1":
                    if not py_blocking:
                        py_blocking = True
                        send_message("Turned on pyramids blocking")
                    else:
                        send_message("Pyramid blocking is already on")
                else:
                    send_message("Syntax: !fpblocking on/off/0/1")
            except IndexError:
                send_message("Syntax: !fpblocking on/off/0/1")
                pass
        elif com == '!fpchannel':
            if len(m_parts) == 2:
                send_message("Switching channel to {}".format(m_parts[1]))
                print("Switching channel to {}".format(m_parts[1]))
                Channel = m_parts[1]
                s.close()
                connect()
            else:
                send_message('Syntax: !fpchannel [channel]')
        elif com == '!fpnobully':
            try:
                if m_parts[1] == 'on' or m_parts[1] == '1':
                    if NoBully:
                        send_message("Already on")
                    else:
                        NoBully = True
                        send_message("Turned on anti-bullying")
                elif m_parts[1] == 'off' or m_parts[1] == '0':
                    if NoBully:
                        NoBully = False
                        send_message('Turned off anti-bullying')
                    else:
                        send_message('Already off')
                else:
                    send_message("Usage: !fpnobully on/off/1/0")
            except:
                send_message("Syntax: !fpnobully on/off/1/0")
        elif com == '!fpping':
            send_message("pong")


def global_commands():
    global mcd
    global m_parts
    com = m_parts[0].lower()

    if com == "!purgeme":
        try:
            send_message("/timeout " + username + " 1")
            send_message("{} has been purged.".format(username.capitalize))
        except:
            send_message("Could not purge {}".format(username.capitalize))

    if com == "@fkpyramids" and (time.time() - mcd) >= 30:
        send_message(mlst[randint(0,1)])
        mcd = time.time()


while True:
    line = s.recv(1024).decode("utf-8")
    if len(line) == 0:
        for i in itertools.count():
            try:
                sys_print_write("Reconnecting in " + str(sec) + " seconds...")
                s.close()
                time.sleep(sec)
                if sec != 16 and i % 2 == 1:
                    sec *= 2
                connect()
                sec = 2
                break
            except:
                pass

    parts = line.split(':')

    if line.startswith('PING'):
        s.send(bytes("PONG\r\n", "UTF-8"))
    elif len(parts) > 2:
        message = ':'.join(parts[2:])
        username = parts[1].split("!")[0]
        m_parts = message.split()

        print_write(
            colored(username, 'blue', attrs=['bold']) + ": " + message[:-1]
        )

        owner_commands()

        if py_blocking:
            block()

        if global_com:
            global_commands()

        if NoBully:
            if 'bully' in message.lower() or 'bulli' in message.lower():
                if time.time() - cooldown > 30:
                    send_message("NoBully")
                    cooldown = time.time()
