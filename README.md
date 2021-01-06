# Ableton Operator AMS Wavetables
Some "massive" wavetables for Ableton Operator additive synthesis oscillators and a Python script to create new ones.
For explanation of how this works, please [check out my blog post](https://bartwronski.com/2021/01/05/converting-wavetables-to-ableton-operator-ams-waves/) about this idea and implementation and how it works.

Hopefully you'll learn something new about additive synthesis used in **Ableton**'s **Operator**s.

### Usage - wavetables

1. Download the AMS files - either one by one, or the zip file.
1. In **Ableton Live**, add an **Operator** device.
1. Navigate to the Oscillator wave.
![Selecting operator custom wavetable](https://github.com/bartwronski/AbletonOperatorAMSWavetables/blob/main/operator_custom_wavetable.jpg)
1. Drag and drop the selected AMS file onto the **Oscillator** window.
1. Enjoy wavetable sounds!

### Usage - creating new AMS waves (advanced)

1. Download Python 3 environment together with numpy and scipy packages. I recommend [Anaconda](https://www.anaconda.com/products/individual) on Windows.
1. Download the [wavetables_to_ableton.py script](https://github.com/bartwronski/AbletonOperatorAMSWavetables/blob/main/wavetables_to_ableton.py)
1. Put all your wavetables in wav files in some folder structure.
1. Check the wavetable wav sample length and structure and if necessary, modify the wavetables_to_ableton.py.
1. Run python wavetables_to_ableton.py *source_folder* *destination_folder*.
1. You should see a progress bars and see conversion happening for sucessive files. I hope no debugging will be necessary!
