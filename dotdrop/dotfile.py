"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2017, deadc0de6
represents a dotfile in dotdrop
"""


class Dotfile:

    def __init__(self, key, dst, src, link=False):
        # key of dotfile in the config
        self.key = key
        # where to install this dotfile
        self.dst = dst
        # stored dotfile in dotdrop
        self.src = src
        # should be a link
        self.link = link

    def __str__(self):
        return 'key:%s, src: %s, dst: %s, link: %s' % (self.key, self.src,
                                                       self.dst, self.link)
