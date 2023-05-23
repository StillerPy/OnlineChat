from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from time import time
from random import randint


class MySubscribeCallback(SubscribeCallback):
    def __init__(self, userId: str, onMessageFunc):
        # onMessageFunc will be called when incoming message received
        # it will take its text
        super().__init__()
        self.userId = userId
        self.onMessageFunc = onMessageFunc

    def presence(self, pubnub, presence):
        pass

    def status(self, pubnub, status):
        pass

    def message(self, pubnub, message):
        if message.publisher == self.userId:
            return
        self.onMessageFunc(message.message)


class Connection:
    publish_key = 'pub-c-f60b5e45-2e40-4e34-a45c-34ce61062fd7'
    subscribe_key = 'sub-c-34a1b99e-36c6-4179-ac76-fec5eb278b7b'

    def __init__(self):
        self.userId = self.makeUserId()
        self.pubNub = self.makePubNub()
        subscribeCallback = MySubscribeCallback(self.userId, self.onMessageFunc)
        self.pubNub.add_listener(subscribeCallback)
        self.pubNub.subscribe().channels("chan-1").execute()
        self.onStart()

    def onMessageFunc(self, text: str):
        print(f'onMessageFunc <{text}>')

    def makeUserId(self) -> str:
        return f'id<{randint(0, 1_000_000)}>'

    def makePubNub(self) -> PubNub:
        pnconfig = PNConfiguration()
        pnconfig.publish_key = self.publish_key
        pnconfig.subscribe_key = self.subscribe_key
        pnconfig.user_id = self.userId
        pnconfig.ssl = True
        return PubNub(pnconfig)

    def my_publish_callback(self, envelope, status):
        # Check whether request successfully completed or not
        if not status.is_error():
            pass

    def send(self, msg: str):
        msg = str(msg)
        self.pubNub.publish().channel("chan-1").message(msg).pn_async(self.my_publish_callback)

    def onStart(self):
        self.send(f'{self.userId} connected')


if __name__ == '__main__':
    connection = Connection()
    while True:
        msg = input('Msg: ')
        if msg:
            connection.send(msg)
    # test comment


