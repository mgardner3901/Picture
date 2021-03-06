"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/

red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
green = Color(0x00ff00, 1.0)
black = Color(0x000000, 1.0)
cyan = Color(0x00EEEE, 1.0)
purple = Color(0x9A32CD, 1.0)

thickline = LineStyle(5, black)
thinline = LineStyle(1, black)
line = LineStyle(3, black)

rectangle = RectangleAsset(500, 500, line, blue)
circle = CircleAsset(100, thickline, purple)
circle2 = CircleAsset(50, thinline, green)
ellipse = EllipseAsset(40, 80, line, cyan)
ellipse2 = EllipseAsset(80, 40, line, cyan)
polygon = PolygonAsset([(50,200), (50,100), (150,200), (150,100)], thinline, red)

Sprite(rectangle)
Sprite(circle, (150,150))
Sprite(circle2, (204,202))
Sprite(ellipse, (210,50))
Sprite(ellipse, (210, 300))
Sprite(ellipse2, (50, 215))
Sprite(ellipse2, (300, 215))
Sprite(polygon, (203,200))






# add your code here /\  /\  /\


myapp = App()
myapp.run()
