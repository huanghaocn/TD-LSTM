#!/usr/bin/env python
# encoding: utf-8
# @author: newbie
# email: zhengshiliang0@gmail.com


import sys


def add_aspect(sf, df):
    fs = open(sf).readlines()
    fd = open(df, 'w')
    for i in xrange(0, len(fs), 3):
        # line = fs[i].split('$t$')
        # line = line[0] + '$T$ $T$' + line[1]
        line = fs[i].replace('$t$', '$t$ $t$')
        fd.write(line)
        fd.write(fs[i+1])
        fd.write(fs[i+2])


def add_weight(fw, bf, df):
    """
    combine weight_fw and weight_bw
    """
    ff = open(fw)
    fb = open(bf)
    fd = open(df, 'w')
    for l1, l2 in zip(ff, fb):
        l1 = l1.split()
        l2 = l2.split()
        tmp = []
        for l in l1:
            if l != '0.0':
                tmp.append(l)
        l2.reverse()
        for l in l2[:-2]:
            if l != '0.0':
                tmp.append(l)
        fd.write(' '.join(tmp) + '\n')


def filter_test(ef, tf, ntf):
    """
    remove word not in word embedding
    """
    words = ['$t$']
    for line in open(ef):
        words.append(line.split()[0])
    ft = open(tf).readlines()
    fn = open(ntf, 'w')
    for i in xrange(0, len(ft), 3):
        line = ft[i]
        line = line.lower().split()
        tmp = []
        for w in line:
            if w in words:
                tmp.append(w)
        fn.write(' '.join(tmp) + '\n')
        fn.write(ft[i+1])
        fn.write(ft[i+2])


if __name__ == '__main__':
    add_aspect(sys.argv[1], sys.argv[2])
    # add_weight(sys.argv[1], sys.argv[2], sys.argv[3])
    # filter_test(sys.argv[1], sys.argv[2], sys.argv[3])

