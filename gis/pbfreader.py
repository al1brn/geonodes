#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:22:32 2023

@author: alain
"""

import zlib
import struct

# ====================================================================================================
# Read variable int

def read_varint(file):
    result = 0
    shift = 0
    while True:
        byte = file.read(1)
        if not byte:
            break
        val = ord(byte)
        result |= (val & 0x7F) << shift
        shift += 7
        if not val & 0x80:
            break
    return result

# ====================================================================================================
# Read blob data

def read_blob_data(file, size):
    blob_data = file.read(size)
    return zlib.decompress(blob_data)

# ====================================================================================================
# Read PBF file

def read_pbf_1(file_path):
    with open(file_path, 'rb') as file:
        while True:
            header_size = read_varint(file)
            header_data = file.read(header_size)
            
            if not header_data:
                break
            
            message_size = read_varint(file)
            message_data = file.read(message_size)
            
            if True:
                pass
                #print(len(message_data))
                #bid  = struct.unpack('<q', message_data[:8])[0]
            
            # Fais quelque chose avec message_data ici
            # Pour des détails spécifiques à OpenStreetMap, tu devras traiter les messages OSM PBF
            
            #print(f"Message Size: {message_size}")
            print('-'*60)
            print(header_size, message_size)
            print(" ",header_data[:50])
            print('>>> ', message_data[:50])
            print()
            
def read_pbf_1(file_path):
    with open(file_path, 'rb') as file:
        while True:
            header_size = read_varint(file)
            header_data = file.read(header_size)
            
            if not header_data:
                break
            
            message_size = read_varint(file)
            message_data = file.read(message_size)
            
            if header_size > 12:
            
                # Décompose les données d'en-tête avec struct
                header_format = "cii"  # c: char, i: int
                header_tuple = struct.unpack(header_format, header_data[:12])
                
                message_type = header_tuple[0]
                version = header_tuple[1]
                message_id = header_tuple[2]
                
                # Fais quelque chose avec les données d'en-tête
                print(f"Message Type: {message_type}, Version: {version}, Message ID: {message_id}")
                
                # Fais quelque chose avec message_data ici
                # Pour des détails spécifiques à OpenStreetMap, tu devras traiter les messages OSM PBF
            
            print(f"Message Size: {message_size}")
            
def read_pbf(file_path):
    with open(file_path, 'rb') as file:
        while True:
            header_size = read_varint(file)
            header_data = file.read(header_size)
            
            if not header_data:
                break
            
            message_size = read_varint(file)
            message_data = file.read(message_size)
            
            if len(header_data) > 3:
            
                # Analyse des trois premiers octets de l'en-tête
                message_type = ord(header_data[0])
                version = ord(header_data[1])
                message_id = struct.unpack('!Q', b'\x00\x00' + header_data[2:])[0]
                
                # Fais quelque chose avec les données d'en-tête
                print(f"Message Type: {message_type}, Version: {version}, Message ID: {message_id}")
                
                # Fais quelque chose avec message_data ici
                # Pour des détails spécifiques à OpenStreetMap, tu devras traiter les messages OSM PBF
                
                print(f"Message Size: {message_size}")            
            

# Remplace le chemin du fichier par celui de ton fichier PBF
fichier_pbf = "/users/alain/temp/PbfFile.pbf"

# Lit le fichier PBF
read_pbf(fichier_pbf)
