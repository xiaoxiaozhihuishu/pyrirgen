from libcpp.vector cimport vector

cdef extern from "rirgen.cpp":
	cdef vector[vector[double]] gen_rir(double c, double fs, vector[vector[double]] rr, vector[double] ss, vector[double] LL, vector[double] beta_input, vector[double] orientation, vector[double] source_orientation, int isHighPassFilter, int nDimension, int nOrder, int nSamples, char microphone_type, char source_type);
	
