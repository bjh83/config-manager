# A config file index
from conf_manager import Repo, Config

Repo('https://github.com/bjh83/config.git', [
    Config('/home/brendan/.vimrc',
        '.vimrc'
        ),
    Config('/home/brendan/.zshrc',
        '.zshrc'
        ),
    Config('/home/brendan/.vim',
        '.vim'
        ),
    Clone('/home/brendan/.vim',
        'git://github.com/gmarik/vundle.git'
        ),
    ])
