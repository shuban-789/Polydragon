import math # math function required for pi exactness and trig functions

# in the program, we have sl = sidelength, ap = apothem (center to side), rd = radius (center to vertex)
def perimeter(sides, measure, option):
  perimeter = 'You did not provide the condition (sl/ap/rd)' # don't calculate if no correct condition is given
  if option == "sl":
    perimeter = (sides * measure) # calculate perimeter from sidelength
  if option == "ap":
    perimeter = (2*measure*sides*math.tan(math.pi/sides)) # perimeter from apothem. tangent to get sidelength
  if option == "rd":
    perimeter = (2*measure*sides*math.sin(math.pi/sides)) # perimeter from radius. sine to get sidelength
  return perimeter

def area(sides, measure, option):
  area = 'You did not provide the condition (sl/ap/rd)'
  if option == "sl":
    area = (sides * (measure**2)) / (4*math.tan(math.pi/sides)) # calculate area from sidelength, tangent to get apothem
  if option == "ap":
    area = ((sides * (measure**2))*(math.tan(math.pi/sides))) # calculate area from apothem, tangent to get sidelength
  if option == "rd":
    area = ((sides * (measure**2))*(math.sin((2*math.pi)/sides)))/2 # calculate area from radius, using sine double angle formula to simplify sidelength*apothem
  return area
  
sidenum = int(input("Enter number of sides > "))
opt = input("What will you be giving? (sl/ap/rd) > ")
m = float(input("What is the length of that variable? > ")) # float to include possibly decimal inputs for lengths
print("Perimeter: " + str(perimeter(sidenum, m, opt)))
print("Area: " + str(area(sidenum, m, opt)))
