
# this script (almost) reproduces htk-mfccs with configuration  config_wav_to_mfcc_2 as used in the paper 
# A. Kruspe - BOOTSTRAPPING A SYSTEM FOR PHONEME RECOGNITION AND KEYWORD SPOTTING IN UNACCOMPANIED SINGING


import extract_mfcc_htk_way as essMFCC_
import HTKPython as HTK
import numpy as np
import matplotlib.pyplot as plt
import librosa
import sys
# In[11]:

########### extract mfcc with htk 

def doit(argv):
#     if len(argv) != 2:
#         sys.exit('usage: {} <audio_URI>'.format(argv[0]))
#     audio_URI  = argv[1]
    
    URImfcFile = 'HTK/vignesh.config_wav_to_mfcc_2' # for configuration MFCC_0_A_D_Z
    audio_URI = 'audio/vignesh.wav'
    
    URImfcFile = 'HTK/trick_me_vocal.config_wav_to_mfcc_2' # for configuration MFCC_0_A_D_Z
    audio_URI = '/Users/joro/Dropbox/HansensDataset/vocal_separated/trick_me_vocals.wav'
    
    URImfcFile = 'HTK/trick_me_acap.config_wav_to_mfcc_2' # for configuration MFCC_0_A_D_Z
    audio_URI = '/Users/joro/Dropbox/HansensDataset/aCappella/trick_me.wav'
    
    
    ### read mfccs extracted with htk
    HTKFeat_reader =  HTK.htk_open(URImfcFile, 'rb')
    htkMFCC = HTKFeat_reader.getall()
    htkMFCC = htkMFCC.T
    

    # dimension [d,t]
    print 'extracting mfccs for file {}...'.format(audio_URI)
    essMFCC = essMFCC_.extractor(audio_URI, 0.97) # the scale of the difference in essentia is very small compared to htk
    essMFCC = essMFCC[[1,2,3,4,5,6,7,8,9,10,11,12,0],:] # append energy at the end as it is in htk 
    
    delta_mfcc = librosa.feature.delta(essMFCC)
    delta_delta_mfcc = librosa.feature.delta(essMFCC, order=2)
    
    essMFCC = np.vstack((essMFCC, delta_mfcc))
    essMFCC = np.vstack((essMFCC, delta_delta_mfcc))
    
    # cepstral zero-mean
    essMFCC  = np.matrix(essMFCC)
    means = essMFCC.mean(axis=1)
    # if np.isnan(means).any(): # this hsould not happen
    #     print 'mean has nans'.format()
    
    essMFCC = essMFCC - means
    
    
    # plot without  deltas and delta deltas
    htkMFCC = htkMFCC[:12,:]
    essMFCC = essMFCC[:12,:]
    plot_mfccs_and_differernce(htkMFCC, essMFCC)


def plot_mfccs_and_differernce(htkMFCC, essMFCC):

    ''' 
    Plotting comparison of MFCCs and their difference
    ''' 
    
    fig, axis_array= plt.subplots(3, sharex=True)
    axis_array[0].imshow(essMFCC, aspect = 'auto', interpolation='none') # ignore enery
    # plt.colorbar(p)
    axis_array[0].set_title('essentia')
    
    axis_array[1].imshow(htkMFCC, aspect = 'auto', interpolation='none') # ignore enery
    # axis_array[1].imshow(htkMFCC[1:,:], aspect = 'auto', interpolation='none') # ignore enery
    # plt.colorbar(p)
    axis_array[1].set_title('htk')
    
    spectral_difference = np.abs(htkMFCC - essMFCC)
    p = axis_array[2].imshow(spectral_difference, aspect = 'auto', interpolation='none') # ignore enery
    plt.colorbar(p)
    plt.show()
    
    print np.sum(spectral_difference)

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


if __name__ == '__main__':
    doit(sys.argv)