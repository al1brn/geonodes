#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:32:50 2023

@author: alain
"""

import bpy
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from geopy.core.mesh import Mesh
from geopy.core.treenodes import Shader


class GisMap:
    def __init__(self, altitudes, images, x0, y0, x1, y1, name="GisMap"):
        
        self.altitudes = altitudes
        self.images    = images

        self.x0        = x0
        self.y0        = y0
        self.x1        = x1
        self.y1        = y1
        
        self.x_size    = x1 - x0
        self.y_size    = y1 - y0
        
        self.name      = name
        
    # ====================================================================================================
    # Create the images of the texture
        
    def create_tex_images(self, tex_folder, matrix=10, image_size=1024):
        
        u_tot, v_tot = self.images.area_shape(matrix, self.x0, self.y0, self.x1, self.y1)
        
        nu, nv = u_tot // image_size, v_tot // image_size
        if u_tot % image_size > 0:
            nu += 1
        if v_tot % image_size > 0:
            nv += 1
        single_image = nu == 1 and nv == 1
            
        if nu >= 10 or nv >= 10:
            raise Exception(f"The area [{self.x0:.1f}, {self.y0:.1f}, {self.x1:.1f}, {self.y1:.1f}] at matrix {matrix} represents {u_tot} x {v_tot} pixels which can't be mapped with image tiles of size {image_size}")

        # ----- Unique name
        
        u0, v0 = self.images.to_matrix(matrix, self.x0, self.y0)
        u0, v0 = round(u0*self.images.tile_len), round(v0*self.images.tile_len), 
            
        name = f"{self.name}_{matrix}_{u0}_{v0}_{u_tot}_{v_tot}"

        # ----- Folder where to save images
        
        tex_folder = Path(tex_folder)
        
        # ----- Single image
        
        if single_image:
            file_path = tex_folder / f"{name}.png"
            if not file_path.exists():
                image = self.images.get_area(matrix, self.x0, self.y0, self.x1, self.y1)
                image.save(str(file_path))
                
                return file_path, (1., 1.)
            
        # ----- Loop on images creation
            
        folder = Path(tex_folder) / name
        if not folder.exists():
            folder.mkdir()
        
        x_size = self.x_size/u_tot*image_size
        y_size = self.y_size/v_tot*image_size
        for u in range(nu):
            x0 = self.x0 + u*x_size
            x1 = x0 + x_size
            for v in range(nv):
                y0 = self.y0 + v*y_size
                y1 = y0 + x_size
                
                file_path = folder / f"tile.u{u+1}_v{v+1}.png"
                    
                if file_path.exists():
                    continue
                
                image = self.images.get_area(matrix, x0, y0, x1, y1)
                image.save(str(file_path))
                    
        # ----- Return file_path and uv_size
        
        uv_size = (u_tot/image_size, v_tot/image_size)
        
        return folder / f"tile.<UVTILE>.png", uv_size
    
    # ====================================================================================================
    # To Mesh
        
    def to_mesh(self, definition=100, scale=1., tex_folder=None, sat_matrix=10, image_size=1024):
        
        # ----------------------------------------------------------------------------------------------------
        # Altitudes
        
        matrix = self.altitudes.get_matrix(definition, self.x_size, self.y_size)
        
        alts = self.altitudes.get_area(matrix, self.x0, self.y0, self.x1, self.y1)
        alts *= scale*1.
        
        mesh = Mesh.Grid(self.x_size*scale, self.y_size*scale, alts.shape[0], alts.shape[1], materials=self.name)
        mesh.points.z = alts.T.flatten()
        
        # ----------------------------------------------------------------------------------------------------
        # Satellite image
        
        if tex_folder is not None:

            # ----- Create the material

            file_path, uv_size = self.create_tex_images(tex_folder, matrix=sat_matrix, image_size=image_size)
            tiled = '<UVTILE>' in str(file_path)
            b_img = bpy.data.images.load(str(file_path), check_existing=True)
            if tiled:
                b_img.source = 'TILED'

            mat = Shader.ImageTexture(b_img, self.name, roughness=1.)
            
            # ----- Resize uv
            
            xs, ys = np.max(mesh.corners.UVMap, axis=0)
            mesh.corners.UVMap *= uv_size[0]/xs, uv_size[1]/ys
        
        
        return mesh
    
# ====================================================================================================
# Demo / test

    
def demo(alt_folder, sat_folder, tex_folder):
    
    from geopy.gis.france import FranceL93Alt, FranceSat
    
    # ----- Somewhere in the Vosges
    
    x, y = 989745, 6791839
    
    # ----- The map
    
    gm = GisMap(FranceL93Alt(alt_folder), FranceSat(sat_folder), x-1000, y-1000, x+1000, y+1000, name="Vosges")
    gm.altitudes.enable_download()

    gm.images.enable_download()
    mesh = gm.to_mesh(1000, tex_folder=tex_folder, sat_matrix=18, image_size=4096)
    
    mesh.to_object("Vosges")
    
        
        
        
    