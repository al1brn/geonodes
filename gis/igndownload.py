#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:10:05 2023

@author: alain
"""

import numpy as np
from time import time
import requests

from PIL import Image
from io import BytesIO

from xml.etree import ElementTree

if __name__ == '__main__':
    import lamb93
    
# =============================================================================================================================
# Utilities
    
def str_time(dt):
    dt = int(dt)
    return f"{dt//60}:{dt%60:02d} min"

def rem_time(dt, p):
    if p < 0.1:
        return "..."
    else:
        return str_time((1 - p)/p*dt)
    
    
# =============================================================================================================================
# Download altitudes from ign - POST

def download_lonlat(lonlat, halt_on_error=False):

    
    url_post = "https://wxs.ign.fr/calcul/alti/wps?service=WPS&version=1.0.0"

    
    base_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <wps:Execute version="1.0.0" service="WPS"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://www.opengis.net/wps/1.0.0" xmlns:wfs="http://www.opengis.net/wfs"
    xmlns:wps="http://www.opengis.net/wps/1.0.0"
    xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:gml="http://www.opengis.net/gml"
    xmlns:ogc="http://www.opengis.net/ogc"
    xmlns:wcs="http://www.opengis.net/wcs/1.1.1" xmlns:xlink="http://www.w3.org/1999/xlink"
    xsi:schemaLocation="http://www.opengis.net/wps/1.0.0
    http://schemas.opengis.net/wps/1.0.0/wpsAll.xsd">
      <ows:Identifier>gs:WPSElevation</ows:Identifier>
      <wps:DataInputs>
        <wps:Input>
          <ows:Identifier>lon</ows:Identifier>
          <wps:Data>
            <wps:LiteralData>[LON]</wps:LiteralData>
          </wps:Data>
        </wps:Input>
        <wps:Input>
            <ows:Identifier>lat</ows:Identifier>
          <wps:Data>
            <wps:LiteralData>[LAT]</wps:LiteralData>
          </wps:Data>
        </wps:Input>
        <wps:Input>
          <ows:Identifier>format</ows:Identifier>
          <wps:Data>
            <wps:LiteralData>json</wps:LiteralData>
          </wps:Data>
        </wps:Input>
        <wps:Input>
          <ows:Identifier>zonly</ows:Identifier>
          <wps:Data>
            <wps:LiteralData>true</wps:LiteralData>
          </wps:Data>
        </wps:Input>
        <wps:Input>
          <ows:Identifier>indent</ows:Identifier>
          <wps:Data>
            <wps:LiteralData>false</wps:LiteralData>
          </wps:Data>
        </wps:Input>
      </wps:DataInputs>
      <wps:ResponseForm>
        <wps:RawDataOutput>
          <ows:Identifier>result</ows:Identifier>
        </wps:RawDataOutput>
      </wps:ResponseForm>
    </wps:Execute>"""
    
    batch_size  = 5000
    batch_count = len(lonlat)//batch_size + 1
    offset      = 0
    top         = time()
    z           = np.ones(len(lonlat), float)*(-99999)
    
    print(f"Download {len(lonlat)} altitudes: {np.min(lonlat[:, 0]):.5f}, {np.min(lonlat[:, 1]):.5f}, {np.max(lonlat[:, 0]):.5f}, {np.max(lonlat[:, 1]):.5f}")
    for i_batch in range(batch_count):
        
        if i_batch % 1 == 0:
            dt = time() - top
            p = i_batch/batch_count
            print(f"   Reading altitudes : {p*100:3.0f} %, rem {rem_time(dt, p)}")
            
        # ----- Number of altitudes to download
        
        count = min(batch_size, len(lonlat) - offset)
        if count == 0:
            break
        
        # ----- Build the request
        
        slon = '|'.join([str(v) for v in lonlat[offset:offset+count, 0]])
        xml = base_xml.replace("[LON]", slon)
        del slon
        
        slat = '|'.join([str(v) for v in lonlat[offset:offset+count, 1]])
        xml = xml.replace("[LAT]", slat)
        del slat
        
        
        # ----- Post the request
    
        res = requests.post(url_post, data=xml)

        # ----- Read the result
        
        if res.status_code != 200:
            print(f"download_lonlat : Error loading altitude batch {i_batch} / {batch_count}")
            
        else:
            try:
                a = eval(res.content.decode('utf-8'))['elevations']
            except Exception as e:
                print(f"download_lonlat : Error reading elevations {i_batch} / {batch_count}")
                print(res.content)
                if halt_on_error:
                    raise e
                else:
                    print(e)
                    a = None
                    
            if a is not None:
                z[offset:offset+count] = a
        
        offset += count
        
    dt = int(time() - top)
    print(f"   Reading altitudes : 100 % in {str_time(dt)}")
        
        
    return z

# =============================================================================================================================
# Download altitudes from ign - GET

def download_lonlat_GET(lonlat, halt_on_error=False):
    """ Download altitudes from an array of longitude, latitude couples.
    
    Arguments
    ---------
        - lonlat (array of couple of floats) : longitude and latitude to query
        
    Returns
    -------
        - array of floats : one value per couple
    """
    
    base = "https://wxs.ign.fr/calcul/alti/rest/elevation.json?zonly=true"

    batch_size  = 150
    batch_count = len(lonlat)//batch_size + 1
    offset      = 0
    top         = time()
    z = np.ones(len(lonlat), float)*(-99999)
    
    print(f"Download {len(lonlat)} altitudes: {np.min(lonlat[:, 0])}, {np.min(lonlat[:, 1])}, {np.max(lonlat[:, 0])}, {np.max(lonlat[:, 1])}")
    for i_batch in range(batch_count):
        
        if i_batch % 100 == 0:
            print(f"   Reading altitudes : {i_batch/batch_count*100:3.0f} %")
            
        # ----- Number of altitudes to download
        
        count = min(batch_size, len(lonlat) - offset)
        if count == 0:
            break
        
        # ------ Build the query url
        
        url = base + '&lon=' + '|'.join([str(v) for v in lonlat[offset:offset+count, 0]])
        url = url  + '&lat=' + '|'.join([str(v) for v in lonlat[offset:offset+count, 1]])
        
        # ----- Query the web service
        
        res = requests.get(url)
        if res.status_code != 200:
            print(f"download_lonlat : Error loading altitude batch {i_batch} / {batch_count}")
            
        else:
            d = eval(res.content.decode('utf-8'))
            a = d.get("elevations")
            if a is None:
                print(f"download_lonlat : Error reading elevations {i_batch} / {batch_count}")
                print(res.content)
                print(d)
                if halt_on_error:
                    raise Exception("Download error")
            else:
                z[offset:offset+count] = a
        
        offset += count
        
    dt = int(time() - top)
    print(f"   Reading altitudes : 100 % in {dt//60}:{dt%60} min")

    return z

# =============================================================================================================================
# Download a satellite image
# col and row are in lambert 93 coo

def download_l93_sat_image(matrix, col, row):
    """ Download a tile from the IGN web service.
    
    Arguments
    ---------
        - matrix (int) : matrix
        - col (int) : tile column
        - row (int) : tile row
        
    Returns
    -------
        - image or None if download is not successful
    """
        
    params = {
        'REQUEST'       :'GetTile',
        'VERSION'       :'1.0.0',
        'LAYER'         :'ORTHOIMAGERY.ORTHOPHOTOS.BDORTHO.L93',
        'TILEMATRIXSET' :'LAMB93',
        'TILEMATRIX'    : matrix,
        'TILECOL'       : col,
        'TILEROW'       : row,
        'STYLE'         : 'normal',
        'FORMAT'        : 'image/jpeg',
        }
    
    base = "https://wxs.ign.fr/lambert93/geoportail/wmts?SERVICE=WMTS"
    url  = base + '&' + "&".join([f"{key}={value}" for key, value in params.items()])

    res = requests.get(url)
    if res.status_code != 200:
        return None
    
    return Image.open(BytesIO(res.content))

# =============================================================================================================================
# Capabilities

def sat_images_capabilities():
    
    # ---------------------------------------------------------------------------
    # Search for a given tag with an Identifier child
    
    def search(element, target_tag, identifier=None):
        
        for child in element:
            
            tag = child.tag.split('}')[-1]
                
            if tag == target_tag:
                if identifier is None:
                    return child
                
                else:
                    for ch in child:
                        tag = ch.tag.split('}')[-1]
                        if tag == 'Identifier' and ch.text == identifier:
                            return child
            else:
                found = search(child, target_tag, identifier)
                if found is not None:
                    return found
                
        return None
    
    # ---------------------------------------------------------------------------
    # Read the matrix set info
    
    def read_matrix_set(layer_element):
        
        raw = {}
        
        for child in layer_element:
            tag = child.tag.split('}')[-1]
            
            if tag == 'TileMatrix':
                mset = {}
                for ch in child:
                    tag = ch.tag.split('}')[-1]
                    mset[tag] = ch.text
                    
                if mset.get('Identifier') is not None:
                    raw[mset['Identifier']] = mset
                    
        lamb93 = {}
        for ident, tm in raw.items():
            corner = tm['TopLeftCorner'].split(' ')
            matrix = int(tm['Identifier'])
            
            lamb93[matrix] = {
                'MatrixHeight': int(tm['MatrixHeight']),
                'MatrixWidth':  int(tm['MatrixWidth']),
                'ScaleDenominator': float(tm['ScaleDenominator']),
                'TileHeight': int(tm['TileHeight']),
                'TileWidth': int(tm['TileWidth']),
                'TopLeftCorner': (float(corner[0]), float(corner[1]))
                }
                
        return lamb93

    # ---------------------------------------------------------------------------
    # Look for the layer
    
    url = "https://wxs.ign.fr/lambert93/geoportail/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities"
    req = requests.get(url)
    
    root = ElementTree.fromstring(req.content)
    
    matrix_tree = search(root, 'TileMatrixSet', 'LAMB93')
    if matrix_tree is None:
        raise Exception("TileMatrixSet LAMB93 not found")
    
    return read_matrix_set(matrix_tree)



# ====================================================================================================
# Tests

if __name__ == '__main__':
    
    """
    Brest : 48.3904° N, 4.4861° W
    Lille : 50.8503° N, 3.0578° E
    Strasbourg : 48.8566° N, 2.3522° E
    Marseille : 43.2965° N, 5.3699° E
    """
    
    lon0 = -5
    lon1 =  3
    lat0 = 42
    lat1 = 52
    
    if False:
        x, y = np.meshgrid(np.linspace(lon0, lon1, 16), np.linspace(lat0, lat1, 16))
        
        lonlat = np.c_[x.flatten(), y.flatten()]
        print(np.shape(lonlat))
        alts = download_lonlat(lonlat, True)
        
        print(f"Altitudes {np.shape(alts)}, min: {np.min(alts)} ({np.sum(alts == np.min(alts))}), max: {np.max(alts)}")
    
    if False:
        x, y = np.meshgrid(np.linspace(lon0, lon1, 96), np.linspace(lat0, lat1, 96))
        
        lonlat = np.c_[x.flatten(), y.flatten()]
        print(np.shape(lonlat))
        
        alts = download_lonlat(lonlat, True)
        print(f"Altitudes {np.shape(alts)}, min: {np.min(alts)} ({np.sum(alts == np.min(alts))}), max: {np.max(alts)}")
        
        
    if False:
        download_l93_sat_image(14, 397, 3145).show()
        
    if False:
        download_l93_sat_image(9, 12, 103).show()
        
    if False:
        print(sat_images_capabilities())   
        
        
        
        
        
        
    
    
    
    
    
    
        
    