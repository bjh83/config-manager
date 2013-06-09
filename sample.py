# A config file index
from conf_manager import Repo, Config

Repo('https://github.com/bjh83/config.git', [
    Config('/home/brendan/test.txt',
        'test.txt'
        ),
    Config('/home/brendan/foo',
        'foo'
        ),
    Config('/home/brendan/bar',
        'foobar'
        ),
    ]).make()
