# Dual Wave Transform

## My first DSP script
I create a clean signal using two constructive waves. 440Hz and 880Hz

Then I create a noise signal to introduce to the constructed wave.

Then I use the Fast Fourier Transform algorithm to isolate the frequencies of both the clean and corrupted waves.

I also use a positive mask to isolated only the positive frequencies.

Finally, I plot the graphs so that the differences in the clean and corrupted waves can be observed.