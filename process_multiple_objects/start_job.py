# -*- coding: utf-8 -*-

""" Loads queue with jobs.

    To run:
    - activate the virtual environment
    - cd to 'queue_demo_code' directory
    - python ./process_multiple_objects/start_job.py

    This will put all the the 'tasks.run_word_count()' jobs on the 'queue_fun' queue,
    though nothing will happen unless there is a monitoring worker.
"""

import os
import rq, redis


## setup queue
q = rq.Queue( u'queue_fun', connection=redis.Redis() )

## site-dict
sites = {
    u'Emma': u'http://www.gutenberg.org/cache/epub/158/pg158.txt',
    u'Mansfield Park': u'http://www.gutenberg.org/cache/epub/141/pg141.txt',
    u'Northanger Abbey': u'http://www.gutenberg.org/cache/epub/121/pg121.txt',
    u'Pride and Prejudice': u'http://www.gutenberg.org/cache/epub/1342/pg1342.txt',
    u'Sense and Sensibility': u'http://www.gutenberg.org/cache/epub/161/pg161.txt',
    }

## put jobs on queue
for (key, value) in sites.items():
    job = q.enqueue_call (
        func=u'process_multiple_objects.tasks.get_keywords',
        kwargs={ u'site_name': key, u'site_url': value } )

print u'---'
print u'all jobs have been put on the queue.'
print u'---'
