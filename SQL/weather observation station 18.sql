select round(abs(c-a)+abs(d-b).4)
from (
  select min(LAT_N) as a , min(LONG_W) as b , max(LAT_N) as c , max(LONG_W) as d
  from STATION 
  ) as min_max_coords;
