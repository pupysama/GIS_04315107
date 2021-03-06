import mapnik
m = mapnik.Map(4000,1200)
m.background = mapnik.Color('yellow')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('black')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('purple'), 1)
line_symbolizer.stroke_width =  1
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="D:/4. Naruto/SMT 6/GIS/SHP_Indonesia_sungai/IND_SNG_polyline.shp")
layer = mapnik.Layer('sungai')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'pupy_sungai.png', 'png')
print "rendered image to 'pupy_sungai.png'"

