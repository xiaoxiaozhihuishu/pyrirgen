import os
import numpy as np
import soundfile as sf
from pyrirgen import generateRir

rir_length = 1024

c = 340
fs = 16000
mtype = 'omnidirectional'
order = -1                 # -1 equals maximum reflection order!
dim = 3                    # Room dimension
orientation = [0, 0]
hp_filter = 1

rev_time_source = 0.16

room_width_min = 4
room_width_max = 4
room_length_min = 4
room_length_max = 4
room_height_min = 4
room_height_max = 4
room_size = [4,4,4]

src_position = [2,2,2]
mic_position = np.array([
    [ 3,2,2],
    [ 2,1,2],
    [ 2,3,2],
    [ 1,2,2]
])
mic_num = mic_position.shape[0]

rir_data = np.zeros([mic_num, rir_length])

rir_data=generateRir(room_size, 
             src_position, 
            (mic_position).tolist(), 
             reverbTime=rev_time_source, 
             orientation=orientation, 
             isHighPassFilter=hp_filter, 
             nDim=dim, 
             nOrder=order, 
             nSamples=rir_length, 
             micType=mtype,
             source_type = 'bin')
print(type(rir_data))
rir_data = np.array(rir_data)
print(type(rir_data))
print(rir_data.shape)
sf.write(f"rir_test_dir.wav",rir_data.transpose(),16000)
