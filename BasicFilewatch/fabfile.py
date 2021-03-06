from fabric.api import *
import time

ansi = dict([ ("clear", '\033[0m') ])

def withAnsi(ctls, string):
    ansichars = map((lambda ctl: ansi[ctl]) , ctls.split(' '))
    ansictl = "".join(ansichars)
    return ansictl + string + ansi["clear"]

def fabMD5(filename):
    md5ret = run("md5sum " + filename)
    return md5ret.split(' ')[0]

def monitor(filename):
    md5init = fabMD5(filename)
    print filename + ": " + md5init
    md5track = md5init

    while(1):
        md5 = fabMD5(filename)
        time.sleep(5)
        if(md5 != md5track):
            print filename + " changed"
            md5track = md5
