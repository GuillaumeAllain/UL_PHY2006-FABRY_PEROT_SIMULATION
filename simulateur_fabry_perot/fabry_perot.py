import numpy as np

def trace_fp(amplitude_osc, bias, ISL, coefficient_reflexion, equation_spectre, resolution_amplitude=1024, resolution_space=16):
    # Conversion de l'ISL en taille physique
    taille_cavite = 3*(10**8)/(2*ISL)

    # Création des grilles de tailles de cavité
    osc, space = np.mgrid[0+bias:amplitude_osc+bias:resolution_amplitude*1j,0:taille_cavite:resolution_space*1j]
    spaces = space*((space[:,-1]+osc[:,-1])/space[:,-1]).reshape(-1,1)

    # Création des cubes de données pour les toutes les réflexions ainsi que pour les configurations de cavité
    refl_number = np.arange(0,5*np.int(np.sqrt(coefficient_reflexion)/(2*(1-coefficient_reflexion))),1).reshape(1,-1)
    spaces_refl = np.repeat(spaces,refl_number.shape[-1],axis=-1).reshape(spaces.shape+(refl_number.shape[-1],))
    miroir_r_refl = np.array(coefficient_reflexion)**refl_number
    spaces_dephasage = np.repeat(refl_number*spaces_refl[:,-1,:],spaces_refl.shape[1],axis=0).reshape(spaces_refl.shape)

    # Calcul des champ électriques
    waves = equation_spectre((spaces_refl + spaces_dephasage))
    waves[:,:,1::2] = waves[:,::-1,1::2]

    # Sortie du résultat en intensité
    waves_sum = np.mean(np.abs(np.sum(waves*miroir_r_refl,axis=-1))**2,axis=-1)
    waves_sum /= np.max(waves_sum)
    return osc[:,0], waves_sum
