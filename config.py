# A config file index
from conf_manager import Repo, Config, Clone
from package_manager import Package

Setup([
    Package('git'),
    Package('zsh'),
    Package('vim'),
    Package('gnome-shell'),
    Package('gnome-tweak-tool'),
    Package('gnome-contacts'),
    Package('gnome-sushi'),
    Package('dconf-tools'),
    Package('g++'),
    Repo('http://github.com/bjh83/config.git', [
        Config('/home/brendan/.vimrc',
            '.vimrc'
            ),
        Config('/home/brendan/.zshrc',
            '.zshrc'
            ),
        Config('/home/brendan/.vim',
            '.vim'
            ),
        ]),
    Clone('/home/brendan/.vim',
        'git://github.com/gmarik/vundle.git'
        ),
    ])
