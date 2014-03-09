# -*- coding: utf-8 -*-

""" Loads queue with jobs.

    To run:
    - activate the virtual environment
    - cd to 'queue_demo_code' directory
    - python ./process_multiple_objects/job_start.py

    This will put all the the 'tasks.run_word_count()' jobs on the 'queue_fun' queue,
    though nothing will happen unless there is a monitoring worker.
"""

import os
import rq, redis


## setup queue
q = rq.Queue( u'queue_fun', connection=redis.Redis() )

## get list of filepaths
filepaths = []
filenames = os.listdir( u'./process_multiple_objects/word_count_files' )
for filename in filenames:
    if not filename.endswith( u'.xml' ):
        continue
    filepaths.append( os.path.abspath(u'process_multiple_objects/word_count_files/%s' % filename) )

## put jobs on queue
for filepath in filepaths:
    job = q.enqueue_call (
      func=u'process_multiple_objects.tasks.run_word_count',
      args = (filepath,),
      timeout = 30
      )

print u'---'
print u'all jobs have been put on the queue.'
print u'---'
