#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Mon Nov 27 16:02:31 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Blender utilities

Some functions to ease the access to standard bpy api
"""

from pathlib import Path
import numpy as np

if __name__ == '__main__':
    import lamb93
    from matrixtiles import MatrixImages, MatrixAltitudes
    from igndownload import download_lonlat, download_l93_sat_image
    
else:
    from geopy.gis import lamb93
    from geopy.gis.matrixtiles import MatrixImages, MatrixAltitudes
    from geopy.gis.igndownload import download_lonlat, download_l93_sat_image
    
FR_LON0 = -5
FR_LON1 = 10
FR_LAT0 = 40
FR_LAT1 = 52

#FR limits: (-5, 40) -> (10, 52) (14410, 5911793) (1181938, 7233428)

L93_X0    =   20000
L93_Y0    = 5920000
L93_SIZE  = 1300000
L93_X1    = L93_X0 + L93_SIZE
L93_Y1    = L93_Y0 + L93_SIZE

    
# =============================================================================================================================
# France altitudes - (longitude, latitude)

class FranceGpsAlt(MatrixAltitudes):
    
    def __init__(self, folder):
        """ Download altitudes from IGN web api.
        
        A tile is 257x257 giving 66049 altitudes per tile.
        
        Altitude tiles are stored in an 2D array of tiles indexed in columns and rows.
            - col : along longitude
            - row : along latitude
            
        An individual tile is (257, 257) to make possible to compute all altitudes inside the tile
        without the need to load neighbour sides.
 
        Arguments
        ---------
            - folder (str) : folder for downloaded images
        """
        
        super().__init__(folder, FR_LON0, FR_LAT0, FR_LON1, FR_LAT1, tile_len=256, use_overlap=True, ok_download=False,
                         tile_prefix='gps', file_ext='npy')
        
        # ----- Download map 0

        self.enable_download()
        _ = self.get_tile(0, 0, 0)
        self.disable_download()
        
        

    def download_tile(self, matrix, col, row):
        """ Download a tile from a Web Service
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column
            - row (int) : tile row
        
        Returns
        -------
            - tile
        """
        
        if matrix == 0:
            tile = np.ones(self.tile_shape, float)*99999
            
        else:
            tile = self.from_lower(matrix, col, row, target='DOWNLOAD')
            
        # ----- Longitude and latitudes to query
        
        ij = np.argwhere(tile > 10000)
        
        lon0, lat0 = self.to_world(matrix, col, row)
        
        lonlat = (lon0, lat0) + (ij*self.tile_size(matrix))/self.tile_len
        assert(len(lonlat) > 0)
        
        # ----- Download the altitudes
        
        tile[ij[:, 0], ij[:, 1]] = download_lonlat(lonlat, halt_on_error=True)

        # ----- Return the result
        
        return tile
        
# =============================================================================================================================
# France altitudes - Lambert93

class FranceL93Alt(MatrixAltitudes):
    
    def __init__(self, folder):
        """ Download altitudes from IGN web api.
        
        A tile is 257x257 giving 66049 altitudes per tile.
        
        Altitude tiles are stored in an 2D array of tiles indexed in columns and rows.
            - col : along longitude
            - row : along latitude
            
        An individual tile is (257, 257) to make possible to compute all altitudes inside the tile
        without the need to load neighbour sides.
        
        Arguments
        ---------
            - folder (str) : folder for downloaded images
        """

        super().__init__(folder, L93_X0, L93_Y0, L93_X1, L93_Y1, tile_len=256, use_overlap=True, ok_download=False,
                         tile_prefix='L93', file_ext='npy')
        
        # ----- Download map 0

        self.enable_download()
        _ = self.get_tile(0, 0, 0)
        self.disable_download()
    
    def download_tile(self, matrix, col, row):
        """ Download a tile from a Web Service
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column
            - row (int) : tile row
        
        Returns
        -------
            - tile
        """
        
        if matrix == 0:
            tile = np.ones(self.tile_shape, float)*99999
            
        else:
            tile = self.from_lower(matrix, col, row, target='DOWNLOAD')
            
        # ----- Longitude and latitudes to query
        
        ij = np.argwhere(tile > 10000)
        
        x0, y0 = self.to_world(matrix, col, row)
        
        xy = (x0, y0) + (ij*self.tile_size(matrix))/self.tile_len
        assert(len(xy) > 0)
        
        # ----- Download the altitudes
        
        lonlat = lamb93.to_lonlat(xy)
        del xy
        
        tile[ij[:, 0], ij[:, 1]] = download_lonlat(lonlat, halt_on_error=True)

        # ----- Return the result
        
        return tile
    
# =============================================================================================================================
# France satellite images

class FranceSat(MatrixImages):
    
    MATRIX_0     = 104579.224549894
    SCALES       = [
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
    
    def __init__(self, folder):
        """ Download satellite images from IGN web api.
        
        Coordinates are Lambert93.
        
        World space is the one chosen by IGN
 
        Arguments
        ---------
            - folder (str) : folder for downloaded images
        """
        
        super().__init__(folder, FR_LON0, FR_LAT0, FR_LON1, FR_LAT1, tile_len=256, use_overlap=True, ok_download=False,
                         tile_prefix='sat', file_ext='png')
        
        
    def to_matrix(self, matrix, x, y):
        factor = 1/256/self.SCALES[matrix]
        return x*factor, (12000000 - y)*factor
    
    def to_world(self, matrix, i, j):
        factor = self.SCALES[matrix]*256
        return i*factor, 12000000 - j*factor
    
    def download_tile(self, matrix, col, row):
        """ Download a image satellite from a Web Service
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column
            - row (int) : tile row
        
        Returns
        -------
            - image
        """
        
        return download_l93_sat_image(matrix, col, row)
    
        
# =============================================================================================================================
# Demo

if __name__ == '__main__':

    folder = "/Users/alain/temp/fralt"
    
    
    def load_matrix0():
        
        fr = FranceGpsAlt(folder)
        print(fr)
    
        fr.enable_download()
        
        tile = fr.get_tile(0, 0, 0)
        print(np.min(tile), '-->', np.max(tile))
        
    def load_matrix1():
    
        fr = FranceGpsAlt(folder)
        print(fr)
        
        fr.enable_download()
    
        tile = fr.get_tile(1, 0, 0)
        print(np.min(tile), '-->', np.max(tile))
    
        tile = fr.get_tile(1, 0, 1)
        print(np.min(tile), '-->', np.max(tile))
    
        tile = fr.get_tile(1, 1, 0)
        print(np.min(tile), '-->', np.max(tile))
    
        tile = fr.get_tile(1, 1, 1)
        print(np.min(tile), '-->', np.max(tile))
    
    def test_l93():
        center = (L93_X0 + L93_SIZE/2, L93_Y0 + L93_SIZE/2)
        l93 = FranceL93Alt(folder, center, size=(2000, 1000))
        print(l93)
        
        l93.enable_download()
        
        tile = l93.get_tile(0, 0, 0)
        print(np.shape(tile), np.min(tile), np.max(tile))
        tile = l93.get_tile(0, 1, 0)
        print(np.shape(tile), np.min(tile), np.max(tile))
    
    fs = FranceSat("/Users/alain/temp/test")
    fs.enable_download()
    for matrix in range(6, 14):
        print("\nmatrix", matrix)
        for x, y in [(L93_X0, L93_Y0), (L93_X1, L93_Y1), (L93_X0 + L93_SIZE/2, L93_Y0 + L93_SIZE/2)]:
            mx, my = fs.to_matrix(matrix, x, y)
            x_, y_ = fs.to_world(matrix, mx, my)
            print(x, y, '-->', x - x_, y - y_)
            print(fs.get_tile_coords(matrix, x, y), mx, my)
            
        if False:
            x, y = (L93_X0 + L93_SIZE/2, L93_Y0 + L93_SIZE/2)
            mx, my = fs.to_matrix(matrix, x, y)
            col, row = int(mx), int(my)
            
            img = fs.download_tile(matrix, col, row)
            if img is None:
                print("OUPS", x, y, col, row)
            else:
                img.show()
                
        if False:
            x, y = (L93_X0 + L93_SIZE/2, L93_Y0 + L93_SIZE/2)
            
            img = fs.get_area(matrix, x, y, x + 10000, y - 10000)
            if img is None:
                print("OUPS", x, y, col, row)
            else:
                img.show()
            
        
            
        
            
    








