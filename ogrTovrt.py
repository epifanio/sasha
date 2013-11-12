#!/usr/bin/env python
###############################################################################
#
#
# Project:
# Purpose:
#
#
# Author:   Massimo Di Stefano , epiesasha@me.com
#
###############################################################################
# Copyright (c) 2009, Massimo Di Stefano <epiesasha@me.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################

__author__ = "Massimo Di Stefano"
__copyright__ = "Copyright 2009, gfoss.it"
__credits__ = [""]
__license__ = "GPL V3"
__version__ = "1.0.0"
__maintainer__ = "Massimo Di Stefano"
__email__ = "epiesasha@me.com"
__status__ = "Production"
__date__ = ""

try:
    from osgeo import osr, ogr, gdal
except ImportError:
    import osr, ogr, gdal

import string
import sys


def GeomType2Name(type):
    if type == ogr.wkbUnknown:
        return 'wkbUnknown'
    elif type == ogr.wkbPoint:
        return 'wkbPoint'
    elif type == ogr.wkbLineString:
        return 'wkbLineString'
    elif type == ogr.wkbPolygon:
        return 'wkbPolygon'
    elif type == ogr.wkbMultiPoint:
        return 'wkbMultiPoint'
    elif type == ogr.wkbMultiLineString:
        return 'wkbMultiLineString'
    elif type == ogr.wkbMultiPolygon:
        return 'wkbMultiPolygon'
    elif type == ogr.wkbGeometryCollection:
        return 'wkbGeometryCollection'
    elif type == ogr.wkbNone:
        return 'wkbNone'
    elif type == ogr.wkbLinearRing:
        return 'wkbLinearRing'
    else:
        return 'wkbUnknown'


def Esc(x):
    return gdal.EscapeString(x, gdal.CPLES_XML)


def makestile(outfile, brush, pen, size, fill, thickness):
    brush = brush.split(',')
    pen = pen.split(',')
    size = size.split(',')
    outfile = outfile.replace('.vrt', '')
    outfile = outfile + '.omd'
    omd = '// vector file rendering options\n'
    omd += 'brush_color: %s %s %s \n' % (brush[0], brush[1], brush[2])
    omd += 'pen_color: %s %s %s \n' % (pen[0], pen[1], pen[2])
    omd += 'point_width_height: %s %s \n' % (size[0], size[1])
    omd += 'fill_flag: %s \n' % (fill)
    omd += 'thickness: %s \n' % (thickness)
    open(outfile, 'w').write(omd)


def ogrvrt(infile, outfile):
    layer_list = []
    relative = "0"
    schema = 0
    print infile
    src_ds = ogr.Open(infile, update=0)
    if len(layer_list) == 0:
        for layer in src_ds:
            layer_list.append(layer.GetLayerDefn().GetName())
    vrt = '<OGRVRTDataSource>\n'
    for name in layer_list:
        layer = src_ds.GetLayerByName(name)
        layerdef = layer.GetLayerDefn()
        vrt += '  <OGRVRTLayer name="%s">\n' % Esc(name)
        vrt += '    <SrcDataSource relativeToVRT="%s" shared="%d">%s</SrcDataSource>\n' \
               % (relative, not schema, Esc(infile))
        if schema:
            vrt += '    <SrcLayer>@dummy@</SrcLayer>\n'
        else:
            vrt += '    <SrcLayer>%s</SrcLayer>\n' % Esc(name)
        vrt += '    <GeometryType>%s</GeometryType>\n' \
               % GeomType2Name(layerdef.GetGeomType())
        srs = layer.GetSpatialRef()
        if srs is not None:
            vrt += '    <LayerSRS>%s</LayerSRS>\n' \
                   % (Esc(srs.ExportToWkt()))
        # Process all the fields.
        for fld_index in range(layerdef.GetFieldCount()):
            src_fd = layerdef.GetFieldDefn(fld_index)
            if src_fd.GetType() == ogr.OFTInteger:
                type = 'Integer'
            elif src_fd.GetType() == ogr.OFTString:
                type = 'String'
            elif src_fd.GetType() == ogr.OFTReal:
                type = 'Real'
            elif src_fd.GetType() == ogr.OFTStringList:
                type = 'StringList'
            elif src_fd.GetType() == ogr.OFTIntegerList:
                type = 'IntegerList'
            elif src_fd.GetType() == ogr.OFTRealList:
                type = 'RealList'
            elif src_fd.GetType() == ogr.OFTBinary:
                type = 'Binary'
            elif src_fd.GetType() == ogr.OFTDate:
                type = 'Date'
            elif src_fd.GetType() == ogr.OFTTime:
                type = 'Time'
            elif src_fd.GetType() == ogr.OFTDateTime:
                type = 'DateTime'
            else:
                type = 'String'

            vrt += '    <Field name="%s" type="%s"' \
                   % (Esc(src_fd.GetName()), type)
            if not schema:
                vrt += ' src="%s"' % Esc(src_fd.GetName())
            if src_fd.GetWidth() > 0:
                vrt += ' width="%d"' % src_fd.GetWidth()
            if src_fd.GetPrecision() > 0:
                vrt += ' precision="%d"' % src_fd.GetPrecision()
            vrt += '/>\n'
        vrt += '  </OGRVRTLayer>\n'
    vrt += '</OGRVRTDataSource>\n'
    file = open(outfile, 'w')
    file.write(vrt)
    file.close()
    print 'vrt wroted'
	
