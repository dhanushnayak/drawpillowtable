from PIL import Image,ImageDraw,ImageFont
import textwrap
from PIL import *
import PIL
class Drawtable:
    """
    Use to create or draw table using PILLOW
    
    Attributes:
        data(list): template for data eg: [(a,b),(c,d)] the length of columns must be sample such as data[i] length must be same foe n
        x(int): X starting co-ordinate 
        y(int): Y starting co-ordinate
        font(PILLOW FONT): eg ImageFont.truetype('TimesNewRoman/times new roman.ttf', font_size)
        drawsheet(PIllow.ImageDRAW object)(optional): Image draw object on which table is drawn
        xend(int)(optional): x co-ordinate to end the table at xend pointx starts from x and ends at xend
        line_spacer(int)(optional): linespace from line to other from ceil text
        margin_text(int)(optional): helps to align the text in ceil
        columnwidth(list)(optional): helps to provide width per ceil custom way, columnwidth must be list eg: [0.1,0.9] and sum must be 1
        line_width(int)(optional): helps to thicker the lines of tables
        return_params(bool)(optional): works for drawsheet to  return the start_x,start_y,end_x,end_y co-ordinates after drawing table on sheet
        
        
        **kwargs
            if drawsheet is not provide:
                create a new image
                image_width(int)(optional): helps to create new image with width
                image_height(int)(optional): helps to create new image with height
            Custom style drawing:
                frame(bool)(default: True): helps only to draw frame
                grid(bool)(default: True): helps to draw innergrid in frame
                columngrid(bool)(default: True): helps to draw columns in frame
                rowgrid(bool)(default: True): helps to draw rows in frame
                header(bool)(default: True): helps to draw columns header line in frame
                headerfont(PILLOW FONT)(default: font): font for header columns and ensure header or columns need to be inserted in 0 index ie. data.insert(0,columns)
                text_color(hexcolor)(color name)(default: black): color for text in cell
                header_color(hexcolor)(color name)(default: black): color for columns in cell
                save(filename) (default: None): if trying to draw on new image to save a image save holds the filename
        
    """
    def __init__(self,data,x,y,font,drawsheet=None,xend=None,line_spacer=20,margin_text=10,line_width=2,return_params=False,**kwargs):
        
        self.__version__ = "0.1.4.1"

        image_width,image_height=0,0
        if type(font) != PIL.ImageFont.FreeTypeFont:raise ValueError("Font type expected to be Pillow Font eg : h2_font=   ImageFont.truetype('TimesNewRoman/times new roman.ttf', font_size)'")
        if not isinstance(data,list): raise ValueError("data must be a list eg: [(1,2),(2,3)]")
        if xend is not None and xend < x: raise ValueError('xend must be greater than x')
        if drawsheet is None:
            try:
                image_width = kwargs['image_width']
                image_height = kwargs['image_height']
                
            except:
                raise AttributeError("Provide Draw Sheet or Provide image_width and image_height to draw on new sheet")
        #self.frame  kwargs.get("frame",True)
        self.outer_frame = kwargs.get("frame",True)
        self.inner_frame = kwargs.get("grid",True)
        self.columns_frame = kwargs.get("columngrid",True)
        self.rows_frame = kwargs.get("rowgrid",True)
        self.header_frame = kwargs.get("header",True)
        self.header_font = kwargs.get("headerfont",font)
        self.columns_width = kwargs.get("columnwidth",None)
        self.line_color =  kwargs.get("line_color","#000000")
        self.header_color = kwargs.get("header_color","#000000")
        self.text_color = kwargs.get("text_color","#000000")
        self.save = kwargs.get("save",None)
        self.return_params  = return_params
        self.font = font
        self.new_img=False
        self.data = data
        self.margin = margin_text
        self.line_spacer = line_spacer
        self.x_init = x
        self.y_init = y
        self.y_rate = self.y_init
        self.number_of_rows = len(self.data)
        self.number_of_columns = len(self.data[0])
        self.line_width=line_width
        self.xend = xend
        if drawsheet is not None : 
            self.__draw= drawsheet
            width = xend-x
            if self.columns_width is not None: 
                if isinstance(self.columns_width,list) and sum(self.columns_width)==1:
                    self.__width_per_cell = [int(width*wi) for wi in self.columns_width]
                else: raise ValueError("columnwidth must be list eg: [0.1,0.9] and sum must be 1")
            if self.columns_width is None:
                self.__width_per_cell = [int(width/self.number_of_columns)]*len(self.data)
        else:
            if image_height!=0 and image_width!=0: 
                if self.xend is not None and self.xend>image_width: raise ValueError("xend must be lesser than image_width")
                self.new_img = True
                self.__test_back =Image.new('RGBA', (image_width, image_height), (255, 255, 255, 255))
                self.__draw = ImageDraw.Draw(self.__test_back)
                if self.xend is None: self.xend = image_width-self.x_init
                width = self.xend-self.x_init
                if self.columns_width is not None: 
                    if isinstance(self.columns_width,list) and sum(self.columns_width)==1:
                        self.__width_per_cell = [int(width*wi) for wi in self.columns_width]
                    else: raise ValueError("columnwidth must be list eg: [0.1,0.9] and sum must be 1")
                if self.columns_width is None:
                    self.__width_per_cell = [int(width/self.number_of_columns)]*len(self.data)
        
        print(self.__width_per_cell,'w')
          
    def __repr__(self):
        return "Drawtable"
    
    def __author__(self):
        return "Name: Dhanush, Email: dhanushnayak.pythonnotebook@gmail.com"
    
    def __str__(self):
        return     """
    Use to create or draw table using PILLOW
    
    Attributes:
        data(list): template for data eg: [(a,b),(c,d)] the length of columns must be sample such as data[i] length must be same foe n
        x(int): X starting co-ordinate 
        y(int): Y starting co-ordinate
        font(PILLOW FONT): eg ImageFont.truetype('TimesNewRoman/times new roman.ttf', font_size)
        drawsheet(PIllow.ImageDRAW object)(optional): Image draw object on which table is drawn
        xend(int)(optional): x co-ordinate to end the table at xend pointx starts from x and ends at xend
        line_spacer(int)(optional): linespace from line to other from ceil text
        margin_text(int)(optional): helps to align the text in ceil
        line_width(int)(optional): helps to thicker the lines of tables
        return_params(bool)(optional): works for drawsheet to  return the start_x,start_y,end_x,end_y co-ordinates after drawing table on sheet
        
        
        **kwargs
            if drawsheet is not provide:
                create a new image
                image_width(int)(optional): helps to create new image with width
                image_height(int)(optional): helps to create new image with height
            Custom style drawing:
                frame(bool)(default: True): helps only to draw frame
                grid(bool)(default: True): helps to draw innergrid in frame
                columngrid(bool)(default: True): helps to draw columns in frame
                rowgrid(bool)(default: True): helps to draw rows in frame
                header(bool)(default: True): helps to draw columns header line in frame
                headerfont(PILLOW FONT)(default: font): font for header columns and ensure header or columns need to be inserted in 0 index ie. data.insert(0,columns)
                text_color(HexColor)or(R,G,B) (default: black): color of text in cell
                header_color(HexColor)or(R,G,B) (default: black): color of columns text in cell
                save(str): provide a name to file to save table rendered  if you try to draw new_image
        
    """
    
    def __draw_text(self,xy, text="text",font=None,fill=None):
        if font is None: font = self.font
        if fill is None : fill = self.text_color   
        return self.__draw.text(xy=xy,text=f"{text}",fill=fill,font=font,align='center')
        
        
    def __draw_line(self,x1,y1,x2,y2):
        xy = ((x1,y1),(x2,y2))
        return self.__draw.line(xy,fill=self.line_color,width=self.line_width)
    
    
    def draw_table(self):
            try:
                cur_h = 0
                for row_idx,row in enumerate(self.data):
                    h_c= []
                    if row_idx==0 and self.outer_frame: self.__draw_line(self.x_init,self.y_rate-int(self.line_spacer//2),self.xend,self.y_rate-int(self.line_spacer//2)) #horizontal
                    for num_columns,j in enumerate(row):
                        lines = textwrap.wrap(str(j),width=((self.__width_per_cell[num_columns])-(self.margin)))
                        cur_h=self.y_rate  
                        for idx,line in enumerate(lines): 
                            if row_idx==0 and self.header_frame:
                                width, height = self.header_font.getsize(line)
                                xy=self.x_init+self.margin+(sum(self.__width_per_cell[:num_columns])),cur_h
                                self.__draw_text(xy,text=line,font=self.header_font,fill=self.header_color)
                                cur_h+=height
                            else:
                                width, height = self.font.getsize(line)
                                xy=self.x_init+self.margin+(sum(self.__width_per_cell[:num_columns])),cur_h
                                self.__draw_text(xy,text=line,fill=self.text_color)
                                cur_h+=height
                        h_c.append(cur_h)


                    self.y_rate = max(h_c)+self.line_spacer
                    if (self.inner_frame or self.rows_frame) and row_idx!=len(self.data)-1:self.__draw_line(self.x_init,self.y_rate-int(self.line_spacer//2),self.xend,self.y_rate-int(self.line_spacer//2)) #horizontal
                    if self.header_frame and row_idx==0 : self.__draw_line(self.x_init,self.y_rate-int(self.line_spacer//2),self.xend,self.y_rate-int(self.line_spacer//2)) #horizontal
                    if row_idx==len(self.data)-1 and self.outer_frame:
                        self.__draw_line(self.x_init,self.y_rate-int(self.line_spacer//2),self.xend,self.y_rate-int(self.line_spacer//2)) #horizontal

                #self.draw_line(self.x_init,self.y_init-int(self.line_spacer//2),self.x_init,self.y_rate-int(self.line_spacer//2))


                if self.inner_frame or self.columns_frame:
                    for  col in range(self.number_of_columns+1):
                        if (col==0 or col==self.number_of_columns)  and self.outer_frame==False:continue
                        else:self.__draw_line(self.x_init+int(sum(self.__width_per_cell[:col])),self.y_init-int(self.line_spacer//2),self.x_init++int(sum(self.__width_per_cell[:col])),self.y_rate-int(self.line_spacer//2))

                if self.return_params:
                    return self.x_init,self.y_init,self.xend,self.y_rate-int(self.line_spacer//2)


                if self.new_img: 
                    if self.save is not None:
                        if str(self.save).find('.')==-1: save = self.save+'.png'
                        else: save = self.save
                        self.__test_back.save(save)
                        print(f"Image saved as {save}")
                    return self.__test_back.show()
                
                
            except:
                raise ValueError("Change fontsize or image_width or providing xend value helps to render the content")
