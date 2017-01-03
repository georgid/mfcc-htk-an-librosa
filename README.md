## comparison of common MFCC variants

This is a humble attempt to reproduce the htk type of MFCC features with [essentia](http://essentia.upf.edu/).  
 for a tutorial how to extract htk see  [compute_htk_the_mfcc_way] (https://github.com/MTG/essentia/blob/master/src/examples/tutorial/example_inverse_mfccs.py)

### Comparison to librosa
We also compared how htk type of MFCCs differ from the ones extracted with [librosa](http://librosa.github.
io/librosa/generated/librosa.feature.mfcc.html?highlight=mfcc)
	 for this comparison [scirpt](https://github.com/georgid/mfcc-htk-an-librosa/blob/master/htk%20and%20librosa%20MFCC%20extract%20comparison.ipynb)

### The differences are due to: 

- preempahsis (not done in librosa)
- liftering (not done in librosa)
- mel triangualr filterbank is unit_sum in librosa and unit_max in htk

For questions: georgi.dzhambazov@upf.edu