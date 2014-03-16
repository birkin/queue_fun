# -*- coding: utf-8 -*-

""" Process multiple object tasks. """

import pprint, time
import requests


def get_keywords( work_title, work_url ):
    """ Takes state name.
            Looks up wikipedia article.
            Sends text to nlp/keyword service.
            Returns nlp output. """
    time.sleep( 2 )
    ## get html
    r = requests.get( work_url )
    html = r.text
    ## get keyword data
    nlp_url = u'http://library.brown.edu/services/nlp/keywords/'
    params = { u'text': html, u'explore': u'false' }
    r = requests.post( nlp_url, data=params )
    ## make return dict
    data_dict = { u'site': work_title, u'keywords': r.json() }
    pprint.pprint( data_dict )
    return
