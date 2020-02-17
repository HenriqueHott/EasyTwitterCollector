from services import streaming
from util import util, log
from manager import persisters
import json
from tweepy import TweepError


""" Modulo principal que inicia a aplicacao"""

def main():

    config = util.get_configs()

    saver = persisters.RawTweetSaver()

    try:
        if config['service'] == 'streaming':
            method = getattr(streaming, config['method'])
            method(**config['parameters'])

        else:
            raise Exception('Service doesn\'t exists')

    except TweepError as te:
        log.write_log('Tweepy Exeception', 'exception', te)

    except Exception as e:
        log.write_log('Base Exeception', 'exception', e)

    finally:
        log.write_log('Processes finished', 'execution')


if __name__ == '__main__':
    main()
