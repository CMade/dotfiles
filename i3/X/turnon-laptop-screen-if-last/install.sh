#!/usr/bin/env bash

set -e

sudo ln -sf $PWD/99-turnon-laptop-screen-if-last.rules /etc/udev/rules.d
ln -sf $PWD/turnon-laptop-screen-if-last.sh $HOME/.local/bin
