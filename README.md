# Drawtable in pillow image 
It used to draw a table in your pillow image by taking data, coordinates font etc

## Installation
```
pip install pillowdrawtable
```

Formats
- data format = [(1,0,1),(10,2,5)]
- font_path is a path of downloaded font from open resource
  

## Code Snippet 

```python
import PIL
text_font =   PIL.ImageFont.truetype("./arial.ttf", 16)
header_font =   PIL.ImageFont.truetype("./arial.ttf", 16)
tdata= [("1",'2'),("19",100),("20",10)]
table = Drawtable(data=tdata,
                  x=60,
                xend=400,
                  y=80,
                  font=text_font,
                  line_spacer=10,
                  margin_text=10,
                  image_width=500,
                  image_height=300,
                  frame=True,
                  grid=True,
                  columngrid=False,
                  rowgrid=False,
                  header=True,
                  text_color='green',
                  header_color='red',
                  headerfont=header_font,
                  save="outputtable2.png"
                 )
table.draw_table()
```

## Output

![image](./output/outputtable.png | width=100)
## License
Copyright (c) 2022 Dhanush Nayak
