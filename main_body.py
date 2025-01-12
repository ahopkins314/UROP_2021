import xarray as xr
import matplotlib.pyplot as plt
import numpy

ds_ua850 = xr.open_dataset("/rds/general/project/circulates/live/data/20CR/ua850_v2c_185101-201412.nc")
#the chosen grid point is [time, 0, 13, 120] -> [time, 850.0, 51.6 N, 337.5 E]
#to access year use .dt.year
#print(type(ds_ua850.time[1].dt.year))
local_speed = np.array([])
for i in range(10, 164): #February, 2014 is 1957
    local_speed = np.append(local_speed, [np.average([float(ds_ua850.ua[12*i-1, 0, 13, 120]), \
                                         float(ds_ua850.ua[12*i, 0, 13, 120]), \
                                       float(ds_ua850.ua[12*i+1, 0, 13, 120])])])
    
plt.plot(ds_ua850.time[120:1957:12].dt.year, local_speed)
plt.title('Time series of observed ua_850 at 51.6N and 337.5E')
plt.ylabel('Mean winter wind speed (m/s)')
plt.xlabel('Year')
plt.show()
