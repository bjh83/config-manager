from collections import namedtuple
import os

class Package(namedtuple('Package', 'name')):
    def pre_validate(self):
        if type(name) is not str:
            raise TypeError('name is not string')

    def post_validate(self):
        pass

    def make(self):
        os.system('apt-get install' + ' ' + name)
