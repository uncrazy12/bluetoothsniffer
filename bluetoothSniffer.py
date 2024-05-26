#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: edwin
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import soapy
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import bluetoothSniffer_epy_block_1_0 as epy_block_1_0  # embedded python block
import bluetoothSniffer_epy_block_1_0_0 as epy_block_1_0_0  # embedded python block
import bluetoothSniffer_epy_block_1_0_1 as epy_block_1_0_1  # embedded python block
import bluetoothSniffer_epy_block_1_0_2 as epy_block_1_0_2  # embedded python block
import bluetoothSniffer_epy_block_1_0_3 as epy_block_1_0_3  # embedded python block



from gnuradio import qtgui

class bluetoothSniffer(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "bluetoothSniffer")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 5e6
        self.vec_length = vec_length = 2048
        self.trigger = trigger = -15
        self.gain = gain = 20
        self.fft_length = fft_length = 2048
        self.center_freq = center_freq = 2440
        self.bandwith_channel = bandwith_channel = 1e6
        self.bandwidth = bandwidth = 6e6
        self.bandpass_filter = bandpass_filter = firdes.complex_band_pass(1.0, samp_rate, -500e3, 500e3, 50e3, window.WIN_HAMMING, 6.76)

        ##################################################
        # Blocks
        ##################################################
        self._trigger_range = Range(-100, 0, 1, -15, 200)
        self._trigger_win = RangeWidget(self._trigger_range, self.set_trigger, "trigger", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._trigger_win)
        self._gain_range = Range(0, 49, 1, 20, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "gain", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_win)
        self.soapy_hackrf_source_0 = None
        dev = 'driver=hackrf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_hackrf_source_0 = soapy.source(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_hackrf_source_0.set_sample_rate(0, 12e6)
        self.soapy_hackrf_source_0.set_bandwidth(0, 6e6)
        self.soapy_hackrf_source_0.set_frequency(0, 2432e6)
        self.soapy_hackrf_source_0.set_gain(0, 'AMP', True)
        self.soapy_hackrf_source_0.set_gain(0, 'LNA', min(max(gain, 0.0), 40.0))
        self.soapy_hackrf_source_0.set_gain(0, 'VGA', min(max(gain, 0.0), 62.0))
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.pfb_channelizer_ccf_1 = pfb.channelizer_ccf(
            6,
            firdes.low_pass(1, 12e6, 100e3, 500e3, window.WIN_HANN),
            2.0,
            100)
        self.pfb_channelizer_ccf_1.set_channel_map([])
        self.pfb_channelizer_ccf_1.declare_sample_delay(0)
        self.freq_xlating_fir_filter_xxx_3_0 = filter.freq_xlating_fir_filter_ccc(1, firdes.complex_band_pass(1, 4e6, -0.5e6, 0.5e6, 50e3, window.WIN_HAMMING), 0, 4e6)
        self.freq_xlating_fir_filter_xxx_3 = filter.freq_xlating_fir_filter_ccc(1, firdes.complex_band_pass(1, 4e6, -0.5e6, 0.5e6, 50e3, window.WIN_HAMMING), 0, 4e6)
        self.freq_xlating_fir_filter_xxx_2 = filter.freq_xlating_fir_filter_ccc(1, firdes.complex_band_pass(1, 4e6, -0.5e6, 0.5e6, 50e3, window.WIN_HAMMING), 0, 4e6)
        self.freq_xlating_fir_filter_xxx_1 = filter.freq_xlating_fir_filter_ccc(1, firdes.complex_band_pass(1, 4e6, -0.5e6, 0.5e6, 50e3, window.WIN_HAMMING), 0, 4e6)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, firdes.complex_band_pass(1, 4e6, -0.5e6, 0.5e6, 50e3, window.WIN_HAMMING), 0, 4e6)
        self.epy_block_1_0_3 = epy_block_1_0_3.selective_save(filepath="/home/edwin/Downloads/channel5_CFO_DEV.csv", sampling_rate=4e6, median_symbols=200)
        self.epy_block_1_0_2 = epy_block_1_0_2.selective_save(filepath="/home/edwin/Downloads/channel4_CFO_DEV.csv", sampling_rate=4e6, median_symbols=200)
        self.epy_block_1_0_1 = epy_block_1_0_1.selective_save(filepath="/home/edwin/Downloads/channel1_CFO_DEV.csv", sampling_rate=4e6, median_symbols=200)
        self.epy_block_1_0_0 = epy_block_1_0_0.selective_save(filepath="/home/edwin/Downloads/channel2_CFO_DEV.csv", sampling_rate=4e6, median_symbols=200)
        self.epy_block_1_0 = epy_block_1_0.selective_save(filepath="/home/edwin/Downloads/channel3_CFO_DEV.csv", sampling_rate=4e6, median_symbols=200)
        self.digital_gfsk_demod_0_2_0 = digital.gfsk_demod(
            samples_per_symbol=4,
            sensitivity=2.546479,
            gain_mu=0.175,
            mu=0.320,
            omega_relative_limit=0.005,
            freq_error=0.01,
            verbose=False,
            log=False)
        self.digital_gfsk_demod_0_2 = digital.gfsk_demod(
            samples_per_symbol=4,
            sensitivity=2.546479,
            gain_mu=0.175,
            mu=0.320,
            omega_relative_limit=0.005,
            freq_error=0.01,
            verbose=False,
            log=False)
        self.digital_gfsk_demod_0_1 = digital.gfsk_demod(
            samples_per_symbol=4,
            sensitivity=2.546479,
            gain_mu=0.175,
            mu=0.320,
            omega_relative_limit=0.005,
            freq_error=0.01,
            verbose=False,
            log=False)
        self.digital_gfsk_demod_0_0 = digital.gfsk_demod(
            samples_per_symbol=4,
            sensitivity=2.546479,
            gain_mu=0.175,
            mu=0.320,
            omega_relative_limit=0.005,
            freq_error=0.01,
            verbose=False,
            log=False)
        self.digital_gfsk_demod_0 = digital.gfsk_demod(
            samples_per_symbol=4,
            sensitivity=2.546479,
            gain_mu=0.175,
            mu=0.320,
            omega_relative_limit=0.005,
            freq_error=0.01,
            verbose=False,
            log=False)
        self._center_freq_tool_bar = Qt.QToolBar(self)
        self._center_freq_tool_bar.addWidget(Qt.QLabel("center_freq" + ": "))
        self._center_freq_line_edit = Qt.QLineEdit(str(self.center_freq))
        self._center_freq_tool_bar.addWidget(self._center_freq_line_edit)
        self._center_freq_line_edit.returnPressed.connect(
            lambda: self.set_center_freq(int(str(self._center_freq_line_edit.text()))))
        self.top_layout.addWidget(self._center_freq_tool_bar)
        self.blocks_sub_xx_0_3 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_2 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_repack_bits_bb_0_3 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_2 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_magphase_to_complex_0_3 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0_2 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0_1 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0_0 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0 = blocks.magphase_to_complex(1)
        self.blocks_file_sink_0_3 = blocks.file_sink(gr.sizeof_char*1, '/home/edwin/channel5.bin', False)
        self.blocks_file_sink_0_3.set_unbuffered(False)
        self.blocks_file_sink_0_2 = blocks.file_sink(gr.sizeof_char*1, '/home/edwin/channel4.bin', False)
        self.blocks_file_sink_0_2.set_unbuffered(False)
        self.blocks_file_sink_0_1 = blocks.file_sink(gr.sizeof_char*1, '/home/edwin/channel3.bin', False)
        self.blocks_file_sink_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/edwin/channel1.bin', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/edwin/channel2.bin', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_delay_0_3 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0_2 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_correctiq_0 = blocks.correctiq()
        self.blocks_complex_to_arg_1_3 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_1_2 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_1_1 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_1_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_1 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_3 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_2 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_1 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.analog_pwr_squelch_xx_0_2_0 = analog.pwr_squelch_cc(trigger, 100e-6, 0, True)
        self.analog_pwr_squelch_xx_0_2 = analog.pwr_squelch_cc(trigger, 1e-4, 0, True)
        self.analog_pwr_squelch_xx_0_1 = analog.pwr_squelch_cc(trigger, 1e-4, 0, True)
        self.analog_pwr_squelch_xx_0_0_0 = analog.pwr_squelch_cc(trigger, 100e-6, 0, True)
        self.analog_pwr_squelch_xx_0_0 = analog.pwr_squelch_cc(trigger, 100e-6, 0, True)
        self.analog_const_source_x_0_3 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0_2 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_magphase_to_complex_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_magphase_to_complex_0_0, 0))
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_magphase_to_complex_0_1, 0))
        self.connect((self.analog_const_source_x_0_2, 0), (self.blocks_magphase_to_complex_0_2, 0))
        self.connect((self.analog_const_source_x_0_3, 0), (self.blocks_magphase_to_complex_0_3, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0, 0), (self.freq_xlating_fir_filter_xxx_1, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0_1, 0), (self.freq_xlating_fir_filter_xxx_2, 0))
        self.connect((self.analog_pwr_squelch_xx_0_2, 0), (self.freq_xlating_fir_filter_xxx_3, 0))
        self.connect((self.analog_pwr_squelch_xx_0_2_0, 0), (self.freq_xlating_fir_filter_xxx_3_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0_1, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_complex_to_arg_0_1, 0), (self.blocks_sub_xx_0_1, 0))
        self.connect((self.blocks_complex_to_arg_0_2, 0), (self.blocks_delay_0_2, 0))
        self.connect((self.blocks_complex_to_arg_0_2, 0), (self.blocks_sub_xx_0_2, 0))
        self.connect((self.blocks_complex_to_arg_0_3, 0), (self.blocks_delay_0_3, 0))
        self.connect((self.blocks_complex_to_arg_0_3, 0), (self.blocks_sub_xx_0_3, 0))
        self.connect((self.blocks_complex_to_arg_1, 0), (self.epy_block_1_0, 0))
        self.connect((self.blocks_complex_to_arg_1_0, 0), (self.epy_block_1_0_0, 0))
        self.connect((self.blocks_complex_to_arg_1_1, 0), (self.epy_block_1_0_1, 0))
        self.connect((self.blocks_complex_to_arg_1_2, 0), (self.epy_block_1_0_2, 0))
        self.connect((self.blocks_complex_to_arg_1_3, 0), (self.epy_block_1_0_3, 0))
        self.connect((self.blocks_correctiq_0, 0), (self.pfb_channelizer_ccf_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_sub_xx_0_1, 1))
        self.connect((self.blocks_delay_0_2, 0), (self.blocks_sub_xx_0_2, 1))
        self.connect((self.blocks_delay_0_3, 0), (self.blocks_sub_xx_0_3, 1))
        self.connect((self.blocks_magphase_to_complex_0, 0), (self.blocks_complex_to_arg_1, 0))
        self.connect((self.blocks_magphase_to_complex_0_0, 0), (self.blocks_complex_to_arg_1_0, 0))
        self.connect((self.blocks_magphase_to_complex_0_1, 0), (self.blocks_complex_to_arg_1_1, 0))
        self.connect((self.blocks_magphase_to_complex_0_2, 0), (self.blocks_complex_to_arg_1_2, 0))
        self.connect((self.blocks_magphase_to_complex_0_3, 0), (self.blocks_complex_to_arg_1_3, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_file_sink_0_3, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_2, 0), (self.blocks_file_sink_0_2, 0))
        self.connect((self.blocks_repack_bits_bb_0_3, 0), (self.blocks_file_sink_0_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_magphase_to_complex_0, 1))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_magphase_to_complex_0_0, 1))
        self.connect((self.blocks_sub_xx_0_1, 0), (self.blocks_magphase_to_complex_0_1, 1))
        self.connect((self.blocks_sub_xx_0_2, 0), (self.blocks_magphase_to_complex_0_2, 1))
        self.connect((self.blocks_sub_xx_0_3, 0), (self.blocks_magphase_to_complex_0_3, 1))
        self.connect((self.digital_gfsk_demod_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.digital_gfsk_demod_0_0, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.digital_gfsk_demod_0_1, 0), (self.blocks_repack_bits_bb_0_3, 0))
        self.connect((self.digital_gfsk_demod_0_2, 0), (self.blocks_repack_bits_bb_0_2, 0))
        self.connect((self.digital_gfsk_demod_0_2_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_complex_to_arg_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.digital_gfsk_demod_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_1, 0), (self.blocks_complex_to_arg_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_1, 0), (self.digital_gfsk_demod_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_2, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_2, 0), (self.digital_gfsk_demod_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_3, 0), (self.blocks_complex_to_arg_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_3, 0), (self.digital_gfsk_demod_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_3, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_3_0, 0), (self.blocks_complex_to_arg_0_3, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_3_0, 0), (self.digital_gfsk_demod_0_2_0, 0))
        self.connect((self.pfb_channelizer_ccf_1, 1), (self.analog_pwr_squelch_xx_0_0, 0))
        self.connect((self.pfb_channelizer_ccf_1, 0), (self.analog_pwr_squelch_xx_0_0_0, 0))
        self.connect((self.pfb_channelizer_ccf_1, 2), (self.analog_pwr_squelch_xx_0_1, 0))
        self.connect((self.pfb_channelizer_ccf_1, 4), (self.analog_pwr_squelch_xx_0_2, 0))
        self.connect((self.pfb_channelizer_ccf_1, 5), (self.analog_pwr_squelch_xx_0_2_0, 0))
        self.connect((self.pfb_channelizer_ccf_1, 3), (self.blocks_null_sink_0, 0))
        self.connect((self.soapy_hackrf_source_0, 0), (self.blocks_correctiq_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "bluetoothSniffer")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_bandpass_filter(firdes.complex_band_pass(1.0, self.samp_rate, -500e3, 500e3, 50e3, window.WIN_HAMMING, 6.76))

    def get_vec_length(self):
        return self.vec_length

    def set_vec_length(self, vec_length):
        self.vec_length = vec_length

    def get_trigger(self):
        return self.trigger

    def set_trigger(self, trigger):
        self.trigger = trigger
        self.analog_pwr_squelch_xx_0_0.set_threshold(self.trigger)
        self.analog_pwr_squelch_xx_0_0_0.set_threshold(self.trigger)
        self.analog_pwr_squelch_xx_0_1.set_threshold(self.trigger)
        self.analog_pwr_squelch_xx_0_2.set_threshold(self.trigger)
        self.analog_pwr_squelch_xx_0_2_0.set_threshold(self.trigger)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.soapy_hackrf_source_0.set_gain(0, 'LNA', min(max(self.gain, 0.0), 40.0))
        self.soapy_hackrf_source_0.set_gain(0, 'VGA', min(max(self.gain, 0.0), 62.0))

    def get_fft_length(self):
        return self.fft_length

    def set_fft_length(self, fft_length):
        self.fft_length = fft_length

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        Qt.QMetaObject.invokeMethod(self._center_freq_line_edit, "setText", Qt.Q_ARG("QString", str(self.center_freq)))

    def get_bandwith_channel(self):
        return self.bandwith_channel

    def set_bandwith_channel(self, bandwith_channel):
        self.bandwith_channel = bandwith_channel

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth

    def get_bandpass_filter(self):
        return self.bandpass_filter

    def set_bandpass_filter(self, bandpass_filter):
        self.bandpass_filter = bandpass_filter




def main(top_block_cls=bluetoothSniffer, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
