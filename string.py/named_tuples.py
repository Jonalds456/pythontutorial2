from collections import namedtuple

color = namedtuple('color', ['green' , 'blue' , 'purple'])

color = color(90 , 60 , 70 )

print (color.purple)


person = namedtuple('person' , ['name' , 'age' , 'course'])

person = person('Jonathan' , '20' , 'software eng')

print (person.course)
                                  
                                 
                                 
                                 