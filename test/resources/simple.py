#! /usr/bin/python

from lch import *

@onRun
def run(args):
    print("run")
    return {"msg":"fsd"}

@onPause
def pause(args):
    print("pause")

@onStart
def start(args):
    print("start")

@onFinish
def finish(args):
    print("finish")