#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:03:00 2022

This is a script to extract population data per admin2 region in Pakistan.
Current example is to extract population in Sindh province for all admin2 region.

Prerequisit:
    CLIMADA Installation.
    
    PAK_POP_FILE: the file that contains population information in Pakistan
    SHP_FILE: Shape files contain the boundaries of the disired regions.
    
Output:
    SAVE_FILE: Saved population file in the admin2 regions.

@author: kampu
"""
import os
import geopandas as gdp

from climada.entity import Exposures

SHP_DIR = './data/boundaries/Sindh_admin2_delineated/'

ADMIN2_LIST = os.listdir(SHP_DIR)

SHP_FILE = SHP_DIR + '/{admin2_name}/{admin2_name_lowercase}.shp'

PAK_POP_FILE = './data/population/pak_ppp_2020_UNadj_constrained.tif'

SAVE_FILE = './data/population/admin1/Sindh/pak_ppp_2020_SINDH_admin1_{admin2_name}_admin2.tif'

for admin2_name in ADMIN2_LIST:
    # read in the shapefile
    admin2_shp = gdp.read_file(SHP_FILE.format(admin2_name=admin2_name, admin2_name_lowercase=admin2_name.lower()))
    
    admin2_pop = Exposures.from_raster(PAK_POP_FILE, geometry=admin2_shp.geometry.values)
    
    admin2_pop.write_raster(SAVE_FILE.format(admin2_name=admin2_name))