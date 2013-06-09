from collections import namedtuple
import os
import shutil

config = 'config'

def clone_repo(name):
    os.system('git clone ' + name + ' ' + config)

class InvalidArgumentException(Exception):
    pass

class Config(namedtuple('Config', 'dest, src')):
    def pre_validate(self):
        if type(dest) is not str:
            raise TypeError('dest is not a valid string')
        if type(src) is not str:
            raise TypeError('src is not a valid string')

    def post_validate(self):
        if src is not in os.listdir('.'):
            raise IOError(src + ' does not exist')

    def make(self):
        shutil.move(self.src, self.dest)

class Repo(namedtuple('Repo', 'repo, files')):
    def make(self):
        if type(self.files) is not list:
            raise TypeError('files does not contain a valid list')
        if type(self.repo) is not str:
            raise TypeError('repo is not a valid string')
        for f in self.files:
            f.pre_validate()
        clone_repo(self.repo)
        cwd = os.getcwd()
        os.chdir(config)
        try:
            for f in self.files:
                f.post_validate()
        except IOError:
            shutil.rmtree(config)
            raise
        for f in self.files:
            f.make()
        os.chdir(cwd)
        shutil.rmtree(config)
