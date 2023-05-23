from connection import Connection


if __name__ == '__main__':
    connection = Connection()
    while True:
        msg = input('Msg: ')
        if msg:
            connection.send(msg)