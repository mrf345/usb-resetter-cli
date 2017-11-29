# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import usb.core
from os import path
import sys


class find_class(object):
    def __init__(self, class_):
        self._class = class_

    def __call__(self, device):
        # first, let's check the device
        if device.bDeviceClass == self._class:
            return True
        for cfg in device:
            intf = usb.util.find_descriptor(cfg, bInterfaceClass=self._class)
            if intf is not None:
                return True

        return False


def listd(tp=None, gui=None):
    vl, ftp = [], []
    if tp is not None:
        for ttp in tp:
            ftp.extend([[ad for ad in usb.core.find(
                find_all=True, custom_match=find_class(ttp))]])
    else:
        ftp = [usb.core.find(find_all=True)]
    for f in ftp:
        for ll in f:
            if gui:
                d = None
                try:
                    d = usb.util.get_string(ll, ll.iProduct)
                except:
                    pass
                if d is None:
                    dld = {0: "Unspecified", 1: "Audio", 2: "Network card",
                           3: "Human interface", 7: "Printer",
                           8: "Mass storage", 9: "Hub", 10: "Network",
                           11: "Smart card", 12: "Content security",
                           13: "Video device", 15: "Audio or Video",
                           16: "Billboard", 17: "USB Type-C",
                           19: "Wireless"}
                    d = "Unspecified"
                    for desc in ll:
                        for dd in dld.keys():
                            if usb.util.find_descriptor(desc,
                                                        bInterfaceClass=dd
                                                        ):
                                d = dld.get(dd)
                                break
                vl.append(
                    str(d) + "," + str(
                        hex(ll.idVendor)) + "," + str(
                            hex(ll.idProduct)))
            else:
                vl.append([hex(ll.idVendor), hex(ll.idProduct)])
    return vl


def resetit(dstr):
    s = dstr.split(',')
    try:
        ud = usb.core.find(idVendor=int(s[1], 16), idProduct=int(s[2], 16))
        if ud is not None:
            ud.reset()
            return True
        else:
            return False
    except:
        return False
