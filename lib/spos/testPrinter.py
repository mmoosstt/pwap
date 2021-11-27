#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtPrintSupport import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets

a=QApplication([])
document = QTextDocument()
html = """
<head>
    <meta charset="utf-8">
    <title>Report</title>
    <style>
    </style>
</head>
<body>
<div class=\"v-card__text\"><h1>Eduard HuberÖÜÄöüä</h1><h2>Klasse: 10A</h2><div class=\"container dense\"><h2>Bewertungskriterien</h2><h3>Datum: 2020-12-03</h3><h3>Uhrzeit: 19:05</h3><h3>Durchschnitt: 0.167</h3><div class=\"row row--dense\"><div class=\"v-card__text\"><h3>Aufmerksamkeit</h3><p class=\"position:absolute; width: 100%;\">ljalsdjfalsdjfjlkajdlfjaldsjfasd</p></div></div><div class=\"row row--dense\"><div class=\"v-card__text\"><h3>Verhalten</h3><p class=\"position:absolute; width: 100%;\">Um dasdfjl adsfjlasjdflasdjï¿½fljadslfjlasdjfl kaljdfl asjflas dflkajsldkf alksjf lalksjdf alsjdf lakj lflkajsdlf lkajldkf akdsfj alsd</p></div></div><div class=\"row row--dense\"><div class=\"v-card__text\"><h3>Zuverlï¿½ssigkeit</h3><p class=\"position:absolute; width: 100%;\">ï¿½laksdfï¿½kadsï¿½</p></div></div><div class=\"row row--dense\"><div class=\"v-card__text\"><h3>Sozialverhalten</h3><p class=\"position:absolute; width: 100%;\">asdkfï¿½kadslï¿½fkaï¿½sdfksa</p></div></div><div class=\"row row--dense\"><div class=\"v-card__text\"><h3>Wortmeldungen</h3><p class=\"position:absolute; width: 100%;\">aï¿½dsfkï¿½adskfï¿½askd</p></div></div><div class=\"row row--dense\"><div class=\"v-card__text\"><h3>Lernbereitschaft</h3><p class=\"position:absolute; width: 100%;\">ï¿½asdkfï¿½kadsï¿½fkaï¿½sdfkdsa</p></div></div></div></div>
</body>
"""

document.setHtml(html)
printer = QPrinter()
printer.setResolution(96)
printer.setPageSize(QPrinter.Letter)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName("test.pdf")
printer.setPageMargins(12, 16, 12, 20, QPrinter.Millimeter)
document.setPageSize(QSizeF(printer.pageRect().size()))
print(document.pageSize(), printer.resolution(), printer.pageRect())

document.print_(printer)