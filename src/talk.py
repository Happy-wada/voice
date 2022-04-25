#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
#txt ファイル
txt_file = "a.txt"
#openjtalk
#dic
x = '/var/lib/mecab/dic/open-jtalk/naist-jdic'
#voice
m = '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice'
#speed
r = '1.0'
ow = '/tmp/tmp.wav'
#aplay
CARD_NO = 1
DEVICE_NO = 0

def talk_text(t):
    open_jtalk = ['open_jtalk']
    xdic = ['-x', x]
    mvoice = ['-m', m]
    rspeed = ['-r', r]
    owoutwav = ['-ow', ow]
    cmd = open_jtalk + xdic + mvoice + rspeed + owoutwav
    c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
    aplay = ['aplay', '-q', ow, ('Dplaughw:' + str(CARD_NO)+''+ str(DEVICE_NO))]
    wr = subprocess.Popen(aplay)
    wr.wait()

def main():
    with open(txt_file) as f:
        for line in f:
            talk_text(line)
if __name__ == '__main__':
    main()
    
