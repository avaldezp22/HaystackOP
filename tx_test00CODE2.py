#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tx Test00Code2
# Generated: Tue Jul 16 23:33:35 2019
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

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import time
import wx


class tx_test00CODE2(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Tx Test00Code2")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.gain2 = gain2 = 5
        self.gain1 = gain1 = 5
        self.gain0 = gain0 = 10
        self.freq = freq = 25000000

        ##################################################
        # Blocks
        ##################################################
        _gain2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain2_sizer,
        	value=self.gain2,
        	callback=self.set_gain2,
        	label='gain2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain2_sizer,
        	value=self.gain2,
        	callback=self.set_gain2,
        	minimum=0,
        	maximum=30,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain2_sizer)
        _gain1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain1_sizer,
        	value=self.gain1,
        	callback=self.set_gain1,
        	label='gain1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain1_sizer,
        	value=self.gain1,
        	callback=self.set_gain1,
        	minimum=0,
        	maximum=30,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain1_sizer)
        _gain0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain0_sizer,
        	value=self.gain0,
        	callback=self.set_gain0,
        	label='gain0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain0_sizer,
        	value=self.gain0,
        	callback=self.set_gain0,
        	minimum=0,
        	maximum=30,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain0_sizer)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=10000000,
        	maximum=100000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=172.16.5.189", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(3),
        	),
        )
        self.uhd_usrp_sink_0.set_clock_rate(125000000, uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_sink_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_sink_0.set_samp_rate(1000000)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(gain0, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_center_freq(freq, 1)
        self.uhd_usrp_sink_0.set_gain(gain1, 1)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_sink_0.set_center_freq(freq, 2)
        self.uhd_usrp_sink_0.set_gain(gain2, 2)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 2)
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_c((numpy.fromfile('/home/alex/HaystackOP/waveforms/code-l10000-b10-000002.bin',dtype=numpy.complex64)).tolist(), True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_c((numpy.fromfile('/home/alex/HaystackOP/waveforms/code-l10000-b10-000001.bin',dtype=numpy.complex64)).tolist(), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c((numpy.fromfile('/home/alex/digital_rf/python/examples/sounder/waveforms/code-l10000-b10-000000.bin',dtype=numpy.complex64)).tolist(), True, 1, [])



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_vector_source_x_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.uhd_usrp_sink_0, 1))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.uhd_usrp_sink_0, 2))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_gain2(self):
        return self.gain2

    def set_gain2(self, gain2):
        self.gain2 = gain2
        self._gain2_slider.set_value(self.gain2)
        self._gain2_text_box.set_value(self.gain2)
        self.uhd_usrp_sink_0.set_gain(self.gain2, 2)


    def get_gain1(self):
        return self.gain1

    def set_gain1(self, gain1):
        self.gain1 = gain1
        self._gain1_slider.set_value(self.gain1)
        self._gain1_text_box.set_value(self.gain1)
        self.uhd_usrp_sink_0.set_gain(self.gain1, 1)


    def get_gain0(self):
        return self.gain0

    def set_gain0(self, gain0):
        self.gain0 = gain0
        self._gain0_slider.set_value(self.gain0)
        self._gain0_text_box.set_value(self.gain0)
        self.uhd_usrp_sink_0.set_gain(self.gain0, 0)


    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 1)
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 2)


def main(top_block_cls=tx_test00CODE2, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
