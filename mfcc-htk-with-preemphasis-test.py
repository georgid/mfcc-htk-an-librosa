
# coding: utf-8

# In[15]:

import extract_mfcc_htk_way as essMFCC_
import HTKPython as HTK
import numpy as np
import matplotlib.pyplot as plt


# In[11]:

########### extract filterbank with htk
URImfcFile = 'HTK/vignesh.config_wav_to_mfcc'
HTKFeat_reader =  HTK.htk_open(URImfcFile, 'rb')
htkMFCC = HTKFeat_reader.getall()
htkMFCC = htkMFCC.T
htkMFCC =htkMFCC[[-1,0,1,2,3,4,5,6,7,8,9,10,11],:]

URImfcFile_no_preemp = 'HTK/vignesh.config_wav_to_mfcc_0' # with cpestral  mean norm
HTKFeat_reader_no_preemp =  HTK.htk_open(URImfcFile_no_preemp, 'rb')
htkMFCC_no_preemp = HTKFeat_reader_no_preemp.getall()
htkMFCC_no_preemp = htkMFCC_no_preemp.T
htkMFCC_no_preemp =htkMFCC_no_preemp[[-1,0,1,2,3,4,5,6,7,8,9,10,11],:]


essMFCC_1 = essMFCC_.extractor('audio/vignesh.wav', 0) # putting zero is same as PREEMCOEF =  0 in htk
essMFCC_2 = essMFCC_.extractor('audio/vignesh.wav', 0.97) # the scale of the difference in essentia is very small compared to htk

# cepstral zero-mean
essMFCC_1  = np.matrix(essMFCC_1)
# essMFCC_1[1:,:] = essMFCC_1[1:,:] - essMFCC_1[1:,:].mean(axis=1) # htk does not normalize 0-cepstrum
essMFCC_1 = essMFCC_1 - essMFCC_1.mean(axis=1) # htk does maybe a bit different normalization of 0-th coefficient


# Plotting MFCCs with preemphasis in Essentia

# In[16]:


fig, axis_array= plt.subplots(3, sharex=True)
axis_array[0].imshow(essMFCC_1, aspect = 'auto', interpolation='none') # ignore enery
axis_array[0].set_title('essentia')

p = axis_array[1].imshow(htkMFCC_no_preemp, aspect = 'auto', interpolation='none') # ignore enery
# axis_array[1].imshow(htkMFCC_no_preemp[1:,:], aspect = 'auto', interpolation='none') # ignore enery

# plt.colorbar(p)
axis_array[1].set_title('htk')

p = axis_array[2].imshow(np.abs(htkMFCC_no_preemp - essMFCC_1), aspect = 'auto', interpolation='none') # ignore enery
plt.colorbar(p)
plt.show()

# Plotting MFCCs with preemphasis in HTK

# In[18]:

# Ploting HTK
plt.imshow(htkMFCC[1:,:], aspect = 'auto', interpolation='none') # ignore enery
plt.title('MFCC HTK')
plt.colorbar()
plt.show() # unnecessary if you started "ipython --pylab"


# Plotting the difference

# In[4]:

# Ploting Difference
plt.imshow(np.abs(essMFCC- htkMFCC[1:,:]), aspect = 'auto', interpolation='none') # ignore enery
plt.title('MFCC Difference')
plt.colorbar()
plt.show() # unnecessary if you started "ipython --pylab"

