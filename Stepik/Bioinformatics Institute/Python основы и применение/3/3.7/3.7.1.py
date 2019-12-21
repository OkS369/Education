from xml.etree import ElementTree

#tree = ElementTree.parse("example.xml")
tree = ElementTree.fromstring(input())
#root = tree.getroot()
result = {"red": 0, "green": 0, "blue": 0}
#print(root.get("color"), 1)
result[tree.get("color")] = result[tree.get("color")] + 1
def cubes(parent, level):
    level += 1
    for cube in parent.findall('cube'):
        #print(cube.get("color"), level)
        result[cube.get("color")] = result[cube.get("color")] + level
        cubes(cube, level)


cubes(tree, 1)
print(result["red"], result["green"], result["blue"])
"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
 
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:
4 3 1
"""