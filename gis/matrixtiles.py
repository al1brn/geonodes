#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:23:47 2023

@author: alain
"""
import numpy as np
from pathlib import Path

from scipy.interpolate import RectBivariateSpline

from PIL import Image, ImageDraw, ImageFont

# ====================================================================================================
# Matrix tiles

class MatrixTiles:
    def __init__(self, folder, x0, y0, x1, y1, tile_len=256, use_overlap=False, x_count=1, y_count = 1, ok_download=True,
                 tile_prefix='tile', file_ext='png'):
        """ Split a big world area into tiles of various definitions.
        
        Each definition level is called a matrix : a matrix of tiles.
        The level 0 covers all the world in one tile.
        The definition of each level is twice the definition of the previous.
        
        Arguments
        ---------
            - folder (str or Path) : folder where to store the tile files
            - size (couple of floats) : size in world units of the whole tile area
            - origin (couple of floats = (0, 0)) : origin of world coordinates
            - tile_len (int = 256) : width and height of the tiles
            - use_overlap (bool = False) = Add 1 to the tiles shape
            - count_x (int = 1) : number of x tiles at matrix = 0
            - count_y (int = 1) : number of y tiles at matrix = 0
            - ok_download (bool=True) : download is enabled
            - tile_prefix (str = 'tile') : tile file prefix
            - file_ext (str = 'png') : tile file extension
        """        
        
        if folder is None:
            self.folder = None
        else:
            self.folder = Path(folder)
            
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.x_size      = (x1 - x0)/x_count
        self.y_size      = (y1 - y0)/y_count
        self.tile_len    = tile_len
        self.use_overlap = use_overlap
        self.x_count     = x_count
        self.y_count     = y_count
        
        self.tile_prefix = tile_prefix
        self.file_ext    = file_ext
        
        # ----- Download enabling

        self.download_enabled = 0 if ok_download else 1
    
        
        
    def __str__(self):
        return f"<{type(self).__name__}: world: {self.x0}, {self.y0}, {self.x1}, {self.y1}, size: {self.x_size*self.x_count}, {self.y_size*self.y_count}, tiles: ({self.x_count}, {self.y_count})>"
        
    # =============================================================================================================================
    # Web download control
    
    @property
    def ok_download(self):
        return self.download_enabled == 0
    
    def disable_download(self):
        self.download_enabled += 1
        
    def enable_download(self):
        self.download_enabled -= 1
        if self.download_enabled < 0:
            raise Exception("MatrixTiles.enable_download error: download already enabled. Certainly a lack of balance between 'enable' and 'disable'")
        return self.download_enabled == 0
        
    # =============================================================================================================================
    # To be overridden
    
    def write_file(self, file_path, tile):
        """ Write the tile data on the disk.
        
        By default, call the method save(file_path) of the tile.
        
        Arguments
        ---------
            - file_path (str or Path) : full path name of the file to write
            - tile (any) : tile date to save
        """
        
        tile.save(file_path)
        
    def read_file(self, file_path):
        """ Read tile from disk.
        
        By default, load an image.
        
        Arguments
        ---------
            - file_path (str or Path) : full path name of the file to read
            
        Returns
        -------
            - tile
        """
        
        return Image.open(file_path)
    
    def empty_tile(self):
        """ Create an empty file.
        
        This method is called when a tile doesn't exist.
        
        Returns
        -------
            - tile
        """
        
        return Image.new("RGB", self.tile_shape, "black")
    
    
    def tile_is_empty(self, tile):
        """ Test if a tile is empty.
        
        To save disk space, empty tiles are saved as empty files.
        
        Arguments
        ---------
            - tile (tile) : tile data to test
            
        Returns
        -------
            - bool : True if tile is empty, False otherwise
        """
        
        a = np.array(tile)
        return np.max(a) <= 0.0001
    
    def download_tile(self, matrix, col, row):
        """ Download a tile from a Web Service
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column in the matrix
            - row (int) : tile row in the matrix
        
        Returns
        -------
            - tile
        """
    
        shape = self.tile_shape
        back_col  = (100 + matrix*6798547 % 155, 100 + matrix*798543 % 155, 100 + matrix*889053 % 155)
        front_col = (0, 0, 0)
        
        image = Image.new("RGB", shape, back_col)
        
        draw = ImageDraw.Draw(image)
        txt = f"[{matrix}] {col} {row}"
        police = ImageFont.load_default(20)
        
        if True:
            bbox = draw.textbbox((0, 0), txt, font=police)
            t_w = bbox[2] - bbox[0]
            t_h = bbox[3] - bbox[1]
            draw.text((shape[0]//2 - t_w//2, shape[1]//2 - t_h//2), txt, font=police, fill=front_col)
            
        else:
            t_w, t_h = draw.multiline_textsize(txt, font=police)    
            draw.text((shape[0]//2, shape[1]//2 + t_h//2), txt, align='center', font=police, fill=front_col)
            
        # Frame
    
        draw.rectangle((5, 5, shape[0] - 5, shape[1] - 5), outline=(0, 0, 0), width=2)    
        
        return image
    
    def from_lower(self, matrix, col, row, target='FINAL'):
        """ Build a tile from the matrix with lower detail
        
        The target defines the user of the tile built from a lower definition:
            - FINAL (default) : tile will be used as final tile
            - DOWNLOAD : unknown values will be downloaded
            
        For altitudes tiles, a DOWNLOAD target indicates to put a 'UNKNOWN' value
        to the unknown altitudes. On the other hand, FINAL target indicates to
        extrapolate the final values from the existing ones.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column in the matrix
            - row (int) : tile row in the matrix
            - target (str = 'USE') : usage target 
        
        Returns
        -------
            - tile
        """
        
        return None
    
    
    
    
    
        # OLD OLD
        
        if matrix == 0:
            return self.empty_tile()
        
        l_col = col // 2
        l_row = row // 2
        
        tile = self.get_tile(matrix-1, l_col, l_row)
        
        q_i = col % 2
        q_j = row % 2
        
        half = self.tile_len // 2
        
        return tile.crop((q_i*half, q_j*half, q_i*half + half, q_j*half + half)).resize(self.tile_shape)
        
        
    # =============================================================================================================================
    # Conversion world - local
        
    def to_matrix(self, matrix, x, y):
        """ Convert world coordinates into coordinates inside the matrix.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - x (float or array of floats) : world x coordinate
            - y (float or array of floats) : world y coordinate
            
        Returns
        -------
            - couple of floats or couple of array of floats
        """
            
        return (x - self.x0)*((1 << matrix)/self.x_size), (y - self.y0)*((1 << matrix)/self.y_size)
    
    def to_world(self, matrix, m_x, m_y):
        """ Convert matrix coordinates int world coordinates.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - m_x (float or array of floats) : matrix x coordinate
            - m_y (float or array of floats) : matrix y coordinate
            
        Returns
        -------
            - couple of floats or couple of array of floats
        """
        
        return self.x0 + m_x*(self.x_size/(1 << matrix)), self.y0 + m_y*(self.y_size/(1 << matrix))
    
    def get_tile_coords(self, matrix, x, y):
        """ Get the tile coordinates of the tile containing the given world coordinates.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - x (float) : world x coordinate
            - y (float) : world y coordinate
            
        Returns
        -------
            - couple of ints
        """
        
        m_x, m_y = self.to_matrix(matrix, x, y)
        return int(m_x), int(m_y)
    
    def get_matrix(self, definition, x_size, y_size):
        """ Get the matrix necessary for a target resolution.
        
        Arguments
        ---------
            - definition (int) : target definition
            - x_size (float) : size along x
            - y_size (float) : size along y
            
        Returns
        -------
            - int : matrix to use
        """
        
        
        
        mat_x = int(np.log(definition/self.tile_len*(self.x_size*self.x_count)/x_size)/np.log(2))
        mat_y = int(np.log(definition/self.tile_len*(self.y_size*self.y_count)/y_size)/np.log(2))
            
        return max(0, mat_x, mat_y)
        

    # =============================================================================================================================
    # Tile key management
    
    def get_tile_key(self, matrix, col, row):
        """ Compute the unique tile key to be used as file name.
        
        The key is built in the following way:
            - tile prefix (default = 'tile')
            - matrix index
            - tile row
            - tile column
            
        For instance, the tile (10, 20) of matrix 2 gives "tile02_10_20"
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int or array of ints) : column in the matrix
            - row (int or array of ints) : row in the matrix
            
        Returns
        -------
            - str
        """
        
        return f"{self.tile_prefix}{matrix:02d}_{col}_{row}"
    
    def tile_key_to_coords(self, key, with_matrix=True):
        """ Get the tile coordinates from a tile key.
        
        This is the reverse operation of method 'get_tile_key'.
        
        Arguments
        ---------
            - key (str) : tile key
            - with_matrix (bool = True) : returns the matrix as third iterm
            
        Returns
        -------
            - couple (with_matrix == False) or triplet (with_matrix == False) of ints : colum, row [, matrix index]
        """
        
        parts = key.split('_')
        if len(parts) != 3 and len(parts[0]) != len(self.tile_prefix) + 2:
            return None
        
        if with_matrix:
            return int(parts[1]), int(parts[2]), int(parts[0][-2:])
        else:
            return int(parts[1]), int(parts[2])
        
    # =============================================================================================================================
    # Empty tile
    
    @property
    def tile_shape(self):
        """ Returns the shape of a tile.
        
        The shape is either ```(tile_len, tile_len)``` or ```(tile_len + 1, tile_len + 1)``` 
        depending on the use_overlap flag.
        """
        
        if self.use_overlap:
            return (self.tile_len + 1, self.tile_len + 1)
        else:
            return (self.tile_len, self.tile_len)
    
    def tile_size(self, matrix):
        """ Returns the size of a tile in world units.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            
        Returns
        -------
            - float
        """
        
        return self.x_size / (1 << matrix), self.y_size / (1 << matrix)
    
    def matrix_width(self, matrix):
        return self.x_count << matrix

    def matrix_height(self, matrix):
        return self.y_count << matrix

        
    # =============================================================================================================================
    # File management
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Files
    
    def get_matrix_folder(self, matrix):
        """ Get the folder where to store files of the given matrix index.
        
        A sub folder is used for each matrix. The sub folder is created if it doesn't already exist.

        Arguments
        ---------
            - matrix (int) : matrix index
            
        Returns
        -------
            - Path
        """
        
        folder = self.folder / f"mat {matrix}"
        if not folder.exists():
            folder.mkdir()
        return folder
    
    def save_tile(self, matrix, col, row, tile):
        """ Save a tile on disk.
        
        The actual saving is performed by overridable methode ```write_file```.

        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column
            - row (int) : tile row
            - tile (any) : tile date to write on disk
        """
        
        if tile is None:
            return

        fname = self.get_matrix_folder(matrix) / self.get_tile_key(matrix, col, row)
        if self.tile_is_empty(tile):
            with Path(f"{fname}.empty").open('w'):
                pass      
        else:
            self.write_file(f"{fname}.{self.file_ext}", tile)

    def load_tile(self, matrix, col, row):
        """ Read a tile from disk.
        
        Returns None if the file doesn't exist.
        If the tile is marked as 'not existing', an empty tile is returned.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column
            - row (int) : tile row
            
        Returns
        -------
            - tile or None
        """
        
        key = self.get_tile_key(matrix, col, row)
        
        fname = self.get_matrix_folder(matrix) /  f"{key}.{self.file_ext}"
        if fname.exists():
            return self.read_file(fname)
        
        fname = self.get_matrix_folder(matrix) /  f"{key}.empty"
        if fname.exists():
            return self.empty_tile()
        
        return None
    
    def file_is_empty(self, matrix, col, row):
        """ Test if a tile file is empty.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column
            - row (int) : tile row
            
        Returns
        -------
            - True if file is not downloadable, False otherwise
        """
        
        key = self.get_tile_key(matrix, col, row)
        
        return (self.get_matrix_folder(matrix) / f"{key}.empty").exists()
    
    def tiles_in_cache(self, matrix):
        
        tile_crs = []
        for f in self.get_matrix_folder(matrix).iterdir():
            if not f.is_file():
                continue
            
            cr = self.tile_key_to_coords(f.stem, with_matrix=False)
            if cr is not None:
                tile_crs.append(cr)
                
        return tile_crs
        
    def cache_size(self, matrix):
        crs = np.array(self.tiles_in_cache(matrix))
        if len(crs):
            return np.min(crs[:, 0]), np.min(crs[:, 1]), np.max(crs[:, 0]), np.max(crs[:, 1])
        else:
            return (0, 0, 0, 0)
        
    def tile_exists(self, matrix, col, row):
        """ Test if a tile file exists.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column
            - row (int) : tile row
            
        Returns
        -------
            - True if file exists, False otherwise
        """
        
        key = self.get_tile_key(matrix, col, row)
        fname = self.get_matrix_folder(matrix) /  f"{key}.{self.file_ext}"
        return fname.exists()
        
    
    # =============================================================================================================================
    # Get the tiles
    
    def get_tile(self, matrix, col, row):
        """ Get a tile.
        
        The method first tries to read the file from disk. If it doesn't exist, it
        downloads it from the web service. It saves it on disk befere returning the service. 
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column
            - row (int) : tile row
            
        Returns
        -------
            - True if file is not downloadable, False otherwise
        """
        
        tile = self.load_tile(matrix, col, row)
        
        if tile is None:
            if self.ok_download:
                tile = self.download_tile(matrix, col, row)
                self.save_tile(matrix, col, row, tile)
                
            else:
                tile = self.from_lower(matrix, col, row, target='FINAL')
            
        return tile
    
    # =============================================================================================================================
    # Get an area
    
    def area_shape(self, matrix, x0, y0, x1, y1):
        """ Computes the shape of an area at the given matrix.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - x0 (float) : left of the area
            - y0 (float) : bottom of the area
            - x1 (float) : right of the area
            - y1 (float) : top of the area
            
        Returns
        -------
            - couple of ints
        """
        
        mx0, my0 = self.to_matrix(matrix, x0, y0)
        mx1, my1 = self.to_matrix(matrix, x1, y1)
        
        if my1 < my0:
            m = my0
            my0 = my1
            my1 = m
            
        return round((mx1 - mx0)*self.tile_len), round((my1 - my0)*self.tile_len)
    
    
    def get_area(self, matrix, x0, y0, x1, y1):
        
        return None
    
    
    
        # OLD OLD
        
        mx0, my0 = self.to_matrix(matrix, x0, y0)
        mx1, my1 = self.to_matrix(matrix, x1, y1)
        
        if my1 < my0:
            m = my0
            my0 = my1
            my1 = m
        
        col0, row0 = int(mx0), int(my0)
        col1, row1 = int(mx1) + 1, int(my1) + 1
        
        nx, ny = col1 - col0, row1 - row0
        tiles = Image.new("RGB", (nx*self.tile_len, ny*self.tile_len), "white")
        
        for col in range(col0, col1):
            for row in range(row0, row1):
                print(f"{type(self).__name__}.get_area {col} in [{col0}-{col1}], {row} in [{row0}, {row1}]")
                
                tile = self.get_tile(matrix, col, row)
                tiles.paste(tile, ((col-col0)*self.tile_len, (row-row0)*self.tile_len))
                
        i0, j0 = round((mx0-col0)*self.tile_len), round((my0-row0)*self.tile_len)
        i1, j1 = round((mx1-col0)*self.tile_len), round((my1-row0)*self.tile_len)
        
        return tiles.crop((i0, j0, i1, j1))
    
# =============================================================================================================================
# Images Tiles

class MatrixImages(MatrixTiles):
    
    def from_lower(self, matrix, col, row, target='FINAL'):
        """ Build an image tile from the matrix with lower detail
        
        The target defines the user of the tile built from a lower definition:
            - FINAL (default) : tile will be used as final tile
            - DOWNLOAD : unknown values will be downloaded
            
        For altitudes tiles, a DOWNLOAD target indicates to put a 'UNKNOWN' value
        to the unknown altitudes. On the other hand, FINAL target indicates to
        extrapolate the final values from the existing ones.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column in the matrix
            - row (int) : tile row in the matrix
            - target (str = 'USE') : usage target 
        
        Returns
        -------
            - tile
        """
        
        if matrix == 0:
            return self.empty_tile()
        
        l_col = col // 2
        l_row = row // 2
        
        tile = self.get_tile(matrix-1, l_col, l_row)
        
        q_i = col % 2
        q_j = row % 2
        
        half = self.tile_len // 2
        
        return tile.crop((q_i*half, q_j*half, q_i*half + half, q_j*half + half)).resize(self.tile_shape)

    # =============================================================================================================================
    # Get an area
    
    def get_area(self, matrix, x0, y0, x1, y1):
        """ Get an image covering the requested area.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - x0 (float) : left of the area
            - y0 (float) : bottom of the area
            - x1 (float) : right of the area
            - y1 (float) : top of the area
            
        Returns
        -------
            - image
        """
        
        mx0, my0 = self.to_matrix(matrix, x0, y0)
        mx1, my1 = self.to_matrix(matrix, x1, y1)
        
        if my1 < my0:
            m = my0
            my0 = my1
            my1 = m
        
        col0, row0 = int(mx0), int(my0)
        col1, row1 = int(mx1) + 1, int(my1) + 1
        
        nx, ny = col1 - col0, row1 - row0
        tiles = Image.new("RGB", (nx*self.tile_len, ny*self.tile_len), "white")
        
        for col in range(col0, col1):
            for row in range(row0, row1):
                print(f"{type(self).__name__}.get_area {col} in [{col0}-{col1}], {row} in [{row0}, {row1}]")
                
                tile = self.get_tile(matrix, col, row)
                tiles.paste(tile, ((col-col0)*self.tile_len, (row-row0)*self.tile_len))
                
        i0, j0 = round((mx0-col0)*self.tile_len), round((my0-row0)*self.tile_len)
        i1, j1 = round((mx1-col0)*self.tile_len), round((my1-row0)*self.tile_len)
        
        return tiles.crop((i0, j0, i1, j1))
    
    

# =============================================================================================================================
# Altitudes Tiles

class MatrixAltitudes(MatrixTiles):

    # =============================================================================================================================
    # No altitude in the tile
    
    def tile_is_empty(self, tile):
        return np.max(tile) < -1000 or np.min(tile) > 10000
    
    # =============================================================================================================================
    # Initialize lower division
    
    def from_lower(self, matrix, col, row, target='FINAL'):
        """ Build a tile from the matrix with lower detail
        
        The target defines the user of the tile built from a lower definition:
            - FINAL (default) : tile will be used as final tile
            - DOWNLOAD : unknown values will be downloaded
            
        For altitudes tiles, a DOWNLOAD target indicates to put a 'UNKNOWN' value
        to the unknown altitudes. On the other hand, FINAL target indicates to
        extrapolate the final values from the existing ones.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - col (int) : tile column in the matrix
            - row (int) : tile row in the matrix
            - target (str = 'USE') : usage target 
        
        Returns
        -------
            - tile
        """
        
        
        # Lower tile is made of 4 quarters of size 129 x 129
        #
        # (0, 0) : [  0...128,   0...128]
        # (1, 0) : [128...256,   0...128]
        # (0, 1) : [  0...128, 128...256]
        # (1, 1) : [128...256, 128...256]
        #
        # The selected quarter must be spread on even indices of the target tile
        #
        #      0 1 2 3 4 5 ... 254 255 256
        #   0  X   X   X   ...  X       X 
        #   1
        #   2  X   X   X   ...  X       X
        #   3
        #
        # 254  X   X   X   ...  X       X 
        # 255
        # 256  X   X   X   ...  X       X 
        
        if matrix == 0:
            raise Exception(f"Matrix 0 is empty !")
            
        # ----- Get the lower matrix
            
        lower_col = col // 2
        lower_row = row // 2
        
        if not self.tile_exists(matrix - 1, lower_col, lower_row):
            if target == 'DOWNLOAD':
                return np.ones(self.tile_shape, float)*99999
        
        lower_tile = self.get_tile(matrix - 1, lower_col, lower_row)
        if self.tile_is_empty(lower_tile):
            return lower_tile
        
        
        # ----- Select the quarter
        
        half = self.tile_len // 2
        col_ofs = (col % 2)*half
        row_ofs = (row % 2)*half
        
        low_i, low_j = np.meshgrid(np.arange(half + 1) + col_ofs, np.arange(half + 1) + row_ofs, indexing='ij')
        
        # ----------------------------------------------------------------------------------------------------
        # Final : we extrapolate the selected quarter
        
        if target == 'FINAL':
    
            x0, y0 = self.to_world(matrix, col, row)
            
            tx = np.linspace(x0, x0 + self.tile_size(matrix)[0], half + 1)
            ty = np.linspace(y0, y0 + self.tile_size(matrix)[1], half + 1)
            
            lower_tile[lower_tile < -1000] = 0
            
            bspl = RectBivariateSpline(tx, ty, lower_tile[low_i, low_j], kx=1, ky=1) 
            
            tx = np.linspace(x0, x0 + self.tile_size(matrix)[0], self.tile_len + 1)
            ty = np.linspace(y0, y0 + self.tile_size(matrix)[1], self.tile_len + 1)
            
            x, y = np.meshgrid(tx, ty, indexing = 'ij')
            
            tile = bspl(x.flatten(), y.flatten(), grid=False)
            
            return np.reshape(tile, self.tile_shape)

        # ----------------------------------------------------------------------------------------------------
        # DOWNLOAD : unknown values are initialized to 99999
            
        elif target == 'DOWNLOAD':
        
            # ----- New tile initialized with 99999 = to be downloaded
            
            tile = np.ones(self.tile_shape, float)*99999
            
            # ----- Read the event indices in the lower tile
    
            evens= np.arange(half + 1)*2
            
            evens_i, evens_j = np.meshgrid(evens, evens, indexing='ij')
    
            tile[evens_i, evens_j] = lower_tile[low_i, low_j]
            
            return tile
        
        else:
            raise AttributeError(f"FranceAlt.from_lower: Unknown target '{target}'")
    
    # =============================================================================================================================
    # To be overridden
    
    def write_file(self, file_path, tile):
        """ Write the tile data on the disk.
        
        By default, call the method save(file_path) of the tile.
        
        Arguments
        ---------
            - file_path (str or Path) : full path name of the file to write
            - tile (any) : tile date to save
        """
        tile[tile < -1000] = 0
        
        np.save(file_path, tile)
        
    def read_file(self, file_path):
        """ Read tile from disk.
        
        By default, load an image.
        
        Arguments
        ---------
            - file_path (str or Path) : full path name of the file to read
            
        Returns
        -------
            - tile
        """
        
        return np.load(file_path)
    
    def empty_tile(self):
        """ Create an empty file.
        
        This method is called when a tile doesn't exist.
        
        Returns
        -------
            - tile
        """
        
        return np.ones(self.tile_shape, float)*(-99999)
    
    # =============================================================================================================================
    # Altitude
    
    def get_altitude(self, matrix, coords):
        
        x = coords[:, 0]
        y = coords[:, 1]
        
        h = np.zeros_like(x)
        
        cs, rs = self.to_matrix(matrix, x, y)
        
        for col in range(np.min(cs), np.max(cs) + 1):
            for row in range(np.min(rs), np.max(rs) + 1):
                
                z = self.get_tile(matrix, col, row)
                
                x0, y0 = self.to_world(matrix, col, row)
                
                tx = np.linspace(x0, x0 + self.tile_size(matrix)[0], self.tile_len + 1)
                ty = np.linspace(y0, y0 + self.tile_size(matrix)[1], self.tile_len + 1)
                
                bspl = RectBivariateSpline(tx, ty, z, kx=1, ky=1)
                
                sel = cs == col & rs == row
                h[sel] = bspl(x[sel], y[sel], grid=False)
                
        return h
    
    def altitude_func(self, center=(0, 0)):
        
        def func(coords):
            target_shape = np.shape(coords)[:-1]
            cf = np.reshape(coords, (np.size(coords)//2, 2)) * (self.tile_size / self.SIDE) - center
            
            return np.reshape(np.c_[cf[:, 0], cf[:, 1], self.get_altitude(cf)], target_shape + (3,))
        
        return func
    
    # =============================================================================================================================
    # Download an area
    
    def download_area(self, x0, y0, x1, y1):
        c0, r0 = self.xy_to_cr(x0, y0)
        c1, r1 = self.xy_to_cr(x1, y1)
        
        self.enable_download()
        
        for col in range(c0, c1+1):
            for row in range(r0, r1+1):
                self.get_tile(col, row)

        self.disable_download()
                
    
    # =============================================================================================================================
    # Dump
    
    def to_object(self, matrix, name=None, individual=False, scale=1.):
        
        from geopy.core.mesh import Mesh
        
        if np.shape(scale) == ():
            scale = (scale, scale, scale)
        
        self.disable_download()
        
        if name is None:
            name = f"Alts [{matrix}]"
            
        c0, r0, c1, r1 = self.cache_size(matrix)
        
        nx, ny = (c1 + 1) - c0, (r1 + 1) - r0
        sx, sy = nx*self.tile_len, ny*self.tile_len
        
        if individual:
            grid = Mesh.Grid(size_x=self.tile_size(matrix)[0]*scale[0], size_y=self.tile_size(matrix)[0]*scale[1], vertices_x=self.tile_len+1, vertices_y=self.tile_len+1)

        else:
            grid = Mesh.Grid(size_x=self.tile_size(matrix)[0]*nx*scale[0], size_y=self.tile_size(matrix)[0]*ny*scale[1], vertices_x=sx+1, vertices_y=sy+1)
            points = grid.points.shaped(sx+1, sy+1)
            
            #CAUTION : grid (row, col)
            h = grid.points.shaped(sy+1, sx+1).z
        
        for c, r in self.tiles_in_cache(matrix):
            a = self.get_tile(matrix, c, r)
            assert(np.shape(a) == self.tile_shape)
            a[a < -1000] = 0
            a *= scale[2]

            if individual:
                grid.points.z = a.T.flatten()
                
                tile = grid.to_object(f"{name} {c} {r}")
                tile.location = (c*257, r*257, 0)
            else:
                # CAUTION : row first !
                h[r*self.tile_len:(r+1)*self.tile_len+1, c*self.tile_len:(c+1)*self.tile_len+1] = a.T
            
        if not individual:
            grid.points.z = h.flatten()
                
            grid.to_object(name)
            
        self.enable_download()
        
    # =============================================================================================================================
    # Get an area
    
    def get_area(self, matrix, x0, y0, x1, y1):
        """ Get an array covering the requested area.
        
        Arguments
        ---------
            - matrix (int) : matrix index
            - x0 (float) : left of the area
            - y0 (float) : bottom of the area
            - x1 (float) : right of the area
            - y1 (float) : top of the area
            
        Returns
        -------
            - array of altitudes
        """
        
        mx0, my0 = self.to_matrix(matrix, x0, y0)
        mx1, my1 = self.to_matrix(matrix, x1, y1)
        
        col0, row0 = int(mx0), int(my0)
        col1, row1 = int(mx1) + 1, int(my1) + 1
        
        nx, ny = col1 - col0, row1 - row0
        
        tiles = np.zeros((nx, self.tile_len, ny, self.tile_len))

        for col in range(col0, col1):
            for row in range(row0, row1):
                print(f"{type(self).__name__}.get_area {col} in [{col0}-{col1}], {row} in [{row0}, {row1}]")
                
                tiles[col - col0, :, row - row0] = self.get_tile(matrix, col, row)[:-1, :-1]
                
        tiles = np.reshape(tiles, (nx*self.tile_len, ny*self.tile_len))
        
        i0, j0 = round((mx0-col0)*self.tile_len), round((my0-row0)*self.tile_len)
        i1, j1 = round((mx1-col0)*self.tile_len), round((my1-row0)*self.tile_len)
        
        i, j = np.meshgrid(np.arange(i0, i1), np.arange(j0, j1), indexing='ij')
        return np.reshape(tiles[i.flatten(), j.flatten()], (i1-i0, (j1-j0)))
    
    
# =============================================================================================================================
# Tests

if __name__ == '__main__':    
    folder = "/Users/alain/temp/tmp"
    
    if False:
        mt = MatrixTiles(folder, -200, -100, 200, 100, x_count=4, y_count=2)
        print(mt)
        
        print("Expected 0, 0        :", mt.to_matrix(0, -200, -100))
        print("Expected 1, 1        :", mt.to_matrix(0, -100,    0))
        print("Expected 4, 2        :", mt.to_matrix(0,  200,  100))
        print("Expected -200, -100  :", mt.to_world(0, 0, 0))
        print("Expected -100,    0  :", mt.to_world(0, 1, 1))
        print("Expected 200, 100    :", mt.to_world(0, 4, 2))
        
        print("Expected 4           :", mt.matrix_width(0))
        print("Expected 2           :", mt.matrix_height(0))
        print("Expected 8           :", mt.matrix_width(1))
        print("Expected 4           :", mt.matrix_height(1))
        
        for matrix in range(2):
            sx, sy = mt.tile_size(matrix)
            print()
            print(f"matrix {matrix}, tile size: {sx:4.0f}, {sy:4.0f}")
            for i in range(mt.matrix_width(matrix)):
                for j in range(mt.matrix_height(matrix)):
                    x, y = mt.to_world(matrix, i, j)
                    
                    print(f"{i:2d}, {j:2d} > {x:4.0f}, {y:4.0f}, {x + sx:4.0f}, {y + sy:4.0f}")
                    
    if False:
        mt = MatrixTiles(folder, 0, 0, 1, 1)
        
        for matrix in range(3):
            mt.get_area(matrix, .2, .2, .8, .8).show()
            
            
    if False:
        mt = MatrixTiles(folder, 0, 0, 1, 1)
        print(mt.get_matrix(2048, 1, 1))
            
            
    
    
    
    
    
    
    
    
    
    




    
        
        