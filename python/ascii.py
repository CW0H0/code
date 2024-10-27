#coding:utf-8

from PIL import Image

def get_char(r,g,b,alpha=256):
    gary = (0.2126*r + 0.7152*g +0.0722*b)
    ascii_char = list("sb")
    x= int((gary / alpha) * len(ascii_char))
    return ascii_char[xi]

def main(file_name, width=300, height=300):
    im = Image open(file_name)
    im = im.resize(width, height)
    im.save("a.png")
    