# CS5 Gold, Lab 3
# Filename: hw3pr1.py
# Name: Lawrence Mao
# Problem description: Lab 3 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # needed in 2015
# if you are having trouble, comment out the above line...

# a function to get started with a reminder 
# about list comprehensions...
def three_ize( L ):
    """ three_ize is the motto of the green CS 5 alien.
        It's also a function that takes in a list and
        returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [ 3 * x for x in L ]
    return LC

# Function to write #1:  scale
def scale(L, scale_factor):
    """
        Using list comprehension, multiply all L by scal_factor
    """
    LC = [scale_factor * x for x in L]
    return LC

# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index( L ):
    """ three_ize_by_index has the same I/O behavior as three_ize
        but it uses the INDEX of each element, instead of
        using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [ 3 * L[i] for i in range(N) ]
    return LC

# Function to write #2:  add_2
def add_2(L, M):
    N = min( len(L), len(M) )
    LC = [L[i]+M[i] for i in range(N)]
    return LC
def add_2_e(L,M):
    large = max([len(L),L],[len(M),M])
    small = min([len(L),L],[len(M),M])
    dif = large[0] - small[0]
    newList = small[1] + [0] * dif
    return add_2(newList,large[1])

# Function to write #3:  add_3
def add_3(L, M, P):
    N = min( len(L), len(M), len(P) )
    LC = [  L[i]+M[i]+P[i] for i in range(N)]
    return LC

# Function to write #4:  add_scale_2
def add_scale_2(L, M, L_scale, M_scale):
    R = min(len(L),len(M))
    LC = [L[i] * L_scale + M[i] * M_scale for i in range(R)]
    return LC

def add_scale_3(L, M, P, L_scale, M_scale, P_scale):
    R = min(len(L),len(M),len(P))
    LC = [L[i] * L_scale + M[i] * M_scale + P[i] * P_scale for i in range(R)]
    return LC

# Helper function:  randomize
def randomize( x, chance_of_replacing ):
    """ randomize takes in an original value, x
        and a fraction named chance_of_replacing.

        With the "chance_of_replacing" chance, it
        should return a random float from -32767 to 32767.

        Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0,1)
    if r < chance_of_replacing:
        return random.uniform(-32768,32767)
    else:
        return x

# Function to write #5:  replace_some
def replace_some(L, chance_of_replacing):
    LC = [randomize(x,chance_of_replacing) for x in L]
    return LC

#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """ a test function that plays swfaith.wav
        You'll need swfailt.wav in this folder.
    """
    play( 'swfaith.wav' )

    
# The example changeSpeed function
def changeSpeed(filename, newsr):
    """ changeSpeed allows the user to change an audio file's speed
        input: filename, the name of the original file
               newsr, the new sampling rate in samples per second
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print("Playing the original sound...")
    play(filename)
    
    sound_data = [0,0]            # an "empty" list
    read_wav(filename,sound_data) # get data INTO sound_data
    
    samps = sound_data[0]         # the raw pressure samples
    
    print( "The first 10 sound-pressure samples are\n", samps[:10])
    sr = sound_data[1]            # the sampling rate, sr
    
    print( "The number of samples per second is", sr)
    
    # we don't really need this line, but for consistency...
    new_sound_data = [ newsamps, newsr ]   # new sound data pair
    write_wav( new_sound_data, "out.wav" ) # write data to out.wav
    print("\nPlaying new sound...")
    play( 'out.wav' )   # play the new file, 'out.wav'
    


def flipflop(filename):
    """ flipflop swaps the halves of an audio file
        input: filename, the name of the original file
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print( "Playing the original sound...")
    play(filename)
    
    print( "Reading in the sound data...")
    sound_data = [0,0]
    read_wav(filename,sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    
    print( "Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr
    new_sound_data = [ newsamps, newsr ]
    
    print( "Writing out the new sound data...")
    write_wav( new_sound_data, "out.wav" ) # write data to out.wav
    
    print( "Playing new sound...")
    play( 'out.wav' )




# Sound function to write #1:  reverse
def reverse(filename):
    """
    the sampling rate should not change, but the function should create a reversed set of sound samples 
    and then handle them in the same way as the two examples above. That is, you'll want to write them 
    to the file out.wav and then play that file.
    """
    print( "Playing the original sound...")
    play(filename)
    
    print( "Reading in the sound data...")
    sound_data = [0,0]
    read_wav(filename,sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    
    print( "Computing new sound...")
    newsamps = samps[len(samps)::-1]
    newsr = sr
    new_sound_data = [ newsamps, newsr ]
    
    print( "Writing out the new sound data...")
    write_wav( new_sound_data, "out.wav" ) # write data to out.wav
    
    print( "Playing new sound...")
    play( 'out.wav' )

# Sound function to write #2:  volume
def volume(filename,scale_factor):
    """
    volume takes in a filename as usual and a floating-point value scale_factor. Then, volume should handle the sound 
    in the usual way, with the output file and played sound being scaled in amplitude (volume) by the scaling factor 
    scale_factor. That is, each sample should be multiplied by scale_factor.
    """
    print( "Playing the original sound...")
    play(filename)
    
    print( "Reading in the sound data...")
    sound_data = [0,0]
    read_wav(filename,sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    
    print( "Computing new sound...")
    newsamps = scale(samps,scale_factor)
    newsr = sr
    new_sound_data = [ newsamps, newsr ]
    
    print( "Writing out the new sound data...")
    write_wav( new_sound_data, "out.wav" ) # write data to out.wav
    
    print( "Playing new sound...")
    play( 'out.wav' )

# Sound function to write #3:  static
def static(filename, probability_of_static):
    """
    static takes in a filename as usual and a floating-point value probability_of_static, which you can assume will be between 0 and 1.
    Then, static should handle the sound in the usual way, with the output samples being replaced with the probability of 
    probability_of_static. When they're replaced, the samples should simply be random values, uniformly chosen in the valid range 
    from -32768 to 32767.
    """
    print( "Playing the original sound...")
    play(filename)
    
    print( "Reading in the sound data...")
    sound_data = [0,0]
    read_wav(filename,sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    
    print( "Computing new sound...")
    newsamps = replace_some(samps,probability_of_static)
    newsr = sr
    new_sound_data = [ newsamps, newsr ]
    
    print( "Writing out the new sound data...")
    write_wav( new_sound_data, "out.wav" ) # write data to out.wav
    
    print( "Playing new sound...")
    play( 'out.wav' )

# Sound function to write #4:  overlay
def overlay(filename1, filename2):
    """
    overlay takes in two filenames as usual, and it creates a new sound that overlays the two. The result should be as 
    long as the shorter of the two. (Drop any extra samples, just as in add_scale_2.)
    """
    print( "Playing the original sounds...")
    play(filename1)
    play(filename2)
    
    print( "Reading in the sound data...")
    sound_data_1 = [0,0]
    read_wav(filename1,sound_data_1)
    samps_1 = sound_data_1[0]
    sr = sound_data_1[1]

    sound_data_2 = [0,0]
    read_wav(filename2,sound_data_2)
    samps_2 = sound_data_2[0]
    sr = sound_data_2[1]
   
    print( "Computing new sound...")
    newsamps = add_scale_2(samps_1,samps_2,0.5,0.5)
    newsr = sr
    new_sound_data = [ newsamps, newsr ]
    
    print( "Writing out the new sound data...")
    write_wav( new_sound_data, "out.wav" ) # write data to out.wav
    
    print( "Playing new sound...")
    play( 'out.wav' )

# Sound function to write #5:  echo
def echo(filename, time_delay):
    """
    echo takes in a filename as usual and a floating-point value time_delay, which represents a number of seconds.
    Then, echo should handle the sound in the usual way, with the original sound being overlaid by a copy of itself 
    shifted forward in time by time_delay.
    """
    print( "Playing the original sound...")
    #play(filename)
    
    print( "Reading in the sound data...")
    sound_data = [0,0]
    read_wav(filename,sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    
    print( "Computing new sound...")
    delay = time_delay * sr
    samps2 = int(delay) * [0] + sound_data[0]
    newsamps = add_scale_2(samps,samps2,1,0.5)
    newsr = sr
    new_sound_data = [ newsamps, newsr ]
    
    print( "Writing out the new sound data...")
    write_wav( new_sound_data, "out.wav" ) # write data to out.wav
    
    print( "Playing new sound...")
    play( 'out.wav' )

# Helper function for generating pure tones
def gen_pure_tone(freq, seconds, sound_data):
    """ pure_tone returns the y-values of a cosine wave
        whose frequency is cyclespersec hertz
        it returns nsamples values, taken once every 1/44100 of a second
        thus, the sampling rate is 44100 hertz
        0.5 second (22050 samples) is probably enough
    """
    if sound_data != [0,0]:
        print("Please input a value of [0,0] for sound_data.")
        return
    sampling_rate = 22050
    # how many data samples to create
    nsamples = int(seconds*sampling_rate) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sampling_rate   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    sound_data[0] = [ a*math.sin(f*n*freq) for n in range(nsamples) ]
    sound_data[1] = sampling_rate
    return sound_data


def pure_tone(freq, time_in_seconds):
    """ swaps the 2nd half with the 1st half """
    print("Generating tone...")
    sound_data = [0,0]
    gen_pure_tone(freq, time_in_seconds, sound_data)
    
    print("Writing out the sound data...")
    write_wav( sound_data, "out.wav" ) # write data to out.wav
    
    print("Playing new sound...")
    play( 'out.wav' )




# Sound function to write #6:  chord
def chord(f1, f2, f3, time_in_seconds):
    """
    The final lab problem is to build on the above example to write a chord-creation function named chord with the following signature:
    def chord(f1, f2, f3, time_in_seconds): 
    such that chord takes in three floating-point frequencies f1, f2, and f3, along with a floating-point time_in_seconds.
    """
    samps1, sr1 = gen_pure_tone( f1, time_in_seconds, [0,0] )
    samps2, sr2 = gen_pure_tone( f2, time_in_seconds, [0,0] )
    samps3, sr3 = gen_pure_tone( f3, time_in_seconds, [0,0] )
    newsamps = add_scale_3(samps1, samps2, samps3, .1, .1, .1)
    newsr = sr1
    new_sound_data = [ newsamps, newsr ]
    
    print( "Writing out the new sound data...")
    write_wav( new_sound_data, "out.wav" ) # write data to out.wav
    
    print( "Playing new sound...")
    play( 'out.wav' )