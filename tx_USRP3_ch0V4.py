#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tx Usrp3 Ch0V4
# Generated: Wed Jul 17 16:56:59 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import sys
import time
from gnuradio import qtgui


class tx_USRP3_ch0V4(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tx Usrp3 Ch0V4")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tx Usrp3 Ch0V4")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "tx_USRP3_ch0V4")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=172.16.5.189", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_sink_0.set_clock_rate(125000000, uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_sink_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_sink_0.set_subdev_spec("A:0 B:0", 0)
        self.uhd_usrp_sink_0.set_samp_rate(1250000)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0.set_center_freq(20000000, 0)
        self.uhd_usrp_sink_0.set_gain(30, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_center_freq(30000000, 1)
        self.uhd_usrp_sink_0.set_gain(30, 1)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 1)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_c((numpy.fromfile('/home/alex/HaystackOP/waveforms/code-l10000-b10-000000.bin',dtype=numpy.complex64)).tolist(), True, 1, [])
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_1 = analog.sig_source_c(1000000, analog.GR_CONST_WAVE, 0, 0.01, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(1000000, analog.GR_SIN_WAVE, 1.0*5000000, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.uhd_usrp_sink_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_multiply_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tx_USRP3_ch0V4")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


def main(top_block_cls=tx_USRP3_ch0V4, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
