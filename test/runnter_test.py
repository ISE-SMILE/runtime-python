import unittest

from pythonAction import pythonrunner
import json
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG

class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open("./resources/simple.py") as f:
            code = f.read()

        runner = pythonrunner.PythonRunner()

        message = {
            'code':code,
        }
        runner.init(message)

        r = runner.features()
        r = json.loads(r)
        assert(all(r.values()))


        r = runner.start(None,None)
        assert (r == (200, {'msg': 'OK'}))

        r = runner.run(None,None)
        print(r)

        r = runner.pause(None,None)
        assert (r == (200, {'msg': 'OK'}))

        r = runner.stop(None,None)
        assert (r == (200, {'msg': 'OK'}))


if __name__ == '__main__':
    unittest.main()
