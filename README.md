Comparison of common MFCC variants
======================================

This is a humble attempt to reproduce the [htk](http://htk.eng.cam.ac.uk/) type of MFCC features with [essentia](http://essentia.upf.edu/). The MFCC extracted with essentia are compared to these extracted with htk and these extracted with 
 [librosa](http://librosa.github.io)  


See a complete tutorial how to [compute mfcc the htk way](https://github.com/MTG/essentia/blob/master/src/examples/tutorial/example_mfcc_the_htk_way.py) with essentia.

## Visualize  MFCCs with essentia's default and htk's default preset of parameters
 [ipython/jupyter notebook](https://github.com/georgid/mfcc-htk-an-librosa/blob/master/mfcc_parameters_comparison_essentia.ipynb)

to extract mfcc with htk check HTK/mfcc_extract_script

 
## Comparison of htk and librosa
We also compared how htk type of MFCCs differ from the ones extracted with [librosa](http://librosa.github.
io/librosa/generated/librosa.feature.mfcc.html?highlight=mfcc)
	 for this comparison [scirpt](https://github.com/georgid/mfcc-htk-an-librosa/blob/master/htk%20and%20librosa%20MFCC%20extract%20comparison.ipynb)

#### The differences are due to

- preempahsis (not done in librosa)
- liftering (not done in librosa)
- mel triangular filterbank is unit_sum in librosa and unit_max in htk


## Adjust many different parameters of mfcc
An example of how to compute different parameters of MFCCs in essentia: preemphasis, cepstral-mean normalization, deltas and acceleration, etc.
[example](https://github.com/georgid/mfcc-htk-an-librosa/blob/master/mfcc-htk-many-parameters.py)

## how to compute inverse MFCC
[ipython notebook](https://github.com/georgid/mfcc-htk-an-librosa/blob/master/inverse_mfccs.ipynb)


### More details in the [essentia news](http://essentia.upf.edu/news). 



## License
 Copyright (C) 2015  Music Technology Group - Universitat Pompeu Fabra  
 
 This notebook is free software: you can redistribute it and/or modify it under  
 the terms of the GNU Affero General Public License as published by the Free  
 Software Foundation (FSF), either version 3 of the License, or (at your  
 option) any later version.  
 
 This program is distributed in the hope that it will be useful, but WITHOUT  
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS  
 FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more  
 details.  
 
 You should have received a copy of the Affero GNU General Public License  
 version 3 along with this program.  If not, see http://www.gnu.org/licenses/  


For questions: georgi.dzhambazov@upf.edu
