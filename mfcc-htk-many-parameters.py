
# coding: utf-8

# In[15]:

import extract_mfcc_htk_way as essMFCC_
import HTKPython as HTK
import numpy as np
import matplotlib.pyplot as plt
import librosa

# In[11]:

########### extract filterbank with htk

URImfcFile_no_preemp = 'HTK/vignesh.config_wav_to_mfcc_2' # with cpestral  mean norm
HTKFeat_reader_no_preemp =  HTK.htk_open(URImfcFile_no_preemp, 'rb')
htkMFCC_no_preemp = HTKFeat_reader_no_preemp.getall()
htkMFCC_no_preemp = htkMFCC_no_preemp.T

# dimension [d,t]
essMFCC = essMFCC_.extractor('audio/vignesh.wav', 0) # putting zero is same as PREEMCOEF =  0 in htk
essMFCC = essMFCC_.extractor('audio/vignesh.wav', 0.97) # the scale of the difference in essentia is very small compared to htk
essMFCC = essMFCC[[1,2,3,4,5,6,7,8,9,10,11,12,0],:] # append energy at the end as in htk 

delta_mfcc = librosa.feature.delta(essMFCC)
delta_delta_mfcc = librosa.feature.delta(essMFCC, order=2)

essMFCC = np.vstack((essMFCC, delta_mfcc))
essMFCC = np.vstack((essMFCC, delta_delta_mfcc))

# cepstral zero-mean
essMFCC  = np.matrix(essMFCC)
essMFCC = essMFCC - essMFCC.mean(axis=1)




# Plotting comparison of MFCCs and their difference 

fig, axis_array= plt.subplots(3, sharex=True)
axis_array[0].imshow(essMFCC, aspect = 'auto', interpolation='none') # ignore enery
axis_array[0].set_title('essentia')

p = axis_array[1].imshow(htkMFCC_no_preemp, aspect = 'auto', interpolation='none') # ignore enery
# axis_array[1].imshow(htkMFCC_no_preemp[1:,:], aspect = 'auto', interpolation='none') # ignore enery

# plt.colorbar(p)
axis_array[1].set_title('htk')

p = axis_array[2].imshow(np.abs(htkMFCC_no_preemp - essMFCC), aspect = 'auto', interpolation='none') # ignore enery
plt.colorbar(p)
plt.show()


# In[18]:

# Ploting HTK only
# plt.imshow(htkMFCC[1:,:], aspect = 'auto', interpolation='none') # ignore enery
# plt.title('MFCC HTK')
# plt.colorbar()
# plt.show() # unnecessary if you started "ipython --pylab"


# Plotting the difference

# In[4]:

# Ploting Difference only
# plt.imshow(np.abs(essMFCC- htkMFCC[1:,:]), aspect = 'auto', interpolation='none') # ignore enery
# plt.title('MFCC Difference')
# plt.colorbar()
# plt.show() # unnecessary if you started "ipython --pylab"

