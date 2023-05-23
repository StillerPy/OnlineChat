from connection import Connection


if __name__ == '__main__':
    connection = Connection(onMessageFunc=lambda text: print(f'!!! {text} !!!'))
    while True:
        msg = input('Msg: ')
        if msg:
            connection.send(msg)
