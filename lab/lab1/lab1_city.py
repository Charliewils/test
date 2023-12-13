
from math import sqrt

def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    x1,x2 = get_lat(city1),get_lat(city2)
    y1,y2 = get_lon(city1),get_lon(city2)
    return sqrt((x1-x2)**2+(y1-y2)**2)

   
def closer_city(lat,lon,city1,city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    city = make_city(_,lat,lon)
    if distance(city,city1) < distance(city,city2):
        return get_name(city1)
    else:
        return get_name(city2)

make_city = lambda name, lat, lon: [lon, [lat], name]
get_name = lambda city: city[2]
get_lat = lambda city: city[1][0]
get_lon = lambda city: city[0]

