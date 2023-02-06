import easyocr
easyreader= easyocr.Reader(['en'],gpu=True)
import numpy as np
import PIL
from PIL import ImageDraw
from haystack.nodes import FARMReader
from pdf2image import convert_from_path
#from IPython.display import display,Image
from haystack import Pipeline, Document
from haystack.utils import print_answers
Im=PIL.Image.open(r"C:\Users\Satya prasad Mohanty\Desktop\working invoices\testing invoices\invoice 0.png")
new_reader = FARMReader(model_name_or_path=r'C:\Users\Satya prasad Mohanty\Downloads\QA_model\my_model')
bounds = easyreader.readtext(Im, min_size=0, slope_ths=0.2, ycenter_ths=0.5,height_ths=0.5,y_ths=0.3,low_text=0.5,text_threshold=0.7,width_ths=0.8,paragraph=True,decoder='beamsearch', beamWidth=10)
def draw_boxes(Im,bounds,color='yellow',width=2):
    draw=ImageDraw.Draw(Im)
    for bound in bounds:
        p0,p1,p2,p3=bound[0]
        draw.line([*p0,*p1,*p2,*p3,*p0], fill=color,width=width)
    return Im
