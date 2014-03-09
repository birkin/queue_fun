# -*- coding: utf-8 -*-

""" Process multiple object tasks. """

import time


def run_word_count( filepath ):
    time.sleep( 2 )
    with open( filepath ) as f:
        data_utf8 = f.read()
        data = data_utf8.decode( u'utf-8', u'replace' )
    wordcount = len( data.split() )
    print { filepath: wordcount }  # could be saved to redis
    return
