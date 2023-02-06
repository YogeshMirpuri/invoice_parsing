from db_connection import Db
import easyocr

easyreader= easyocr.Reader(['en'],gpu=False,detector=True)
import numpy as np
import pandas as pd
import PIL
#from IPython.display import display,Image
from haystack import Document, Pipeline
from haystack.nodes import FARMReader
from haystack.utils import print_answers
from pdf2image import convert_from_path
from PIL import ImageDraw
def extraction(file):
    new_reader = FARMReader(model_name_or_path=r"C:\Users\niroo\Documents\PROJECTS\Invoice automation\qa model v1")

    # image = convert_from_path(r"C:\Users\niroo\Documents\invoice_parsing\invoices to test\invoice_4_color_B_253.pdf")
    image = convert_from_path(file)
        
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
    # res7 = p.run(query="Seller website?", documents=[Document(content=context)])


    #Buyer details
    res8 = p.run(query="Buyer billing name?", documents=[Document(content=context)])
    res9 = p.run(query="Buyer shipping address?", documents=[Document(content=context)])
    res10 = p.run(query="Buyer phone number?", documents=[Document(content=context)])
    res11 = p.run(query="Buyer email Id?", documents=[Document(content=context)])
    res12 = p.run(query="Buyer Tax/GST/VAT number?", documents=[Document(content=context)])


    #Total amount details
    res13 = p.run(query="Sales tax/GST percentage?", documents=[Document(content=context)])
    res14 = p.run(query="Gross total?", documents=[Document(content=context)])
    
    #adding 1



    myData={}
    myData={res1.get('query'):res1['answers'][0].answer, 
            res2.get('query'):res2['answers'][0].answer, 
            res3.get('query'):res3['answers'][0].answer,
            res4.get('query'):res4['answers'][0].answer,
            res5.get('query'):res5['answers'][0].answer,
            res6.get('query'):res6['answers'][0].answer,
            # res7.get('query'):res7['answers'][0].answer,
            res8.get('query'):res8['answers'][0].answer,
            res9.get('query'):res9['answers'][0].answer,
            res10.get('query'):res10['answers'][0].answer,
            res11.get('query'):res11['answers'][0].answer,
            res12.get('query'):res12['answers'][0].answer,
            res13.get('query'):res13['answers'][0].answer,
            res14.get('query'):res14['answers'][0].answer
            }
    
    data={}
    for i in range(1,100):

        # x = "Amount "+str(i)+"?" 
        # amt = p.run(query=x, documents=[Document(content=context)])
   
        # if ((amt['answers'][0].score >= 0.6) and (amt['answers'][0].score <= 1) ) and amt['answers'][0].answer is not "":
        #     #print("description ", i, (desc['answers'][0].answer))
          
        #     ordqty = p.run(query="Order quantity "+str(i)+"?", documents=[Document(content=context)])
        #     netprice = p.run(query="Net unit price "+str(i)+"?", documents=[Document(content=context)])
        #     desc = p.run(query="description "+str(i)+"?", documents=[Document(content=context)])

        #     data[desc.get('query')]=desc['answers'][0].answer
        #     data[ordqty.get('query')]=ordqty['answers'][0].answer
        #     data[netprice.get('query')]=netprice['answers'][0].answer
        #     data[amt.get('query')]=amt['answers'][0].answer

        no_of_desccriptions = i    
        x = str(i)+"?" 
        amt = p.run(query="Amount "+x, documents=[Document(content=context)])
   
        if ((amt['answers'][0].score >= 0.6) and (amt['answers'][0].score <= 1) ) and amt['answers'][0].answer is not "":
      
            ordqty = p.run(query="Order quantity "+x, documents=[Document(content=context)])
            netprice = p.run(query="Net unit price "+x, documents=[Document(content=context)])
            desc = p.run(query="description "+x, documents=[Document(content=context)])

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
    for item in data.items():
        print(item)

    return myData 
    # data={}
    # for i in range(1,11):
       
    #     amt = p.run(query="Amount "+str(i)+"?", documents=[Document(content=context)])
    #     print(i, amt['answers'][0].answer)
        
    #     if amt['answers'][0].answer is not None:
    #         desc = p.run(query="description "+str(i)+"?", documents=[Document(content=context)])
    #         ordqty = p.run(query="Order quantity "+str(i)+"?", documents=[Document(content=context)])
    #         netprice = p.run(query="Net unit price "+str(i)+"?", documents=[Document(content=context)])
    #         data[desc.get('query')]=desc['answers'][0].answer
    #         data[ordqty.get('query')]=ordqty['answers'][0].answer
    #         data[netprice.get('query')]=netprice['answers'][0].answer
    #         data[amt.get('query')]=amt['answers'][0].answer
    #     else:
    #         break
     
    #     myData.update(data)
     
    # return myData


def result_data(file):
    data = extraction(file)
    result={}
    
    result['seller_name']=data['Seller name?']
    result['seller_address']=data['Address?'] 
    # result['seller_phone_num']=data['Seller Phone number?']
    result['seller_phone_num']='-'
    # result['seller_mailid']=data['Seller email Id?']
    result['seller_mailid']='-'
    # result['seller_website']=data['Seller website?']
    # result['seller_tax_id_num']=data['Net unit price 1?']
    result['customer_name']=data['Buyer billing name?']
    result['customer_address']=data['Buyer shipping address?']
    # result['customer_phone_num']=data['Buyer phone number?']
    result['customer_phone_num']='-'
    # result['customer_mailid']=data['Buyer email Id?']
    result['customer_mailid']='-'
    result['customer_tax_id_num']=data['Buyer Tax/GST/VAT number?']
    result['invoice_number']=data['invoice number?']
    result['invoice_date']=data['invoice date?'] 
    result['tax_percentage']=data['Sales tax/GST percentage?']
    
    # if data['description 1?'] is None:
    #     result['product_description1']='-'
    # else:
    z = data['no_of_desccriptions']
    for y in range(1, z+1):
        a = str(y)
        b = str(y)+"?"
        # result['product_description'+x]=data["description "+x+"?"]
        result['product_description'+a]=data['description '+b]
        result['quantity'+a]=data['Order quantity '+b]
        result['net_price'+a]=data['Net unit price '+b]
        result['amount'+a]=data['Amount '+b]

            

    
    # # if data['description 2?'] is None:
    # #     result['product_description2']='-'
    # # else:
    # result['product_description2']=data['description 2?']
    # result['quantity2']=data['Order quantity 2?']
    # result['net_price2']=data['Net unit price 2?']
    # result['amount2']=data['Amount 2?']
    
    # # if data['description 3?'] is None:
    # #     result['product_description3']='-'
    # # else:
    # result['product_description3']=data['description 3?']
    # result['quantity3']=data['Order quantity 3?']
    # result['net_price3']=data['Net unit price 3?']
    # result['amount3']=data['Amount 3?']
    
    # # if data['description 4?'] is None:
    # #     result['product_description4']='-'
    # # else:
    # result['product_description4']=data['description 4?']
    # result['quantity4']=data['Order quantity 4?']
    # result['net_price4']=data['Net unit price 4?']
    # result['amount4']=data['Amount 4?']

    # # if data['description 5?'] is None:
    # #     result['product_description5']='-'
    # # else:
    # result['product_description5']=data['description 5?']
    # result['quantity5']=data['Order quantity 5?']
    # result['net_price5']=data['Net unit price 5?']
    # result['amount5']=data['Amount 5?']
    
    # # if data['description 6?'] is None:
    # #     result['product_description6']='-'
    # # else:
    # result['product_description6']=data['description 6?']
    # result['quantity6']=data['Order quantity 6?']
    # result['net_price6']=data['Net unit price 6?']
    # result['amount6']=data['Amount 6?']
    
    # # if data['description 7?'] is None:
    # #     result['product_description7']='-'
    # # else:
    # # result['product_description7']=data['description 7?']
    # result['product_description7']='-'
    # # result['quantity7']=data['Order quantity 7?']
    # result['quantity7']='-'
    # # result['net_price7']=data['Net unit price 7?']
    # result['net_price7']='-'
    # # result['amount7']=data['Amount 7?']
    # result['amount7']='-'
    
    # # if data['description 8?'] is None:
    # #     result['product_description8']='-'
    # # else:
    # # result['product_description8']=data['description 8?']
    # result['product_description8']='-'
    # # result['quantity8']=data['Order quantity 8?']
    # result['quantity8']='-'
    # # result['net_price8']=data['Net unit price 8?']
    # result['net_price8']='-'
    # # result['amount8']=data['Amount 8?']
    # result['amount8']='-'

    # # if data['description 9?'] is None:
    # #     result['product_description9']='-'
    # # else:
    # # result['product_description9']=data['description 9?']
    # result['product_description9']='-'
    # # result['quantity9']=data['Order quantity 9?']
    # result['quantity9']='-'
    # # result['net_price9']=data['Net unit price 9?']
    # result['net_price9']='-'
    # # result['amount9']=data['Amount 9?']
    # result['amount9']='-'
    
    # # if data['description 10?'] is None:
    # #     result['product_description9']='-'
    # # else:
    # # result['product_description10']=data['description 10?']
    # result['product_description10']='-'
    # # result['quantity10']=data['Order quantity 10?']
    # result['quantity10']='-'
    # # result['net_price10']=data['Net unit price 10?']
    # result['net_price10']='-'
    # # result['amount10']=data['Amount 10?']
    # result['amount10']='-'
    result['gross_total']=data['Gross total?']

   

    df = pd.DataFrame(result,index=[0])
    df=df.fillna(' ')
    print(df)
    Db.seller_table_insert(df)
    Db.customer_table_insert(df)
    Db.product_table_insert(df)
    
    
    for item in result.items():
        print(item)

# result_data()