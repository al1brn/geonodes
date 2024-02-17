#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Wed Nov  9 15:26:58 2022

@author: alain.bernard
@email: alain@ligloo.net

-----

GIS computations

"""

VILLES = {
    'Paris': (651781.13, 6862214.34),
    'Marseille': (82543.58, 6270295.24),
    'Lyon': (184204.29, 5130128.73),
    'Toulouse': (161817.91, 523232.63),
    'Nice': (108571.53, 6307848.06),
    'Nantes': (352228.18, 6691700.36),
    'Strasbourg': (839650.37, 6891202.25),
    'Montpellier': (176888.91, 6275088.71),
    'Bordeaux': (313326.52, 6422390.40),
    'Lille': (700089.94, 7050828.85),
    'Rennes': (350225.08, 6838278.88),
    'Reims': (823313.48, 6931180.32),
    'Le Havre': (526121.57, 6954071.87),
    'Saint-Etienne': (215065.36, 5058474.16),
    'Toulon': (132586.53, 6286844.03),    
    }

# Conversion of gps coordinated into meters
# Ref: https://fr.wikipedia.org/wiki/Projection_conique_conforme_de_Lambert

# Projection	  | λ0	  |  φ0	  |  φ1	 |  φ2	|   X0	    |    Y0	        | EPSG	| IGNF   |
# Lambert 93	  | 3°E	  | 46.5° | 44°	 |  49°	| 700 000 m	| 6 600 000 m	| 2154	| LAMB93 |

import numpy as np
from numpy import pi, tan, cos, sin, log, power, sqrt, exp, arctan
pi2 = pi/2
pi4 = pi/4

# ====================================================================================================
# 
# https://geodesie.ign.fr/contenu/fichiers/documentation/algorithmes/notice/NTG_71.pdf

# ----------------------------------------------------------------------------------------------------
# ALG0001 Calcul de la latitude isométrique

def lat_to_y(phi, e):
    esin = e*sin(phi)
    return log(tan(pi4 + phi/2) * power( (1 - esin) / (1 + esin), e/2) )

# ----------------------------------------------------------------------------------------------------
# ALG0002 Calcul de la latitude 

def y_to_lat(y, e, epsilon):
    
    fact = exp(y)
    
    def f(phi):
        esin = e*sin(phi)
        return 2*arctan(power( (1 + esin)/(1 - esin), e/2)*fact ) - pi2
    
    phi = 2*arctan(fact) - pi2
    
    for _ in range(20):
        phi_ = f(phi)
        if False:
            if abs(phi - phi_) < epsilon:
                break
        else:
            if np.all(np.abs(phi - phi_) < epsilon):
                break
        phi = phi_
        
    return phi

# ----------------------------------------------------------------------------------------------------
# ALG0003 Transformation des coordonnées : gps to xy

def gps_to_xy(lat, lon, n, c, e, lon_c, xs, ys):
    
    y = lat_to_y(lat, e)
    
    cey  = c*exp(-n*y)
    nlon = n*(lon - lon_c)
    
    return xs + cey*sin(nlon), ys - cey*cos(nlon)

# ----------------------------------------------------------------------------------------------------
# ALG0004 Transformation des coordonnées : xy to gps

def xy_to_gps(x, y, n, c, e, lon_c, xs, ys, epsilon):
    
    x -= xs
    y -= ys
    
    R = sqrt(x*x + y*y)
    g = arctan(-x/y)
    
    lon = lon_c + g/n
    L = -1/n*log(R/c)
    
    return y_to_lat(L, e, epsilon), lon

# ----------------------------------------------------------------------------------------------------
# ALG0021 Calcul de la grande normale

def grande_normale(lat, a, e):
    esin = e*sin(lat)
    return a/sqrt(1 - esin*esin)

# ----------------------------------------------------------------------------------------------------
# ALG0019 Projection de Lambert conique, cas tangent

def lambert_tangent(a, e, lat_0, lon_0, k0, x0, y0):
    
    n = sin(lat_0)
    k0Nco = k0*grande_normale(lat_0, a, e)/tan(lat_0)
    
    return {
        "n"        : n,
        "c"        : k0Nco*exp(n*lat_to_y(lat_0, e)),
        "e"        : e,
        "lon_c"    : lon_0,
        "xs"       : x0,
        "ys"       : y0 + k0Nco,
        }


# ----------------------------------------------------------------------------------------------------
# ALG0054 Projection de Lambert conique, cas secantes

def lambert_secante(a, e, lat_0, lat_1, lat_2, lon_0, x0, y0):
    
    N1 = grande_normale(lat_1, a, e)
    N2 = grande_normale(lat_2, a, e)
    
    n = log( (N2*cos(lat_2)) / (N1*cos(lat_1)) )
    n /= ( lat_to_y(lat_1, e) - lat_to_y(lat_2, e) )
    
    c =  N1*cos(lat_1)/n*exp(n*lat_to_y(lat_1, e))

    return {
        "n"        : n,
        "c"        :c,
        "e"        : e,
        "lon_c"    : lon_0,
        "xs"       : x0,
        "ys"       : y0 if abs(lat_0 - pi2) < 0.0001 else y0 + c*exp(-n*lat_to_y(lat_0, e)),
        }

# ====================================================================================================
# Run the tests

def tests():
    
    # ----- lat_to_y
    
    phis = [0.87266462600, -0.30000000000, 0.19998903370]
    es   = [0.08199188998, 0.08199188998, 0.08199188998]
    res  = [1.00552653649, -0.30261690063, 0.200000000009]
    
    print("\nlat_to_y")
    for phi, e, r in zip(phis, es, res):
        print(abs(r - lat_to_y(phi, e)) < 1e-10)

    # ----- y_to_lat
    
    ys  = [1.00552653648, -0.30261690060, 0.200000000000]
    res = [0.87266462600, -0.29999999997, 0.19998903369]
    epsilon = 1e-11

    print("\ny_to_lat")
    for y, e, r in zip(ys, es, res):
        print(abs(r - y_to_lat(y, e, epsilon)) < epsilon)
        
    # ----- gps_to_xy

    print("\ngps_to_xy")
    x, y = gps_to_xy(
        lat    = 0.87266462600, 
        lon    = 0.14551209900,
        n      = 0.760405966,
        c      = 11603796.9767,
        e      = 0.0824832568,
        lon_c  = 0.04079234433,
        xs     = 600000,
        ys     = 5657616.6740,
        )
    
    print(x, y)
    print(abs(x - 1029705.0818) < 1e-4)
    print(abs(y - 272723.8510) < 1e-4)
        
    # ----- xy_to_gps

    print("\nxy_to_gps")

    lat, lon = xy_to_gps(
        x      = 1029705.0830, 
        y      = 272723.8490,
        n      = 0.760405966,
        c      = 11603796.9767,
        e      = 0.0824832568,
        lon_c  = 0.04079234433,
        xs     = 600000,
        ys     = 5657616.6740,
        epsilon = epsilon,
        )
    
    print(lat, lon)
    print(abs(lat - 0.87266462600) < 1e-4)
    print(abs(lon - 0.14551209900) < 1e-4)
    
    # ----- lmabert tangent

    print("\nlambert_tangent")
    
    lon_0s = (0.18112808800, 0.04079234433)
    lat_0s = (0.97738438100, 0.86393798000)
    k0s    = (1.0000000000, 0.9998773400)
    x0s    = (0.0000, 600000.0000)
    y0s    = (0.0000, 200000.000)
    a_s    = (6378388.0000, 6378249.2000)
    es     = (0.081991890, 0.0824832568)
    
    res = [
        {
            "n"        : 0.8290375725, 
            "c"        : 11464828.2192,
            "e"        : 0.081991890,
            "lon_c"    : 0.18112808800,
            "xs"       : 0.,
            "ys"       : 4312250.9718,
        },
        {
            "n"        : 0.7604059658,
            "c"        : 11603796.9760,
            "e"        : 0.0824832568,
            "lon_c"    : 0.04079234433,
            "xs"       : 600000.,
            "ys"       : 5657616.6712,
        },
        ]
    
    for lon_0, lat_0, k0, x0, y0, a, e, r in zip(lon_0s, lat_0s, k0s, x0s, y0s, a_s, es, res):
        calc = lambert_tangent(a, e, lat_0, lon_0, k0, x0, y0)
        for k, v in r.items():
            print(f"{k:6s}: {str(abs(v - calc[k]) < 1e-4):6s}  --> {v - calc[k]}")
        print()
        
    # ----- lmabert secante

    print("\nlambert_secante")
    
    lon_0s = (0., 0.07623554539)
    lat_0s = (0., 1.57079632700)
    lat_1s = (-0.57595865300, 0.86975574400)
    lat_2s = (-0.78539816300, 0.89302680100)
    x0s    = (0.0000,  150000.0000)
    y0s    = (0.0000, 5400000.000)
    a_s    = (6378388.0000, 6378388.0000)
    es     = (0.081991890, 0.081991890)
    
    res = [
        {
            "n"        : -0.6304963300, 
            "c"        : -12453174.1795,
            "e"        : 0.081991890,
            "lon_c"    : 0.,
            "xs"       : 0.,
            "ys"       : -12453174.1795,
        },
        {
            "n"        : 0.7716421867,
            "c"        : 11565915.8294,
            "e"        : 0.081991890,
            "lon_c"    : 0.07623554539,
            "xs"       : 150000.0000,
            "ys"       : 5400000.0000,
        },
        ]
    
    for lon_0, lat_0, lat_1, lat_2, x0, y0, a, e, r in zip(lon_0s, lat_0s, lat_1s, lat_2s, x0s, y0s, a_s, es, res):
        calc = lambert_secante(a, e, lat_0, lat_1, lat_2, lon_0, x0, y0)
        for k, v in r.items():
            print(f"{k:6s}: {str(abs(v - calc[k]) < 1e-4):6s}  --> {v - calc[k]}")
        print()
        
# ====================================================================================================
# Lmabert 93

L93_n     = 0.7256077650
L93_c     = 11754255.426
L93_xs    = 700000.0
L93_ys    = 12655612.050
#L93_e     = 0.08248325676
L93_e     = 0.08181919104
L93_lon_c = np.radians(2. + 20/60 + 14.025/3600)
L93_lon_c = np.radians(3)

    
# ====================================================================================================
# Conversions GPS / xy

def to_xy(lon, lat=None):
    
    single_array = lat is None
    if single_array:
        assert(len(np.shape(lon))==2)
        ln = lon[:, 0]
        lt = lon[:, 1]
    else:
        ln = lon
        lt = lat
    
    x, y = gps_to_xy(np.radians(lt), np.radians(ln), n=L93_n, c=L93_c, e=L93_e, lon_c=L93_lon_c, xs=L93_xs, ys=L93_ys)
    
    if single_array:
        return np.c_[x, y]
    else:
        return x, y

def to_lonlat(x, y=None):

    single_array = y is None
    if single_array:
        assert(len(np.shape(x))==2)
        xx = x[:, 0]
        yy = x[:, 1]
    else:
        xx = x
        yy = y
    
    lat, lon = xy_to_gps(xx, yy, n=L93_n, c=L93_c, e=L93_e, lon_c=L93_lon_c, xs=L93_xs, ys=L93_ys, epsilon=1e-10)
    
    if single_array:
        return np.degrees(np.c_[lon, lat])
    else:
        return np.degrees(lon), np.degrees(lat)

# ====================================================================================================
# Conversion from lambert 93 location to pixels within a given zoom matrix
# The following values are read from ign web site:
# - Lambert 93 capabilities
# - resolution = 0.00028*capa['ScaleDenominator']

L93_SCALES = [
    104579.224549894,
    52277.5323537905,
    26135.4870785954,
    13066.891381800002,
    6533.2286041135,
    3266.5595244627,
    1633.2660045973998,
    816.6295549859999,
    408.3139146768,
    204.1567415109,
    102.0783167832,
    51.0391448966,
    25.5195690743,
    12.7597836936,
    6.379891636,
    3.1899457653,
    1.5949728695,
    0.7974864315000001,
    0.3987432149,
    0.19937160729999998,
    0.09968580370000002,
    0.04984290179999999,
]

def l93_scale(matrix):
    return L93_SCALES[matrix]
    
def l93_xy_to_pix(x, y, matrix):
    inv_scale = 1/l93_scale(matrix)
    return int(round(x*inv_scale)), int(round((12000000 - y)*inv_scale))

def l93_pix_to_xy(i, j, matrix):
    scale = l93_scale(matrix)
    return i*scale, 12000000 - j*scale
    
    
# ====================================================================================================
#  Web Mercator

def wm_to_xy(lon, lat, zoom):
    f = 128/pi*(1<<zoom)
    return f*(np.radians(lon) + pi), f*(pi - log(tan(pi/4 + np.radians(lat)/2)))

def wm_to_lonlat(x, y, zoom):
    f = pi/128/(1<<zoom)
    return np.degrees(x*f - pi), np.degrees(2*(arctan(exp(pi - y*f)) - pi/4))

# ====================================================================================================
#  Mercator

MER_RADIUS = 6378137.0
MER_INV    = 1/MER_RADIUS

def mer_to_xy(lon, lat):
    return np.radians(lon) * MER_RADIUS, log(tan(pi/4 + np.radians(lat)/2)) * MER_RADIUS

def mer_to_lonlat(x, y):
    return np.degrees(x*MER_INV), np.degrees(2*arctan(exp(y*MER_INV)) - pi/2)



if __name__ == '__main__':
    paris_lat = 48.866667
    paris_lon = 2.333333
    
    x, y = to_xy(paris_lon, paris_lat)
    lo, la = to_lonlat(x, y)
    
    print(paris_lon, paris_lat)
    print("L93 ", x, y)
    print("BACK", lo, la)
    
    print(to_lonlat(0, 12000000))
    
    lon = 9.260633
    lat = 41.360010
    
    print("CORSE SUD", to_xy(lon, lat))
    
    # ----- FR Limites
    
    FR_LON0 = -5
    FR_LON1 = 10
    FR_LAT0 = 40
    FR_LAT1 = 52
    
    print(f"FR limits: ({FR_LON0}, {FR_LAT0}) -> ({FR_LON1}, {FR_LAT1})", to_xy(FR_LON0, FR_LAT0), to_xy(FR_LON1, FR_LAT1))
    

