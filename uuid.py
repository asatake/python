# -*- coding: utf-8 -*-

"""UUID v4 Generator
This extension uuid strings"""

from albertv0 import *
import uuid

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "UUID"
__version__ = "1.0"
__trigger__ = "uuid "
__author__ = "UUID Generator"
__dependencies__ = ["uuid"]

iconPath = iconLookup('x-office-calendar')


def handleQuery(query):
    fields = list(filter(None, query.string.split()))
    if fields and fields[0].startswith("uuid"):
        text = str(uuid.uuid4())
        return Item(
                id=__prettyname__,
                icon=iconPath,
                text=text,
                subtext="UUID v4 Generate",
                completion=query.rawString,
                actions=[ClipAction("Copy to clipboard", text)]
            )
