# -*- coding: utf-8 -*-

""" Task class & runner functions. """

import time
from redis import Redis
from rq import Queue


class Task(object):

  def do_first( self ):
    time.sleep( 3 )
    print u'hello_world_A'
    return

  def do_second( self ):
    time.sleep( 3 )
    print u'hello_world_B'
    return

  def do_third( self ):
    time.sleep( 3 )
    print u'hello_world_C'
    return


## runners ##

task = Task()
q = Queue( u'queue_fun', connection=Redis() )

def run_first_task():
  task.do_first()
  job = q.enqueue_call (
    func=u'tasks_spawn_tasks.tasks.run_second_task',
    args = (),
    timeout = 30
    )
  return

def run_second_task():
  task.do_second()
  job = q.enqueue_call (
    func=u'tasks_spawn_tasks.tasks.run_third_task',
    args = (),
    timeout = 30
    )
  return

def run_third_task():
  task.do_third()
  return
