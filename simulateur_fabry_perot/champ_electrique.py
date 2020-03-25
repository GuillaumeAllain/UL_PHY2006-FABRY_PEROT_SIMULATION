import numpy as np

class champ_electrique:
    def __init__(self,func):
        self.__func_interne = func
    def __add__(self,func_2):
        assert type(func_2)==type(self), "Type is not champ_electrique: %r" % self
        return champ_electrique(lambda param: self.__func_interne(param)+func_2(param))
    def __mul__(self,func_2):
        assert type(func_2)==type(self), "Type is not champ_electrique: %r" % self
        return champ_electrique(lambda param: self.__func_interne(param)*func_2(param))
    def __truediv__(self,func_2):
        assert type(func_2)==type(self), "Type is not champ_electrique: %r" % self
        return champ_electrique(lambda param: self.__func_interne(param)/func_2(param))
    def __sub__(self,func_2):
        assert type(func_2)==type(self), "Type is not champ_electrique: %r" % self
        return champ_electrique(lambda param: self.__func_interne(param)-func_2(param))
    def __call__(self,param):
        return self.__func_interne(param)

def champ_electrique_discret_func(long_onde_list=632.8e-9, intensite_relative=1):
    long_onde_arr = np.array(long_onde_list)
    rel_intensity_arr = np.array(intensite_relative)
    assert long_onde_arr.shape==rel_intensity_arr.shape
    if long_onde_arr.shape == np.array(1).shape:
        return champ_electrique(lambda z: rel_intensity_arr*np.exp(-1j*(2*np.pi/long_onde_arr)*z))
    else:
        return champ_electrique(lambda z: np.sum([rel_intensity_arr[ww]*np.exp(-1j*(2*np.pi/long_onde_arr[ww])*z) for ww in range(long_onde_arr.shape[0])],axis=0))

def champ_electrique_laser_func(long_onde_centrale=632.8e-9, isl_laser=300e9, smsr=4):
    delta_lambda = isl_laser*long_onde_centrale**2/3e8
    nombre_long_ondes = np.int(np.log(1e-4)/np.log(1/smsr))   
    long_onde_list = delta_lambda*np.arange(-nombre_long_ondes,nombre_long_ondes+1)
    long_onde_list += long_onde_centrale
    intensite_relative_list = smsr**(-1*abs(np.arange(-nombre_long_ondes,nombre_long_ondes+1, dtype=float)))
    return champ_electrique_discret_func(long_onde_list, intensite_relative_list)


