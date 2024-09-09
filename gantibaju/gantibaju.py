#!/usr/bin/env python

import subprocess
import  optparse
import re

def dapetargumen_nuz():
    parser = optparse.OptionParser()
    parser.add_option("-i", dest="int", help="interface yang dirubah")
    parser.add_option("-m", dest="macbaru", help="mac address yang baru")
    (optns, argmnts) = parser.parse_args()
    if not optns.int:
        parser.error("Masukkan interface yang ingin dirubah! misal: -i eth0")
    elif not optns.macbaru:
        parser.error("Masukkan MAC address baru! misal: -m 00.11.11.11.11.11")
    return optns



def rubahmac_nuz(int, macbaru):
    print("Merubah MAC address untuk " + int + " ke " + macbaru)
    subprocess.call(["ifconfig", int, "down"])
    subprocess.call(["ifconfig", int, "hw", "ether", macbaru])
    subprocess.call(["ifconfig", int, "up"])


def dapetmacskrng_nuz(int):
    cekhasil_ifconf = subprocess.check_output(["ifconfig", int])
    hasilcari_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(cekhasil_ifconf))
    if hasilcari_mac:
        return hasilcari_mac.group(0)
    else:
        print("Tidak bisa cek MAC address.")

optns = dapetargumen_nuz()
macskrng = dapetmacskrng_nuz(optns.int)
print("MAC sekarang >>> " + str(macskrng))
rubahmac_nuz(optns.int, optns.macbaru)
macskrng = dapetmacskrng_nuz(optns.int)
if macskrng == optns.macbaru:
    print("[!] MAC address BERHASIL dirubah ke " + macskrng + " [!]")
else:
    print("[!] MAC address TIDAK BERHASIL dirubah [!]")

penutupan = '''
    dibuat dengan niat oleh 
     ______   _ _   _ _   _ _______________
    |__  / | | | \ | | | | |__  /__  /__  /
      / /| | | |  \| | | | | / /  / /  / / 
     / /_| |_| | |\  | |_| |/ /_ / /_ / /_ 
    /____|\___/|_| \_|\___//____/____/____|

    https://steamcommunity.com/id/zunuzzz/

    =========GUNAKAN DENGAN BIJAK=========
    '''

print(penutupan)
