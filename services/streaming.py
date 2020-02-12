from util import util, log
from datetime import datetime
from tweepy.streaming import StreamListener, Stream
from tweepy import OAuthHandler, API


""" Modulo para executar o acesso ao servico de streaming da Twitter API """


def stream_tweets(api_token: str, api_secret: str, access_token: str, access_secret: str, saver,
                  keywords: list = None, users: list = None, locations: list = None, stall_warning: bool = False):

    """
        Metodo para executar a coleta em tempo real de tweets filtrando a coleta conforme
        os parametros enviados pelo ususario caso queira mudar a forma como os dados coletados
        sao tratados e necessario alterar a variavel manager para aquela que contem a instacia
        da classe respectiva que fara a tratativa dos dados recebidos.

    """

    auth = OAuthHandler(api_token, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = API(auth)
    listener = TwitterListener(manager=saver, api=api)
    stream = Stream(auth=auth, listener=listener)
    log.write_log('Streaming started', 'execution')
    stream.filter(track=keywords, follow=users, locations=locations, stall_warnings=stall_warning)


class TwitterListener(StreamListener):
    """
        StreamListeners class to handle Twitter streamApi with tweepy lib

    """

    import json
    from time import sleep

    def __init__(self, manager, api=None):
        StreamListener.__init__(self, api)
        self.__manager = manager

    def on_data(self, raw_data):
        data = self.json.loads(raw_data)
        if 'in_reply_to_status_id' in data:
            if self.on_status(data) is False:
                return False

        elif 'warning' in data:
            if self.on_warning(data['warning']) is False:
                return False

        elif 'disconnect' in data:
            if self.on_disconnect(data['disconnect']) is False:
                return False

        elif 'limit' in data:
            if self.on_limit(data['disconnect']) is False:
                return False
        else:
            if self.on_message(data) is False:
                return False

    def on_status(self, status):

        self.__manager.persist(status, data_type='statuses')
        return

    def on_message(self, msg):
        log.write_log('Message recived from API', 'execution')
        self.__manager.persist(msg, data_type='apiMessage')
        return

    def on_timeout(self):
        self.sleep(60) # Dont't spam  in requests
        return True # Don't kill stream

    def on_disconnect(self, data):
        log.write_log('Disconnect msg: ' + str(data['disconnect']), 'error')
        self.__manager.persist(data, data_type='apiMessage')
        print(data['disconnect'])
        return False

    def on_warning(self, data):
        log.write_log('Warning msg: ' + str(data['warning']), 'error')
        self.__manager.persist(data, data_type='apiMessage')
        return

    def on_limit(self, data):
        log.write_log('limit msg: ' + str(data['limit']), 'error')
        self.__manager.persist(data, data_type='apiMessage')
        return False
