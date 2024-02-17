#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:03:27 2023

@author: alain
"""

"""
Download tile images from geoservices.ign.fr

https://geoservices.ign.fr/documentation/services/api-et-services-ogc/images-tuilees-wmts-ogc#877

NB : L’échelle cartographique approximative est calculée à partir de la résolution en utilisant
une dimension arbitraire de pixel de 0.28mm x 0.28mm (définie dans le standard WMTS) selon la formule :

Dénominateur d'échelle = résolution / taille pixel

"""

import requests
from pathlib import Path
import numpy as np

from PIL import Image

SAMPLE_URL = "https://wxs.ign.fr/essentiels/geoportail/wmts?SERVICE=WMTS&REQUEST=GetTile&"
SAMPLE_URL += "VERSION=1.0.0&LAYER=ORTHOIMAGERY.ORTHOPHOTOS&TILEMATRIXSET=PM&TILEMATRIX=14&TILECOL=8180&"
SAMPLE_URL += "TILEROW=5905&STYLE=normal&FORMAT=image/jpeg"

# ====================================================================================================
# get_tile parameters

def get_tile_params(**kwargs):
    
    return {
        'REQUEST'       : 'GetTile',
        'VERSION'       : kwargs.get('version',     '1.0.0'),
        'LAYER'         : kwargs.get('layer',       'ORTHOIMAGERY.ORTHOPHOTOS'),
        'TILEMATRIXSET' : kwargs.get('matrix_set',  'PM'),
        'TILEMATRIX'    : kwargs.get('matrix',      '14'),
        'TILECOL'       : kwargs.get('col',         '8180'),
        'TILEROW'       : kwargs.get('row',         '5905'),
        'STYLE'         : kwargs.get('style',       'normal'),
        'FORMAT'        : kwargs.get('format',      'image/jpeg'),
        }

def get_tile(folder, matrix, col, row):
    
    fname = f"tile {col}-{row}.jpg"

    base = "https://wxs.ign.fr/essentiels/geoportail/wmts?SERVICE=WMTS"
    
    url = base + '&' + "&".join([f"{key}={value}" for key, value in get_tile_params(matrix=matrix, col=col, row=row).items()])
    
    res = requests.get(url)
    if res.status_code != 200:
        print("Error loading tile", fname)
        print(url)
        return False
    
    with open(Path(folder) / fname, 'wb') as f:
        print("Writing", fname)
        f.write(res.content)
        
    return True

def test():
    get_tile("/Users/alain/Pictures/", 14, 8180, 5905)


# ====================================================================================================
# Load tile images

class Tiles:
    def __init__(self, folder, matrix, i0=0, i1=None, j0=0, j1=None):
        
        self.folder = Path(folder) / f"mat {matrix}"
        prefix = f"tile"
        
        self.keys = {}
        
        # ----- All the tiles
        
        self.col0 = None
        
        for fpath in self.folder.glob(f"{prefix}*.jpg"):
            
            key = fpath.stem[len(prefix):]
            
            col, row  = self.key_to_cr(key)
            self.keys[key] = {'col': col, 'row': row, 'file_name': fpath.name}
            
            if self.col0 is None:
                self.col0 = col
                self.col1 = col
                self.row0 = row
                self.row1 = row
            else:
                self.col0 = min(col, self.col0)
                self.row0 = min(row, self.row0)
                self.row1 = max(row, self.row1)
                self.col1 = max(col, self.col1)
                
        if self.col0 is None:
            raise Exception(f"No image tile in {self.folder}")
                
        # ----- Build the array with the requested window
        
        self.col_count = self.col1 - self.col0 + 1
        self.row_count = self.row1 - self.row0 + 1
        
        #print("Matrix", matrix, self.col0, self.col1, self.row0, self.row1, '-->', self.col_count, self.row_count, "/", i1, j1)
        
        if i1 is None:
            i1 = self.col_count - 1
        if j1 is None:
            j1 = self.row_count - 1
            
        self.shape = (i1 - i0 + 1, j1 - j0 + 1)
        
        #print(i0, i1, j0, j1, self.shape)
        #print()
        
        
        self.col0 += i0
        self.row0 += j0
        
        #print(self)
        
    # ====================================================================================================
    # Utilities
    
    def __str__(self):
        return f"<Satellite tiles: {self.shape} tiles, starting at col {self.col0}, row {self.row0}, image ({self.shape[0]*256} x {self.shape[1]*256}) in folder {self.folder}>"
        
    @staticmethod
    def key_to_cr(key):
        p = key.find('-')
        return int(key[:p]), int(key[p+1:])
    
    @staticmethod
    def cr_to_key(col, row):
        return f"{col:04d}-{row:04d}"
    
    @staticmethod
    def file_name(col, row):
        return f"tile {col}-{row}.jpg"        
        
    # ====================================================================================================
    # Download tiles
    
    # ----- One tile
        
    @staticmethod
    def download_tile(folder, matrix, col, row):
        
        file_name = Path(folder) / Tiles.file_name(col, row)
        if file_name.exists():
            return True
    
        base = "https://wxs.ign.fr/essentiels/geoportail/wmts?SERVICE=WMTS"
        
        url = base + '&' + "&".join([f"{key}={value}" for key, value in get_tile_params(matrix=matrix, col=col, row=row).items()])
        
        res = requests.get(url)
        if res.status_code != 200:
            print("Error loading tile", file_name)
            print(url)
            return False
        
        with open(file_name, 'wb') as f:
            print("Writing", file_name)
            f.write(res.content)
            
        return True
    
    # ----- Several tiles
        
    @classmethod
    def Download(self, folder, matrix, col0, col1, row0, row1, rev_row=False):
        
        mat_folder = Path(folder) / f"mat {matrix}"
        if not mat_folder.exists():
            mat_folder.mkdir()
        
        for col in range(col0, col1):
            null_count = 0
            
            rg = range(row0, row1)
            if rev_row:
                rg = reversed(rg)
            for row in rg:
                print(f"Download {col - col0}/{col1 - col0} {row - row0}/{row1 - row0}")
                if not Tiles.download_tile(mat_folder, matrix, col, row):
                    null_count += 1
                    if null_count > 3:
                        break
                    #pass
                    #raise Exception(f"matrix {matrix}: Impossible to download tile", col, row)
                
        return Tiles(folder, matrix)
    
    # ====================================================================================================
    # Get a tile
    
    def __getitem__(self, index):
        
        fname = self.file_name(self.col0 + index[0], self.row0 + index[1])
        try:
            return Image.open(self.folder / fname)        
        except:
            return None
        
    # ====================================================================================================
    # Merge the tiles in one image
    
    def image(self, as_image=True, show_tiles=True):
        
        row_size = 256*self.shape[0]
        col_size = 256*self.shape[1]
        
        zone  = None
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                
                tile = self[i, j]
                if tile is None:
                    continue
                
                if zone is None:
                    zone = np.zeros((col_size, row_size, 3,), np.array(tile).dtype)
                    
                z_i = j*256
                z_j = i*256
                    
                zone[z_i:z_i+256, z_j:z_j+256] = np.array(tile) #.transpose((0, 1, 2))
                
                if show_tiles:
                    zone[z_i:z_i+256, z_j+255] = 255
                    zone[z_i+255, z_j:z_j+256] = 255
                
        if as_image:
            return Image.fromarray(zone)
        else:
            return zone
        
img_folder = "/Users/alain/Pictures/Rge/"
        
alpes_folder  = Path(img_folder) / "south tiles"
falaises_folder = Path(img_folder) / "north tiles"

# ====================================================================================================
# Load falaises

def load_falaises():
    
    # ----- 8
    
    matrix = 8
    
    col0, col1 = 128, 129
    row0, row1 = 86, 88
    
    tiles = Tiles.Download(falaises_folder, matrix, col0, col1, row0, row1)
    print(f"Matrix {matrix:2d}: {tiles}")
    #tiles.image().show()
    
    # ----- 9
    
    matrix = 9
    
    col0 *= 2
    col1 *= 2
    row0 *= 2
    row1 *= 2
    
    tiles = Tiles.Download(falaises_folder, matrix, col0, col1, row0, row1)
    print(f"Matrix {matrix:2d}: {tiles}")
    #tiles.image().show()
    
    i0 = 0
    i1 = 1
    j0 = 1
    j1 = 2
    tiles = Tiles(falaises_folder, matrix, i0, i1, j0, j1)
    #tiles.image().show()
    
    # ----- 10
    
    matrix = 10
    
    c0 = col0
    col0 = (c0 + i0)*2
    col1 = (c0 + i1 + 1)*2
        
    r0 = row0
    row0 = (r0 + j0)*2
    row1 = (r0 + j1 + 1)*2
    
    print(f"Matrix {matrix} tiles:", col0, col1, row0, row1)
    
    tiles = Tiles.Download(falaises_folder, matrix, col0, col1, row0, row1)
    #tiles.image().show()
    
    i0 = 0
    i1 = 3
    j0 = 1
    j1 = 3
    tiles = Tiles(falaises_folder, matrix, i0, i1, j0, j1)
    tiles.image().show()
    
    # ----- 11
    
    matrix = 11
    
    c0 = col0
    col0 = (c0 + i0)*2
    col1 = (c0 + i1 + 1)*2
        
    r0 = row0
    row0 = (r0 + j0)*2
    row1 = (r0 + j1 + 1)*2
    
    print(f"Matrix {matrix} tiles:", col0, col1, row0, row1)
    
    tiles = Tiles.Download(falaises_folder, matrix, col0, col1, row0, row1)
    #tiles.image().show()
    
    i0 = 0
    i1 = 4
    j0 = 1
    j1 = 4
    tiles = Tiles(falaises_folder, matrix, i0, i1, j0, j1)
    #tiles.image().show()
    
    # ----- 12 +

    c0 = col0
    col0 = c0 + i0
    col1 = c0 + i1 + 1
        
    r0 = row0
    row0 = r0 + j0
    row1 = r0 + j1 + 1
    
    for m in range(12, 18):
        matrix = m

        col0 *= 2
        col1 *= 2
        row0 *= 2
        row1 *= 2
        
        if m < 16:
            continue
    
        tiles = Tiles.Download(falaises_folder, matrix, col0, col1, row0, row1, rev_row=True)
        if m <= 13:
            tiles.image().show()
        

# ====================================================================================================
# Load Alpes 

def load_alpes():
            
    
    # ----- 8
    
    matrix = 8
    
    col0, col1 = 132, 134
    row0, row1 = 92, 94
    
    tiles = Tiles.Download(alpes_folder, matrix, col0, col1, row0, row1)
    print(f"Matrix {matrix:2d}: {tiles}")
    #tiles.image().show()
    
    # ----- 9
    
    matrix = 9
    
    col0 *= 2
    col1 *= 2
    row0 *= 2
    row1 *= 2
    
    tiles = Tiles.Download(alpes_folder, matrix, col0, col1, row0, row1)
    print(f"Matrix {matrix:2d}: {tiles}")
    #tiles.image().show()
    
    i0 = 1
    i1 = 2
    j0 = 1
    j1 = 3
    tiles = Tiles(alpes_folder, matrix, i0, i1, j0, j1)
    #tiles.image().show()
    
    # ----- 10
    
    matrix = 10
    
    c0 = col0
    col0 = (c0 + i0)*2
    col1 = (c0 + i1 + 1)*2
        
    r0 = row0
    row0 = (r0 + j0)*2
    row1 = (r0 + j1 + 1)*2
    
    print(f"Matrix {matrix} tiles:", col0, col1, row0, row1)
    
    tiles = Tiles.Download(alpes_folder, matrix, col0, col1, row0, row1)
    #tiles.image().show()
    
    i0 = 0
    i1 = 3
    j0 = 2
    j1 = 4
    tiles = Tiles(alpes_folder, matrix, i0, i1, j0, j1)
    #tiles.image().show()
    
    # ----- 11
    
    matrix = 11
    
    c0 = col0
    col0 = (c0 + i0)*2
    col1 = (c0 + i1 + 1)*2
        
    r0 = row0
    row0 = (r0 + j0)*2
    row1 = (r0 + j1 + 1)*2
    
    print(f"Matrix {matrix} tiles:", col0, col1, row0, row1)
    
    tiles = Tiles.Download(alpes_folder, matrix, col0, col1, row0, row1)
    #tiles.image().show()
    
    
    i0 = 2
    i1 = 6
    j0 = 1
    j1 = 4
    tiles = Tiles(alpes_folder, matrix, i0, i1, j0, j1)
    #tiles.image().show()
    
    # ----- 12
    
    matrix = 12
    
    c0 = col0
    col0 = (c0 + i0)*2
    col1 = (c0 + i1 + 1)*2
        
    r0 = row0
    row0 = (r0 + j0)*2
    row1 = (r0 + j1 + 1)*2
    
    row1 += 1
    
    print(f"Matrix {matrix} tiles:", col0, col1, row0, row1)
    
    tiles = Tiles.Download(alpes_folder, matrix, col0, col1, row0, row1)
    #tiles.image().show()
    
    i0 = 0
    i1 = 8
    j0 = 0
    j1 = 8
    tiles = Tiles(alpes_folder, matrix, i0, i1, j0, j1)
    image = tiles.image()
    image = image.rotate(angle=-37.6, expand=True)
    #image.show()
    
    for m in range(13, 19):
        matrix = m
    
        col0 *= 2
        col1 *= 2
        row0 *= 2
        row1 *= 2
        
        if m < 17:
            continue
        
        print(col0)
        col0 = 68209
    
        tiles = Tiles.Download(alpes_folder, matrix, col0, col1, row0, row1)
        #tiles.image().show()


# ====================================================================================================
# Build the global map at resolution matrix = 13
#
# Only one image

def smooth(a0, a1, w):
    return (a1 - a0) * (3.0 - w * 2.0) * w * w + a0

def south_13(seam = True):
    
    # ----- Load, rotate

    m13 = Tiles(alpes_folder, 13)
    image = m13.image(show_tiles=False)
    image = image.rotate(51.6 + 1.5, expand=True)
    print("Shape 13", np.shape(image), image.size)
    
    # ----- Zone to extract

    x0     = 2410
    y0     = 1636
    size_x = 2000
    size_y = 3676
    
    # ----- Seam
    
    if seam:
        
        total_x = image.size[0]
        length  = int(.1*size_y)
        
        y_bot = y0 + size_y - length
        y_top = y0 - length

        for j in range(length):
            j_bot = y_bot + j
            j_top = y_top + j
            w = j/length
            top = smooth(0, 1, w)
            bot = smooth(1, 0, w)
            for i in range(total_x):
                pix_bot = np.array(image.getpixel((i, j_bot)))
                pix_top = np.array(image.getpixel((i, j_top)))
                pix = tuple(np.clip((pix_bot*bot + pix_top*top).astype(int), 0, 255))
                image.putpixel((i, j_bot), pix)
        
    # ----- Cropping
        
    image = image.crop((x0, y0, x0 + size_x, y0 + size_y))

    # ----- Save the result
   
    image.save(Path(img_folder) / "south 13.jpg")
    print("Final shape", np.shape(image), image.size)

    
# ====================================================================================================
# Build the global map at resolution matrix = 13
#
# Only one image

def north_13(seam = True):

    # ----- Load, rotate

    m13 = Tiles(falaises_folder, 13)
    image = m13.image(show_tiles=False)
    image = image.rotate(55.0, expand=True)
    print("Shape 13", np.shape(image), image.size)
    
    #image.show()
    
    # ----- Zone to extract
    
    x0     = 2430
    y0     = 1590
    size_x = 1690
    size_y = int(size_x/21500*49999)
    
    # ----- Seam
    
    if seam:
        
        total_x = image.size[0]
        length  = int(.1*size_y)
        
        y_bot = y0 + size_y - length
        y_top = y0 - length

        for j in range(length):
            j_bot = y_bot + j
            j_top = y_top + j
            w = j/length
            top = smooth(0, 1, w)
            bot = smooth(1, 0, w)
            for i in range(total_x):
                pix_bot = np.array(image.getpixel((i, j_bot)))
                pix_top = np.array(image.getpixel((i, j_top)))
                pix = tuple(np.clip((pix_bot*bot + pix_top*top).astype(int), 0, 255))
                image.putpixel((i, j_bot), pix)
        
    # ----- Cropping
        
    image = image.crop((x0, y0, x0 + size_x, y0 + size_y))

    # ----- Save the result
   
    image.save(Path(img_folder) / "north 13.jpg")
    print("Final shape", np.shape(image), image.size)


# ====================================================================================================
# Build the global map at resolution matrix
#
# Only one image

def north_global_map(matrix=15, seam = True):

    # ----- Load, rotate

    mats = Tiles(falaises_folder, matrix)
    image = mats.image(show_tiles=False)
    image = image.rotate(55.0, expand=True)
    print(f"Shape {matrix}", np.shape(image), image.size)
    
    #image.show()
    
    # ----- Zone to extract
    
    x0     = 2430
    y0     = 1590
    size_x = 1690
    size_y = int(size_x/21500*49999)
    
    # ----- Seam
    
    if seam:
        
        total_x = image.size[0]
        length  = int(.1*size_y)
        
        y_bot = y0 + size_y - length
        y_top = y0 - length

        for j in range(length):
            j_bot = y_bot + j
            j_top = y_top + j
            w = j/length
            top = smooth(0, 1, w)
            bot = smooth(1, 0, w)
            for i in range(total_x):
                pix_bot = np.array(image.getpixel((i, j_bot)))
                pix_top = np.array(image.getpixel((i, j_top)))
                pix = tuple(np.clip((pix_bot*bot + pix_top*top).astype(int), 0, 255))
                image.putpixel((i, j_bot), pix)
        
    # ----- Cropping
        
    image = image.crop((x0, y0, x0 + size_x, y0 + size_y))

    # ----- Save the result
   
    image.save(Path(img_folder) / f"test {matrix}.jpg")
    print("Final shape", np.shape(image), image.size)




#load_alpes()    
#load_falaises()

#south_13(seam=True)
#north_13(seam=True)

north_global_map(matrix=15, seam = True)












        
        
        
        
        

