import math

Point = tuple[float, float, float]

def distance_between_points(p1: Point, p2: Point) -> float:
   return math.sqrt( (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

def sphere_movement(s: Point, sv:Point, t: float) -> Point:
   return [s[i]+t*sv[i] for i in [0, 1, 2]]

def point_of_collision(radius, p1, p2) -> Point:
   # this comes from replacing the formula for a point:  point = p0 + t*v  
   # (where p0 is an origin point, t is a scalar and v the direction vector)
   # into the formula for distance between points, to obtain the value of scalar t
   # used to generate the new points coordinates given a distance in this case the radius
      
   d = distance_between_points(p1, p2)
   t = radius/d
   return tuple(p1[i]+(t*(p2[i]-p1[i])) for i in [0,1,2])

def colision_detection(a:Point, av:Point, ar: float, b:Point, bv:Point, br: float) -> tuple[bool, Point | float]:
   colision = False
   skew_or_parallel = False
   t = 0.000001
   last_distance = None

   while not colision and not skew_or_parallel :
      at = sphere_movement(a, av, t)
      bt = sphere_movement(b, bv, t)
      distance = distance_between_points(at, bt)
      colision = distance <= ar+br
      if(last_distance == None):
         last_distance = distance
      else:
         skew_or_parallel = distance > last_distance
      t += 0.000001
      
   if(colision):
      colision_point =  point_of_collision(ar, at, bt)
      return True, colision_point
   
   if(skew_or_parallel):
      return False, last_distance
   
if __name__ == "__main__":

   input_file_name = 'input.txt'
   output_file_name = 'output.txt'
   get_data = lambda s: [float(i) for  i  in s.strip().replace('\n', '').split(' ')]
   get_origin_point = lambda d: d[1:4]
   get_speed = lambda d: d[4:7]
   get_radius = lambda d: d[0]
   with open(input_file_name) as input_file, open(output_file_name, 'w') as output_file:
      for input in input_file:
         ball_1_data = get_data(input)
         ball_2_data = get_data(next(input_file))
         result = colision_detection(get_origin_point(ball_1_data), get_speed(ball_1_data), get_radius(ball_1_data), 
                                     get_origin_point(ball_2_data), get_speed(ball_2_data), get_radius(ball_2_data))
         if result[0]:
            result = 'YES\n{:.5f} {:.5f} {:.5f}\n'.format(*result[1])
         else:
            result = 'NO\n{:.5f}\n'.format(result[1])

         output_file.write(result)
