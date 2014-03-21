latitude = '-111:32.1' # Degree:minute.second
longitude = '35:05.8' # " "
elevation = 0 #Meters above surface

date = '2014/3/20 00:00' #UTC time

import ephem

#Get galactic center information
gc = ephem.Galactic(0,0) #By definition
gc_eq = ephem.Equatorial(gc) #Coordinate transform

#Set up the FixedBody for tracking
body = ephem.FixedBody()
body._ra = gc_eq.ra
body._dec = gc_eq.dec
body._epoch = gc_eq.epoch

#Set up observer

#Know the city?
#observer = ephem.city('Chicago')


#Know the lat/lon?
observer = ephem.Observer()
observer.lat = latitude # Degree:minute.second
observer.lon = longitude
observer.elevation = elevation #In meters


#Set time and date
#All times in UTC
observer.date = date

#Calculate position relative to observer
body.compute(observer)

#Print azimuth east of north
#Print altitude above horizon
print 'Az:', body.az, 'Alt:', body.alt