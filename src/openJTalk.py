#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def openJTalk(speech_content):
    open_jtalk = ['open_jtalk']
    mech = ['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice = ['-m','/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice']
    speed = ['-r','1.0']
    outwav = ['-ow','open_jtalk.wav']
    cmd = open_jtalk + mech +htsvoice + speed + outwav
    c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
    c.stdin.write(speech_content)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)
