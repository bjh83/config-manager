from collections import namedtuple
import os
import shutil

config = 'config'

def clone_repo(name, dest=config):
    os.system('git clone ' + name + ' ' + dest)

class InvalidArgumentException(Exception):
    pass

class Exec(namedtuple('Exec', 'command')):
    def pre_validate(self):
        if type(command) is not str:
            raise TypeError('command is not a valid string')

    def post_validate(self):
        pass

    def make(self):
        os.system(command)

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

class Clone(namedtuple('Clone', 'dest, src')):
    def pre_validate(self):
        if type(dest) is not str:
            raise TypeError('dest is not a valid string')
        if type(src) is not str:
            raise TypeError('src is not a valid string')

    def post_validate(self):
        pass

    def make(self):
        clone_repo(src, dest)

class Repo(namedtuple('Repo', 'repo, files')):
    def pre_validate(self):
        if type(self.files) is not list:
            raise TypeError('files does not contain a valid list')
        if type(self.repo) is not str:
            raise TypeError('repo is not a valid string')
        for f in self.files:
            f.pre_validate()

    def make(self):
        clone_repo(self.repo)
        cwd = os.getcwd()
        os.chdir(config)

    def post_validate(self):
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

def Setup(files):
    if type(self.files) is not list:
        raise TypeError('files does not contain a valid list')
    for f in self.files:
        f.pre_validate()
    for f in self.files:
        f.post_validate()
    for f in self.files:
        f.make()
