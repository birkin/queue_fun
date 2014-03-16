# -*- coding: utf-8 -*-

""" Loads queue with 'run_first_task' job.

    To run:
    - source the env
    - python this-file.py

    This will put the 'run_first_task' job on the 'queue_fun' queue, though nothing will happen unless there is a monitoring worker.
"""

import rq, redis


## setup queue
q = rq.Queue( u'queue_fun', connection=redis.Redis() )

## put the first task on the queue
job = q.enqueue_call (
  func=u'tasks_spawn_tasks.tasks.run_first_task',
  args = (),
  timeout = 30
  )

print u'---'
print u'the initial job has been put on the queue'
print u'---'
