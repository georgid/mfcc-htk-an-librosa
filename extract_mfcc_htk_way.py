#### this reproduces the way htk extracts MFCC with the default configuration:
# SOURCEFORMAT = WAV
# TARGETKIND = MFCC_0
# TARGETRATE = 100000.0
# SAVECOMPRESSED = T
# SAVEWITHCRC = T
# WINDOWSIZE = 250000.0
# USEHAMMING = T
# PREEMCOEF = 0
# NUMCHANS = 26
# CEPLIFTER = 22
# NUMCEPS = 12
# ENORMALISE = F
# HIFREQ=8000
import essentia
import essentia.standard as ess
import matplotlib.pyplot as plt
import numpy as np



# def preemph(x, alpha):
#     y = x[1:] - alpha * x[:-1]
#     return y


def preemph(x,alpha):
  y = np.array(x, copy=True)
  y[1:] -= alpha * y[:-1] # starting from 1 instead of 2 gives smaller error
  y[0] *= (1.0 - alpha)
  return y

def extractor(filename, PREEMPH):    

    fs = 44100
    audio = ess.MonoLoader(filename = filename, 
                                          sampleRate = fs)()
    # dynamic range expansion as done in HTK implementation
    audio = audio*2**15
    
    
    frameSize = 1102 # corresponds to htk default WINDOWSIZE = 250000.0
#     frameSize = 2048 # corresponds to htk default WINDOWSIZE = 464399.0 
 
    hopSize = 441 # corresponds to htk default TARGETRATE = 100000.0
    fftSize = 2048
    spectrumSize= fftSize//2+1
    zeroPadding = int(fftSize - frameSize)

    w = ess.Windowing(type = 'hamming', #  corresponds to htk default  USEHAMMING = T
                        size = frameSize, 
                        zeroPadding = zeroPadding,
                        normalized = False,
                        zeroPhase = False)

    spectrum = ess.Spectrum(size = fftSize)

    mfcc_htk = ess.MFCC(inputSize = spectrumSize,
                        type = 'magnitude', # htk uses mel filterbank magniude
                        warpingFormula = 'htkMel', # htk's mel warping formula
                        weighting = 'linear', # computation of filter weights done in Hz domain
                        highFrequencyBound = 8000, # corresponds to htk default
                        lowFrequencyBound = 0, # corresponds to htk default
                        numberBands = 26, # corresponds to htk default  NUMCHANS = 26
                        numberCoefficients = 13,
                        normalize = 'unit_max', # htk filter normaliation to have constant height = 1  
                        dctType = 3, # htk uses DCT type III
                        logType = 'log',
                        liftering = 22) # corresponds to htk default CEPLIFTER = 22

    preemph_filter = ess.IIR(numerator=[1.,-PREEMPH])
    mfccs = []
    # startFromZero = True, validFrameThresholdRatio = 1 : the way htk computes windows
    for i,frame in enumerate(ess.FrameGenerator(audio, frameSize = frameSize, hopSize = hopSize , startFromZero = True, validFrameThresholdRatio = 1)):
            
# WITH essentia preemph filter
#             frame_doubled_first = np.insert(frame,0,frame[0])  ##### if PREEMPHASIS needed
#             preemph_frame = preemph_filter(frame_doubled_first)
#             frame = preemph_frame[1:]
            
#         frame_doubled_first = np.insert(frame,0,frame[0])  ##### need an additional sample to compensate for the one lost in preemphasis
        frame = preemph(frame, PREEMPH)

        spect = spectrum(w(frame))
        mel_bands, mfcc_coeffs = mfcc_htk(spect)
        
        if np.isnan(mfcc_coeffs).any():
            print 'frame  {} has nans'.format(i)
            mfcc_coeffs = np.nan_to_num(mfcc_coeffs) #source separartion results in NaN MFCCs, extracted with essentia. workaround for NaNs -> to zero
          
        mfccs.append(mfcc_coeffs)

    # transpose to have it in a better shape
    # we need to convert the list to an essentia.array first (== numpy.array of floats)
    # mfccs = essentia.array(pool['MFCC']).T
    mfccs = essentia.array(mfccs).T

    # and plot
    # plt.imshow(mfccs[1:,:], aspect = 'auto', interpolation='none') # ignore enery
    # plt.imshow(mfccs, aspect = 'auto', interpolation='none')
    # plt.colorbar()
    # plt.show() # unnecessary if you started "ipython --pylab"
    return mfccs

# some python magic so that this file works as a script as well as a module
# if you do not understand what that means, you don't need to care
if __name__ == '__main__':
    import sys
    print 'Script %s called with arguments: %s' % (sys.argv[0], sys.argv[1:])

    try:
        extractor(sys.argv[1])
        print 'Success!'

    except KeyError:
        print 'ERROR: You need to call this script with a filename argument...'