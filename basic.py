from db_connection import Db
import easyocr

easyreader= easyocr.Reader(['en'],gpu=False,detector=True)
import numpy as np
import pandas as pd
import json
import PIL

from haystack import Document, Pipeline
from haystack.nodes import FARMReader
from haystack.utils import print_answers
from pdf2image import convert_from_path
from PIL import ImageDraw

'''
Reading the Q&A model
'''
def extraction(file):
    new_reader = FARMReader(model_name_or_path=r"C:\Users\niroo\Documents\PROJECTS\Invoice automation\my_model_new_63")

    image = convert_from_path(file)

    '''
    Creating bounding boxes
    Extracting text from the invoices
    ''' 
    bounds = easyreader.readtext(np.array(image[0]), min_size=0, slope_ths=0.2, ycenter_ths=0.5,height_ths=0.5,y_ths=0.3,low_text=0.5,text_threshold=0.7,width_ths=0.8,paragraph=True,decoder='beamsearch', beamWidth=10)
    def draw_boxes(image,bounds,color='yellow',width=2):
        draw=ImageDraw.Draw(image)
        for bound in bounds:
            p0,p1,p2,p3=bound[0]
            draw.line([*p0,*p1,*p2,*p3,*p0], fill=color,width=width)
        return image

    draw_boxes(image[0],bounds)
    context=''
    for i in range(len(bounds)):
        context=context+bounds[i][1]+'\n'
    print(context)

    from haystack import Document, Pipeline
    from haystack.utils import print_answers

    '''
    Extracting information from the invoices
    '''

    p = Pipeline()
    p.add_node(component=new_reader, name="reader", inputs=["Query"])
    # Invoice details
    res1 = p.run(query="invoice number?", documents=[Document(content=context)])
    res2 = p.run(query="invoice date?", documents=[Document(content=context)])

    #Vendor details
    res3 = p.run(query="Seller name?", documents=[Document(content=context)])
    res4 = p.run(query="Address?", documents=[Document(content=context)])
    res5 = p.run(query="Seller Phone number?", documents=[Document(content=context)])
    res6 = p.run(query="Seller email Id?", documents=[Document(content=context)])
    res7 = p.run(query="Seller website?", documents=[Document(content=context)])
    res16 = p.run(query="Seller Tax/GST/VAT number?", documents=[Document(content=context)])


    #Buyer details
    res8 = p.run(query="Buyer billing name?", documents=[Document(content=context)])
    res9 = p.run(query="Buyer shipping address?", documents=[Document(content=context)])
    res10 = p.run(query="Buyer phone number?", documents=[Document(content=context)])
    res11 = p.run(query="Buyer email Id?", documents=[Document(content=context)])
    res12 = p.run(query="Buyer Tax/GST/VAT number?", documents=[Document(content=context)])


    #Total amount details
    res13 = p.run(query="Sales tax/GST percentage?", documents=[Document(content=context)])
    res14 = p.run(query="Gross total?", documents=[Document(content=context)])
    res15 = p.run(query="Net amount?", documents=[Document(content=context)])
    
    #adding 1

    '''
    Converting extracted details into dictionary format
    '''

    myData={}
    myData={res1.get('query'):res1['answers'][0].answer, 
            res2.get('query'):res2['answers'][0].answer, 
            res3.get('query'):res3['answers'][0].answer,
            res4.get('query'):res4['answers'][0].answer,
            res5.get('query'):res5['answers'][0].answer,
            res6.get('query'):res6['answers'][0].answer,
            res7.get('query'):res7['answers'][0].answer,
            res8.get('query'):res8['answers'][0].answer,
            res9.get('query'):res9['answers'][0].answer,
            res10.get('query'):res10['answers'][0].answer,
            res11.get('query'):res11['answers'][0].answer,
            res12.get('query'):res12['answers'][0].answer,
            res13.get('query'):res13['answers'][0].answer,
            res14.get('query'):res14['answers'][0].answer,
            res15.get('query'):res15['answers'][0].answer,
            res16.get('query'):res16['answers'][0].answer
            }
    
    '''
    Checking amount is present or not,
    if amount is present check description, order quantity and net price
    otherwise terminate
    '''


    data={}
    for i in range(1,100):
        no_of_desccriptions = i    
        x = str(i)+"?" 
        amt = p.run(query="Amount "+x, documents=[Document(content=context)])
   
        if ((amt['answers'][0].score >= 0.7) and (amt['answers'][0].score <= 1) ) and amt['answers'][0].answer is not "":
            
            ordqty = p.run(query="Order quantity "+x, documents=[Document(content=context)])
            if ((ordqty['answers'][0].score >= 0.7) and (ordqty['answers'][0].score <= 1) ):
                print(ordqty.get('query'),ordqty['answers'][0].answer)
            netprice = p.run(query="Net unit price "+x, documents=[Document(content=context)])
            if ((netprice['answers'][0].score >= 0.7) and (netprice['answers'][0].score <= 1) ):
                print(netprice.get('query'),netprice['answers'][0].answer)
            desc = p.run(query="description "+x, documents=[Document(content=context)])
            if ((desc['answers'][0].score >= 0.7) and (desc['answers'][0].score <= 1) ):
                print(desc.get('query'),desc['answers'][0].answer)

            data[desc.get('query')]=desc['answers'][0].answer
            data[ordqty.get('query')]=ordqty['answers'][0].answer
            data[netprice.get('query')]=netprice['answers'][0].answer
            data[amt.get('query')]=amt['answers'][0].answer
            data['no_of_desccriptions']=no_of_desccriptions
        else:
            no_of_desccriptions = i-1
        
            print("NUMBER OF ITEMS IN INVOICE = ", no_of_desccriptions, ".", x, "doesn't exist")
            data['no_of_desccriptions']=no_of_desccriptions
            break
    
    
    print(data['no_of_desccriptions'])         
    myData.update(data)

    return myData 


def result_data(file):
    data = extraction(file)
    result={}

    result['invoice_number']=data['invoice number?']
    result['invoice_date']=data['invoice date?']    
    result['seller_name']=data['Seller name?']
    result['seller_address']=data['Address?']

    if data['Seller Phone number?'] is None:
        result['seller_phone_num'] = '-'
    else:
        result['seller_phone_num']=data['Seller Phone number?']
    
    if data['Seller email Id?'] is None:
        result['seller_mailid'] = '-'
    else:
        result['seller_mailid']=data['Seller email Id?']
    
    if data['Seller website?'] is None:
        result['seller_website'] = '-'
    else:
        result['seller_website']=data['Seller website?']  
    result['seller_tax_id_num']=data['Seller Tax/GST/VAT number?']      
    
    result['customer_name']=data['Buyer billing name?']
    result['customer_address']=data['Buyer shipping address?']

    if data['Buyer phone number?'] is None:
        result['customer_phone_num'] = '-'
    else:
        result['customer_phone_num']=data['Buyer phone number?']

    if data['Buyer email Id?'] is None:
        result['customer_mailid'] = '-'
    else:
        result['customer_mailid']=data['Buyer email Id?']

    result['customer_tax_id_num']=data['Buyer Tax/GST/VAT number?']
    
    z = data['no_of_desccriptions']
    for y in range(1, z+1):
        a = str(y)
        b = str(y)+"?"
        result['product_description'+a]=data['description '+b]
        result['quantity'+a]=data['Order quantity '+b]
        result['net_price'+a]=data['Net unit price '+b]
        result['amount'+a]=data['Amount '+b]   
    result['tax_percentage']=data['Sales tax/GST percentage?']     
    result['gross_total']=data['Gross total?']
    result['net_amount']=data['Net amount?']

   

    df = pd.DataFrame(result,index=[0])
    df=df.fillna(' ')
    save_file = open("output_file.json", "a")  
    json.dump(result, save_file, indent = 6)  
    save_file.close()    
    
    for item in result.items():
        print(item)

# result_data()