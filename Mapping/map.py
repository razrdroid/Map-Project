import folium
import pandas
data=pandas.read_csv("Vol.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
ele=list(data["ELEV"])
name=list(data["NAME"])
map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")
def color_det(ele):
    if ele>2000 and ele<3000:
        return 'orange'
    elif ele<2000:
        return 'green'
    else: return 'red'
for lt, ln, el, nm in zip(lat,lon,ele,name):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm)+'\n'+str(el)+' m',parse_html=True), icon=folium.Icon(color=color_det(el))))
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                         else 'red' if 10000000<=x['properties']['POP2005']<20000000
                         else 'yellow' if 20000000<=x['properties']['POP2005']<=30000000
                         else 'blue'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
