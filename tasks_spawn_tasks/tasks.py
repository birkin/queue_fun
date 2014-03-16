# -*- coding: utf-8 -*-

""" Task class & runner functions. """

import pprint, time
import requests, rq, redis


class Task(object):

    def do_first( self ):
        """ Creates and returns works dict. """
        time.sleep( 2 )
        works = {
            u'Brown_Home': u'http://www.brown.edu',
            u'Brown_Library': u'http://library.brown.edu',
            u'Brown_Home2': u'http://www.brown.edu',
            u'Brown_Library2': u'http://library.brown.edu',
            }
        # works = {
        #     u'Emma': u'http://www.gutenberg.org/cache/epub/158/pg158.txt',
        #     u'Mansfield Park': u'http://www.gutenberg.org/cache/epub/141/pg141.txt',
        #     u'Northanger Abbey': u'http://www.gutenberg.org/cache/epub/121/pg121.txt',
        #     u'Pride and Prejudice': u'http://www.gutenberg.org/cache/epub/1342/pg1342.txt',
        #     u'Sense and Sensibility': u'http://www.gutenberg.org/cache/epub/161/pg161.txt',
        #     }
        return works

    def do_second( self, work_title, work_url ):
        """ Takes title and url strings.
            Gets work text.
            Returns title and text dict. """
        time.sleep( 2 )
        r = requests.get( work_url )
        return r.text

    def do_third( self, work_title, work_text ):
        """ Takes work_title and text strings.
            Gets keywords json.
            Prints it out. """
        time.sleep( 2 )
        nlp_url = u'http://library.brown.edu/services/nlp/keywords/'
        params = { u'text': work_text, u'explore': u'false' }
        r = requests.post( nlp_url, data=params )
        data_dict = { u'work': work_title, u'keywords': r.json() }
        pprint.pprint( data_dict )
        return


## runners ##

task = Task()
q = rq.Queue( u'queue_fun', connection=redis.Redis() )

def run_first_task():
    works_dict = task.do_first()
    for (key, value) in works_dict.items():
        job = q.enqueue_call (
            func=u'tasks_spawn_tasks.tasks.run_second_task',
            kwargs={ u'work_title': key, u'work_url': value } )
    return

def run_second_task( work_title, work_url ):
    text = task.do_second( work_title, work_url )
    job = q.enqueue_call (
        func=u'tasks_spawn_tasks.tasks.run_third_task',
        kwargs={ u'work_title': work_title, u'work_text': text } )
    return

def run_third_task( work_title, work_text ):
  task.do_third( work_title, work_text )
  return
