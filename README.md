# Drawtable in pillow image 
It used to draw a table in your pillow image by taking data, coordinates font etc

## Installation
```
pip install pillowdrawtable
```

## Code Snippet 

```python
import PIL
from pillowdrawtable.drawtable import Drawtable
text_font =   PIL.ImageFont.truetype("font_path", 100)
header_font =   PIL.ImageFont.truetype("font_path", 90)
table = Drawtable(data=data,
                  x=60,
                  y=80,
                  font=text_font,
                  line_spacer=50,
                  margin_text=60,
                  image_width=5000,
                  image_height=1000,
                  frame=False,
                  grid=False,
                  columngrid=True,
                  rowgrid=False,
                  header=True,
                  headerfont=header_font)
table.draw_table()

```

## License
Copyright (c) 2022 Dhanush Nayak
