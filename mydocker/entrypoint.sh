#!/bin/bash

git clone --recursive http://github.com/mgautam/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
git checkout container
~/.dotfiles/install.sh

watch ~/.dotfiles/install.sh
