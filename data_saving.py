import csv
import numpy as np 
import pmt
from gnuradio import gr

class selective_save(gr.sync_block):
    def __init__(self, filepath='output.csv', sampling_rate=1e6, median_symbols=100):
        gr.sync_block.__init__(
            self,
            name="Selective Save",
            in_sig=[np.float32],
            out_sig=None
        )
        self.filepath = filepath
        self.sampling_rate = sampling_rate
        self.duration_samples = int((50e-6) * self.sampling_rate)  # 100 us worth of samples
        self.median_symbols = median_symbols
        self.squelch_active = False
        self.sample_count = 0
        self.positive_phases = []
        self.negative_phases = []
        self.data_points = []
        self.csvfile = open(self.filepath, 'w', newline='')
        self.csvwriter = csv.writer(self.csvfile, delimiter=',')
        self.index = 1

    def work(self, input_items, output_items):
        in0 = input_items[0]
        ninput_items = len(in0)
        tags = self.get_tags_in_window(0, 0, ninput_items)

        # Check for squelch_sob tag to activate recording
        for tag in tags:
            key = pmt.symbol_to_string(tag.key)
            if key == 'squelch_sob':
                self.squelch_active = True
                self.sample_count = 0

        # If squelch is active and we haven't reached the desired duration, record data
        if self.squelch_active:
            end_idx = min(ninput_items, self.sample_count + self.duration_samples)
            for idx in range(self.sample_count, end_idx):
                value = in0[idx]
                # Only save values within -0.5 to 0.5
                if -0.15 <= value <= 0.15:
                    if value > 0:
                        self.positive_phases.append(value)
                    elif value < 0:
                        self.negative_phases.append(value)
            self.sample_count += ninput_items

            # Stop recording if we've reached the duration limit
            if self.sample_count >= self.duration_samples:
                self.squelch_active = False

        # Proceed with calculations if enough data points are collected
        if len(self.positive_phases) > self.median_symbols and len(self.negative_phases) > self.median_symbols:
            pos_quantile = np.median(self.positive_phases)
            neg_quantile = np.median(self.negative_phases)
            cfo = (pos_quantile + neg_quantile) / 2
            deviation = (pos_quantile - cfo)

            # Write calculations to CSV
            self.csvwriter.writerow([cfo, deviation])
            
            # Reset the lists
            self.positive_phases = []
            self.negative_phases = []

        return ninput_items

    def stop(self):
        self.csvfile.close()
        return True

