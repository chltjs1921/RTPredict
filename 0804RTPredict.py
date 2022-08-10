# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '0804layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
import mplcursors

from PyQt5 import Qt, QtCore, QtGui, QtWidgets, QtWebEngineWidgets

from PyQt5.QtWidgets import QHeaderView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from rdkit import Chem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1573, 1015)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.RTpredict = QtWidgets.QWidget()
        self.RTpredict.setObjectName("RTpredict")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.RTpredict)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Predictmin = QtWidgets.QLabel(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.Predictmin.sizePolicy().hasHeightForWidth())
        self.Predictmin.setSizePolicy(sizePolicy)
        self.Predictmin.setMinimumSize(QtCore.QSize(0, 50))
        self.Predictmin.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Predictmin.setFont(font)
        self.Predictmin.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Predictmin.setObjectName("Predictmin")
        self.gridLayout_2.addWidget(self.Predictmin, 8, 3, 1, 1)
        self.Applysmi = QtWidgets.QPushButton(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Applysmi.sizePolicy().hasHeightForWidth())
        self.Applysmi.setSizePolicy(sizePolicy)
        self.Applysmi.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Applysmi.setFont(font)
        self.Applysmi.clicked.connect(self.PredictRT)
        self.Applysmi.setObjectName("Applysmi")
        self.gridLayout_2.addWidget(self.Applysmi, 7, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./SG.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.Drawsketcher = QtWidgets.QLabel(self.RTpredict)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Drawsketcher.setFont(font)
        self.Drawsketcher.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Drawsketcher.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Drawsketcher.setAutoFillBackground(False)
        self.Drawsketcher.setTextFormat(QtCore.Qt.AutoText)
        self.Drawsketcher.setScaledContents(True)
        self.Drawsketcher.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Drawsketcher.setObjectName("Drawsketcher")
        self.gridLayout_2.addWidget(self.Drawsketcher, 3, 1, 1, 3)
        self.PredictRT = QtWidgets.QLabel(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PredictRT.sizePolicy().hasHeightForWidth())
        self.PredictRT.setSizePolicy(sizePolicy)
        self.PredictRT.setMinimumSize(QtCore.QSize(0, 50))
        self.PredictRT.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.PredictRT.setFont(font)
        self.PredictRT.setObjectName("PredictRT")
        self.gridLayout_2.addWidget(self.PredictRT, 8, 1, 1, 1)
        self.Showpredict = QtWidgets.QLineEdit(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Showpredict.sizePolicy().hasHeightForWidth())
        self.Showpredict.setSizePolicy(sizePolicy)
        self.Showpredict.setMinimumSize(QtCore.QSize(0, 50))
        self.Showpredict.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Showpredict.setFont(font)
        self.Showpredict.setAlignment(QtCore.Qt.AlignCenter)
        self.Showpredict.setReadOnly(True)
        self.Showpredict.setObjectName("Showpredict")
        self.gridLayout_2.addWidget(self.Showpredict, 8, 2, 1, 1)
        self.RTscatter = QtWidgets.QWidget(self.centralwidget)
        self.RTscatter.setAutoFillBackground(False)
        self.RTscatter.setObjectName("RTscatter")

        self.fig1 = plt.Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        self.canvas1_toolbar = NavigationToolbar(self.canvas1, self.RTscatter)
        self.vbox1 = QtWidgets.QVBoxLayout(self.RTscatter)
        self.vbox1.addWidget(self.canvas1_toolbar)
        self.vbox1.addWidget(self.canvas1)

        self.gridLayout_2.addWidget(self.RTscatter, 5, 4, 2, 3)
        self.label_2 = QtWidgets.QLabel(self.RTpredict)
        self.label_2.setMaximumSize(QtCore.QSize(200, 150))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./KY.jpg"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 6, 1, 1)
        self.Insertsmi = QtWidgets.QLineEdit(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Insertsmi.sizePolicy().hasHeightForWidth())
        self.Insertsmi.setSizePolicy(sizePolicy)
        self.Insertsmi.setMinimumSize(QtCore.QSize(0, 50))
        self.Insertsmi.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Insertsmi.setFont(font)
        self.Insertsmi.setAlignment(QtCore.Qt.AlignCenter)
        self.Insertsmi.setObjectName("Insertsmi")
        self.gridLayout_2.addWidget(self.Insertsmi, 7, 2, 1, 1)
        self.Showall = QtWidgets.QPushButton(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Showall.sizePolicy().hasHeightForWidth())
        self.Showall.setSizePolicy(sizePolicy)
        self.Showall.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Showall.setFont(font)
        self.Showall.setAutoFillBackground(True)
        self.Showall.clicked.connect(self.totalgraph)
        self.Showall.setObjectName("Showall")
        self.gridLayout_2.addWidget(self.Showall, 3, 4, 1, 1)
        self.Smi = QtWidgets.QLabel(self.RTpredict)
        self.Smi.setMinimumSize(QtCore.QSize(0, 50))
        self.Smi.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Smi.setFont(font)
        self.Smi.setObjectName("Smi")
        self.gridLayout_2.addWidget(self.Smi, 7, 1, 1, 1)
        self.Outlierdescription = QtWidgets.QLabel(self.RTpredict)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Outlierdescription.setFont(font)
        self.Outlierdescription.setObjectName("Outlierdescription")
        self.gridLayout_2.addWidget(self.Outlierdescription, 8, 4, 1, 3)
        self.Title = QtWidgets.QLabel(self.RTpredict)
        self.Title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.gridLayout_2.addWidget(self.Title, 1, 2, 1, 4)
        self.Sketcher = QtWebEngineWidgets.QWebEngineView(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sketcher.sizePolicy().hasHeightForWidth())
        self.Sketcher.setSizePolicy(sizePolicy)
        self.Sketcher.setMinimumSize(QtCore.QSize(680, 450))
        self.Sketcher.setMaximumSize(QtCore.QSize(1300, 450))
        self.Sketcher.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Sketcher.setAutoFillBackground(True)
        self.Sketcher.setUrl(QtCore.QUrl("https://pubchem.ncbi.nlm.nih.gov//edit3/index.html"))
        self.Sketcher.setObjectName("Sketcher")
        self.gridLayout_2.addWidget(self.Sketcher, 5, 1, 1, 3)
        self.Outlier = QtWidgets.QLabel(self.RTpredict)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Outlier.setFont(font)
        self.Outlier.setObjectName("Outlier")
        self.gridLayout_2.addWidget(self.Outlier, 7, 4, 1, 2)
        self.Showspecific = QtWidgets.QPushButton(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Showspecific.sizePolicy().hasHeightForWidth())
        self.Showspecific.setSizePolicy(sizePolicy)
        self.Showspecific.setMinimumSize(QtCore.QSize(150, 50))
        self.Showspecific.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Showspecific.setFont(font)
        self.Showspecific.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Showspecific.setAutoFillBackground(True)
        self.Showspecific.clicked.connect(self.specific)
        self.Showspecific.setObjectName("Showspecific")
        self.gridLayout_2.addWidget(self.Showspecific, 3, 6, 1, 1)
        self.plainTextEdit = QtWidgets.QLineEdit(self.RTpredict)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(500, 50))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 3, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 6, 1, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.RTpredict, "")
        self.RTfit = QtWidgets.QWidget()
        self.RTfit.setObjectName("RTfit")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.RTfit)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.KY_fit = QtWidgets.QLabel(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KY_fit.sizePolicy().hasHeightForWidth())
        self.KY_fit.setSizePolicy(sizePolicy)
        self.KY_fit.setMinimumSize(QtCore.QSize(100, 150))
        self.KY_fit.setMaximumSize(QtCore.QSize(230, 160))
        self.KY_fit.setText("")
        self.KY_fit.setPixmap(QtGui.QPixmap("./KY.jpg"))
        self.KY_fit.setObjectName("KY_fit")
        self.gridLayout_4.addWidget(self.KY_fit, 0, 5, 1, 1)
        self.Title_fit = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Title_fit.setFont(font)
        self.Title_fit.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_fit.setObjectName("Title_fit")
        self.gridLayout_4.addWidget(self.Title_fit, 0, 1, 1, 4)
        self.Entermin = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Entermin.setFont(font)
        self.Entermin.setObjectName("Entermin")
        self.gridLayout_4.addWidget(self.Entermin, 4, 5, 1, 1)
        self.InsertRT = QtWidgets.QLineEdit(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InsertRT.sizePolicy().hasHeightForWidth())
        self.InsertRT.setSizePolicy(sizePolicy)
        self.InsertRT.setMinimumSize(QtCore.QSize(0, 40))
        self.InsertRT.setMaximumSize(QtCore.QSize(400, 60))
        self.InsertRT.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.InsertRT.setFont(font)
        self.InsertRT.setObjectName("InsertRT")
        self.gridLayout_4.addWidget(self.InsertRT, 4, 4, 1, 1)
        self.SG_fit = QtWidgets.QLabel(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SG_fit.sizePolicy().hasHeightForWidth())
        self.SG_fit.setSizePolicy(sizePolicy)
        self.SG_fit.setMinimumSize(QtCore.QSize(150, 150))
        self.SG_fit.setMaximumSize(QtCore.QSize(150, 150))
        self.SG_fit.setText("")
        self.SG_fit.setPixmap(QtGui.QPixmap("./SG.png"))
        self.SG_fit.setScaledContents(True)
        self.SG_fit.setObjectName("SG_fit")
        self.gridLayout_4.addWidget(self.SG_fit, 0, 0, 1, 1)
        self.Calculate = QtWidgets.QPushButton(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Calculate.setFont(font)
        self.Calculate.clicked.connect(self.fitrt)
        self.Calculate.setObjectName("Calculate")
        self.gridLayout_4.addWidget(self.Calculate, 5, 4, 1, 1)
        self.FitRT = QtWidgets.QPushButton(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FitRT.sizePolicy().hasHeightForWidth())
        self.FitRT.setSizePolicy(sizePolicy)
        self.FitRT.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FitRT.setFont(font)
        self.FitRT.clicked.connect(self.bringfit)
        self.FitRT.setObjectName("FitRT")
        self.gridLayout_4.addWidget(self.FitRT, 4, 2, 1, 1)
        self.FindRT = QtWidgets.QPushButton(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FindRT.sizePolicy().hasHeightForWidth())
        self.FindRT.setSizePolicy(sizePolicy)
        self.FindRT.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FindRT.setFont(font)
        self.FindRT.clicked.connect(self.findpredrt)
        self.FindRT.setObjectName("FindRT")
        self.gridLayout_4.addWidget(self.FindRT, 4, 0, 1, 1)
        self.Fitfigure = QtWidgets.QWidget(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fitfigure.sizePolicy().hasHeightForWidth())
        self.Fitfigure.setSizePolicy(sizePolicy)
        self.Fitfigure.setMaximumSize(QtCore.QSize(850, 580))
        self.Fitfigure.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fitfigure.setAutoFillBackground(False)

        self.fig2 = plt.Figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.canvas2_toolbar = NavigationToolbar(self.canvas2, self.Fitfigure)
        self.vbox2 = QtWidgets.QVBoxLayout(self.Fitfigure)
        self.vbox2.addWidget(self.canvas2_toolbar)
        self.vbox2.addWidget(self.canvas2)

        self.Fitfigure.setObjectName("Fitfigure")
        self.gridLayout_4.addWidget(self.Fitfigure, 1, 3, 1, 3)
        self.Fittable = QtWidgets.QTableWidget(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fittable.sizePolicy().hasHeightForWidth())
        self.Fittable.setSizePolicy(sizePolicy)
        self.Fittable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Fittable.setFont(font)
        self.Fittable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fittable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Fittable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Fittable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.Fittable.setRowCount(6)
        self.Fittable.setColumnCount(3)
        self.Fittable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)  # 셀 수정 가능하게 변경
        self.Fittable.setHorizontalHeaderLabels(["Metabolite", "Your experimental RT", "Predicted RT"])
        self.Fittable.resizeColumnToContents(3)
        self.Fittable.resizeRowToContents(6)
        self.Fittable.setObjectName("Fittable")
        self.Fittable.horizontalHeader().setCascadingSectionResizes(False)
        self.Fittable.horizontalHeader().setDefaultSectionSize(200)
        self.Fittable.horizontalHeader().setHighlightSections(False)
        self.Fittable.verticalHeader().setCascadingSectionResizes(False)
        self.Fittable.verticalHeader().setDefaultSectionSize(90)
        self.Fittable.verticalHeader().setSortIndicatorShown(False)
        self.Fittable.verticalHeader().setStretchLastSection(False)
        self.gridLayout_4.addWidget(self.Fittable, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 0, 1, 6)
        self.Fitmin = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Fitmin.setFont(font)
        self.Fitmin.setObjectName("Fitmin")
        self.gridLayout_4.addWidget(self.Fitmin, 7, 5, 1, 1)
        self.Fitresult = QtWidgets.QLineEdit(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fitresult.sizePolicy().hasHeightForWidth())
        self.Fitresult.setSizePolicy(sizePolicy)
        self.Fitresult.setMinimumSize(QtCore.QSize(0, 40))
        self.Fitresult.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Fitresult.setFont(font)
        self.Fitresult.setObjectName("Fitresult")
        self.Fitresult.setAlignment(QtCore.Qt.AlignCenter)
        self.Fitresult.setReadOnly(True)
        self.gridLayout_4.addWidget(self.Fitresult, 7, 4, 1, 1)
        self.EnterRT = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.EnterRT.setFont(font)
        self.EnterRT.setAlignment(QtCore.Qt.AlignCenter)
        self.EnterRT.setObjectName("EnterRT")
        self.gridLayout_4.addWidget(self.EnterRT, 4, 3, 1, 1)
        self.FittedRT = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.FittedRT.setFont(font)
        self.FittedRT.setAlignment(QtCore.Qt.AlignCenter)
        self.FittedRT.setObjectName("FittedRT")
        self.gridLayout_4.addWidget(self.FittedRT, 7, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.tabWidget.addTab(self.RTfit, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1573, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def PredictRT(self):  # 입력된 SMILES에서 RT 예측시켜주는 함수.
        smi_enter = self.Insertsmi.text()
        mol_enter = Chem.MolFromSmiles(smi_enter)  # 이 단계에서의 에러 핸들링해야 함
        smi = Chem.MolToSmiles(mol_enter)
        pred_rt = {'Cn1cnc(C[C@H](N)C(=O)O)c1': 7.97,
                   'NCCCN': [3.91, 18.96],
                   'O=C(O)Cc1ccc(O)cc1': 17.19,
                   'N[C@@H](Cc1ccc(O)c(I)c1)C(=O)O': 19.07,
                   'COc1cc(CCN)ccc1O': 24.56,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O': 3.80,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O': 4.48,
                   'N': 9.14,
                   'NCCC(=O)O': 7.35,
                   'CN(CC(O)=O)C(N)=N': 3.58,
                   'O=C(O)C1CCCCN1': 11.48,
                   'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](CO)O2)c(=O)[nH]1': 8.13,
                   'CNC': 14.82,
                   'Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)n1': [4.17, 9.86],
                   'Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1': [2.95, 3.55],
                   'N[C@@H](CCSC[C@H](N)C(=O)O)C(=O)O': [14.23, 14.38],
                   'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1': 8.06,
                   'NCCCC(=O)O': [8.53, 14.80],
                   'COc1cc(CC(=O)O)ccc1O': 17.38,
                   'NCC(=O)O': 6.94,
                   'N=C(N)NCC(=O)O': 3.56,
                   'O=C(O)Cc1cc(O)ccc1O': 22.51,
                   'Nc1nc2c(ncn2[C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': 4.66,
                   'N[C@@H](CCC(=O)O)C(=O)O': [7.56, 10.90],
                   'NCCO': 5.18,
                   'O=C(O)c1cc(O)ccc1O': [17.14, 22.89],
                   'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@@H]2O': 23.24,
                   'Oc1ncnc2nc[nH]c12': [4.05, 9.14, 10.20],
                   'N[C@@H](Cc1ccc(O)cc1)C(=O)O': 21.32,
                   'N[C@@H](Cc1ccccc1)C(=O)O': 13.45,
                   'C[C@H](N)C(=O)O': 7.96,
                   'O=C(O)[C@@H]1CCCN1': 11.17,
                   'CN': 9.92,
                   'C[C@@H](O)[C@H](N)C(=O)O': 6.05,
                   'NC(=O)C[C@H](N)C(=O)O': [4.45, 8.69],
                   'CC[C@H](C)[C@H](N)C(=O)O': 13.63,
                   'N[C@@H](Cc1cnc[nH]1)C(=O)O': 11.6190443,
                   'NCCCC[C@H](N)C(=O)O': 16.02,
                   'N[C@@H](CO)C(=O)O': 4.70,
                   'N[C@@H](CC(=O)O)C(=O)O': 5.64,
                   'N[C@@H](CSSC[C@H](N)C(=O)O)C(=O)O': 14.88,
                   'CC(=O)NCCCC[C@H](N)C(=O)O': 8.10,
                   'CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)O': 11.12,
                   'NCCC[C@H](N)C(=O)O': 16.09,
                   'NCCOP(=O)(O)O': 2.83,
                   'Oc1ccccc1': 23.03,
                   'C[C@H](O)C(=O)C1=Nc2c([nH]c(N)nc2=O)NC1': 7.53,
                   'Cc1ncc(CO)c(CO)c1O': [10.71, 16.75],
                   'NCCS(=O)(=O)O': 4.60,
                   'NCCc1c[nH]c2ccc(O)cc12': 22.52,
                   'Cc1c[nH]c(=O)[nH]c1=O': 12.02,
                   'N[C@@H](Cc1cc(I)c(Oc2ccc(O)c(I)c2)c(I)c1)C(=O)O': 18.60,
                   'CNCC(=O)O': 8.09,
                   'N[C@@H](CCCCN[C@@H](CCC(=O)O)C(=O)O)C(=O)O': [4.83, 8.38],
                   'COc1cc([C@H](O)C(=O)O)ccc1O': [14.58, 18.32],
                   'O=c1[nH]c(=O)c2[nH]cnc2[nH]1': 9.47,
                   'O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': [7.34, 10.93],
                   'O=c1cc[nH]c(=O)[nH]1': 11.04,
                   'O=C(O)/C=C/c1c[nH]cn1': 12.38,
                   'NCCc1c[nH]c2ccccc12': 16.26,
                   'NCCc1ccc(O)cc1': 23.92,
                   'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@H]2O': 23.24,
                   'NC(CP(=O)(O)O)C(=O)O': 3.13,
                   'O=C(O)c1cccc(O)c1O': 17.26,
                   'O=C(O)Cc1cccc(O)c1': 16.92,
                   'CC(=O)N[C@@H](CCCCN)C(=O)O': 7.57,
                   'NC[C@H](O)CC[C@H](N)C(=O)O': 13.26,
                   'CC[C@H](N)C(=O)O': 9.67,
                   'NC(CSCC[C@H](N)C(=O)O)C(=O)O': [14.23, 14.38],
                   'C[C@H](O)[C@H](O)c1c[nH]c2nc(N)nc(=O)c-2n1': 7.25,
                   'O=c1[nH]cc(CO)c(=O)[nH]1': 8.91,
                   'CN(C)c1ncnc2nc[nH]c12': 15.99,
                   'Cn1cncc1C[C@H](N)C(=O)O': 6.88,
                   'CO=C(O)c1ccc(O)c(O)c1': 17.57,
                   'O=C(O)c1ccc(O)cc1': 17.29,
                   'N[C@@H](Cc1c[nH]c2ccc(O)cc12)C(=O)O': 19.96,
                   'N[C@@H](CCCC(=O)O)C(=O)O': 8.30,
                   'N=C(N)NCCC[C@H](N)C(=O)O': 3.84,
                   'CC[C@@H](C)[C@H](N)C(=O)O': 13.63,
                   'N[C@@H](CS)C(=O)O': 10.16,
                   'N[C@H]1[C@H](O)O[C@H](COS(=O)(=O)O)[C@@H](O)[C@@H]1O': 3.36,
                   'CNC[C@H](O)c1ccc(O)c(O)c1': [9.16, 8.85, 9.19],
                   'Nc1ccnc(=O)[nH]1': 9.33,
                   'NC(=O)CC[C@H](N)C(=O)O': 5.94,
                   'CC[C@@H](N)C(=O)O': 9.67,
                   'N[C@@H](Cc1ccc(Oc2ccc(O)cc2)cc1)C(=O)O': 22.48,
                   'O=C(O)Cc1ccccc1O': 16.75,
                   'N=C(N)NCCCC[C@H](N)C(=O)O': 3.41,
                   'NC(CCSSCC[C@H](N)C(=O)O)C(=O)O': 14.35,
                   'NC(=O)NCCCC[C@H](N)C(=O)O': 4.29,
                   'Nc1ccccc1C(=O)C[C@H](N)C(=O)O': [11.60, 14.17],
                   'CC(C)C[C@H](N)C(=O)O': 12.82,
                   'CSCC[C@H](N)C(=O)O': 10.60,
                   'Nc1nc(=O)c2ncc(=O)[nH]c2[nH]1': [10.02, 10.34],
                   'N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 10.41,
                   'O=C(O)CNC(=O)c1ccccc1': 12.05,
                   'O=C(O)[C@@H]1CCCCN1': 11.48,
                   'O=C(O)[C@H](CCO)NO': [6.28, 10.81],
                   'NCC(=O)N1CCC[C@H]1C(=O)O': 7.54,
                   'O=C(O)[C@@H]1C[C@@H](O)CN1': 8.20,
                   'O=C(O)/C=C/c1c[nH]c2ccccc12': 17.85,
                   'O=C(O)C(O)c1cccc(O)c1': [14.54, 22.89],
                   'O=C(O)C(O)Cc1ccc(O)cc1': 14.33,
                   'CC(C)C[C@H](NC(=O)CN)C(=O)O': 10.06,
                   'O=C(O)Cc1c[nH]c2ccc(O)cc12': 14.60,
                   'COc1cc(C(O)CN)ccc1O': 21.35,
                   'O=C(O)CNC(=O)c1ccccc1O': 10.25,
                   'O=C(O)c1cc(O)c2cccc(O)c2n1': [14.24, 23.58],
                   'CC(C)[C@H](N)C(=O)O': 11.23,
                   'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]c1=O': [6.83, 7.77, 10.35],
                   'Cn1cnc2[nH]c(N)nc(=O)c21': 9.64,
                   'NC(=O)NCCC[C@H](N)C(=O)O': 4.11,
                   'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)(O)O)O1': 4.16,
                   'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 12.85,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CSCC[C@H](N)C(=O)O)[C@@H](O)[C@H]1O': 11.23,
                   'COc1cc(/C=C/C(=O)O)ccc1O': 18.57,
                   'COc1ccc(/C=C/C(=O)O)cc1O': 18.42,
                   'Oc1ccccc1O': 26.52,
                   'NCCS(=O)O': 4.89,
                   'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)nc1N': [4.51, 5.28],
                   'CCCCCCC(N)C(=O)O': 14.90,
                   'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]1': 4.15,
                   'N[C@@H](CCC(=O)N[C@@H](CS)C(=O)O)C(=O)O': 8.63,
                   'NCC(O)c1ccccc1': [12.84, 13.16],
                   'Nc1nc(Nc2ccccc2)nc2c1ncn2C1OC(CO)C(O)C1O': 7.45,
                   'Nc1ccccc1C(=O)O': 14.52,
                   'NCC(=O)CCC(=O)O': 8.35,
                   'Nc1ccc(O)cc1': [15.74, 25.02],
                   'CSC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O': 8.38,
                   'Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1': 4.07,
                   'O=[N+]([O-])c1ccc(O)cc1': 23.91,
                   'CC(=O)NCCc1c[nH]c2ccc(O)cc12': 14.05,
                   'N[C@H]1[C@@H](O)O[C@H](COP(=O)(O)O)[C@@H](O)[C@@H]1O': 3.16,
                   'NCCCCNCCCN': 13.04,
                   'O=C(O)Cc1ccc(O)c(O)c1': 22.80,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O': 2.96,
                   'N[C@@H](CCC[C@H](N)C(=O)O)C(=O)O': [14.18, 14.03],
                   'Nc1ccc(C(=O)O)cc1': 13.28,
                   'Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1': 3.51,
                   'COc1ccccc1O': 21.92,
                   'C[N+](C)(C)CCOP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2ccc(N)nc2=O)[C@H](O)[C@@H]1O': [2.95, 3.08],
                   'NCCCCN': 18.92,
                   'Cc1ncc(CO)c(CN)c1O': 21.58,
                   'N=C(N)NCCCCN': [3.56, 14.29],
                   'Nc1c(O)cccc1C(=O)O': 13.80,
                   'CNC(=N)N': [4.12, 21.06],
                   'c1c[nH]cn1': 14.47,
                   'Cc1ncc(CO)c(C=O)c1O': 14.38,
                   'CCCC[C@H](N)C(=O)O': 12.54,
                   'O=C(O)/C=C/c1cccc(O)c1': 19.44,
                   'Nc1nc(N)c2nc(CNc3ccc(C(=O)NC(CCC(=O)O)C(=O)O)cc3)cnc2n1': 8.32,
                   'N=C(N)N': 3.73,
                   'CC(C)NCC(O)COc1cccc2ccccc12': 21.79,
                   'OCCc1c[nH]c2ccc(O)cc12': 14.71,
                   'O=C(O)c1ccc(O)c(O)c1': 23.03,
                   'Cc1ccc(O)cc1': 24.25,
                   'CC(=O)Nc1ccc(O)cc1': 17.02,
                   'Cn1cncc1CCN': 6.92,
                   'O=C(O)C(O)c1ccc(O)c(O)c1': 19.94,
                   'Nc1ccc(C(=O)NCC(=O)O)cc1': 8.80,
                   'COc1ccc(O)c(C(=O)O)c1': 17.74,
                   'NC(Cc1ccc(O)c(Cl)c1)C(=O)O': 20.72,
                   'CN1C2=C(NC=N2)C(=O)N(C)C1=O': 14.64,
                   'Nc1cccc(C(=O)O)c1': 13.64,
                   'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O': 10.78,
                   'O=C(O)c1ccccc1O': 18.05,
                   'NCCCCCC(=O)O': 9.78,
                   'N[C@@H](Cc1ccc(O)c([N+](=O)[O-])c1)C(=O)O': [20.61, 23.10],
                   'CC(C)(N)C(=O)O': 9.42,
                   'NCCCC(O)(P(=O)(O)O)P(=O)(O)O': 2.74,
                   'N[C@@H](Cc1cc(I)c(Oc2cc(I)c(O)c(I)c2)c(I)c1)C(=O)O': 26.03,
                   'CC(C)NCC(O)COc1ccc(CC(N)=O)cc1': 13.14,
                   'COCCc1ccc(OCC(O)CNC(C)C)cc1': 19.68,
                   'CC(C)(C)NCC(O)c1ccc(O)c(CO)c1': [8.39, 11.73],
                   'NCCCC[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O': 8.05,
                   'C[C@@H](N)[C@@H](O)c1ccccc1': 15.13,
                   'CN[C@@H](C)[C@@H](O)c1ccccc1': 18.57,
                   'O=C(O)/C=C/c1ccc(O)c(O)c1': 18.94,
                   'Nc1cccc(C(=O)O)c1O': 13.70,
                   'CS(=O)CC[C@H](N)C(=O)O': [7.68, 7.99],
                   'NC[C@H](N)C(=O)O': 16.45,
                   'CC(N)c1ccccc1': 20.02,
                   'O=C(O)Cc1cnc[nH]1': 10.78,
                   'Cc1cccc(O)c1': 24.04,
                   'Cc1ccccc1O': 23.81,
                   'CC(=O)NCCCCN': 7.76,
                   'COc1cc(C(=O)O)cc(OC)c1O': 17.82732582,
                   'CNc1ncnc2nc[nH]c12': [12.18, 12.84],
                   'CSC[C@@H](N)C(=O)O': 9.48,
                   'Nc1cc(=O)nc(N)[nH]1': 8.54,
                   'CNC(C)(C)C(=O)O': 13.46,
                   'CNC[C@H](O)c1cccc(O)c1': 25.08,
                   'O=C(O)CCc1ccc(O)cc1': 17.16,
                   'N[C@@H](CCS(=O)(=O)O)C(=O)O': 4.74,
                   'NC(C(=O)O)c1ccccc1': 13.58,
                   'NCCCCCN': 18.19,
                   'COc1ccc2[nH]cc(C[C@H](N)C(=O)O)c2c1': 12.06,
                   'NCCC(N)C(=O)O': 16.01,
                   'Cc1cccc(C(=O)O)c1O': 18.40,
                   'CN[C@H](CC(=O)O)C(=O)O': 8.31,
                   'O=C(O)c1ccc(O)nc1': [12.75, 12.47],
                   'O=C1C[C@@H](c2ccc(O)cc2)Oc2cc(O)cc(O)c21': 22.11,
                   'N=C(N)NOCC[C@H](N)C(=O)O': [12.35, 12.30],
                   'NCCS': 11.40,
                   'Nc1ccccc1': 18.31,
                   'N[C@@H](CCCCNC(=O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12)C(=O)O': 7.41,
                   'N=C(N)N[C@@H](CC(=O)O)C(=O)O': 3.48,
                   'O=C(/C=C/c1ccc(O)c(O)c1)O[C@@H]1C[C@](O)(C(=O)O)C[C@@H](O)[C@H]1O': [17.73, 19.18],
                   'Cn1c(N)nc2nc[nH]c2c1=O': 9.94,
                   'O=C(O)c1c[nH]c2ccccc12': 17.28,
                   'CN=C(NC)NCCCC(N)C(=O)O': 3.91,
                   'N[C@@H](CCC(=O)N[C@@H](CSSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O)C(=O)NCC(=O)O)C(=O)O': 14.30,
                   'NO': 9.70,
                   'NCCCCC(=O)O': 8.73,
                   'NC(=O)CC[C@@H](N)C(=O)O': 5.94,
                   'N[C@H](CO)Cc1c[nH]cn1': 7.42,
                   'N=C(N)NCCCC(=O)O': [4.51, 7.04],
                   'N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O': [13.31, 22.61],
                   'CC(C)[C@@H](N)CC(=O)O': [12.16, 17.98],
                   'CC(CN)C(=O)O': [9.21, 14.83],
                   'COc1ccc2[nH]cc(CCN)c2c1': 16.29,
                   'NC(C[Se][Se]CC(N)C(=O)O)C(=O)O': 15.00,
                   'OCCNCCO': 4.60,
                   'Oc1ccc(Cl)cc1Cl': 24.61,
                   'Cc1cc(C(=O)O)ccc1O': 17.89,
                   'NCCCC[C@H](NC(=O)[C@@H](N)CC(=O)O)C(=O)O': 12.22,
                   'CCOC(=O)c1ccc(N)cc1': 16.12,
                   'NC(Cc1ccccc1O)C(=O)O': 21.52,
                   'N[C@@H](Cc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O': 12.92,
                   'N[C@@H](CCC(=O)N[C@@H](CCC(=O)O)C(=O)O)C(=O)O': 5.48,
                   'CC(C)C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 15.85,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 15.57,
                   'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O': 12.68,
                   'CC(C)C[C@H](NC(=O)[C@H](C)N)C(=O)O': 11.43,
                   'C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 12.05,
                   'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 11.60,
                   'C[C@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 20.22,
                   'N=C(N)NCCC[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 6.90,
                   'CCC(C)C(N=C(O)CN)C(=O)O': 11.65,
                   'NCC(O)=NC(Cc1ccccc1)C(=O)O': 9.79,
                   'NCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)O': 10.70,
                   'NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 18.52,
                   'CC(C)[C@H](NC(=O)CN)C(=O)O': 9.44,
                   'C[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O': 11.74,
                   'CC(C)C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O': 14.26,
                   'CC(C)CC(N)C(O)=NC(Cc1c[nH]c2ccccc12)C(=O)O': 14.88,
                   'CC(C)CC(N)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 22.96,
                   'C[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 11.06,
                   'N[C@@H](Cc1ccccc1)C(=O)NCC(=O)O': 9.34,
                   'CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 12.92,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 23.60,
                   'CC(C)[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 14.19,
                   'CC(C)C[C@H](NC(=O)[C@@H](N)CO)C(=O)O': 9.63,
                   'N[C@@H](CO)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 9.83,
                   'CC(C)C[C@H](NC(=O)[C@@H](N)[C@@H](C)O)C(=O)O': 10.46,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(CCC(=O)O)C(=O)O': 9.48,
                   'CC(C)CC(N=C(O)C(N)Cc1c[nH]c2ccccc12)C(=O)O': 14.34,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccccc1)C(=O)O': 14.48,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 23.34,
                   'CC(NC(=O)C(N)Cc1ccc(O)cc1)C(=O)O': 20.05,
                   'N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)O': 18.92,
                   'CC(C)CC(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 22.42,
                   'CC(C)C(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 21.82,
                   'CCc1ccc(O)cc1': 23.82,
                   'O=C(O)c1ccc(O)c(O)c1O': 21.20,
                   'COc1cc(O)cc(OC)c1': 22.15,
                   'COc1ccc(C(=O)O)cc1O': 17.63,
                   'NCC(=O)NCC(=O)NCC(=O)NCC(=O)O': 3.68,
                   'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O': 8.28,
                   'CCCC(NC(=O)CN)C(=O)O': 9.53,
                   'CCCCC(NC(=O)CN)C(=O)O': 10.43,
                   'CC(C)C[C@H](Nc1ccccc1)C(=O)O': 18.91,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 17.57
                   }
        try:
            pred = pred_rt[smi]
        except:
            QtWidgets.QMessageBox.critical(Qt.qApp.activeWindow(), " ", "Please enter the right SMILES")
        else:  # float냐 list에 따라서 달리 처리할 것. string으로 변환시킬 것
            if str(type(pred)) == "<class 'float'>":
                RT_pred = str(pred)
                self.Showpredict.setText(RT_pred)
                self.Showpredict.setAlignment(QtCore.Qt.AlignCenter)
            elif str(type(pred)) == "<class 'list'>":
                RT_pred = " , ".join([str(i) for i in pred])
                self.Showpredict.setText(str(RT_pred))
                self.Showpredict.setAlignment(QtCore.Qt.AlignCenter)
            else:
                QtWidgets.QMessageBox.critical(Qt.qApp.activeWindow(), " ", "Please enter the right SMILES")

    def totalgraph(self):  # 전체 그래프 띄우기

        total = pd.read_csv("RT_predict_confirm.csv")
        exp_tot = total['Experimental_RT']  # 전체 실험값
        pred_tot = total['Predicted_RT']  # 전체 예측값
        Residual = pred_tot - exp_tot

        def outliers_iqr(data):
            q1, q3 = np.percentile(data, [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - (iqr * 1.5)
            upper_bound = q3 + (iqr * 1.5)
            return np.where((data > upper_bound) | (data < lower_bound))

        outlier_index = outliers_iqr(Residual)[0]
        outlier = total.loc[outlier_index, :]
        exp_outlier = outlier['Experimental_RT']
        pred_outlier = outlier['Predicted_RT']
        df = total.drop(outlier_index)

        df_train = df.loc[
                   [11, 5, 3, 4, 0, 7, 6, 18, 8, 2, 1, 22, 36, 39, 20, 13,
                    10, 32, 9, 17, 30, 15, 21, 52, 46, 16, 43, 33, 65, 70, 37,
                    29, 14, 27, 63, 44, 76, 35, 26, 74, 47, 49, 28, 78, 41, 55,
                    80, 95, 88, 53, 58, 64, 51, 83, 62, 57, 66, 79, 68, 98, 71,
                    56, 84, 104, 137, 90, 149, 96, 87, 97, 134, 89, 72, 94, 92,
                    106, 100, 86, 108, 101, 132, 103, 113, 99, 133, 105, 117, 116,
                    120, 154, 115, 124, 129, 126, 138, 111, 107, 140, 171, 136,
                    166, 148, 139, 122, 127, 121, 146, 131, 128, 135, 125, 159, 168,
                    175, 158, 179, 182, 176, 172, 201, 153, 183, 188, 177, 205, 193,
                    180, 169, 181, 151, 143, 191, 190, 165, 144, 160, 157, 200, 189,
                    178, 199, 130, 173, 170, 174, 162, 213, 119, 202, 196, 197, 211,
                    207, 216, 217, 194, 161, 203, 208, 209, 249, 228, 242, 214, 222,
                    198, 259, 219, 236, 232, 244, 230, 239, 218, 224, 220, 204, 231,
                    253, 235, 233, 240, 223, 254, 238, 229, 226, 234, 245, 256, 266,
                    221, 270, 258, 257, 247, 243, 225, 261, 269, 263, 248, 271, 265,
                    260, 252, 255, 293, 268, 272, 267, 279, 275, 283, 273, 297, 277,
                    282, 300, 305, 274, 285, 286, 291, 299, 294, 276, 290, 302, 296,
                    308, 303, 292, 281, 311, 312, 287, 310, 314, 313], :]
        df_test = df.loc[
                  [38, 34, 19, 40, 12, 45, 24, 25, 31, 48, 23, 82, 93, 42, 91, 114, 81, 77,
                   85, 75, 67, 60, 102, 109, 73, 123, 61, 155, 54, 118, 142, 145, 112, 187, 110,
                   164, 156, 167, 206, 185, 210, 186, 141, 212, 227, 251, 237, 280, 241, 298,
                   246, 295, 278, 307, 289, 288, 309, 304, 306, 301], :]

        # train과 test 나눠서 scatter 그리기

        exp_df = df['Experimental_RT']
        pred_df = df['Predicted_RT']

        exp_df_train = df_train['Experimental_RT']
        pred_df_train = df_train['Predicted_RT']

        z = np.polyfit(exp_df_train, pred_df_train, 1)
        p = np.poly1d(z)

        exp_df_test = df_test['Experimental_RT']
        pred_df_test = df_test['Predicted_RT']

        outlier_list = ['3-methyl-histidine', 'L-Histidinol', '1-Methylhistidine', 'L-Histidine', 'Histidinyl-Alanine',
                        'Hippuric acid', 'Alanyl-Histidine', '3-Hydroxyanthranilic acid', 'Xanthurenic acid',
                        'Oxidized glutathione', '2-aminooctanoic acid', 'Cadaverine', 'Caffeic acid', 'Iodotyrosine',
                        'Naringenin']
        # 다시 쓰기 #만일 아웃라이어 smi입력한다면?

        # 아웃라이어는 별도의 산점도로

        self.fig1.clear()

        ax = self.fig1.subplots()
        # 그래프 사이즈 캔버스에 맞게 조정
        ax.text(13, 4, 'y = 0.87 * x + 1.79', color='black', weight='bold', fontsize=15,
                horizontalalignment='center', verticalalignment='bottom')
        ax.text(13, 2, 'Adjusted R square = 0.96', color='black', weight='bold', fontsize=15,
                horizontalalignment='center', verticalalignment='bottom')
        ax.scatter(exp_df_train, pred_df_train, facecolors='none', edgecolors='black', s=20)
        ax.scatter(exp_df_test, pred_df_test, color='blue', s=20)
        ax.scatter(exp_outlier, pred_outlier, color='red', s=20)
        ax.plot(exp_df_train, p(exp_df_train), color='black', linewidth=2, linestyle='--')
        # 아웃라이어 제거. 그 후 무엇이 아웃라이어인지 명시할 것(논문과 프로그램 양쪽)
        # 프로그램은 메시지박스. 논문은 글로 써서 명시
        ax.set_xlim(0, 30)
        ax.set_ylim(0, 30)
        ax.axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.axes.yaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.set_xlabel("Experimental RT")
        ax.set_ylabel("Predicted RT")
        ax.set_title("Experimental RT vs Predicted RT")
        self.fig1.tight_layout()

        self.canvas1.draw()

        cursor1 = mplcursors.cursor(ax.scatter(exp_df_train, pred_df_train, facecolors='none', edgecolors='black', s=20),
                                    hover=True)
        cursor1.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

        cursor2 = mplcursors.cursor(ax.scatter(exp_df_test, pred_df_test, color='blue', s=20), hover=True)
        cursor2.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

        cursor3 = mplcursors.cursor(ax.scatter(exp_outlier, pred_outlier, color='red', s=20), hover=True)
        cursor3.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

    def specific(self):  # 업데이트된 그래프 띄우기. 텍스트 창이 비어있으면 채우라고 메시지 띄우기
        # 키 값을 하나로 통일할 것. smi>키
        # 마우스 커서 혹은 그거와 상관없이 특정 값 좌표 띄우기
        # Dns화 된 이미지도 같이 띄우기>>특정 Dns. Dns 그림 원본을 작고 선명하게 바꾸기
        total = pd.read_csv("RT_predict_confirm.csv")
        exp_tot = total['Experimental_RT']  # 전체 실험값
        pred_tot = total['Predicted_RT']  # 전체 예측값
        exp_rt = {'Cn1cnc(C[C@H](N)C(=O)O)c1': 2.17,
                  'NCCCN': [2.63, 20.49],
                  'O=C(O)Cc1ccc(O)cc1': 16.91,
                  'N[C@@H](Cc1ccc(O)c(I)c1)C(=O)O': 23.88,
                  'COc1cc(CCN)ccc1O': 25.49,
                  'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O': 1.75,
                  'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O': 3.94,
                  'N': 5.82,
                  'NCCC(=O)O': 7.24,
                  'CN(CC(O)=O)C(N)=N': 3.02,
                  'O=C(O)C1CCCCN1': 13.23,
                  'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](CO)O2)c(=O)[nH]1': 8.49,
                  'CNC': 15.07,
                  'Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)n1': [5.87, 7.38],
                  'Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1': [1.88, 2.87],
                  'N[C@@H](CCSC[C@H](N)C(=O)O)C(=O)O': [13.34, 13.69],
                  'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1': 8.72,
                  'NCCCC(=O)O': [7.79, 13.57],
                  'COc1cc(CC(=O)O)ccc1O': 16.51,
                  'NCC(=O)O': 6.59,
                  'N=C(N)NCC(=O)O': 2.74,
                  'O=C(O)Cc1cc(O)ccc1O': 24.84,
                  'Nc1nc2c(ncn2[C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': 2.22,
                  'N[C@@H](CCC(=O)O)C(=O)O': [5.05, 9.46],
                  'NCCO': 6.00,
                  'O=C(O)c1cc(O)ccc1O': [17.11, 24.69],
                  'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@@H]2O': 20.36,
                  'Oc1ncnc2nc[nH]c12': [2.12, 8.73, 9.65],
                  'N[C@@H](Cc1ccc(O)cc1)C(=O)O': 22.65,
                  'N[C@@H](Cc1ccccc1)C(=O)O': 12.74,
                  'C[C@H](N)C(=O)O': 7.57,
                  'O=C(O)[C@@H]1CCCN1': 10.18,
                  'CN': 9.82,
                  'C[C@@H](O)[C@H](N)C(=O)O': 5.79,
                  'NC(=O)C[C@H](N)C(=O)O': [3.00, 6.40],
                  'CC[C@H](C)[C@H](N)C(=O)O': 13.06,
                  'N[C@@H](Cc1cnc[nH]1)C(=O)O': 18.09,
                  'NCCCC[C@H](N)C(=O)O': 17.47,
                  'N[C@@H](CO)C(=O)O': 4.40,
                  'N[C@@H](CC(=O)O)C(=O)O': 5.16,
                  'N[C@@H](CSSC[C@H](N)C(=O)O)C(=O)O': 14.11,
                  'CC(=O)NCCCC[C@H](N)C(=O)O': 5.71,
                  'CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)O': 8.37,
                  'NCCC[C@H](N)C(=O)O': 16.58,
                  'NCCOP(=O)(O)O': 2.02,
                  'Oc1ccccc1': 23.16,
                  'C[C@H](O)C(=O)C1=Nc2c([nH]c(N)nc2=O)NC1': 10.14,
                  'Cc1ncc(CO)c(CO)c1O': [10.12, 18.01],
                  'NCCS(=O)(=O)O': 2.24,
                  'NCCc1c[nH]c2ccc(O)cc12': 24.65,
                  'Cc1c[nH]c(=O)[nH]c1=O': 13.21,
                  'N[C@@H](Cc1cc(I)c(Oc2ccc(O)c(I)c2)c(I)c1)C(=O)O': 19.14,
                  'CNCC(=O)O': 9.34,
                  'N[C@@H](CCCCN[C@@H](CCC(=O)O)C(=O)O)C(=O)O': [2.26, 5.65],
                  'COc1cc([C@H](O)C(=O)O)ccc1O': [12.81, 21.31],
                  'O=c1[nH]c(=O)c2[nH]cnc2[nH]1': 8.95,
                  'O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': [7.84, 8.67],
                  'O=c1cc[nH]c(=O)[nH]1': 11.34,
                  'O=C(O)/C=C/c1c[nH]cn1': 13.52,
                  'NCCc1c[nH]c2ccccc12': 18.03,
                  'NCCc1ccc(O)cc1': 25.83,
                  'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@H]2O': 23.93,
                  'NC(CP(=O)(O)O)C(=O)O': 1.69,
                  'O=C(O)c1cccc(O)c1O': 16.31,
                  'O=C(O)Cc1cccc(O)c1': 16.72,
                  'CC(=O)N[C@@H](CCCCN)C(=O)O': 6.79,
                  'NC[C@H](O)CC[C@H](N)C(=O)O': 13.88,
                  'CC[C@H](N)C(=O)O': 9.13,
                  'NC(CSCC[C@H](N)C(=O)O)C(=O)O': [13.33, 13.61],
                  'C[C@H](O)[C@H](O)c1c[nH]c2nc(N)nc(=O)c-2n1': 6.03,
                  'O=c1[nH]cc(CO)c(=O)[nH]1': 8.87,
                  'CN(C)c1ncnc2nc[nH]c12': 18.56,
                  'Cn1cncc1C[C@H](N)C(=O)O': 2.01,
                  'CO=C(O)c1ccc(O)c(O)c1': 17.34,
                  'O=C(O)c1ccc(O)cc1': 17.57,
                  'N[C@@H](Cc1c[nH]c2ccc(O)cc12)C(=O)O': 20.29,
                  'N[C@@H](CCCC(=O)O)C(=O)O': 5.97,
                  'N=C(N)NCCC[C@H](N)C(=O)O': 2.44,
                  'CC[C@@H](C)[C@H](N)C(=O)O': 13.20,
                  'N[C@@H](CS)C(=O)O': 14.12,
                  'N[C@H]1[C@H](O)O[C@H](COS(=O)(=O)O)[C@@H](O)[C@@H]1O': 1.79,
                  'CNC[C@H](O)c1ccc(O)c(O)c1': [6.19, 7.20, 8.59],
                  'Nc1ccnc(=O)[nH]1': 7.58,
                  'NC(=O)CC[C@H](N)C(=O)O': 3.32,
                  'CC[C@@H](N)C(=O)O': 9.23,
                  'N[C@@H](Cc1ccc(Oc2ccc(O)cc2)cc1)C(=O)O': 25.44,
                  'O=C(O)Cc1ccccc1O': 16.42,
                  'N=C(N)NCCCC[C@H](N)C(=O)O': 3.00,
                  'NC(CCSSCC[C@H](N)C(=O)O)C(=O)O': 15.82,
                  'NC(=O)NCCCC[C@H](N)C(=O)O': 4.47,
                  'Nc1ccccc1C(=O)C[C@H](N)C(=O)O': [11.44, 11.97],
                  'CC(C)C[C@H](N)C(=O)O': 13.36,
                  'CSCC[C@H](N)C(=O)O': 10.89,
                  'Nc1nc(=O)c2ncc(=O)[nH]c2[nH]1': [9.55, 10.82],
                  'N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 10.07,
                  'O=C(O)CNC(=O)c1ccccc1': 7.07,
                  'O=C(O)[C@@H]1CCCCN1': 13.45,
                  'O=C(O)[C@H](CCO)NO': [4.05, 9.26],
                  'NCC(=O)N1CCC[C@H]1C(=O)O': 7.17,
                  'O=C(O)[C@@H]1C[C@@H](O)CN1': 5.17,
                  'O=C(O)/C=C/c1c[nH]c2ccccc12': 20.61,
                  'O=C(O)C(O)c1cccc(O)c1': [12.94, 21.64],
                  'O=C(O)C(O)Cc1ccc(O)cc1': 14.39,
                  'CC(C)C[C@H](NC(=O)CN)C(=O)O': 11.22,
                  'O=C(O)Cc1c[nH]c2ccc(O)cc12': 15.09,
                  'COc1cc(C(O)CN)ccc1O': 23.41,
                  'O=C(O)CNC(=O)c1ccccc1O': 11.05,
                  'O=C(O)c1cc(O)c2cccc(O)c2n1': [9.06, 26.34],
                  'CC(C)[C@H](N)C(=O)O': 10.81,
                  'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]c1=O': [5.85, 8.54, 9.39],
                  'Cn1cnc2[nH]c(N)nc(=O)c21': 10.32,
                  'NC(=O)NCCC[C@H](N)C(=O)O': 3.74,
                  'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)(O)O)O1': 4.58,
                  'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 11.44,
                  'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CSCC[C@H](N)C(=O)O)[C@@H](O)[C@H]1O': 10.52,
                  'COc1cc(/C=C/C(=O)O)ccc1O': 18.47,
                  'COc1ccc(/C=C/C(=O)O)cc1O': 17.49,
                  'Oc1ccccc1O': 26.70,
                  'NCCS(=O)O': 2.47,
                  'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)nc1N': [2.94, 5.98],
                  'CCCCCCC(N)C(=O)O': 19.20,
                  'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]1': 5.57,
                  'N[C@@H](CCC(=O)N[C@@H](CS)C(=O)O)C(=O)O': 8.62,
                  'NCC(O)c1ccccc1': [10.77, 13.77],
                  'Nc1nc(Nc2ccccc2)nc2c1ncn2C1OC(CO)C(O)C1O': 8.73,
                  'Nc1ccccc1C(=O)O': 16.62,
                  'NCC(=O)CCC(=O)O': 7.59,
                  'Nc1ccc(O)cc1': [16.30, 25.04],
                  'CSC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O': 6.97,
                  'Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1': 4.66,
                  'O=[N+]([O-])c1ccc(O)cc1': 23.45,
                  'CC(=O)NCCc1c[nH]c2ccc(O)cc12': 14.32,
                  'N[C@H]1[C@@H](O)O[C@H](COP(=O)(O)O)[C@@H](O)[C@@H]1O': 1.60,
                  'NCCCCNCCCN': 10.54,
                  'O=C(O)Cc1ccc(O)c(O)c1': 23.90,
                  'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O': 1.49,
                  'N[C@@H](CCC[C@H](N)C(=O)O)C(=O)O': [12.30, 12.96],
                  'Nc1ccc(C(=O)O)cc1': 11.52,
                  'Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1': 1.15,
                  'COc1ccccc1O': 22.54,
                  'C[N+](C)(C)CCOP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2ccc(N)nc2=O)[C@H](O)[C@@H]1O': [1.48, 1.28],
                  'NCCCCN': 21.27,
                  'Cc1ncc(CO)c(CN)c1O': 19.47,
                  'N=C(N)NCCCCN': [4.52, 15.28],
                  'Nc1c(O)cccc1C(=O)O': 18.14,
                  'CNC(=N)N': [3.84, 22.52],
                  'c1c[nH]cn1': 14.29,
                  'Cc1ncc(CO)c(C=O)c1O': 12.01,
                  'CCCC[C@H](N)C(=O)O': 14.11,
                  'O=C(O)/C=C/c1cccc(O)c1': 18.51,
                  'Nc1nc(N)c2nc(CNc3ccc(C(=O)NC(CCC(=O)O)C(=O)O)cc3)cnc2n1': 6.06,
                  'N=C(N)N': 3.00,
                  'CC(C)NCC(O)COc1cccc2ccccc12': 24.95,
                  'OCCc1c[nH]c2ccc(O)cc12': 15.55,
                  'O=C(O)c1ccc(O)c(O)c1': 24.51,
                  'Cc1ccc(O)cc1': 24.54,
                  'CC(=O)Nc1ccc(O)cc1': 16.35,
                  'Cn1cncc1CCN': 3.27,
                  'O=C(O)C(O)c1ccc(O)c(O)c1': 21.73,
                  'Nc1ccc(C(=O)NCC(=O)O)cc1': 8.38,
                  'COc1ccc(O)c(C(=O)O)c1': 16.38,
                  'NC(Cc1ccc(O)c(Cl)c1)C(=O)O': 23.57,
                  'CN1C2=C(NC=N2)C(=O)N(C)C1=O': 15.42,
                  'Nc1cccc(C(=O)O)c1': 11.76,
                  'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O': 13.72,
                  'O=C(O)c1ccccc1O': 15.62,
                  'NCCCCCC(=O)O': 10.21,
                  'N[C@@H](Cc1ccc(O)c([N+](=O)[O-])c1)C(=O)O': [22.61, 22.61],
                  'CC(C)(N)C(=O)O': 8.91,
                  'NCCCC(O)(P(=O)(O)O)P(=O)(O)O': 1.59,
                  'N[C@@H](Cc1cc(I)c(Oc2cc(I)c(O)c(I)c2)c(I)c1)C(=O)O': 27.74,
                  'CC(C)NCC(O)COc1ccc(CC(N)=O)cc1': 11.91,
                  'COCCc1ccc(OCC(O)CNC(C)C)cc1': 22.09,
                  'CC(C)(C)NCC(O)c1ccc(O)c(CO)c1': [8.27, 8.42],
                  'NCCCC[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O': 7.68,
                  'C[C@@H](N)[C@@H](O)c1ccccc1': 15.13,
                  'CN[C@@H](C)[C@@H](O)c1ccccc1': 19.38,
                  'O=C(O)/C=C/c1ccc(O)c(O)c1': 24.64,
                  'Nc1cccc(C(=O)O)c1O': 12.22,
                  'CS(=O)CC[C@H](N)C(=O)O': [3.72, 4.20],
                  'NC[C@H](N)C(=O)O': 15.65,
                  'CC(N)c1ccccc1': 18.63,
                  'O=C(O)Cc1cnc[nH]1': 11.12,
                  'Cc1cccc(O)c1': 24.44,
                  'Cc1ccccc1O': 24.60,
                  'CC(=O)NCCCCN': 7.25,
                  'COc1cc(C(=O)O)cc(OC)c1O': 18.10,
                  'CNc1ncnc2nc[nH]c12': [12.22, 12.74],
                  'CSC[C@@H](N)C(=O)O': 9.37,
                  'Nc1cc(=O)nc(N)[nH]1': 8.95,
                  'CNC(C)(C)C(=O)O': 13.65,
                  'CNC[C@H](O)c1cccc(O)c1': 25.39,
                  'O=C(O)CCc1ccc(O)cc1': 18.04,
                  'N[C@@H](CCS(=O)(=O)O)C(=O)O': 1.64,
                  'NC(C(=O)O)c1ccccc1': 11.69,
                  'NCCCCCN': 22.39,
                  'COc1ccc2[nH]cc(C[C@H](N)C(=O)O)c2c1': 9.79,
                  'NCCC(N)C(=O)O': 15.80,
                  'Cc1cccc(C(=O)O)c1O': 16.80,
                  'CN[C@H](CC(=O)O)C(=O)O': 7.53,
                  'O=C(O)c1ccc(O)nc1': [12.21, 15.32],
                  'O=C1C[C@@H](c2ccc(O)cc2)Oc2cc(O)cc(O)c21': 15.29,
                  'N=C(N)NOCC[C@H](N)C(=O)O': [11.37, 11.59],
                  'NCCS': 15.08,
                  'Nc1ccccc1': 17.32,
                  'N[C@@H](CCCCNC(=O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12)C(=O)O': 6.72,
                  'N=C(N)N[C@@H](CC(=O)O)C(=O)O': 2.81,
                  'O=C(/C=C/c1ccc(O)c(O)c1)O[C@@H]1C[C@](O)(C(=O)O)C[C@@H](O)[C@H]1O': [19.45, 21.24],
                  'Cn1c(N)nc2nc[nH]c2c1=O': 9.57,
                  'O=C(O)c1c[nH]c2ccccc12': 19.27,
                  'CN=C(NC)NCCCC(N)C(=O)O': 3.05,
                  'N[C@@H](CCC(=O)N[C@@H](CSSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O)C(=O)NCC(=O)O)C(=O)O': 8.07,
                  'NO': 12.02,
                  'NCCCCC(=O)O': 8.68,
                  'NC(=O)CC[C@@H](N)C(=O)O': 3.32,
                  'N[C@H](CO)Cc1c[nH]cn1': 1.44,
                  'N=C(N)NCCCC(=O)O': [3.65, 11.00],
                  'N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O': [11.82, 24.18],
                  'CC(C)[C@@H](N)CC(=O)O': [10.78, 20.77],
                  'CC(CN)C(=O)O': [8.67, 16.29],
                  'COc1ccc2[nH]cc(CCN)c2c1': 16.52,
                  'NC(C[Se][Se]CC(N)C(=O)O)C(=O)O': 15.09,
                  'OCCNCCO': 5.49,
                  'Oc1ccc(Cl)cc1Cl': 26.30,
                  'Cc1cc(C(=O)O)ccc1O': 19.43,
                  'NCCCC[C@H](NC(=O)[C@@H](N)CC(=O)O)C(=O)O': 13.61,
                  'CCOC(=O)c1ccc(N)cc1': 20.08,
                  'NC(Cc1ccccc1O)C(=O)O': 22.38,
                  'N[C@@H](Cc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O': 13.13,
                  'N[C@@H](CCC(=O)N[C@@H](CCC(=O)O)C(=O)O)C(=O)O': 3.44,
                  'CC(C)C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 16.59,
                  'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 16.55,
                  'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O': 17.62,
                  'CC(C)C[C@H](NC(=O)[C@H](C)N)C(=O)O': 11.36,
                  'C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 12.11,
                  'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 11.09,
                  'C[C@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 21.85,
                  'N=C(N)NCCC[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 6.80,
                  'CCC(C)C(N=C(O)CN)C(=O)O': 10.78,
                  'NCC(O)=NC(Cc1ccccc1)C(=O)O': 11.65,
                  'NCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)O': 11.19,
                  'NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 21.63,
                  'CC(C)[C@H](NC(=O)CN)C(=O)O': 9.19,
                  'C[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O': 16.69,
                  'CC(C)C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O': 12.99,
                  'CC(C)CC(N)C(O)=NC(Cc1c[nH]c2ccccc12)C(=O)O': 15.77,
                  'CC(C)CC(N)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 23.98,
                  'C[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 10.58,
                  'N[C@@H](Cc1ccccc1)C(=O)NCC(=O)O': 9.43,
                  'CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 13.87,
                  'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 24.22,
                  'CC(C)[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 13.62,
                  'CC(C)C[C@H](NC(=O)[C@@H](N)CO)C(=O)O': 8.90,
                  'N[C@@H](CO)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 9.38,
                  'CC(C)C[C@H](NC(=O)[C@@H](N)[C@@H](C)O)C(=O)O': 10.18,
                  'NC(Cc1c[nH]c2ccccc12)C(=O)NC(CCC(=O)O)C(=O)O': 8.29,
                  'CC(C)CC(N=C(O)C(N)Cc1c[nH]c2ccccc12)C(=O)O': 14.60,
                  'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccccc1)C(=O)O': 15.36,
                  'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 23.25,
                  'CC(NC(=O)C(N)Cc1ccc(O)cc1)C(=O)O': 20.86,
                  'N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)O': 20.19,
                  'CC(C)CC(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 23.77,
                  'CC(C)C(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 22.83,
                  'CCc1ccc(O)cc1': 25.63,
                  'O=C(O)c1ccc(O)c(O)c1O': 24.10,
                  'COc1cc(O)cc(OC)c1': 23.75,
                  'COc1ccc(C(=O)O)cc1O': 15.69,
                  'NCC(=O)NCC(=O)NCC(=O)NCC(=O)O': 3.39,
                  'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O': 7.60,
                  'CCCC(NC(=O)CN)C(=O)O': 9.51,
                  'CCCCC(NC(=O)CN)C(=O)O': 11.36,
                  'CC(C)C[C@H](Nc1ccccc1)C(=O)O': 15.90,
                  'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 19.95}
        smi_enter2 = self.plainTextEdit.text()
        mol_enter2 = Chem.MolFromSmiles(smi_enter2)
        smi2 = Chem.MolToSmiles(mol_enter2)
        print(smi2)
        exp = exp_rt[smi2]
        pred_rt = {'Cn1cnc(C[C@H](N)C(=O)O)c1': 7.97,
                   'NCCCN': [3.91, 18.96],
                   'O=C(O)Cc1ccc(O)cc1': 17.19,
                   'N[C@@H](Cc1ccc(O)c(I)c1)C(=O)O': 19.07,
                   'COc1cc(CCN)ccc1O': 24.56,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O': 3.80,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O': 4.48,
                   'N': 9.14,
                   'NCCC(=O)O': 7.35,
                   'CN(CC(O)=O)C(N)=N': 3.58,
                   'O=C(O)C1CCCCN1': 11.48,
                   'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](CO)O2)c(=O)[nH]1': 8.13,
                   'CNC': 14.82,
                   'Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)n1': [4.17, 9.86],
                   'Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1': [2.95, 3.55],
                   'N[C@@H](CCSC[C@H](N)C(=O)O)C(=O)O': [14.23, 14.38],
                   'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1': 8.06,
                   'NCCCC(=O)O': [8.53, 14.80],
                   'COc1cc(CC(=O)O)ccc1O': 17.38,
                   'NCC(=O)O': 6.94,
                   'N=C(N)NCC(=O)O': 3.56,
                   'O=C(O)Cc1cc(O)ccc1O': 22.51,
                   'Nc1nc2c(ncn2[C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': 4.66,
                   'N[C@@H](CCC(=O)O)C(=O)O': [7.56, 10.90],
                   'NCCO': 5.18,
                   'O=C(O)c1cc(O)ccc1O': [17.14, 22.89],
                   'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@@H]2O': 23.24,
                   'Oc1ncnc2nc[nH]c12': [4.05, 9.14, 10.20],
                   'N[C@@H](Cc1ccc(O)cc1)C(=O)O': 21.32,
                   'N[C@@H](Cc1ccccc1)C(=O)O': 13.45,
                   'C[C@H](N)C(=O)O': 7.96,
                   'O=C(O)[C@@H]1CCCN1': 11.17,
                   'CN': 9.92,
                   'C[C@@H](O)[C@H](N)C(=O)O': 6.05,
                   'NC(=O)C[C@H](N)C(=O)O': [4.45, 8.69],
                   'CC[C@H](C)[C@H](N)C(=O)O': 13.63,
                   'N[C@@H](Cc1cnc[nH]1)C(=O)O': 11.6190443,
                   'NCCCC[C@H](N)C(=O)O': 16.02,
                   'N[C@@H](CO)C(=O)O': 4.70,
                   'N[C@@H](CC(=O)O)C(=O)O': 5.64,
                   'N[C@@H](CSSC[C@H](N)C(=O)O)C(=O)O': 14.88,
                   'CC(=O)NCCCC[C@H](N)C(=O)O': 8.10,
                   'CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)O': 11.12,
                   'NCCC[C@H](N)C(=O)O': 16.09,
                   'NCCOP(=O)(O)O': 2.83,
                   'Oc1ccccc1': 23.03,
                   'C[C@H](O)C(=O)C1=Nc2c([nH]c(N)nc2=O)NC1': 7.53,
                   'Cc1ncc(CO)c(CO)c1O': [10.71, 16.75],
                   'NCCS(=O)(=O)O': 4.60,
                   'NCCc1c[nH]c2ccc(O)cc12': 22.52,
                   'Cc1c[nH]c(=O)[nH]c1=O': 12.02,
                   'N[C@@H](Cc1cc(I)c(Oc2ccc(O)c(I)c2)c(I)c1)C(=O)O': 18.60,
                   'CNCC(=O)O': 8.09,
                   'N[C@@H](CCCCN[C@@H](CCC(=O)O)C(=O)O)C(=O)O': [4.83, 8.38],
                   'COc1cc([C@H](O)C(=O)O)ccc1O': [14.58, 18.32],
                   'O=c1[nH]c(=O)c2[nH]cnc2[nH]1': 9.47,
                   'O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': [7.34, 10.93],
                   'O=c1cc[nH]c(=O)[nH]1': 11.04,
                   'O=C(O)/C=C/c1c[nH]cn1': 12.38,
                   'NCCc1c[nH]c2ccccc12': 16.26,
                   'NCCc1ccc(O)cc1': 23.92,
                   'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@H]2O': 23.24,
                   'NC(CP(=O)(O)O)C(=O)O': 3.13,
                   'O=C(O)c1cccc(O)c1O': 17.26,
                   'O=C(O)Cc1cccc(O)c1': 16.92,
                   'CC(=O)N[C@@H](CCCCN)C(=O)O': 7.57,
                   'NC[C@H](O)CC[C@H](N)C(=O)O': 13.26,
                   'CC[C@H](N)C(=O)O': 9.67,
                   'NC(CSCC[C@H](N)C(=O)O)C(=O)O': [14.23, 14.38],
                   'C[C@H](O)[C@H](O)c1c[nH]c2nc(N)nc(=O)c-2n1': 7.25,
                   'O=c1[nH]cc(CO)c(=O)[nH]1': 8.91,
                   'CN(C)c1ncnc2nc[nH]c12': 15.99,
                   'Cn1cncc1C[C@H](N)C(=O)O': 6.88,
                   'CO=C(O)c1ccc(O)c(O)c1': 17.57,
                   'O=C(O)c1ccc(O)cc1': 17.29,
                   'N[C@@H](Cc1c[nH]c2ccc(O)cc12)C(=O)O': 19.96,
                   'N[C@@H](CCCC(=O)O)C(=O)O': 8.30,
                   'N=C(N)NCCC[C@H](N)C(=O)O': 3.84,
                   'CC[C@@H](C)[C@H](N)C(=O)O': 13.63,
                   'N[C@@H](CS)C(=O)O': 10.16,
                   'N[C@H]1[C@H](O)O[C@H](COS(=O)(=O)O)[C@@H](O)[C@@H]1O': 3.36,
                   'CNC[C@H](O)c1ccc(O)c(O)c1': [9.16, 8.85, 9.19],
                   'Nc1ccnc(=O)[nH]1': 9.33,
                   'NC(=O)CC[C@H](N)C(=O)O': 5.94,
                   'CC[C@@H](N)C(=O)O': 9.67,
                   'N[C@@H](Cc1ccc(Oc2ccc(O)cc2)cc1)C(=O)O': 22.48,
                   'O=C(O)Cc1ccccc1O': 16.75,
                   'N=C(N)NCCCC[C@H](N)C(=O)O': 3.41,
                   'NC(CCSSCC[C@H](N)C(=O)O)C(=O)O': 14.35,
                   'NC(=O)NCCCC[C@H](N)C(=O)O': 4.29,
                   'Nc1ccccc1C(=O)C[C@H](N)C(=O)O': [11.60, 14.17],
                   'CC(C)C[C@H](N)C(=O)O': 12.82,
                   'CSCC[C@H](N)C(=O)O': 10.60,
                   'Nc1nc(=O)c2ncc(=O)[nH]c2[nH]1': [10.02, 10.34],
                   'N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 10.41,
                   'O=C(O)CNC(=O)c1ccccc1': 12.05,
                   'O=C(O)[C@@H]1CCCCN1': 11.48,
                   'O=C(O)[C@H](CCO)NO': [6.28, 10.81],
                   'NCC(=O)N1CCC[C@H]1C(=O)O': 7.54,
                   'O=C(O)[C@@H]1C[C@@H](O)CN1': 8.20,
                   'O=C(O)/C=C/c1c[nH]c2ccccc12': 17.85,
                   'O=C(O)C(O)c1cccc(O)c1': [14.54, 22.89],
                   'O=C(O)C(O)Cc1ccc(O)cc1': 14.33,
                   'CC(C)C[C@H](NC(=O)CN)C(=O)O': 10.06,
                   'O=C(O)Cc1c[nH]c2ccc(O)cc12': 14.60,
                   'COc1cc(C(O)CN)ccc1O': 21.35,
                   'O=C(O)CNC(=O)c1ccccc1O': 10.25,
                   'O=C(O)c1cc(O)c2cccc(O)c2n1': [14.24, 23.58],
                   'CC(C)[C@H](N)C(=O)O': 11.23,
                   'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]c1=O': [6.83, 7.77, 10.35],
                   'Cn1cnc2[nH]c(N)nc(=O)c21': 9.64,
                   'NC(=O)NCCC[C@H](N)C(=O)O': 4.11,
                   'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)(O)O)O1': 4.16,
                   'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 12.85,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CSCC[C@H](N)C(=O)O)[C@@H](O)[C@H]1O': 11.23,
                   'COc1cc(/C=C/C(=O)O)ccc1O': 18.57,
                   'COc1ccc(/C=C/C(=O)O)cc1O': 18.42,
                   'Oc1ccccc1O': 26.52,
                   'NCCS(=O)O': 4.89,
                   'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)nc1N': [4.51, 5.28],
                   'CCCCCCC(N)C(=O)O': 14.90,
                   'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]1': 4.15,
                   'N[C@@H](CCC(=O)N[C@@H](CS)C(=O)O)C(=O)O': 8.63,
                   'NCC(O)c1ccccc1': [12.84, 13.16],
                   'Nc1nc(Nc2ccccc2)nc2c1ncn2C1OC(CO)C(O)C1O': 7.45,
                   'Nc1ccccc1C(=O)O': 14.52,
                   'NCC(=O)CCC(=O)O': 8.35,
                   'Nc1ccc(O)cc1': [15.74, 25.02],
                   'CSC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O': 8.38,
                   'Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1': 4.07,
                   'O=[N+]([O-])c1ccc(O)cc1': 23.91,
                   'CC(=O)NCCc1c[nH]c2ccc(O)cc12': 14.05,
                   'N[C@H]1[C@@H](O)O[C@H](COP(=O)(O)O)[C@@H](O)[C@@H]1O': 3.16,
                   'NCCCCNCCCN': 13.04,
                   'O=C(O)Cc1ccc(O)c(O)c1': 22.80,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O': 2.96,
                   'N[C@@H](CCC[C@H](N)C(=O)O)C(=O)O': [14.18, 14.03],
                   'Nc1ccc(C(=O)O)cc1': 13.28,
                   'Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1': 3.51,
                   'COc1ccccc1O': 21.92,
                   'C[N+](C)(C)CCOP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2ccc(N)nc2=O)[C@H](O)[C@@H]1O': [2.95, 3.08],
                   'NCCCCN': 18.92,
                   'Cc1ncc(CO)c(CN)c1O': 21.58,
                   'N=C(N)NCCCCN': [3.56, 14.29],
                   'Nc1c(O)cccc1C(=O)O': 13.80,
                   'CNC(=N)N': [4.12, 21.06],
                   'c1c[nH]cn1': 14.47,
                   'Cc1ncc(CO)c(C=O)c1O': 14.38,
                   'CCCC[C@H](N)C(=O)O': 12.54,
                   'O=C(O)/C=C/c1cccc(O)c1': 19.44,
                   'Nc1nc(N)c2nc(CNc3ccc(C(=O)NC(CCC(=O)O)C(=O)O)cc3)cnc2n1': 8.32,
                   'N=C(N)N': 3.73,
                   'CC(C)NCC(O)COc1cccc2ccccc12': 21.79,
                   'OCCc1c[nH]c2ccc(O)cc12': 14.71,
                   'O=C(O)c1ccc(O)c(O)c1': 23.03,
                   'Cc1ccc(O)cc1': 24.25,
                   'CC(=O)Nc1ccc(O)cc1': 17.02,
                   'Cn1cncc1CCN': 6.92,
                   'O=C(O)C(O)c1ccc(O)c(O)c1': 19.94,
                   'Nc1ccc(C(=O)NCC(=O)O)cc1': 8.80,
                   'COc1ccc(O)c(C(=O)O)c1': 17.74,
                   'NC(Cc1ccc(O)c(Cl)c1)C(=O)O': 20.72,
                   'CN1C2=C(NC=N2)C(=O)N(C)C1=O': 14.64,
                   'Nc1cccc(C(=O)O)c1': 13.64,
                   'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O': 10.78,
                   'O=C(O)c1ccccc1O': 18.05,
                   'NCCCCCC(=O)O': 9.78,
                   'N[C@@H](Cc1ccc(O)c([N+](=O)[O-])c1)C(=O)O': [20.61, 23.10],
                   'CC(C)(N)C(=O)O': 9.42,
                   'NCCCC(O)(P(=O)(O)O)P(=O)(O)O': 2.74,
                   'N[C@@H](Cc1cc(I)c(Oc2cc(I)c(O)c(I)c2)c(I)c1)C(=O)O': 26.03,
                   'CC(C)NCC(O)COc1ccc(CC(N)=O)cc1': 13.14,
                   'COCCc1ccc(OCC(O)CNC(C)C)cc1': 19.68,
                   'CC(C)(C)NCC(O)c1ccc(O)c(CO)c1': [8.39, 11.73],
                   'NCCCC[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O': 8.05,
                   'C[C@@H](N)[C@@H](O)c1ccccc1': 15.13,
                   'CN[C@@H](C)[C@@H](O)c1ccccc1': 18.57,
                   'O=C(O)/C=C/c1ccc(O)c(O)c1': 18.94,
                   'Nc1cccc(C(=O)O)c1O': 13.70,
                   'CS(=O)CC[C@H](N)C(=O)O': [7.68, 7.99],
                   'NC[C@H](N)C(=O)O': 16.45,
                   'CC(N)c1ccccc1': 20.02,
                   'O=C(O)Cc1cnc[nH]1': 10.78,
                   'Cc1cccc(O)c1': 24.04,
                   'Cc1ccccc1O': 23.81,
                   'CC(=O)NCCCCN': 7.76,
                   'COc1cc(C(=O)O)cc(OC)c1O': 17.82732582,
                   'CNc1ncnc2nc[nH]c12': [12.18, 12.84],
                   'CSC[C@@H](N)C(=O)O': 9.48,
                   'Nc1cc(=O)nc(N)[nH]1': 8.54,
                   'CNC(C)(C)C(=O)O': 13.46,
                   'CNC[C@H](O)c1cccc(O)c1': 25.08,
                   'O=C(O)CCc1ccc(O)cc1': 17.16,
                   'N[C@@H](CCS(=O)(=O)O)C(=O)O': 4.74,
                   'NC(C(=O)O)c1ccccc1': 13.58,
                   'NCCCCCN': 18.19,
                   'COc1ccc2[nH]cc(C[C@H](N)C(=O)O)c2c1': 12.06,
                   'NCCC(N)C(=O)O': 16.01,
                   'Cc1cccc(C(=O)O)c1O': 18.40,
                   'CN[C@H](CC(=O)O)C(=O)O': 8.31,
                   'O=C(O)c1ccc(O)nc1': [12.75, 12.47],
                   'O=C1C[C@@H](c2ccc(O)cc2)Oc2cc(O)cc(O)c21': 22.11,
                   'N=C(N)NOCC[C@H](N)C(=O)O': [12.35, 12.30],
                   'NCCS': 11.40,
                   'Nc1ccccc1': 18.31,
                   'N[C@@H](CCCCNC(=O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12)C(=O)O': 7.41,
                   'N=C(N)N[C@@H](CC(=O)O)C(=O)O': 3.48,
                   'O=C(/C=C/c1ccc(O)c(O)c1)O[C@@H]1C[C@](O)(C(=O)O)C[C@@H](O)[C@H]1O': [17.73, 19.18],
                   'Cn1c(N)nc2nc[nH]c2c1=O': 9.94,
                   'O=C(O)c1c[nH]c2ccccc12': 17.28,
                   'CN=C(NC)NCCCC(N)C(=O)O': 3.91,
                   'N[C@@H](CCC(=O)N[C@@H](CSSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O)C(=O)NCC(=O)O)C(=O)O': 14.30,
                   'NO': 9.70,
                   'NCCCCC(=O)O': 8.73,
                   'NC(=O)CC[C@@H](N)C(=O)O': 5.94,
                   'N[C@H](CO)Cc1c[nH]cn1': 7.42,
                   'N=C(N)NCCCC(=O)O': [4.51, 7.04],
                   'N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O': [13.31, 22.61],
                   'CC(C)[C@@H](N)CC(=O)O': [12.16, 17.98],
                   'CC(CN)C(=O)O': [9.21, 14.83],
                   'COc1ccc2[nH]cc(CCN)c2c1': 16.29,
                   'NC(C[Se][Se]CC(N)C(=O)O)C(=O)O': 15.00,
                   'OCCNCCO': 4.60,
                   'Oc1ccc(Cl)cc1Cl': 24.61,
                   'Cc1cc(C(=O)O)ccc1O': 17.89,
                   'NCCCC[C@H](NC(=O)[C@@H](N)CC(=O)O)C(=O)O': 12.22,
                   'CCOC(=O)c1ccc(N)cc1': 16.12,
                   'NC(Cc1ccccc1O)C(=O)O': 21.52,
                   'N[C@@H](Cc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O': 12.92,
                   'N[C@@H](CCC(=O)N[C@@H](CCC(=O)O)C(=O)O)C(=O)O': 5.48,
                   'CC(C)C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 15.85,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 15.57,
                   'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O': 12.68,
                   'CC(C)C[C@H](NC(=O)[C@H](C)N)C(=O)O': 11.43,
                   'C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 12.05,
                   'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 11.60,
                   'C[C@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 20.22,
                   'N=C(N)NCCC[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 6.90,
                   'CCC(C)C(N=C(O)CN)C(=O)O': 11.65,
                   'NCC(O)=NC(Cc1ccccc1)C(=O)O': 9.79,
                   'NCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)O': 10.70,
                   'NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 18.52,
                   'CC(C)[C@H](NC(=O)CN)C(=O)O': 9.44,
                   'C[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O': 11.74,
                   'CC(C)C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O': 14.26,
                   'CC(C)CC(N)C(O)=NC(Cc1c[nH]c2ccccc12)C(=O)O': 14.88,
                   'CC(C)CC(N)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 22.96,
                   'C[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 11.06,
                   'N[C@@H](Cc1ccccc1)C(=O)NCC(=O)O': 9.34,
                   'CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 12.92,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 23.60,
                   'CC(C)[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 14.19,
                   'CC(C)C[C@H](NC(=O)[C@@H](N)CO)C(=O)O': 9.63,
                   'N[C@@H](CO)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 9.83,
                   'CC(C)C[C@H](NC(=O)[C@@H](N)[C@@H](C)O)C(=O)O': 10.46,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(CCC(=O)O)C(=O)O': 9.48,
                   'CC(C)CC(N=C(O)C(N)Cc1c[nH]c2ccccc12)C(=O)O': 14.34,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccccc1)C(=O)O': 14.48,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 23.34,
                   'CC(NC(=O)C(N)Cc1ccc(O)cc1)C(=O)O': 20.05,
                   'N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)O': 18.92,
                   'CC(C)CC(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 22.42,
                   'CC(C)C(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 21.82,
                   'CCc1ccc(O)cc1': 23.82,
                   'O=C(O)c1ccc(O)c(O)c1O': 21.20,
                   'COc1cc(O)cc(OC)c1': 22.15,
                   'COc1ccc(C(=O)O)cc1O': 17.63,
                   'NCC(=O)NCC(=O)NCC(=O)NCC(=O)O': 3.68,
                   'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O': 8.28,
                   'CCCC(NC(=O)CN)C(=O)O': 9.53,
                   'CCCCC(NC(=O)CN)C(=O)O': 10.43,
                   'CC(C)C[C@H](Nc1ccccc1)C(=O)O': 18.91,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 17.57
                   }
        pred = pred_rt[smi2]

        Dns_struct = {'Cn1cnc(C[C@H](N)C(=O)O)c1': './Dnspng/1-Methylhistidine.png',
                      'NCCCN': ['./Dnspng/1,3-Diaminopropane.png', './Dnspng/1,3-Diaminopropane_multi_tags.png'],
                      'O=C(O)Cc1ccc(O)cc1': './Dnspng/p-Hydroxyphenylacetic_acid.png',
                      'N[C@@H](Cc1ccc(O)c(I)c1)C(=O)O': './Dnspng/Iodotyrosine.png',
                      'COc1cc(CCN)ccc1O': './Dnspng/3-Methoxytyramine.png',
                      'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O': './Dnspng/Adenosine_monophosphate.png',
                      'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O': './Dnspng/Adenosine.png',
                      'N': './Dnspng/Ammonia.png',
                      'NCCC(=O)O': './Dnspng/Beta-Alanine.png',
                      'CN(CC(O)=O)C(N)=N': './Dnspng/Creatine.png',
                      'O=C(O)C1CCCCN1': './Dnspng/D-Pipecolic_acid.png',
                      'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](CO)O2)c(=O)[nH]1': './Dnspng/Deoxyguanosine.png',
                      'CNC': './Dnspng/Dimethylamine.png',
                      'Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)n1': ['./Dnspng/Cytidine.png',
                                                                           './Dnspng/Cytidine-H2O.png'],
                      'Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1': [
                          './Dnspng/Cytidine_monophosphate.png', './Dnspng/Cytidine_monophosphate_Isomer.png'],
                      'N[C@@H](CCSC[C@H](N)C(=O)O)C(=O)O': ['./Dnspng/L-Cystathionine.png',
                                                            './Dnspng/L-Cystathionine_Isomer.png'],
                      'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1': './Dnspng/Deoxyadenosinee.png',
                      'NCCCC(=O)O': ['./Dnspng/Gamma-Aminobutyric_acid.png',
                                     './Dnspng/Gamma-Aminobutyric_acid-H2O.png'],
                      'COc1cc(CC(=O)O)ccc1O': './Dnspng/Homovanillic_acid.png',
                      'NCC(=O)O': './Dnspng/Glycine.png',
                      'N=C(N)NCC(=O)O': './Dnspng/Guanidoacetic_acid.png',
                      'O=C(O)Cc1cc(O)ccc1O': './Dnspng/Homogentisic_acid.png',
                      'Nc1nc2c(ncn2[C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': './Dnspng/Guanosine.png',
                      'N[C@@H](CCC(=O)O)C(=O)O': ['./Dnspng/L-Glutamic_Acid.png', './Dnspng/L-Glutamic_Acid-H2O.png'],
                      'NCCO': './Dnspng/Ethanolamine.png',
                      'O=C(O)c1cc(O)ccc1O': ['./Dnspng/Gentisic_acid.png', './Dnspng/Gentisic_acid_multi_tags.png'],
                      'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@@H]2O': './Dnspng/Estriol.png',
                      'Oc1ncnc2nc[nH]c12': ['./Dnspng/Hypoxanthine+H2O.png', './Dnspng/Hypoxanthine_multi_tags.png',
                                            './Dnspng/Hypoxanthine_Isomer.png'],
                      'N[C@@H](Cc1ccc(O)cc1)C(=O)O': './Dnspng/L-Tyrosine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)O': './Dnspng/L-Phenylalanine.png',
                      'C[C@H](N)C(=O)O': './Dnspng/L-Alanine.png',
                      'O=C(O)[C@@H]1CCCN1': './Dnspng/L-Proline.png',
                      'CN': './Dnspng/Methylamine.png',
                      'C[C@@H](O)[C@H](N)C(=O)O': './Dnspng/L-Threonine.png',
                      'NC(=O)C[C@H](N)C(=O)O': ['./Dnspng/L-Asparagine.png', './Dnspng/L-Asparagine-H2O.png'],
                      'CC[C@H](C)[C@H](N)C(=O)O': './Dnspng/L-Isoleucine.png',
                      'N[C@@H](Cc1cnc[nH]1)C(=O)O': './Dnspng/L-Histidine.png',
                      'NCCCC[C@H](N)C(=O)O': './Dnspng/L-Lysine.png',
                      'N[C@@H](CO)C(=O)O': './Dnspng/L-Serine.png',
                      'N[C@@H](CC(=O)O)C(=O)O': './Dnspng/L-Aspartic_Acid.png',
                      'N[C@@H](CSSC[C@H](N)C(=O)O)C(=O)O': './Dnspng/L-Cystine.png',
                      'CC(=O)NCCCC[C@H](N)C(=O)O': './Dnspng/N6-Acetyl-L-Lysine.png',
                      'CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)O': './Dnspng/Pantothenic_acid.png',
                      'NCCC[C@H](N)C(=O)O': './Dnspng/Ornithine.png',
                      'NCCOP(=O)(O)O': './Dnspng/O-Phosphoethanolamine.png',
                      'Oc1ccccc1': './Dnspng/Phenol.png',
                      'C[C@H](O)C(=O)C1=Nc2c([nH]c(N)nc2=O)NC1': './Dnspng/Sepiapterin.png',
                      'Cc1ncc(CO)c(CO)c1O': ['./Dnspng/Pyridoxine.png', './Dnspng/Pyridoxine-H2O.png'],
                      'NCCS(=O)(=O)O': './Dnspng/Taurine.png',
                      'NCCc1c[nH]c2ccc(O)cc12': './Dnspng/Serotonin.png',
                      'Cc1c[nH]c(=O)[nH]c1=O': './Dnspng/Thymine.png',
                      'N[C@@H](Cc1cc(I)c(Oc2ccc(O)c(I)c2)c(I)c1)C(=O)O': './Dnspng/Liothyronine.png',
                      'CNCC(=O)O': './Dnspng/Sarcosine.png',
                      'N[C@@H](CCCCN[C@@H](CCC(=O)O)C(=O)O)C(=O)O': ['./Dnspng/Saccharopine.png',
                                                                     './Dnspng/Saccharopine-H2O.png'],
                      'COc1cc([C@H](O)C(=O)O)ccc1O': ['./Dnspng/Vanillylmandelic_acid.png',
                                                      './Dnspng/Vanillylmandelic_acid-H2O.png'],
                      'O=c1[nH]c(=O)c2[nH]cnc2[nH]1': './Dnspng/Xanthine.png',
                      'O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': ['./Dnspng/Uridine.png',
                                                                               './Dnspng/Uridine-H2O.png'],
                      'O=c1cc[nH]c(=O)[nH]1': './Dnspng/Uracil.png',
                      'O=C(O)/C=C/c1c[nH]cn1': './Dnspng/Urocanic_acid.png',
                      'NCCc1c[nH]c2ccccc12': './Dnspng/Tryptamine.png',
                      'NCCc1ccc(O)cc1': './Dnspng/Tyramine.png',
                      'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@H]2O': './Dnspng/17-Epiestriol.png',
                      'NC(CP(=O)(O)O)C(=O)O': './Dnspng/2-Amino-3-phosphonopropionic_acid.png',
                      'O=C(O)c1cccc(O)c1O': './Dnspng/2-Pyrocatechuic_acid.png',
                      'O=C(O)Cc1cccc(O)c1': './Dnspng/3-Hydroxyphenylacetic_acid.png',
                      'CC(=O)N[C@@H](CCCCN)C(=O)O': './Dnspng/N-Alpha-acetyllysine.png',
                      'NC[C@H](O)CC[C@H](N)C(=O)O': './Dnspng/5-Hydroxylysine.png',
                      'CC[C@H](N)C(=O)O': './Dnspng/L-Alpha-aminobutyric_acid.png',
                      'NC(CSCC[C@H](N)C(=O)O)C(=O)O': ['./Dnspng/Allocystathionine.png',
                                                       './Dnspng/Allocystathionine_Isomer.png'],
                      'C[C@H](O)[C@H](O)c1c[nH]c2nc(N)nc(=O)c-2n1': './Dnspng/Biopterin.png',
                      'O=c1[nH]cc(CO)c(=O)[nH]1': './Dnspng/5-Hydroxymethyluracil.png',
                      'CN(C)c1ncnc2nc[nH]c12': './Dnspng/6-Dimethylaminopurine.png',
                      'Cn1cncc1C[C@H](N)C(=O)O': './Dnspng/3-methyl-histidine.png',
                      'CO=C(O)c1ccc(O)c(O)c1': './Dnspng/Vanillic_acid.png',
                      'O=C(O)c1ccc(O)cc1': './Dnspng/4-Hydroxybenzoic_acid.png',
                      'N[C@@H](Cc1c[nH]c2ccc(O)cc12)C(=O)O': './Dnspng/5-Hydroxy-L-tryptophan.png',
                      'N[C@@H](CCCC(=O)O)C(=O)O': './Dnspng/Aminoadipic_acid.png',
                      'N=C(N)NCCC[C@H](N)C(=O)O': './Dnspng/L-Arginine.png',
                      'CC[C@@H](C)[C@H](N)C(=O)O': './Dnspng/L-Alloisoleucine.png',
                      'N[C@@H](CS)C(=O)O': './Dnspng/Cysteine.png',
                      'N[C@H]1[C@H](O)O[C@H](COS(=O)(=O)O)[C@@H](O)[C@@H]1O': './Dnspng/Glucosamine_6-sulfate.png',
                      'CNC[C@H](O)c1ccc(O)c(O)c1': ['./Dnspng/Epinephrine.png', './Dnspng/Epinephrine_Isomer1.png',
                                                    './Dnspng/Epinephrine_Isomer2.png'],
                      'Nc1ccnc(=O)[nH]1': './Dnspng/Cytosine.png',
                      'NC(=O)CC[C@H](N)C(=O)O': './Dnspng/L-Glutamine.png',
                      'CC[C@@H](N)C(=O)O': './Dnspng/D-Alpha-aminobutyric_acid.png',
                      'N[C@@H](Cc1ccc(Oc2ccc(O)cc2)cc1)C(=O)O': './Dnspng/L-Thyroine.png',
                      'O=C(O)Cc1ccccc1O': './Dnspng/Ortho-Hydroxyphenylacetic_acid.png',
                      'N=C(N)NCCCC[C@H](N)C(=O)O': './Dnspng/Homo-L-arginine.png',
                      'NC(CCSSCC[C@H](N)C(=O)O)C(=O)O': './Dnspng/L-Homocystine.png',
                      'NC(=O)NCCCC[C@H](N)C(=O)O': './Dnspng/Homocitrulline.png',
                      'Nc1ccccc1C(=O)C[C@H](N)C(=O)O': ['./Dnspng/L-Kynurenine.png', './Dnspng/L-Kynurenine-H2O.png'],
                      'CC(C)C[C@H](N)C(=O)O': './Dnspng/L-leucine.png',
                      'CSCC[C@H](N)C(=O)O': './Dnspng/L-Methionine.png',
                      'Nc1nc(=O)c2ncc(=O)[nH]c2[nH]1': ['./Dnspng/Isoxanthopterin.png',
                                                        './Dnspng/Isoxanthopterin_Isomer.png'],
                      'N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': './Dnspng/L-Aspartyl-L-phenylalanine.png',
                      'O=C(O)CNC(=O)c1ccccc1': './Dnspng/Hippuric_acid.png',
                      'O=C(O)[C@@H]1CCCCN1': './Dnspng/L-Pipecolic_acid.png',
                      'O=C(O)[C@H](CCO)NO': ['./Dnspng/L-Homoserine.png', './Dnspng/L-Homoserine-H2O.png'],
                      'NCC(=O)N1CCC[C@H]1C(=O)O': './Dnspng/Glycylproline.png',
                      'O=C(O)[C@@H]1C[C@@H](O)CN1': './Dnspng/Trans-4-Hydroxyl-L-Proline.png',
                      'O=C(O)/C=C/c1c[nH]c2ccccc12': './Dnspng/Indoleacrylic_acid.png',
                      'O=C(O)C(O)c1cccc(O)c1': ['./Dnspng/3-Hydroxymandelic_acid.png',
                                                './Dnspng/3-Hydroxymandelic_acid-HCOOH.png'],
                      'O=C(O)C(O)Cc1ccc(O)cc1': './Dnspng/Hydroxyphenyllactici_acid.png',
                      'CC(C)C[C@H](NC(=O)CN)C(=O)O': './Dnspng/Glycyl-L-Leucine.png',
                      'O=C(O)Cc1c[nH]c2ccc(O)cc12': './Dnspng/5-Hydroxyindoleacetic_acid.png',
                      'COc1cc(C(O)CN)ccc1O': './Dnspng/Normetanephrine.png',
                      'O=C(O)CNC(=O)c1ccccc1O': './Dnspng/Salicyluric_acid.png',
                      'O=C(O)c1cc(O)c2cccc(O)c2n1': ['./Dnspng/Xanthurenic_acid.png',
                                                     './Dnspng/Xanthurenic_acid_multi_tags.png'],
                      'CC(C)[C@H](N)C(=O)O': './Dnspng/L-Valine.png',
                      'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]c1=O': ['./Dnspng/Ribothymidine.png',
                                                                                './Dnspng/Ribothymidine_Isomer.png',
                                                                                './Dnspng/Ribothymidine-H2O.png'],
                      'Cn1cnc2[nH]c(N)nc(=O)c21': './Dnspng/7-Methylguanine.png',
                      'NC(=O)NCCC[C@H](N)C(=O)O': './Dnspng/Citrulline.png',
                      'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)(O)O)O1': './Dnspng/Deoxyadenosine_monophosphate.png',
                      'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': './Dnspng/L-Tryptophan.png',
                      'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CSCC[C@H](N)C(=O)O)[C@@H](O)[C@H]1O': './Dnspng/S-Adenosylhomocysteine.png',
                      'COc1cc(/C=C/C(=O)O)ccc1O': './Dnspng/trans-Ferulic_acid.png',
                      'COc1ccc(/C=C/C(=O)O)cc1O': './Dnspng/Isoferulic_acid.png',
                      'Oc1ccccc1O': './Dnspng/pyrocatechol.png',
                      'NCCS(=O)O': './Dnspng/Hypotaurine.png',
                      'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)nc1N': ['./Dnspng/5-Methylcytidine.png',
                                                                            './Dnspng/5-Methylcytidine_Isomer.png'],
                      'CCCCCCC(N)C(=O)O': './Dnspng/2-aminooctanoic_acid.png',
                      'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]1': "./Dnspng/2'-Deoxyguanosine_5'-monophosphate.png",
                      'N[C@@H](CCC(=O)N[C@@H](CS)C(=O)O)C(=O)O': './Dnspng/Gamma-Glutamylcysteine.png',
                      'NCC(O)c1ccccc1': ['./Dnspng/2-Hydroxyphenethlamine.png',
                                         './Dnspng/2-Hydroxyphenethlamine_Isomer.png'],
                      'Nc1nc(Nc2ccccc2)nc2c1ncn2C1OC(CO)C(O)C1O': './Dnspng/2-Phenylaminoadenosine.png',
                      'Nc1ccccc1C(=O)O': './Dnspng/2-Aminobenzoic_acid.png',
                      'NCC(=O)CCC(=O)O': './Dnspng/5-Aminolevulinic_acid.png',
                      'Nc1ccc(O)cc1': ['./Dnspng/4-Aminophenol.png', './Dnspng/4-Aminophenol_multi_tags.png'],
                      'CSC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O': "./Dnspng/5'-Methylthioadenosine.png",
                      'Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1': './Dnspng/dCMP.png',
                      'O=[N+]([O-])c1ccc(O)cc1': './Dnspng/4-Nitrophenol.png',
                      'CC(=O)NCCc1c[nH]c2ccc(O)cc12': './Dnspng/N-Acetylserotonin.png',
                      'N[C@H]1[C@@H](O)O[C@H](COP(=O)(O)O)[C@@H](O)[C@@H]1O': './Dnspng/Guanosine_monophosphate.png',
                      'NCCCCNCCCN': './Dnspng/Spermidine.png',
                      'O=C(O)Cc1ccc(O)c(O)c1': './Dnspng/3,4-Dihydroxybenzeneacetic_acid.png',
                      'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O': './Dnspng/ADP.png',
                      'N[C@@H](CCC[C@H](N)C(=O)O)C(=O)O': ['./Dnspng/Diaminopimelic_acid.png',
                                                           './Dnspng/Diaminopimelic_acid_Isomer.png'],
                      'Nc1ccc(C(=O)O)cc1': './Dnspng/p-Aminobenzoic_acid.png',
                      'Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1':
                          './Dnspng/Guanosine_monophosphate.png',
                      'COc1ccccc1O': './Dnspng/Guaiacol.png',
                      'C[N+](C)(C)CCOP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2ccc(N)nc2=O)[C@H](O)[C@@H]1O': [
                          './Dnspng/Citicoline.png', './Dnspng/Citicoline_Isomer.png'],
                      'NCCCCN': './Dnspng/1,4-diaminobutane.png',
                      'Cc1ncc(CO)c(CN)c1O': './Dnspng/Pyridoxamine.png',
                      'N=C(N)NCCCCN': ['./Dnspng/Agmatine.png', './Dnspng/Agmatine_multi_tags.png'],
                      'Nc1c(O)cccc1C(=O)O': './Dnspng/3-Hydroxyanthranilic_acid.png',
                      'CNC(=N)N': ['./Dnspng/Methylguanidine.png', './Dnspng/Methylguanidine_multi_tags.png'],
                      'c1c[nH]cn1': './Dnspng/Imidazole.png',
                      'Cc1ncc(CO)c(C=O)c1O': './Dnspng/Pyridoxal.png',
                      'CCCC[C@H](N)C(=O)O': './Dnspng/L-Norleucine.png',
                      'O=C(O)/C=C/c1cccc(O)c1': './Dnspng/m-Coumaric_acid.png',
                      'Nc1nc(N)c2nc(CNc3ccc(C(=O)NC(CCC(=O)O)C(=O)O)cc3)cnc2n1': './Dnspng/Aminopterin.png',
                      'N=C(N)N': './Dnspng/Guanidine.png',
                      'CC(C)NCC(O)COc1cccc2ccccc12': './Dnspng/Propranolol.png',
                      'OCCc1c[nH]c2ccc(O)cc12': './Dnspng/5-Hydroxytryptophol.png',
                      'O=C(O)c1ccc(O)c(O)c1': './Dnspng/Protocatechuic_acid.png',
                      'Cc1ccc(O)cc1': './Dnspng/p-Cresol.png',
                      'CC(=O)Nc1ccc(O)cc1': './Dnspng/Acetaminophen.png',
                      'Cn1cncc1CCN': './Dnspng/3-Methylhistamine.png',
                      'O=C(O)C(O)c1ccc(O)c(O)c1': './Dnspng/3,4-Dihydroxymandelic_acid.png',
                      'Nc1ccc(C(=O)NCC(=O)O)cc1': './Dnspng/4-Aminohippuric_acid.png',
                      'COc1ccc(O)c(C(=O)O)c1': './Dnspng/5-Methoxysalicylic_acid.png',
                      'NC(Cc1ccc(O)c(Cl)c1)C(=O)O': './Dnspng/3-Chlorotyrosine.png',
                      'CN1C2=C(NC=N2)C(=O)N(C)C1=O': './Dnspng/Theophylline.png',
                      'Nc1cccc(C(=O)O)c1': './Dnspng/m-Aminobenzoic_acid.png',
                      'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O': './Dnspng/Aspartame.png',
                      'O=C(O)c1ccccc1O': './Dnspng/Salicylic_acid.png',
                      'NCCCCCC(=O)O': './Dnspng/Aminocaproic_acid.png',
                      'N[C@@H](Cc1ccc(O)c([N+](=O)[O-])c1)C(=O)O': ['./Dnspng/3-Nitrotyrosine.png',
                                                                    './Dnspng/3-Nitrotyrosine-H2O.png'],
                      'CC(C)(N)C(=O)O': './Dnspng/2-Aminoisobutyric_acid.png',
                      'NCCCC(O)(P(=O)(O)O)P(=O)(O)O': './Dnspng/Alendronic_acid.png',
                      'N[C@@H](Cc1cc(I)c(Oc2cc(I)c(O)c(I)c2)c(I)c1)C(=O)O': './Dnspng/Thyroxine.png',
                      'CC(C)NCC(O)COc1ccc(CC(N)=O)cc1': './Dnspng/Atenolol.png',
                      'COCCc1ccc(OCC(O)CNC(C)C)cc1': './Dnspng/Metoprolol.png',
                      'CC(C)(C)NCC(O)c1ccc(O)c(CO)c1': ['./Dnspng/Salbutamol.png', './Dnspng/Salbutamol-H2O.png'],
                      'NCCCC[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O': './Dnspng/Lisinopril.png',
                      'C[C@@H](N)[C@@H](O)c1ccccc1': './Dnspng/Phenylpropanolamine.png',
                      'CN[C@@H](C)[C@@H](O)c1ccccc1': './Dnspng/Pseudoephedrine.png',
                      'O=C(O)/C=C/c1ccc(O)c(O)c1': './Dnspng/Caffeic_acid.png',
                      'Nc1cccc(C(=O)O)c1O': './Dnspng/3-Aminosalicylic_acid.png',
                      'CS(=O)CC[C@H](N)C(=O)O': ['./Dnspng/Methionine_Sulfoxide.png',
                                                 './Dnspng/Methionine_Sulfoxide_Isomer.png'],
                      'NC[C@H](N)C(=O)O': './Dnspng/2,3-Diaminoproprionic_acid.png',
                      'CC(N)c1ccccc1': './Dnspng/1-Phenylethylamine.png',
                      'O=C(O)Cc1cnc[nH]1': './Dnspng/Imidazoleacetic_acid.png',
                      'Cc1cccc(O)c1': './Dnspng/m-Cresol.png',
                      'Cc1ccccc1O': './Dnspng/o-Cresol.png',
                      'CC(=O)NCCCCN': './Dnspng/N-Acetylputrescine.png',
                      'COc1cc(C(=O)O)cc(OC)c1O': './Dnspng/Syringic_acid.png',
                      'CNc1ncnc2nc[nH]c12': ['./Dnspng/6-Methyladenine.png', './Dnspng/6-Methyladenine_Isomer.png'],
                      'CSC[C@@H](N)C(=O)O': './Dnspng/Methylcysteine.png',
                      'Nc1cc(=O)nc(N)[nH]1': './Dnspng/2,4-Diamino-6-hydroxypyrimidine.png',
                      'CNC(C)(C)C(=O)O': './Dnspng/N-Methyl-a-aminoisobutyric_acid.png',
                      'CNC[C@H](O)c1cccc(O)c1': './Dnspng/Phenylephrine.png',
                      'O=C(O)CCc1ccc(O)cc1': './Dnspng/Desaminotyrosine.png',
                      'N[C@@H](CCS(=O)(=O)O)C(=O)O': './Dnspng/L-Homocysteic_acid.png',
                      'NC(C(=O)O)c1ccccc1': './Dnspng/2-Phenylglycine.png',
                      'NCCCCCN': './Dnspng/Cadaverine.png',
                      'COc1ccc2[nH]cc(C[C@H](N)C(=O)O)c2c1': './Dnspng/5-Methoxytryptophan.png',
                      'NCCC(N)C(=O)O': './Dnspng/2,4-Diaminobutyric_acid.png',
                      'Cc1cccc(C(=O)O)c1O': './Dnspng/3-Cresotinic_acid.png',
                      'CN[C@H](CC(=O)O)C(=O)O': './Dnspng/N-methyl-D-aspartic_acid.png',
                      'O=C(O)c1ccc(O)nc1': ['./Dnspng/6-Hydroxynicotinic_acid.png',
                                            './Dnspng/6-Hydroxynicotinic_acid_Isomer.png'],
                      'O=C1C[C@@H](c2ccc(O)cc2)Oc2cc(O)cc(O)c21': './Dnspng/Naringenin.png',
                      'N=C(N)NOCC[C@H](N)C(=O)O': ['./Dnspng/Canavanine.png', './Dnspng/Canavanine_Isomer.png'],
                      'NCCS': './Dnspng/Cysteamine.png',
                      'Nc1ccccc1': './Dnspng/Aniline.png',
                      'N[C@@H](CCCCNC(=O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12)C(=O)O': './Dnspng/Biocytin.png',
                      'N=C(N)N[C@@H](CC(=O)O)C(=O)O': './Dnspng/Guanidinosuccinic_acid.png',
                      'O=C(/C=C/c1ccc(O)c(O)c1)O[C@@H]1C[C@](O)(C(=O)O)C[C@@H](O)[C@H]1O': [
                          './Dnspng/Chlorogenic_acid.png', './Dnspng/Chlorogenic_acid_Isomer.png'],
                      'Cn1c(N)nc2nc[nH]c2c1=O': './Dnspng/1-Methylguanine.png',
                      'O=C(O)c1c[nH]c2ccccc12': './Dnspng/Indole-3-carboxylic_acid.png',
                      'CN=C(NC)NCCCC(N)C(=O)O': './Dnspng/Symmetric_dimethylarginine.png',
                      'N[C@@H](CCC(=O)N[C@@H](CSSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O)C(=O)NCC(=O)O)C(=O)O':
                          './Dnspng/Oxidized_glutathione.png',
                      'NO': './Dnspng/Hydroxylamine.png',
                      'NCCCCC(=O)O': './Dnspng/5-Aminopentanoic_acid.png',
                      'NC(=O)CC[C@@H](N)C(=O)O': './Dnspng/D-Glutamine.png',
                      'N[C@H](CO)Cc1c[nH]cn1': './Dnspng/L-Histidinol.png',
                      'N=C(N)NCCCC(=O)O': ['./Dnspng/4-Guanidinobutanoic_acid.png',
                                           './Dnspng/4-Guanidinobutanoic_acid-H2O.png'],
                      'N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O': ['./Dnspng/3,5-Diiodo-L-tyrosine.png',
                                                            './Dnspng/3,5-Diiodo-L-tyrosine_multi tags.png'],
                      'CC(C)[C@@H](N)CC(=O)O': ['./Dnspng/Beta-Leucine.png', './Dnspng/Beta-Leucine-H2O.png'],
                      'CC(CN)C(=O)O': ['./Dnspng/3-Aminoisobutanoic_acid.png',
                                       './Dnspng/3-Aminoisobutanoic_acid-H2O.png'],
                      'COc1ccc2[nH]cc(CCN)c2c1': './Dnspng/5-Methoxytryptamine.png',
                      'NC(C[Se][Se]CC(N)C(=O)O)C(=O)O': './Dnspng/Selenocystine.png',
                      'OCCNCCO': './Dnspng/Diethanolamine.png',
                      'Oc1ccc(Cl)cc1Cl': './Dnspng/2,4-Dichlorophenol.png',
                      'Cc1cc(C(=O)O)ccc1O': './Dnspng/4-Hydroxy-3-methylbenzoic_acid.png',
                      'NCCCC[C@H](NC(=O)[C@@H](N)CC(=O)O)C(=O)O': './Dnspng/Alpha-Aspartyl-lysine.png',
                      'CCOC(=O)c1ccc(N)cc1': './Dnspng/Benzocaine.png',
                      'NC(Cc1ccccc1O)C(=O)O': './Dnspng/o-Tyrosine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O': './Dnspng/L-phenylalanyl-L-proline.png',
                      'N[C@@H](CCC(=O)N[C@@H](CCC(=O)O)C(=O)O)C(=O)O': './Dnspng/Gamma Glutamylglutamic_acid.png',
                      'CC(C)C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': './Dnspng/Leucyl-phenylalanine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': './Dnspng/Phenylalanylphenylalanine.png',
                      'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O': './Dnspng/Alanyl-Histidine.png',
                      'CC(C)C[C@H](NC(=O)[C@H](C)N)C(=O)O': './Dnspng/Alanyl-Leucine.png',
                      'C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': './Dnspng/Alanyl-Phenylalanine.png',
                      'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': './Dnspng/Alanyl-Tryptophan.png',
                      'C[C@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': './Dnspng/Alanyl-Tyrosine.png',
                      'N=C(N)NCCC[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': './Dnspng/Arginyl-Phenylalanine.png',
                      'CCC(C)C(N=C(O)CN)C(=O)O': './Dnspng/Glycyl-Isoleucine.png',
                      'NCC(O)=NC(Cc1ccccc1)C(=O)O': './Dnspng/Glycyl-Phenylalanine.png',
                      'NCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)O': './Dnspng/Glycyl-Tryptophan.png',
                      'NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': './Dnspng/Glycyl-Tyrosine.png',
                      'CC(C)[C@H](NC(=O)CN)C(=O)O': './Dnspng/Glycyl-Valine.png',
                      'C[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O': './Dnspng/Histidinyl-Alanine.png',
                      'CC(C)C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O': './Dnspng/Leucyl-Proline.png',
                      'CC(C)CC(N)C(O)=NC(Cc1c[nH]c2ccccc12)C(=O)O': './Dnspng/Leucyl-Tryptophan.png',
                      'CC(C)CC(N)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': './Dnspng/Leucyl-Tyrosine.png',
                      'C[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': './Dnspng/Phenylalanyl-Alanine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)NCC(=O)O': './Dnspng/Phenylalanyl-Glycine.png',
                      'CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': './Dnspng/Phenylalanyl-Methionine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': './Dnspng/Phenylalanyl-Tyrosine.png',
                      'CC(C)[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': './Dnspng/Phenylalanyl-Valine.png',
                      'CC(C)C[C@H](NC(=O)[C@@H](N)CO)C(=O)O': './Dnspng/Serinyl-Leucine.png',
                      'N[C@@H](CO)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': './Dnspng/Serinyl-Phenylalanine.png',
                      'CC(C)C[C@H](NC(=O)[C@@H](N)[C@@H](C)O)C(=O)O': './Dnspng/Threoninyl-Leucine.png',
                      'NC(Cc1c[nH]c2ccccc12)C(=O)NC(CCC(=O)O)C(=O)O': './Dnspng/Tryptophyl-Glutamate.png',
                      'CC(C)CC(N=C(O)C(N)Cc1c[nH]c2ccccc12)C(=O)O': './Dnspng/Tryptophyl-Leucine.png',
                      'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccccc1)C(=O)O': './Dnspng/Tryptophyl-Phenylalanine.png',
                      'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': './Dnspng/Tryptophyl-Tyrosine.png',
                      'CC(NC(=O)C(N)Cc1ccc(O)cc1)C(=O)O': './Dnspng/Tyrosyl-Alanine.png',
                      'N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)O': './Dnspng/Tyrosyl-Glycine.png',
                      'CC(C)CC(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': './Dnspng/Tyrosyl-Leucine.png',
                      'CC(C)C(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': './Dnspng/Tyrosyl-Valine.png',
                      'CCc1ccc(O)cc1': './Dnspng/4-Ethylphenol.png',
                      'O=C(O)c1ccc(O)c(O)c1O': './Dnspng/2,3,4-Trihydroxybenzoic_acid.png',
                      'COc1cc(O)cc(OC)c1': './Dnspng/3,5-Dimethoxyphenol.png',
                      'COc1ccc(C(=O)O)cc1O': './Dnspng/Isovanillic_acid.png',
                      'NCC(=O)NCC(=O)NCC(=O)NCC(=O)O': './Dnspng/Gly-Gly-Gly-Gly.png',
                      'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O': './Dnspng/Trp-Gly-Gly.png',
                      'CCCC(NC(=O)CN)C(=O)O': './Dnspng/Gly-Norvaline.png',
                      'CCCCC(NC(=O)CN)C(=O)O': './Dnspng/Gly-Norleucine.png',
                      'CC(C)C[C@H](Nc1ccccc1)C(=O)O': './Dnspng/Phenyl-Leucine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O':
                          './Dnspng/Phe-Phe-Phe.png'}

        Residual = pred_tot - exp_tot

        def outliers_iqr(data):
            q1, q3 = np.percentile(data, [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - (iqr * 1.5)
            upper_bound = q3 + (iqr * 1.5)
            return np.where((data > upper_bound) | (data < lower_bound))

        outlier_index = outliers_iqr(Residual)[0]
        outlier = total.loc[outlier_index, :]
        exp_outlier = outlier['Experimental_RT']
        pred_outlier = outlier['Predicted_RT']
        df = total.drop(outlier_index)

        df_train = df.loc[
                   [11, 5, 3, 4, 0, 7, 6, 18, 8, 2, 1, 22, 36, 39, 20, 13,
                    10, 32, 9, 17, 30, 15, 21, 52, 46, 16, 43, 33, 65, 70, 37,
                    29, 14, 27, 63, 44, 76, 35, 26, 74, 47, 49, 28, 78, 41, 55,
                    80, 95, 88, 53, 58, 64, 51, 83, 62, 57, 66, 79, 68, 98, 71,
                    56, 84, 104, 137, 90, 149, 96, 87, 97, 134, 89, 72, 94, 92,
                    106, 100, 86, 108, 101, 132, 103, 113, 99, 133, 105, 117, 116,
                    120, 154, 115, 124, 129, 126, 138, 111, 107, 140, 171, 136,
                    166, 148, 139, 122, 127, 121, 146, 131, 128, 135, 125, 159, 168,
                    175, 158, 179, 182, 176, 172, 201, 153, 183, 188, 177, 205, 193,
                    180, 169, 181, 151, 143, 191, 190, 165, 144, 160, 157, 200, 189,
                    178, 199, 130, 173, 170, 174, 162, 213, 119, 202, 196, 197, 211,
                    207, 216, 217, 194, 161, 203, 208, 209, 249, 228, 242, 214, 222,
                    198, 259, 219, 236, 232, 244, 230, 239, 218, 224, 220, 204, 231,
                    253, 235, 233, 240, 223, 254, 238, 229, 226, 234, 245, 256, 266,
                    221, 270, 258, 257, 247, 243, 225, 261, 269, 263, 248, 271, 265,
                    260, 252, 255, 293, 268, 272, 267, 279, 275, 283, 273, 297, 277,
                    282, 300, 305, 274, 285, 286, 291, 299, 294, 276, 290, 302, 296,
                    308, 303, 292, 281, 311, 312, 287, 310, 314, 313], :]
        df_test = df.loc[
                  [38, 34, 19, 40, 12, 45, 24, 25, 31, 48, 23, 82, 93, 42, 91, 114, 81, 77,
                   85, 75, 67, 60, 102, 109, 73, 123, 61, 155, 54, 118, 142, 145, 112, 187, 110,
                   164, 156, 167, 206, 185, 210, 186, 141, 212, 227, 251, 237, 280, 241, 298,
                   246, 295, 278, 307, 289, 288, 309, 304, 306, 301], :]

        exp_df_train = df_train['Experimental_RT']
        pred_df_train = df_train['Predicted_RT']

        z = np.polyfit(exp_df_train, pred_df_train, 1)
        p = np.poly1d(z)

        exp_df_test = df_test['Experimental_RT']
        pred_df_test = df_test['Predicted_RT']

        self.fig1.clear()

        ax = self.fig1.add_subplot(111)

        # 그래프 사이즈 캔버스에 맞게 조정
        ax.text(13, 4, 'y = 0.87 * x + 1.79', color='black', weight='bold', fontsize=15,
                horizontalalignment='center', verticalalignment='bottom')
        ax.text(13, 2, 'Adjusted R square = 0.96', color='black', weight='bold', fontsize=15,
                horizontalalignment='center', verticalalignment='bottom')
        ax.scatter(exp_df_train, pred_df_train, facecolors='none', edgecolors='black', s=20)
        ax.scatter(exp_df_test, pred_df_test, color='blue', s=20)
        ax.scatter(exp_outlier, pred_outlier, color='red', s=20)
        ax.plot(exp_df_train, p(exp_df_train), color='black', linewidth=2, linestyle='--')
        ax.scatter(exp, pred, marker='*', color='orange', s=150)

        if type(pred) == list:
            # 텍스트가 뭉쳐있을 때는?
            x = [5, 10, 19]
            y = [25, 28, 11]
            for i, v in enumerate(exp):
                ax.annotate('(%.2f, %.2f)' % (v, pred[i]), xy=(x[i], y[i]), fontsize=15)
        else:
            ax.annotate('(%.2f, %.2f)' % (exp, pred), xy=(5, 25))
        if type(Dns_struct[smi2]) == list:
            paths = Dns_struct[smi2]
        else:
            paths = list(Dns_struct[smi2].split())

        if len(paths) == 1:
            im = plt.imread(paths[0], format='png')
            im2 = OffsetImage(im, zoom=1)
            ab = AnnotationBbox(im2, (7, 20), frameon=False)
            ax.add_artist(ab)
            ax.annotate('', xytext=(7, 15), xy=(exp, pred),
                        arrowprops={'facecolor': 'black', 'edgecolor': 'black', 'headwidth': 5, 'width': 0.5})

        else:
            x0 = [5, 15, 25]
            y0 = [18, 24, 10]
            x01 = [5, 12, 24]
            y01 = [13, 18, 10]
            for i in range(len(paths)):
                im = plt.imread(paths[i], format='png')
                im2 = OffsetImage(im, zoom=1)
                ab = AnnotationBbox(im2, (x0[i], y0[i]), frameon=False)
                ax.add_artist(ab)
                ax.annotate('', xytext=(x01[i], y01[i]), xy=(exp[i], pred[i]),
                            arrowprops={'facecolor': 'black', 'edgecolor': 'black', 'headwidth': 5, 'width': 0.5})

        ax.set_xlim(0, 30)
        ax.set_ylim(0, 30)
        ax.axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.axes.yaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.set_xlabel("Experimental RT")
        ax.set_ylabel("Predicted RT")
        ax.set_title("Experimental RT vs Predicted RT")
        self.fig1.tight_layout()

        self.canvas1.draw()

        cursor1 = mplcursors.cursor(
            ax.scatter(exp_df_train, pred_df_train, facecolors='none', edgecolors='black', s=20),
            hover=True)
        cursor1.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

        cursor2 = mplcursors.cursor(ax.scatter(exp_df_test, pred_df_test, color='blue', s=20), hover=True)
        cursor2.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

        cursor3 = mplcursors.cursor(ax.scatter(exp_outlier, pred_outlier, color='red', s=20), hover=True)
        cursor3.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

    def findpredrt(self):
        pred_rt_name = {'1-Methylhistidine': 7.97,
                        '1,3-Diaminopropane': [3.91, 18.96],
                        'p-Hydroxyphenylacetic acid': 17.19,
                        'Iodotyrosine': 19.07,
                        '3-Methoxytyramine': 24.56,
                        'Adenosine monophosphate': 3.80,
                        'Adenosine': 4.48,
                        'Ammonia': 9.14,
                        'Beta-Alanine': 7.35,
                        'Creatine': 3.58,
                        'D-Pipecolic acid': 11.48,
                        'Deoxyguanosine': 8.13,
                        'Dimethylamine': 14.82,
                        'Cytidine': [4.17, 9.86],
                        'Cytidine monophosphate': [2.95, 3.55],
                        'L-Cystathionine': [14.23, 14.38],
                        'Deoxyadenosine': 8.06,
                        'Gamma-Aminobutyric acid': [8.53, 14.80],
                        'Homovanillic acid': 17.38,
                        'Glycine': 6.94,
                        'Guanidoacetic acid': 3.56,
                        'Homogentisic acid': 22.51,
                        'Guanosine': 4.66,
                        'L-Glutamic Acid': [7.56, 10.90],
                        'Ethanolamine': 5.18,
                        'Gentisic acid': [17.14, 22.89],
                        'Estriol': 23.24,
                        'Hypoxanthine': [4.05, 9.14, 10.20],
                        'L-Tyrosine': 21.32,
                        'L-Phenylalanine': 13.45,
                        'L-Alanine': 7.96,
                        'L-Proline': 11.17,
                        'Methylamine': 9.92,
                        'L-Threonine': 6.05,
                        'L-Asparagine': [4.45, 8.69],
                        'L-Isoleucine': 13.63,
                        'L-Histidine': 11.6190443,
                        'L-Lysine': 16.02,
                        'L-Serine': 4.70,
                        'L-Aspartic Acid': 5.64,
                        'L-Cystine': 14.88,
                        'N6-Acetyl-L-Lysine': 8.10,
                        'Pantothenic acid': 11.12,
                        'Ornithine': 16.09,
                        'O-Phosphoethanolamine': 2.83,
                        'Phenol': 23.03,
                        'Sepiapterin': 7.53,
                        'Pyridoxine': [10.71, 16.75],
                        'Taurine': 4.60,
                        'Serotonin': 22.52,
                        'Thymine': 12.02,
                        'Liothyronine': 18.60,
                        'CNCC(=O)O': 8.09,
                        'Sarcosine': [4.83, 8.38],
                        'Saccharopine': [14.58, 18.32],
                        'Xanthine': 9.47,
                        'Uridine': [7.34, 10.93],
                        'Uracil': 11.04,
                        'Urocanic acid': 12.38,
                        'Tryptamine': 16.26,
                        'Tyramine': 23.92,
                        '17-Epiestriol': 23.24,
                        '2-Amino-3-phosphonopropionic acid': 3.13,
                        '2-Pyrocatechuic acid': 17.26,
                        '3-Hydroxyphenylacetic acid': 16.92,
                        'N-Alpha-acetyllysine': 7.57,
                        '5-Hydroxylysine': 13.26,
                        'L-Alpha-aminobutyric acid': 9.67,
                        'Allocystathionine': [14.23, 14.38],
                        'Biopterin': 7.25,
                        '5-Hydroxymethyluracil': 8.91,
                        '6-Dimethylaminopurine': 15.99,
                        '3-methyl-histidine': 6.88,
                        'Vanillic acid': 17.57,
                        '4-Hydroxybenzoic acid': 17.29,
                        '5-Hydroxy-L-tryptophan': 19.96,
                        'Aminoadipic acid': 8.30,
                        'L-Arginine': 3.84,
                        'L-Alloisoleucine': 13.63,
                        'Cysteine': 10.16,
                        'Glucosamine 6-sulfate': 3.36,
                        'Epinephrine': [9.16, 8.85, 9.19],
                        'Cytosine': 9.33,
                        'L-Glutamine': 5.94,
                        'D-Alpha-aminobutyric acid': 9.67,
                        'L-Thyroine': 22.48,
                        'Ortho-Hydroxyphenylacetic acid': 16.75,
                        'Homo-L-arginine': 3.41,
                        'L-Homocystine': 14.35,
                        'Homocitrulline': 4.29,
                        'L-Kynurenine': [11.60, 14.17],
                        'L-leucine': 12.82,
                        'L-Methionine': 10.60,
                        'Isoxanthopterin': [10.02, 10.34],
                        'L-Aspartyl-L-phenylalanine': 10.41,
                        'Hippuric acid': 12.05,
                        'L-Pipecolic acid': 11.48,
                        'L-Homoserine': [6.28, 10.81],
                        'Glycylproline': 7.54,
                        'Trans-4-Hydroxyl-L-Proline': 8.20,
                        'Indoleacrylic acid': 17.85,
                        '3-Hydroxymandelic acid': [14.54, 22.89],
                        'Hydroxyphenyllactici acid': 14.33,
                        'Glycyl-L-Leucine': 10.06,
                        '5-Hydroxyindoleacetic acid': 14.60,
                        'Normetanephrine': 21.35,
                        'Salicyluric acid': 10.25,
                        'Xanthurenic acid': [14.24, 23.58],
                        'L-Valine': 11.23,
                        'Ribothymidine': [6.83, 7.77, 10.35],
                        '7-Methylguanine': 9.64,
                        'Citrulline': 4.11,
                        'Deoxyadenosine monophosphate': 4.16,
                        'L-Tryptophan': 12.85,
                        'S-Adenosylhomocysteine': 11.23,
                        'trans-Ferulic acid': 18.57,
                        'Isoferulic acid': 18.42,
                        'pyrocatechol': 26.52,
                        'Hypotaurine': 4.89,
                        '5-Methylcytidine': [4.51, 5.28],
                        '2-aminooctanoic acid': 14.90,
                        '2\'-Deoxyguanosine 5\'-monophosphate': 4.15,
                        'Gamma-Glutamylcysteine': 8.63,
                        '2-Hydroxyphenethlamine': [12.84, 13.16],
                        '2-Phenylaminoadenosine': 7.45,
                        '2-Aminobenzoic acid': 14.52,
                        '5-Aminolevulinic acid': 8.35,
                        '4-Aminophenol': [15.74, 25.02],
                        '5\'-Methylthioadenosine': 8.38,
                        'dCMP': 4.07,
                        '4-Nitrophenol': 23.91,
                        'N-Acetylserotonin': 14.05,
                        'Glucosamine 6-phosphate': 3.16,
                        'Spermidine': 13.04,
                        '3,4-Dihydroxybenzeneacetic acid': 22.80,
                        'ADP': 2.96,
                        'Diaminopimelic acid': [14.18, 14.03],
                        'p-Aminobenzoic acid': 13.28,
                        'Guanosine monophosphate': 3.51,
                        'Guaiacol': 21.92,
                        'Citicoline': [2.95, 3.08],
                        '1,4-diaminobutane': 18.92,
                        'Pyridoxamine': 21.58,
                        'Agmatine': [3.56, 14.29],
                        '3-Hydroxyanthranilic acid': 13.80,
                        'Methylguanidine': [4.12, 21.06],
                        'Imidazole': 14.47,
                        'Pyridoxal': 14.38,
                        'L-Norleucine': 12.54,
                        'm-Coumaric acid': 19.44,
                        'Aminopterin': 8.32,
                        'Guanidine': 3.73,
                        'Propranolol': 21.79,
                        '5-Hydroxytryptophol': 14.71,
                        'Protocatechuic acid': 23.03,
                        'p-Cresol': 24.25,
                        'Acetaminophen': 17.02,
                        '3-Methylhistamine': 6.92,
                        '3,4-Dihydroxymandelic acid': 19.94,
                        '4-Aminohippuric acid': 8.80,
                        '5-Methoxysalicylic acid': 17.74,
                        '3-Chlorotyrosine': 20.72,
                        'Theophylline': 14.64,
                        'm-Aminobenzoic acid': 13.64,
                        'Aspartame': 10.78,
                        'Salicylic acid': 18.05,
                        'Aminocaproic acid': 9.78,
                        '3-Nitrotyrosine': [20.61, 23.10],
                        '2-Aminoisobutyric acid': 9.42,
                        'Alendronic acid': 2.74,
                        'Thyroxine': 26.03,
                        'Atenolol': 13.14,
                        'Metoprolol': 19.68,
                        'Salbutamol': [8.39, 11.73],
                        'Lisinopril': 8.05,
                        'Phenylpropanolamine': 15.13,
                        'Pseudoephedrine': 18.57,
                        'Caffeic acid': 18.94,
                        '3-Aminosalicylic acid': 13.70,
                        'Methionine Sulfoxide': [7.68, 7.99],
                        '2,3-Diaminoproprionic acid': 16.45,
                        '1-Phenylethylamine': 20.02,
                        'Imidazoleacetic acid': 10.78,
                        'm-Cresol': 24.04,
                        'o-Cresol': 23.81,
                        'N-Acetylputrescine': 7.76,
                        'Syringic acid': 17.82732582,
                        '6-Methyladenine': [12.18, 12.84],
                        'Methylcysteine': 9.48,
                        '2,4-Diamino-6-hydroxypyrimidine': 8.54,
                        'N-Methyl-a-aminoisobutyric acid': 13.46,
                        'Phenylephrine': 25.08,
                        'Desaminotyrosine': 17.16,
                        'L-Homocysteic acid': 4.74,
                        '2-Phenylglycine': 13.58,
                        'Cadaverine': 18.19,
                        '5-Methoxytryptophan': 12.06,
                        '2,4-Diaminobutyric acid': 16.01,
                        '3-Cresotinic acid': 18.40,
                        'N-methyl-D-aspartic acid': 8.31,
                        '6-Hydroxynicotinic acid': [12.75, 12.47],
                        'Naringenin': 22.11,
                        'Canavanine': [12.35, 12.30],
                        'Cysteamine': 11.40,
                        'Aniline': 18.31,
                        'Biocytin': 7.41,
                        'Guanidinosuccinic acid': 3.48,
                        'Chlorogenic acid': [17.73, 19.18],
                        '1-Methylguanine': 9.94,
                        'Indole-3-carboxylic acid': 17.28,
                        'Symmetric dimethylarginine': 3.91,
                        'Oxidized glutathione': 14.30,
                        'Hydroxylamine': 9.70,
                        '5-Aminopentanoic acid': 8.73,
                        'D-Glutamine': 5.94,
                        'L-Histidinol': 7.42,
                        '4-Guanidinobutanoic acid': [4.51, 7.04],
                        '3,5-Diiodo-L-tyrosine': [13.31, 22.61],
                        'Beta-Leucine': [12.16, 17.98],
                        '3-Aminoisobutanoic acid': [9.21, 14.83],
                        '5-Methoxytryptamine': 16.29,
                        'Selenocystine': 15.00,
                        'Diethanolamine': 4.60,
                        '2,4-Dichlorophenol': 24.61,
                        '4-Hydroxy-3-methylbenzoic acid': 17.89,
                        'Alpha-Aspartyl-lysine': 12.22,
                        'Benzocaine': 16.12,
                        'o-Tyrosine': 21.52,
                        'L-phenylalanyl-L-proline': 12.92,
                        'Gamma Glutamylglutamic acid': 5.48,
                        'Leucyl-phenylalanine': 15.85,
                        'Phenylalanylphenylalanine': 15.57,
                        'Alanyl-Histidine': 12.68,
                        'Alanyl-Leucine': 11.43,
                        'Alanyl-Phenylalanine': 12.05,
                        'Alanyl-Tryptophan': 11.60,
                        'Alanyl-Tyrosine': 20.22,
                        'Arginyl-Phenylalanine': 6.90,
                        'Glycyl-Isoleucine': 11.65,
                        'Glycyl-Phenylalanine': 9.79,
                        'Glycyl-Tryptophan': 10.70,
                        'Glycyl-Tyrosine': 18.52,
                        'Glycyl-Valine': 9.44,
                        'Histidinyl-Alanine': 11.74,
                        'Leucyl-Proline': 14.26,
                        'Leucyl-Tryptophan': 14.88,
                        'Leucyl-Tyrosine': 22.96,
                        'Phenylalanyl-Alanine': 11.06,
                        'Phenylalanyl-Glycine': 9.34,
                        'Phenylalanyl-Methionine': 12.92,
                        'Phenylalanyl-Tyrosine': 23.60,
                        'Phenylalanyl-Valine': 14.19,
                        'Serinyl-Leucine': 9.63,
                        'Serinyl-Phenylalanine': 9.83,
                        'Threoninyl-Leucine': 10.46,
                        'Tryptophyl-Glutamate': 9.48,
                        'Tryptophyl-Leucine': 14.34,
                        'Tryptophyl-Phenylalanine': 14.48,
                        'Tryptophyl-Tyrosine': 23.34,
                        'Tyrosyl-Alanine': 20.05,
                        'Tyrosyl-Glycine': 18.92,
                        'Tyrosyl-Leucine': 22.42,
                        'Tyrosyl-Valine': 21.82,
                        '4-Ethylphenol': 23.82,
                        '2,3,4-Trihydroxybenzoic acid': 21.20,
                        '3,5-Dimethoxyphenol': 22.15,
                        'Isovanillic acid': 17.63,
                        'Gly-Gly-Gly-Gly': 3.68,
                        'Trp-Gly-Gly': 8.28,
                        'Gly-Norvaline': 9.53,
                        'Gly-Norleucine': 10.43,
                        'Phenyl-Leucine': 18.91,
                        'Phe-Phe-Phe': 17.57}  # 화학종 이름과 예측 RT 대응
        pred_rt_value = []
        standarddata = self.Fittable.rowCount()
        for i in range(0, standarddata):
            pred_rt = pred_rt_name[str(self.Fittable.item(i, 0).text())]
            pred_rt_value.append(pred_rt)
        # 리스트 값을 입력하기
        for i in range(0, standarddata):
            self.Fittable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(pred_rt_value[i]))) #float로 바꾸기
            self.Fittable.item(i, 2).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def bringfit(self):  # 표에 입력된 값 가져오고 피팅
        pred_rt_name = {'1-Methylhistidine': 7.97,
                        '1,3-Diaminopropane': [3.91, 18.96],
                        'p-Hydroxyphenylacetic acid': 17.19,
                        'Iodotyrosine': 19.07,
                        '3-Methoxytyramine': 24.56,
                        'Adenosine monophosphate': 3.80,
                        'Adenosine': 4.48,
                        'Ammonia': 9.14,
                        'Beta-Alanine': 7.35,
                        'Creatine': 3.58,
                        'D-Pipecolic acid': 11.48,
                        'Deoxyguanosine': 8.13,
                        'Dimethylamine': 14.82,
                        'Cytidine': [4.17, 9.86],
                        'Cytidine monophosphate': [2.95, 3.55],
                        'L-Cystathionine': [14.23, 14.38],
                        'Deoxyadenosine': 8.06,
                        'Gamma-Aminobutyric acid': [8.53, 14.80],
                        'Homovanillic acid': 17.38,
                        'Glycine': 6.94,
                        'Guanidoacetic acid': 3.56,
                        'Homogentisic acid': 22.51,
                        'Guanosine': 4.66,
                        'L-Glutamic Acid': [7.56, 10.90],
                        'Ethanolamine': 5.18,
                        'Gentisic acid': [17.14, 22.89],
                        'Estriol': 23.24,
                        'Hypoxanthine': [4.05, 9.14, 10.20],
                        'L-Tyrosine': 21.32,
                        'L-Phenylalanine': 13.45,
                        'L-Alanine': 7.96,
                        'L-Proline': 11.17,
                        'Methylamine': 9.92,
                        'L-Threonine': 6.05,
                        'L-Asparagine': [4.45, 8.69],
                        'L-Isoleucine': 13.63,
                        'L-Histidine': 11.6190443,
                        'L-Lysine': 16.02,
                        'L-Serine': 4.70,
                        'L-Aspartic Acid': 5.64,
                        'L-Cystine': 14.88,
                        'N6-Acetyl-L-Lysine': 8.10,
                        'Pantothenic acid': 11.12,
                        'Ornithine': 16.09,
                        'O-Phosphoethanolamine': 2.83,
                        'Phenol': 23.03,
                        'Sepiapterin': 7.53,
                        'Pyridoxine': [10.71, 16.75],
                        'Taurine': 4.60,
                        'Serotonin': 22.52,
                        'Thymine': 12.02,
                        'Liothyronine': 18.60,
                        'CNCC(=O)O': 8.09,
                        'Sarcosine': [4.83, 8.38],
                        'Saccharopine': [14.58, 18.32],
                        'Xanthine': 9.47,
                        'Uridine': [7.34, 10.93],
                        'Uracil': 11.04,
                        'Urocanic acid': 12.38,
                        'Tryptamine': 16.26,
                        'Tyramine': 23.92,
                        '17-Epiestriol': 23.24,
                        '2-Amino-3-phosphonopropionic acid': 3.13,
                        '2-Pyrocatechuic acid': 17.26,
                        '3-Hydroxyphenylacetic acid': 16.92,
                        'N-Alpha-acetyllysine': 7.57,
                        '5-Hydroxylysine': 13.26,
                        'L-Alpha-aminobutyric acid': 9.67,
                        'Allocystathionine': [14.23, 14.38],
                        'Biopterin': 7.25,
                        '5-Hydroxymethyluracil': 8.91,
                        '6-Dimethylaminopurine': 15.99,
                        '3-methyl-histidine': 6.88,
                        'Vanillic acid': 17.57,
                        '4-Hydroxybenzoic acid': 17.29,
                        '5-Hydroxy-L-tryptophan': 19.96,
                        'Aminoadipic acid': 8.30,
                        'L-Arginine': 3.84,
                        'L-Alloisoleucine': 13.63,
                        'Cysteine': 10.16,
                        'Glucosamine 6-sulfate': 3.36,
                        'Epinephrine': [9.16, 8.85, 9.19],
                        'Cytosine': 9.33,
                        'L-Glutamine': 5.94,
                        'D-Alpha-aminobutyric acid': 9.67,
                        'L-Thyroine': 22.48,
                        'Ortho-Hydroxyphenylacetic acid': 16.75,
                        'Homo-L-arginine': 3.41,
                        'L-Homocystine': 14.35,
                        'Homocitrulline': 4.29,
                        'L-Kynurenine': [11.60, 14.17],
                        'L-leucine': 12.82,
                        'L-Methionine': 10.60,
                        'Isoxanthopterin': [10.02, 10.34],
                        'L-Aspartyl-L-phenylalanine': 10.41,
                        'Hippuric acid': 12.05,
                        'L-Pipecolic acid': 11.48,
                        'L-Homoserine': [6.28, 10.81],
                        'Glycylproline': 7.54,
                        'Trans-4-Hydroxyl-L-Proline': 8.20,
                        'Indoleacrylic acid': 17.85,
                        '3-Hydroxymandelic acid': [14.54, 22.89],
                        'Hydroxyphenyllactici acid': 14.33,
                        'Glycyl-L-Leucine': 10.06,
                        '5-Hydroxyindoleacetic acid': 14.60,
                        'Normetanephrine': 21.35,
                        'Salicyluric acid': 10.25,
                        'Xanthurenic acid': [14.24, 23.58],
                        'L-Valine': 11.23,
                        'Ribothymidine': [6.83, 7.77, 10.35],
                        '7-Methylguanine': 9.64,
                        'Citrulline': 4.11,
                        'Deoxyadenosine monophosphate': 4.16,
                        'L-Tryptophan': 12.85,
                        'S-Adenosylhomocysteine': 11.23,
                        'trans-Ferulic acid': 18.57,
                        'Isoferulic acid': 18.42,
                        'pyrocatechol': 26.52,
                        'Hypotaurine': 4.89,
                        '5-Methylcytidine': [4.51, 5.28],
                        '2-aminooctanoic acid': 14.90,
                        "2'-Deoxyguanosine 5'-monophosphate": 4.15,
                        'Gamma-Glutamylcysteine': 8.63,
                        '2-Hydroxyphenethlamine': [12.84, 13.16],
                        '2-Phenylaminoadenosine': 7.45,
                        '2-Aminobenzoic acid': 14.52,
                        '5-Aminolevulinic acid': 8.35,
                        '4-Aminophenol': [15.74, 25.02],
                        "5'-Methylthioadenosine": 8.38,
                        'dCMP': 4.07,
                        '4-Nitrophenol': 23.91,
                        'N-Acetylserotonin': 14.05,
                        'Glucosamine 6-phosphate': 3.16,
                        'Spermidine': 13.04,
                        '3,4-Dihydroxybenzeneacetic acid': 22.80,
                        'ADP': 2.96,
                        'Diaminopimelic acid': [14.18, 14.03],
                        'p-Aminobenzoic acid': 13.28,
                        'Guanosine monophosphate': 3.51,
                        'Guaiacol': 21.92,
                        'Citicoline': [2.95, 3.08],
                        '1,4-diaminobutane': 18.92,
                        'Pyridoxamine': 21.58,
                        'Agmatine': [3.56, 14.29],
                        '3-Hydroxyanthranilic acid': 13.80,
                        'Methylguanidine': [4.12, 21.06],
                        'Imidazole': 14.47,
                        'Pyridoxal': 14.38,
                        'L-Norleucine': 12.54,
                        'm-Coumaric acid': 19.44,
                        'Aminopterin': 8.32,
                        'Guanidine': 3.73,
                        'Propranolol': 21.79,
                        '5-Hydroxytryptophol': 14.71,
                        'Protocatechuic acid': 23.03,
                        'p-Cresol': 24.25,
                        'Acetaminophen': 17.02,
                        '3-Methylhistamine': 6.92,
                        '3,4-Dihydroxymandelic acid': 19.94,
                        '4-Aminohippuric acid': 8.80,
                        '5-Methoxysalicylic acid': 17.74,
                        '3-Chlorotyrosine': 20.72,
                        'Theophylline': 14.64,
                        'm-Aminobenzoic acid': 13.64,
                        'Aspartame': 10.78,
                        'Salicylic acid': 18.05,
                        'Aminocaproic acid': 9.78,
                        '3-Nitrotyrosine': [20.61, 23.10],
                        '2-Aminoisobutyric acid': 9.42,
                        'Alendronic acid': 2.74,
                        'Thyroxine': 26.03,
                        'Atenolol': 13.14,
                        'Metoprolol': 19.68,
                        'Salbutamol': [8.39, 11.73],
                        'Lisinopril': 8.05,
                        'Phenylpropanolamine': 15.13,
                        'Pseudoephedrine': 18.57,
                        'Caffeic acid': 18.94,
                        '3-Aminosalicylic acid': 13.70,
                        'Methionine Sulfoxide': [7.68, 7.99],
                        '2,3-Diaminoproprionic acid': 16.45,
                        '1-Phenylethylamine': 20.02,
                        'Imidazoleacetic acid': 10.78,
                        'm-Cresol': 24.04,
                        'o-Cresol': 23.81,
                        'N-Acetylputrescine': 7.76,
                        'Syringic acid': 17.82732582,
                        '6-Methyladenine': [12.18, 12.84],
                        'Methylcysteine': 9.48,
                        '2,4-Diamino-6-hydroxypyrimidine': 8.54,
                        'N-Methyl-a-aminoisobutyric acid': 13.46,
                        'Phenylephrine': 25.08,
                        'Desaminotyrosine': 17.16,
                        'L-Homocysteic acid': 4.74,
                        '2-Phenylglycine': 13.58,
                        'Cadaverine': 18.19,
                        '5-Methoxytryptophan': 12.06,
                        '2,4-Diaminobutyric acid': 16.01,
                        '3-Cresotinic acid': 18.40,
                        'N-methyl-D-aspartic acid': 8.31,
                        '6-Hydroxynicotinic acid': [12.75, 12.47],
                        'Naringenin': 22.11,
                        'Canavanine': [12.35, 12.30],
                        'Cysteamine': 11.40,
                        'Aniline': 18.31,
                        'Biocytin': 7.41,
                        'Guanidinosuccinic acid': 3.48,
                        'Chlorogenic acid': [17.73, 19.18],
                        '1-Methylguanine': 9.94,
                        'Indole-3-carboxylic acid': 17.28,
                        'Symmetric dimethylarginine': 3.91,
                        'Oxidized glutathione': 14.30,
                        'Hydroxylamine': 9.70,
                        '5-Aminopentanoic acid': 8.73,
                        'D-Glutamine': 5.94,
                        'L-Histidinol': 7.42,
                        '4-Guanidinobutanoic acid': [4.51, 7.04],
                        '3,5-Diiodo-L-tyrosine': [13.31, 22.61],
                        'Beta-Leucine': [12.16, 17.98],
                        '3-Aminoisobutanoic acid': [9.21, 14.83],
                        '5-Methoxytryptamine': 16.29,
                        'Selenocystine': 15.00,
                        'Diethanolamine': 4.60,
                        '2,4-Dichlorophenol': 24.61,
                        '4-Hydroxy-3-methylbenzoic acid': 17.89,
                        'Alpha-Aspartyl-lysine': 12.22,
                        'Benzocaine': 16.12,
                        'o-Tyrosine': 21.52,
                        'L-phenylalanyl-L-proline': 12.92,
                        'Gamma Glutamylglutamic acid': 5.48,
                        'Leucyl-phenylalanine': 15.85,
                        'Phenylalanylphenylalanine': 15.57,
                        'Alanyl-Histidine': 12.68,
                        'Alanyl-Leucine': 11.43,
                        'Alanyl-Phenylalanine': 12.05,
                        'Alanyl-Tryptophan': 11.60,
                        'Alanyl-Tyrosine': 20.22,
                        'Arginyl-Phenylalanine': 6.90,
                        'Glycyl-Isoleucine': 11.65,
                        'Glycyl-Phenylalanine': 9.79,
                        'Glycyl-Tryptophan': 10.70,
                        'Glycyl-Tyrosine': 18.52,
                        'Glycyl-Valine': 9.44,
                        'Histidinyl-Alanine': 11.74,
                        'Leucyl-Proline': 14.26,
                        'Leucyl-Tryptophan': 14.88,
                        'Leucyl-Tyrosine': 22.96,
                        'Phenylalanyl-Alanine': 11.06,
                        'Phenylalanyl-Glycine': 9.34,
                        'Phenylalanyl-Methionine': 12.92,
                        'Phenylalanyl-Tyrosine': 23.60,
                        'Phenylalanyl-Valine': 14.19,
                        'Serinyl-Leucine': 9.63,
                        'Serinyl-Phenylalanine': 9.83,
                        'Threoninyl-Leucine': 10.46,
                        'Tryptophyl-Glutamate': 9.48,
                        'Tryptophyl-Leucine': 14.34,
                        'Tryptophyl-Phenylalanine': 14.48,
                        'Tryptophyl-Tyrosine': 23.34,
                        'Tyrosyl-Alanine': 20.05,
                        'Tyrosyl-Glycine': 18.92,
                        'Tyrosyl-Leucine': 22.42,
                        'Tyrosyl-Valine': 21.82,
                        '4-Ethylphenol': 23.82,
                        '2,3,4-Trihydroxybenzoic acid': 21.20,
                        '3,5-Dimethoxyphenol': 22.15,
                        'Isovanillic acid': 17.63,
                        'Gly-Gly-Gly-Gly': 3.68,
                        'Trp-Gly-Gly': 8.28,
                        'Gly-Norvaline': 9.53,
                        'Gly-Norleucine': 10.43,
                        'Phenyl-Leucine': 18.91,
                        'Phe-Phe-Phe': 17.57}  # 화학종 이름과 예측 RT 대응
        data = []
        standarddata = self.Fittable.rowCount()  # 셀 내용 가져오는 코드.
        for i in range(0, standarddata):
            data.append(float(self.Fittable.item(i, 1).text()))  # standard RT를 하나의 리스트로
        if data is not None:
            standard = np.array(data)  # 이것을 numpy array로 변경
            original = []  # 화학종에 대응되는 예측 RT 띄우기. 만일 둘의 길이가 다르다면 에러메시지 띄우기
            # for 문 활용해서 빈 리스트 채워넣기
            for i in range(0, standarddata):
                pred_rt = pred_rt_name[str(self.Fittable.item(i, 0).text())]
                original.append(pred_rt)
            predict = np.array(original)

            z = np.polyfit(predict, standard, 1)
            p = np.poly1d(z)

            x = np.arange(0, 31.01, 0.01)

            self.fig2.clear()

            ax = self.fig2.add_subplot(111)
            ax.plot(x, p(x), c="red", label='RT Fit function')
            ax.scatter(predict, standard, c="green", s=30, label='Standard fit')
            for i, v in enumerate(predict):
                ax.annotate('(%.2f, %.2f)' % (v, standard[i]), xy=(v, standard[i]), fontsize=10)
                # ax.text(v, predict[i], (v, predict[i]), color='blue', fontsize=10,
                #         horizontalalignment='center', verticalalignment='bottom')
            ax.set_xlim(0, 35)
            ax.set_ylim(0, 30)
            ax.grid()
            ax.axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
            ax.axes.yaxis.set_major_locator(ticker.MultipleLocator(5))
            ax.axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))
            ax.axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
            ax.set_xlabel("Predicted RT")
            ax.set_ylabel("Your experimental RT")
            ax.set_title("Predicted RT vs Your experimental RT")
            self.fig2.tight_layout()

            self.canvas2.draw()

            mplcursors.cursor(ax.plot(x, p(x), c="red", label='RT Fit function'), hover=True)
            # fit 결과 그래프로 띄우기
        else:  # 데이터 입력하라고 창 띄우기. 근데 창이 안 뜸
            QtWidgets.QMessageBox.critical(Qt.qApp.activeWindow(), " ", "Please enter the data")

    def fitrt(self):
        global predict, standard
        pred_rt_name = {'1-Methylhistidine': 7.97,
                        '1,3-Diaminopropane': [3.91, 18.96],
                        'p-Hydroxyphenylacetic acid': 17.19,
                        'Iodotyrosine': 19.07,
                        '3-Methoxytyramine': 24.56,
                        'Adenosine monophosphate': 3.80,
                        'Adenosine': 4.48,
                        'Ammonia': 9.14,
                        'Beta-Alanine': 7.35,
                        'Creatine': 3.58,
                        'D-Pipecolic acid': 11.48,
                        'Deoxyguanosine': 8.13,
                        'Dimethylamine': 14.82,
                        'Cytidine': [4.17, 9.86],
                        'Cytidine monophosphate': [2.95, 3.55],
                        'L-Cystathionine': [14.23, 14.38],
                        'Deoxyadenosine': 8.06,
                        'Gamma-Aminobutyric acid': [8.53, 14.80],
                        'Homovanillic acid': 17.38,
                        'Glycine': 6.94,
                        'Guanidoacetic acid': 3.56,
                        'Homogentisic acid': 22.51,
                        'Guanosine': 4.66,
                        'L-Glutamic Acid': [7.56, 10.90],
                        'Ethanolamine': 5.18,
                        'Gentisic acid': [17.14, 22.89],
                        'Estriol': 23.24,
                        'Hypoxanthine': [4.05, 9.14, 10.20],
                        'L-Tyrosine': 21.32,
                        'L-Phenylalanine': 13.45,
                        'L-Alanine': 7.96,
                        'L-Proline': 11.17,
                        'Methylamine': 9.92,
                        'L-Threonine': 6.05,
                        'L-Asparagine': [4.45, 8.69],
                        'L-Isoleucine': 13.63,
                        'L-Histidine': 11.6190443,
                        'L-Lysine': 16.02,
                        'L-Serine': 4.70,
                        'L-Aspartic Acid': 5.64,
                        'L-Cystine': 14.88,
                        'N6-Acetyl-L-Lysine': 8.10,
                        'Pantothenic acid': 11.12,
                        'Ornithine': 16.09,
                        'O-Phosphoethanolamine': 2.83,
                        'Phenol': 23.03,
                        'Sepiapterin': 7.53,
                        'Pyridoxine': [10.71, 16.75],
                        'Taurine': 4.60,
                        'Serotonin': 22.52,
                        'Thymine': 12.02,
                        'Liothyronine': 18.60,
                        'CNCC(=O)O': 8.09,
                        'Sarcosine': [4.83, 8.38],
                        'Saccharopine': [14.58, 18.32],
                        'Xanthine': 9.47,
                        'Uridine': [7.34, 10.93],
                        'Uracil': 11.04,
                        'Urocanic acid': 12.38,
                        'Tryptamine': 16.26,
                        'Tyramine': 23.92,
                        '17-Epiestriol': 23.24,
                        '2-Amino-3-phosphonopropionic acid': 3.13,
                        '2-Pyrocatechuic acid': 17.26,
                        '3-Hydroxyphenylacetic acid': 16.92,
                        'N-Alpha-acetyllysine': 7.57,
                        '5-Hydroxylysine': 13.26,
                        'L-Alpha-aminobutyric acid': 9.67,
                        'Allocystathionine': [14.23, 14.38],
                        'Biopterin': 7.25,
                        '5-Hydroxymethyluracil': 8.91,
                        '6-Dimethylaminopurine': 15.99,
                        '3-methyl-histidine': 6.88,
                        'Vanillic acid': 17.57,
                        '4-Hydroxybenzoic acid': 17.29,
                        '5-Hydroxy-L-tryptophan': 19.96,
                        'Aminoadipic acid': 8.30,
                        'L-Arginine': 3.84,
                        'L-Alloisoleucine': 13.63,
                        'Cysteine': 10.16,
                        'Glucosamine 6-sulfate': 3.36,
                        'Epinephrine': [9.16, 8.85, 9.19],
                        'Cytosine': 9.33,
                        'L-Glutamine': 5.94,
                        'D-Alpha-aminobutyric acid': 9.67,
                        'L-Thyroine': 22.48,
                        'Ortho-Hydroxyphenylacetic acid': 16.75,
                        'Homo-L-arginine': 3.41,
                        'L-Homocystine': 14.35,
                        'Homocitrulline': 4.29,
                        'L-Kynurenine': [11.60, 14.17],
                        'L-leucine': 12.82,
                        'L-Methionine': 10.60,
                        'Isoxanthopterin': [10.02, 10.34],
                        'L-Aspartyl-L-phenylalanine': 10.41,
                        'Hippuric acid': 12.05,
                        'L-Pipecolic acid': 11.48,
                        'L-Homoserine': [6.28, 10.81],
                        'Glycylproline': 7.54,
                        'Trans-4-Hydroxyl-L-Proline': 8.20,
                        'Indoleacrylic acid': 17.85,
                        '3-Hydroxymandelic acid': [14.54, 22.89],
                        'Hydroxyphenyllactici acid': 14.33,
                        'Glycyl-L-Leucine': 10.06,
                        '5-Hydroxyindoleacetic acid': 14.60,
                        'Normetanephrine': 21.35,
                        'Salicyluric acid': 10.25,
                        'Xanthurenic acid': [14.24, 23.58],
                        'L-Valine': 11.23,
                        'Ribothymidine': [6.83, 7.77, 10.35],
                        '7-Methylguanine': 9.64,
                        'Citrulline': 4.11,
                        'Deoxyadenosine monophosphate': 4.16,
                        'L-Tryptophan': 12.85,
                        'S-Adenosylhomocysteine': 11.23,
                        'trans-Ferulic acid': 18.57,
                        'Isoferulic acid': 18.42,
                        'pyrocatechol': 26.52,
                        'Hypotaurine': 4.89,
                        '5-Methylcytidine': [4.51, 5.28],
                        '2-aminooctanoic acid': 14.90,
                        "2'-Deoxyguanosine 5'-monophosphate": 4.15,
                        'Gamma-Glutamylcysteine': 8.63,
                        '2-Hydroxyphenethlamine': [12.84, 13.16],
                        '2-Phenylaminoadenosine': 7.45,
                        '2-Aminobenzoic acid': 14.52,
                        '5-Aminolevulinic acid': 8.35,
                        '4-Aminophenol': [15.74, 25.02],
                        "5'-Methylthioadenosine": 8.38,
                        'dCMP': 4.07,
                        '4-Nitrophenol': 23.91,
                        'N-Acetylserotonin': 14.05,
                        'Glucosamine 6-phosphate': 3.16,
                        'Spermidine': 13.04,
                        '3,4-Dihydroxybenzeneacetic acid': 22.80,
                        'ADP': 2.96,
                        'Diaminopimelic acid': [14.18, 14.03],
                        'p-Aminobenzoic acid': 13.28,
                        'Guanosine monophosphate': 3.51,
                        'Guaiacol': 21.92,
                        'Citicoline': [2.95, 3.08],
                        '1,4-diaminobutane': 18.92,
                        'Pyridoxamine': 21.58,
                        'Agmatine': [3.56, 14.29],
                        '3-Hydroxyanthranilic acid': 13.80,
                        'Methylguanidine': [4.12, 21.06],
                        'Imidazole': 14.47,
                        'Pyridoxal': 14.38,
                        'L-Norleucine': 12.54,
                        'm-Coumaric acid': 19.44,
                        'Aminopterin': 8.32,
                        'Guanidine': 3.73,
                        'Propranolol': 21.79,
                        '5-Hydroxytryptophol': 14.71,
                        'Protocatechuic acid': 23.03,
                        'p-Cresol': 24.25,
                        'Acetaminophen': 17.02,
                        '3-Methylhistamine': 6.92,
                        '3,4-Dihydroxymandelic acid': 19.94,
                        '4-Aminohippuric acid': 8.80,
                        '5-Methoxysalicylic acid': 17.74,
                        '3-Chlorotyrosine': 20.72,
                        'Theophylline': 14.64,
                        'm-Aminobenzoic acid': 13.64,
                        'Aspartame': 10.78,
                        'Salicylic acid': 18.05,
                        'Aminocaproic acid': 9.78,
                        '3-Nitrotyrosine': [20.61, 23.10],
                        '2-Aminoisobutyric acid': 9.42,
                        'Alendronic acid': 2.74,
                        'Thyroxine': 26.03,
                        'Atenolol': 13.14,
                        'Metoprolol': 19.68,
                        'Salbutamol': [8.39, 11.73],
                        'Lisinopril': 8.05,
                        'Phenylpropanolamine': 15.13,
                        'Pseudoephedrine': 18.57,
                        'Caffeic acid': 18.94,
                        '3-Aminosalicylic acid': 13.70,
                        'Methionine Sulfoxide': [7.68, 7.99],
                        '2,3-Diaminoproprionic acid': 16.45,
                        '1-Phenylethylamine': 20.02,
                        'Imidazoleacetic acid': 10.78,
                        'm-Cresol': 24.04,
                        'o-Cresol': 23.81,
                        'N-Acetylputrescine': 7.76,
                        'Syringic acid': 17.82732582,
                        '6-Methyladenine': [12.18, 12.84],
                        'Methylcysteine': 9.48,
                        '2,4-Diamino-6-hydroxypyrimidine': 8.54,
                        'N-Methyl-a-aminoisobutyric acid': 13.46,
                        'Phenylephrine': 25.08,
                        'Desaminotyrosine': 17.16,
                        'L-Homocysteic acid': 4.74,
                        '2-Phenylglycine': 13.58,
                        'Cadaverine': 18.19,
                        '5-Methoxytryptophan': 12.06,
                        '2,4-Diaminobutyric acid': 16.01,
                        '3-Cresotinic acid': 18.40,
                        'N-methyl-D-aspartic acid': 8.31,
                        '6-Hydroxynicotinic acid': [12.75, 12.47],
                        'Naringenin': 22.11,
                        'Canavanine': [12.35, 12.30],
                        'Cysteamine': 11.40,
                        'Aniline': 18.31,
                        'Biocytin': 7.41,
                        'Guanidinosuccinic acid': 3.48,
                        'Chlorogenic acid': [17.73, 19.18],
                        '1-Methylguanine': 9.94,
                        'Indole-3-carboxylic acid': 17.28,
                        'Symmetric dimethylarginine': 3.91,
                        'Oxidized glutathione': 14.30,
                        'Hydroxylamine': 9.70,
                        '5-Aminopentanoic acid': 8.73,
                        'D-Glutamine': 5.94,
                        'L-Histidinol': 7.42,
                        '4-Guanidinobutanoic acid': [4.51, 7.04],
                        '3,5-Diiodo-L-tyrosine': [13.31, 22.61],
                        'Beta-Leucine': [12.16, 17.98],
                        '3-Aminoisobutanoic acid': [9.21, 14.83],
                        '5-Methoxytryptamine': 16.29,
                        'Selenocystine': 15.00,
                        'Diethanolamine': 4.60,
                        '2,4-Dichlorophenol': 24.61,
                        '4-Hydroxy-3-methylbenzoic acid': 17.89,
                        'Alpha-Aspartyl-lysine': 12.22,
                        'Benzocaine': 16.12,
                        'o-Tyrosine': 21.52,
                        'L-phenylalanyl-L-proline': 12.92,
                        'Gamma Glutamylglutamic acid': 5.48,
                        'Leucyl-phenylalanine': 15.85,
                        'Phenylalanylphenylalanine': 15.57,
                        'Alanyl-Histidine': 12.68,
                        'Alanyl-Leucine': 11.43,
                        'Alanyl-Phenylalanine': 12.05,
                        'Alanyl-Tryptophan': 11.60,
                        'Alanyl-Tyrosine': 20.22,
                        'Arginyl-Phenylalanine': 6.90,
                        'Glycyl-Isoleucine': 11.65,
                        'Glycyl-Phenylalanine': 9.79,
                        'Glycyl-Tryptophan': 10.70,
                        'Glycyl-Tyrosine': 18.52,
                        'Glycyl-Valine': 9.44,
                        'Histidinyl-Alanine': 11.74,
                        'Leucyl-Proline': 14.26,
                        'Leucyl-Tryptophan': 14.88,
                        'Leucyl-Tyrosine': 22.96,
                        'Phenylalanyl-Alanine': 11.06,
                        'Phenylalanyl-Glycine': 9.34,
                        'Phenylalanyl-Methionine': 12.92,
                        'Phenylalanyl-Tyrosine': 23.60,
                        'Phenylalanyl-Valine': 14.19,
                        'Serinyl-Leucine': 9.63,
                        'Serinyl-Phenylalanine': 9.83,
                        'Threoninyl-Leucine': 10.46,
                        'Tryptophyl-Glutamate': 9.48,
                        'Tryptophyl-Leucine': 14.34,
                        'Tryptophyl-Phenylalanine': 14.48,
                        'Tryptophyl-Tyrosine': 23.34,
                        'Tyrosyl-Alanine': 20.05,
                        'Tyrosyl-Glycine': 18.92,
                        'Tyrosyl-Leucine': 22.42,
                        'Tyrosyl-Valine': 21.82,
                        '4-Ethylphenol': 23.82,
                        '2,3,4-Trihydroxybenzoic acid': 21.20,
                        '3,5-Dimethoxyphenol': 22.15,
                        'Isovanillic acid': 17.63,
                        'Gly-Gly-Gly-Gly': 3.68,
                        'Trp-Gly-Gly': 8.28,
                        'Gly-Norvaline': 9.53,
                        'Gly-Norleucine': 10.43,
                        'Phenyl-Leucine': 18.91,
                        'Phe-Phe-Phe': 17.57}  # 화학종 이름과 예측 RT 대응
        data = []
        standarddata = self.Fittable.rowCount()  # 셀 내용 가져오는 코드.
        for i in range(0, standarddata):
            data.append(float(self.Fittable.item(i, 1).text()))  # standard RT를 하나의 리스트로
        if data is not None:
            standard = np.array(data)  # 이것을 numpy array로 변경
            original = []  # 화학종에 대응되는 예측 RT 띄우기. 만일 둘의 길이가 다르다면 에러메시지 띄우기
            # for 문 활용해서 빈 리스트 채워넣기
            for i in range(0, standarddata):
                pred_rt = pred_rt_name[str(self.Fittable.item(i, 0).text())]
                original.append(pred_rt)
            predict = np.array(original)

        def fit(A, B):
            fp1 = np.polyfit(A, B, 1)
            f1 = np.poly1d(fp1)  # 관계식 f1
            return f1

        f1 = fit(predict, standard)  # fit 시킴
        total = pd.read_csv("RT_predict_confirm.csv")
        TotalRT = total['Predicted_RT']
        rt = self.InsertRT.text()

        def find_nearest(totalRT, fitRT):  # 가장 가까운 예상값 구하기
            totalRT = np.asarray(totalRT)
            idx = (np.abs(totalRT - fitRT)).argmin()
            return totalRT[idx]

        rt_key = find_nearest(TotalRT, f1(float(rt)))  # 가장 근접한 값 찾기. 이것을 key값으로 하기
        RT_pred = str(np.round(f1(float(rt)), 2))
        RT_pred_near = str(np.round(float(rt_key), 2))
        self.Fitresult.setText(RT_pred)
        self.Fitresult.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "AI Predictor of LC Retention Time for Dansylated Metabolites"))
        self.Predictmin.setText(_translate("MainWindow", "min"))
        self.Applysmi.setText(_translate("MainWindow", "Apply SMILES\n"
                                                       " to predict retention time"))
        self.Drawsketcher.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:14pt;\">Draw a structure in the sketcher below</span></p></body></html>"))
        self.PredictRT.setText(_translate("MainWindow", "Predicted retention time:"))
        self.Showall.setText(_translate("MainWindow", "Show all metabolites"))
        self.Smi.setText(_translate("MainWindow", "SMILES:"))
        self.Outlierdescription.setText(_translate("MainWindow", "There are outliers in scatter above.\n"
                                                                 "Outliers are these:\n"
                                                                 "3-methyl-histidine, L-Histidinol, 1-Methylhistidine, L-Histidine, Histidinyl-Alanine, Hippuric acid,\n"
                                                                 "Alanyl-Histidine, 3-Hydroxyanthranilic acid, Xanthurenic acid, Oxidized glutathione,\n"
                                                                 "2-aminooctanoic acid, Cadaverine, Caffeic acid, Iodotyrosine, and Naringenin."))
        self.Title.setText(_translate("MainWindow", "AI Predictor of LC Retention Time for \n"
                                                    "Dansylated Metabolites"))
        self.Outlier.setText(_translate("MainWindow", "About outlier:"))
        self.Showspecific.setText(_translate("MainWindow", "Show specific metabolites"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RTpredict),
                                  _translate("MainWindow", "Retention time predict"))
        self.Title_fit.setText(_translate("MainWindow", "AI Predictor of LC Retention Time for \n"
                                                        "Dansylated Metabolites"))
        self.Entermin.setText(_translate("MainWindow", "min"))
        self.Calculate.setText(_translate("MainWindow", "Calculate!"))
        self.FitRT.setText(_translate("MainWindow", "Fit retention time"))
        self.FindRT.setText(_translate("MainWindow", "Find predicted retention time"))
        self.Fitmin.setText(_translate("MainWindow", "min"))
        self.EnterRT.setText(_translate("MainWindow", "Enter Predicted retention time"))
        self.FittedRT.setText(_translate("MainWindow", "Fitted retention time\n(Excepted experimental retention time)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RTfit), _translate("MainWindow", "Retention time fit"))


from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
