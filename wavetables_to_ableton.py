import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import math
import sys
import os
from tqdm import tqdm


# Number of samples per single wavetable in a file.
WIN_LEN = 2048
# Starting sample of the wavetable. Some wav wavetables seem to have zeros at beginning of the file.
START_POS = 0
# How many harmonics to save
SAVE_RANGE = 64


def process_wavetable(dest_file, data):
  fft_d = np.abs(np.fft.fft(data-np.mean(data)))[1:WIN_LEN//2]
  fft_d = fft_d[0:SAVE_RANGE]
  # Normalize against the highest harmonic.
  fft_d = fft_d / np.max(fft_d)

  # AMS output string
  str='AMS 1\nGenerate MultiCycleFM\nBaseFreq 261.625549\nRootKey 60\nSampleRate 44100\nChannels 1\nBitsPerSample 32\nVolume Auto'

  for x in range(SAVE_RANGE):
    if fft_d[x] > 0.01:
      str += f'\nSine {x+1} {fft_d[x]:.2f}'
  f = open(dest_file, 'w')
  f.write(str)
  f.close()

def process_file(dest_dir, f):
  rate, data = scipy.io.wavfile.read(f)
  for i in tqdm(range(0, (len(data)-START_POS) // WIN_LEN)):
    data_window = data[START_POS + (i*WIN_LEN) : START_POS + (i+1)*WIN_LEN]
    process_wavetable(os.path.join(dest_dir, str(i)) + '.ams', data_window)

def main():
  if not os.path.isdir(sys.argv[2]):
    print(f'{sys.argv[2]} doesn\'t exist, creating it')
    os.mkdir(sys.argv[2])
  sub_dirs = [x for x in os.walk(sys.argv[1])]
  for sub_dir in sub_dirs:
    sub_dir_path = os.path.relpath(sub_dir[0], sys.argv[1])
    for f in sub_dir[2]:
      if f.lower().endswith('wav'):
        if not os.path.isdir(os.path.join(sys.argv[2], sub_dir_path)):
          os.mkdir(os.path.join(sys.argv[2], sub_dir_path))
        file_full_path = os.path.join(sub_dir[0], f)
        print(f'Processing {file_full_path}')
        rel_path = os.path.relpath(file_full_path, sys.argv[1])
        wavetable_dir = os.path.join(sys.argv[2], os.path.splitext(rel_path)[0])
        if not os.path.isdir(wavetable_dir):
          os.mkdir(wavetable_dir)
        process_file(wavetable_dir, file_full_path)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print('Usage python wavetables_to_ableton.py source_folder dest_folder')
    exit(-1)
  main()
