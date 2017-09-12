# coding=utf-8
import os, sys
import time

import qrcode

# generate the qrcode and save it definition

usage = """
Usage:
    python qrCodeGen.py <output file name> <data to put in the qrcode>
"""

def gen_qrcode(dataList, path):
    # generate the qrcode
    qr = qrcode.QRCode(5, error_correction=qrcode.constants.ERROR_CORRECT_L)
    data = ""
    for d in dataList:
        data += d + " "
    qr.add_data(data)
    qr.make()
    im = qr.make_image()

    count = 1
    old_path = path.split(".")
    while os.path.isfile(path):
        path = old_path[0] + "({}).".format(count) + old_path[1]
        count += 1
    
    # save the image out
    im.save(path, format='png')
    # print that its been successful
    print("QRCode has been generated under {0}".format(path))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(usage)
    else:
        gen_qrcode(sys.argv[2:], sys.argv[1])