
def onPause(func):
    def wrapper(args):
        return func(args)
    return wrapper


def onRun(func):
    def wrapper(args):
        return func(args)
    return wrapper

def onStart(func):
    def wrapper(args):
        return func(args)
    return wrapper


def onFinish(func):
    def wrapper(args):
        return func(args)
    return wrapper