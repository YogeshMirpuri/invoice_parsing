import easyocr

easyreader= easyocr.Reader(['en'],gpu=False,detector=True)
import numpy as np
import PIL
#from IPython.display import display,Image
from haystack import Document, Pipeline
from haystack.nodes import FARMReader
from haystack.utils import print_answers
from pdf2image import convert_from_path
from PIL import ImageDraw

def extraction():
    #new_reader = FARMReader(model_name_or_path=r'C:\Users\Satya prasad Mohanty\Downloads\QA_model\my_model')
    new_reader = FARMReader(model_name_or_path=r"C:\Users\niroo\Documents\invoice_parsing\Testing_model")
    #for image invoices
    # image=PIL.Image.open(r"C:\Users\Satya prasad Mohanty\Documents\Invoice parsing\Sample invoices\Testing invoices\MicrosoftTeams-image (23).png")
    # bounds = easyreader.readtext(image, min_size=0, slope_ths=0.2, ycenter_ths=0.5,height_ths=0.5,y_ths=0.3,low_text=0.5,text_threshold=0.7,width_ths=0.8,paragraph=True,decoder='beamsearch', beamWidth=10)
    # def draw_boxes(image,bounds,color='yellow',width=2):
    #     draw=ImageDraw.Draw(image)
    #     for bound in bounds:
    #         p0,p1,p2,p3=bound[0]
    #         draw.line([*p0,*p1,*p2,*p3,*p0], fill=color,width=width)
    #     return image

    # draw_boxes(image,bounds)
    # image=pdfPath

    #for pdf invoices
    image = convert_from_path(r"C:\Users\niroo\Documents\invoice_parsing\invoice\invoice_2_charspace_3.pdf")
        
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

    # reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
    p = Pipeline()
    p.add_node(component=new_reader, name="reader", inputs=["Query"])

    res1 = p.run(
        query="invoice date?", documents=[Document(content=context)]
    )
    res2 = p.run(
        query="invoice number?", documents=[Document(content=context)]
    )
    res3 = p.run(
        query="Address?", documents=[Document(content=context)]
    )
    # res4 = p.run(
    #     query="CIN?", documents=[Document(content=context)]
    # )
    res5 = p.run(
        query="Gross total?", documents=[Document(content=context)]
    )

    res9 = p.run(
        query="description 1?", documents=[Document(content=context)]
    )

    # res11 = p.run(
    #     query="Account number?", documents=[Document(content=context)]
    # )
    # res12 = p.run(
    #     query="Approval Invoice date?", documents=[Document(content=context)]
    # )
    # res13 = p.run(
    #     query="Approval Invoice number?", documents=[Document(content=context)]
    # )
    res14 = p.run(
        query="Buyer email Id?", documents=[Document(content=context)]
    )
    # res15 = p.run(
    #     query="Buyer PAN number?", documents=[Document(content=context)]
    # )
    res16 = p.run(
        query="Buyer billing name?", documents=[Document(content=context)]
    )
    res17 = p.run(
        query="Buyer phone number?", documents=[Document(content=context)]
    )
    res18 = p.run(
        query="Buyer shipping address?", documents=[Document(content=context)]
    )
    res19 = p.run(
        query="Buyer Tax/GST/VAT number?", documents=[Document(content=context)]
    )
    res20 = p.run(
        query="Company name?", documents=[Document(content=context)]
    )
    res21 = p.run(
        query="Customer number?", documents=[Document(content=context)]
    )
    # res22 = p.run(
    #     query="Customer Purchase Order number?", documents=[Document(content=context)]
    # )
    res23 = p.run(
        query="description 2?", documents=[Document(content=context)]
    )
    res24 = p.run(
        query="description 3?", documents=[Document(content=context)]
    )
    res25 = p.run(
        query="description 4?", documents=[Document(content=context)]
    )
    # res26 = p.run(
    #     query="Fax number?", documents=[Document(content=context)]
    # )
    # res27 = p.run(
    #     query="Freight number?", documents=[Document(content=context)]
    # )
    # res28 = p.run(
    #     query="Buyer GST number?", documents=[Document(content=context)]
    # )
    # res29 = p.run(
    #     query="Item number 1?", documents=[Document(content=context)]
    # )
    # res30 = p.run(
    #     query="Item number 2?", documents=[Document(content=context)]
    # )
    # res31 = p.run(
    #     query="Item number 3?", documents=[Document(content=context)]
    # )
    # res32 = p.run(
    #     query="Item number 4?", documents=[Document(content=context)]
    # )
    res33 = p.run(
        query="Miscellaneous charges?", documents=[Document(content=context)]
    )
    res34 = p.run(
        query="Net amount?", documents=[Document(content=context)]
    )
    # res35 = p.run(
    #     query="Net merchandise total?", documents=[Document(content=context)]
    # )
    # res37 = p.run(
    #     query="Net unit price 1?", documents=[Document(content=context)]
    # )
    # res38 = p.run(
    #     query="Net unit price 2?", documents=[Document(content=context)]
    # )
    # res39 = p.run(
    #     query="Net unit price 3?", documents=[Document(content=context)]
    # )
    # res40 = p.run(
    #     query="Part number?", documents=[Document(content=context)]
    # )
    # res41 = p.run(
    #     query="Pick up date?", documents=[Document(content=context)]
    # )
    res42 = p.run(
        query="Purchase order date?", documents=[Document(content=context)]
    )
    res43 = p.run(
        query="Purchase order number?", documents=[Document(content=context)]
    )
    # res44 = p.run(
    #     query="Sales order date?", documents=[Document(content=context)]
    # )
    # res45 = p.run(
    #     query="Sales order number?", documents=[Document(content=context)]
    # )
    res46 = p.run(
        query="Sales tax/GST?", documents=[Document(content=context)]
    )
    res47 = p.run(
        query="Sales tax/GST percentage?", documents=[Document(content=context)]
    )
    res48 = p.run(
        query="Seller email Id?", documents=[Document(content=context)]
    )
    # res49 = p.run(
    #     query="Seller PAN number?", documents=[Document(content=context)]
    # )
    res50 = p.run(
        query="Seller Phone number?", documents=[Document(content=context)]
    )
    res51 = p.run(
        query="Shiping quantity?", documents=[Document(content=context)]
    )
    res52 = p.run(
        query="Shipping and handling charges?", documents=[Document(content=context)]
    )
    res53 = p.run(
        query="Shipping method?", documents=[Document(content=context)]
    )
    # res54 = p.run(
    #     query="shipping terms?", documents=[Document(content=context)]
    # )

    res56 = p.run(
        query="Terms?", documents=[Document(content=context)]
    )

    # res58 = p.run(
    #     query="Tracking number?", documents=[Document(content=context)]
    # )
    # res59 = p.run(
    #     query="Buyer GST number?", documents=[Document(content=context)]
    # )
    # res60 = p.run(
    #     query="Buyer Tax number?", documents=[Document(content=context)]
    # )
    # res61 = p.run(
    #     query="Buyer website?", documents=[Document(content=context)]
    # )
    res62 = p.run(
        query="CGST %?", documents=[Document(content=context)]
    )
    res63 = p.run(
        query="CGST?", documents=[Document(content=context)]
    )
    res64 = p.run(
        query="client number?", documents=[Document(content=context)]
    )
    res65 = p.run(
        query="Discount?", documents=[Document(content=context)]
    )
    res66 = p.run(
        query="Discount %?", documents=[Document(content=context)]
    )
    res67 = p.run(
        query="Due date?", documents=[Document(content=context)]
    )
    res68 = p.run(
        query="IGST?", documents=[Document(content=context)]
    )
    res69 = p.run(
        query="Order date?", documents=[Document(content=context)]
    )
    res70 = p.run(
        query="PO number?", documents=[Document(content=context)]
    )
    res71 = p.run(
        query="Seller name?", documents=[Document(content=context)]
    )
    res72 = p.run(
        query="Seller website?", documents=[Document(content=context)]
    )
    res73 = p.run(
        query="SGST %?", documents=[Document(content=context)]
    )
    res74 = p.run(
        query="SGST?", documents=[Document(content=context)]
    )
    res75 = p.run(
        query="Tax?", documents=[Document(content=context)]
    )

    # print(res1.get('query'),None if res1['answers'][0].score>1 or res1['answers'][0].score<0.6 else res1['answers'][0].score and  res1['answers'][0].answer)
    # print(res2.get('query'),None if res2['answers'][0].score>1 or res2['answers'][0].score<0.6 else res2['answers'][0].score and  res2['answers'][0].answer)
    # print(res3.get('query'),None if res3['answers'][0].score>1 or res3['answers'][0].score<0.6 else res3['answers'][0].score and  res3['answers'][0].answer)
    # print(res4.get('query'),None if res4['answers'][0].score>1 or res4['answers'][0].score<0.6 else res4['answers'][0].score and  res4['answers'][0].answer)
    # print(res5.get('query'),None if res5['answers'][0].score>1 or res5['answers'][0].score<0.6 else res5['answers'][0].score and  res5['answers'][0].answer)
    # print(res6.get('query'),None if res6['answers'][0].score>1 or res6['answers'][0].score<0.6 else res6['answers'][0].score and  res6['answers'][0].answer)
    # print(res7.get('query'),None if res7['answers'][0].score>1 or res7['answers'][0].score<0.6 else res7['answers'][0].score and  res7['answers'][0].answer)
    # print(res8.get('query'),None if res8['answers'][0].score>1 or res8['answers'][0].score<0.6 else res8['answers'][0].score and  res8['answers'][0].answer)
    # print(res9.get('query'),None if res9['answers'][0].score>1 or res9['answers'][0].score<0.6 else res9['answers'][0].score and  res9['answers'][0].answer)
    # print(res10.get('query'),None if res10['answers'][0].score>1 or res10['answers'][0].score<0.6 else res10['answers'][0].score and  res10['answers'][0].answer)


    # print(res1.get('query'),res1['answers'][0].answer,res1['answers'][0].score)
    # print(res2.get('query'),res2['answers'][0].answer,res2['answers'][0].score)
    # print(res3.get('query'),res3['answers'][0].answer,res3['answers'][0].score)
    # print(res4.get('query'),res4['answers'][0].answer,res4['answers'][0].score)
    # print(res5.get('query'),res5['answers'][0].answer,res5['answers'][0].score)
    # print(res6.get('query'),res6['answers'][0].answer,res6['answers'][0].score)
    # print(res7.get('query'),res7['answers'][0].answer,res7['answers'][0].score)
    # print(res9.get('query'),res9['answers'][0].answer,res9['answers'][0].score)
    # if  (1<= res1['answers'][0].score >= 0.6):
    #     print(res1.get('query'),res1['answers'][0].answer)
    # if ((res1['answers'][0].score >= 0.6) and (res1['answers'][0].score <= 1) ):
    #      print(res1.get('query'),res1['answers'][0].answer)

    #result ={}
    #result['buyer_invoice_date']=res1['answers'][0].answer if ((res1['answers'][0].score >= 0.6) and (res1['answers'][0].score <= 1) ):
        #print(res1.get('query'),res1['answers'][0].answer)
    #result['buyer_invoice_date'] = res1['answers'][0].answer if ((res1['answers'][0].score >= 0.6) and (res1['answers'][0].score <= 1) ) pass
    # result['buyer_invoice_number'] = res2['answers'][0].answer if ((res2['answers'][0].score >= 0.6) and (res2['answers'][0].score <= 1) ) else None
    # result['billing_address'] = res3['answers'][0].answer if ((res3['answers'][0].score >= 0.6) and (res3['answers'][0].score <= 1) ) else None
    # result['shipping_address'] = res4['answers'][0].answer if ((res4['answers'][0].score >= 0.6) and (res4['answers'][0].score <= 1) ) else None
    # result['total_amount'] = res5['answers'][0].answer if ((res5['answers'][0].score >= 0.6) and (res5['answers'][0].score <= 1) ) else None
    # result['buyer_billing_name'] = res6['answers'][0].answer if ((res6['answers'][0].score >= 0.6) and (res6['answers'][0].score <= 1) ) else None
    # result['seller_name'] = res7['answers'][0].answer if ((res7['answers'][0].score >= 0.6) and (res7['answers'][0].score <= 1) ) else None
    # result['po_number'] = res8['answers'][0].answer if ((res8['answers'][0].score >= 0.6) and (res8['answers'][0].score <= 1) ) else None
    # print(result)
    # import pprint
    # pprint.pprint(result)

    #result['buyer_invoice_number'] = res2['answers'][0].answer if ((res2['answers'][0].score >= 0.6) and (res2['answers'][0].score <= 1) ) else None
    #print(result)
    # import mysql.connector
    # import pandas as pd
    # import pyodbc

    # df = pd.DataFrame(result,index=[0])
    # print(df)
    # Connect to SQL Server
    # conn = mysql.connector.connect(user='root', password='brightpoint@123', host='127.0.0.1', database='invoice_data')
    # cursor = conn.cursor()
    # cursor = conn.cursor('''create table buyers_details (buyer_invoice_date varchar(10),buyer_invoice_number varchar(20),billing_address varchar(200))''')
    # #cursor.execute('''create table buyers_details (buyer_invoice_date varchar(10),buyer_invoice_number varchar(20),billing_address varchar(200))''')
    # # # cursor = conn.cursor('''create table buyer_details (buyer_billing_name varchar(50), buyer_billing_address varchar(200), buyer_phone_number varchar(30), buyer_email_id varchar(50), buyer_Tax_GST_number varchar(30),
    # # # buyer_fax_number varchar(15), buyer_PAN_number varchar(15), buyer_shipping_address varchar(200), buyer_invoice_number varchar(30), buyer_invoice_date varchar(20))''')
    # # # cursor.execute('''create table buyer_details (buyer_billing_name varchar(50), buyer_billing_address varchar(200), buyer_phone_number varchar(30), buyer_email_id varchar(50), buyer_Tax_GST_number varchar(30),
    # # # buyer_fax_number varchar(15), buyer_PAN_number varchar(15), buyer_shipping_address varchar(200), buyer_invoice_number varchar(30), buyer_invoice_date varchar(20))''')
    # # # cursor.execute('''create table bill_details (purchase_order_number varchar(30), purchase_order_date varchar(20), approval_invoice_number varchar(30),
    # # # approval_invoice_date varchar(20), sales_order_number varchar(30), sales_order_date varchar(20), shipping_terms varchar(30))''')
    # # # Insert DataFrame to Table
    # for row in df.itertuples():
    #     cursor.execute('''INSERT INTO buyers_details(buyer_invoice_date,buyer_invoice_number,billing_address)
    #                 VALUES (%s,%s,%s)''',
    #                    (row.buyer_invoice_date,
    #                     row.buyer_invoice_number,
    #                     row.billing_address))
    # conn.commit()


    if ((res1['answers'][0].score >= 0.6) and (res1['answers'][0].score <= 1) ):
        print(res1.get('query'),res1['answers'][0].answer)
    if ((res2['answers'][0].score >= 0.6) and (res2['answers'][0].score <= 1) ):
        print(res2.get('query'),res2['answers'][0].answer)
    if ((res3['answers'][0].score >= 0.6) and (res3['answers'][0].score <= 1) ):
        print(res3.get('query'),res3['answers'][0].answer)
    # if ((res4['answers'][0].score >= 0.6) and (res4['answers'][0].score <= 1) ):
    #      print(res4.get('query'),res4['answers'][0].answer)
    if ((res5['answers'][0].score >= 0.6) and (res5['answers'][0].score <= 1) ):
        print(res5.get('query'),res5['answers'][0].answer)
    # # if ((res6['answers'][0].score >= 0.6) and (res6['answers'][0].score <= 1) ):
    # #      print(res6.get('query'),res6['answers'][0].answer)     
    # # if ((res7['answers'][0].score >= 0.6) and (res7['answers'][0].score <= 1) ):
    # #      print(res7.get('query'),res7['answers'][0].answer)
    # # if ((res8['answers'][0].score >= 0.6) and (res8['answers'][0].score <= 1) ):
    # #      print(res8.get('query'),res8['answers'][0].answer)
    if ((res9['answers'][0].score >= 0.6) and (res9['answers'][0].score <= 1) ):
        print(res9.get('query'),res9['answers'][0].answer)
    # # if ((res10['answers'][0].score >= 0.6) and (res10['answers'][0].score <= 1) ):
    # #      print(res10.get('query'),res10['answers'][0].answer)

    # if ((res11['answers'][0].score >= 0.6) and (res11['answers'][0].score <= 1) ):
    #      print(res11.get('query'),res11['answers'][0].answer)
    # if ((res12['answers'][0].score >= 0.6) and (res12['answers'][0].score <= 1) ):
    #      print(res12.get('query'),res12['answers'][0].answer)
    # if ((res13['answers'][0].score >= 0.6) and (res13['answers'][0].score <= 1) ):
    #      print(res13.get('query'),res13['answers'][0].answer)
    if ((res14['answers'][0].score >= 0.6) and (res14['answers'][0].score <= 1) ):
        print(res14.get('query'),res14['answers'][0].answer)
    # if ((res15['answers'][0].score >= 0.6) and (res15['answers'][0].score <= 1) ):
    #      print(res15.get('query'),res15['answers'][0].answer)
    if ((res16['answers'][0].score >= 0.6) and (res16['answers'][0].score <= 1) ):
        print(res16.get('query'),res16['answers'][0].answer)     
    if ((res17['answers'][0].score >= 0.6) and (res17['answers'][0].score <= 1) ):
        print(res17.get('query'),res17['answers'][0].answer)
    if ((res18['answers'][0].score >= 0.6) and (res18['answers'][0].score <= 1) ):
        print(res18.get('query'),res18['answers'][0].answer)
    if ((res19['answers'][0].score >= 0.6) and (res19['answers'][0].score <= 1) ):
        print(res19.get('query'),res19['answers'][0].answer)
    if ((res20['answers'][0].score >= 0.6) and (res20['answers'][0].score <= 1) ):
        print(res20.get('query'),res20['answers'][0].answer)


    if ((res21['answers'][0].score >= 0.6) and (res21['answers'][0].score <= 1) ):
        print(res21.get('query'),res21['answers'][0].answer)
    # if ((res22['answers'][0].score >= 0.6) and (res22['answers'][0].score <= 1) ):
    #      print(res22.get('query'),res22['answers'][0].answer)
    if ((res23['answers'][0].score >= 0.6) and (res23['answers'][0].score <= 1) ):
        print(res23.get('query'),res23['answers'][0].answer)
    if ((res24['answers'][0].score >= 0.6) and (res24['answers'][0].score <= 1) ):
        print(res24.get('query'),res24['answers'][0].answer)
    if ((res25['answers'][0].score >= 0.6) and (res25['answers'][0].score <= 1) ):
        print(res25.get('query'),res25['answers'][0].answer)
    # if ((res26['answers'][0].score >= 0.6) and (res26['answers'][0].score <= 1) ):
    #      print(res26.get('query'),res26['answers'][0].answer)     
    # if ((res27['answers'][0].score >= 0.6) and (res27['answers'][0].score <= 1) ):
    #      print(res27.get('query'),res27['answers'][0].answer)
    # if ((res28['answers'][0].score >= 0.6) and (res28['answers'][0].score <= 1) ):
    #      print(res28.get('query'),res28['answers'][0].answer)
    # if ((res29['answers'][0].score >= 0.6) and (res29['answers'][0].score <= 1) ):
    #      print(res29.get('query'),res29['answers'][0].answer)
    # if ((res30['answers'][0].score >= 0.6) and (res30['answers'][0].score <= 1) ):
    #      print(res30.get('query'),res30['answers'][0].answer)

    # if ((res31['answers'][0].score >= 0.6) and (res31['answers'][0].score <= 1) ):
    #      print(res31.get('query'),res31['answers'][0].answer)
    # if ((res32['answers'][0].score >= 0.6) and (res32['answers'][0].score <= 1) ):
    #      print(res32.get('query'),res32['answers'][0].answer)
    if ((res33['answers'][0].score >= 0.6) and (res33['answers'][0].score <= 1) ):
        print(res33.get('query'),res33['answers'][0].answer)
    if ((res34['answers'][0].score >= 0.6) and (res34['answers'][0].score <= 1) ):
        print(res34.get('query'),res34['answers'][0].answer)
    # if ((res35['answers'][0].score >= 0.6) and (res35['answers'][0].score <= 1) ):
    #      print(res35.get('query'),res35['answers'][0].answer)
    # if ((res36['answers'][0].score >= 0.6) and (res36['answers'][0].score <= 1) ):
    #      print(res36.get('query'),res36['answers'][0].answer)     
    # if ((res37['answers'][0].score >= 0.6) and (res37['answers'][0].score <= 1) ):
    #      print(res37.get('query'),res37['answers'][0].answer)
    # if ((res38['answers'][0].score >= 0.6) and (res38['answers'][0].score <= 1) ):
    #      print(res38.get('query'),res38['answers'][0].answer)
    # if ((res39['answers'][0].score >= 0.6) and (res39['answers'][0].score <= 1) ):
    #      print(res39.get('query'),res39['answers'][0].answer)
    # if ((res40['answers'][0].score >= 0.6) and (res40['answers'][0].score <= 1) ):
    #      print(res40.get('query'),res40['answers'][0].answer)


    # if ((res41['answers'][0].score >= 0.6) and (res41['answers'][0].score <= 1) ):
    #      print(res41.get('query'),res41['answers'][0].answer)
    if ((res42['answers'][0].score >= 0.6) and (res42['answers'][0].score <= 1) ):
        print(res42.get('query'),res42['answers'][0].answer)
    if ((res43['answers'][0].score >= 0.6) and (res43['answers'][0].score <= 1) ):
        print(res43.get('query'),res43['answers'][0].answer)
    # if ((res44['answers'][0].score >= 0.6) and (res44['answers'][0].score <= 1) ):
    #      print(res44.get('query'),res44['answers'][0].answer)
    # if ((res45['answers'][0].score >= 0.6) and (res45['answers'][0].score <= 1) ):
    #      print(res45.get('query'),res45['answers'][0].answer)
    if ((res46['answers'][0].score >= 0.6) and (res46['answers'][0].score <= 1) ):
        print(res46.get('query'),res46['answers'][0].answer)     
    if ((res47['answers'][0].score >= 0.6) and (res47['answers'][0].score <= 1) ):
        print(res47.get('query'),res47['answers'][0].answer)
    if ((res48['answers'][0].score >= 0.6) and (res48['answers'][0].score <= 1) ):
        print(res48.get('query'),res48['answers'][0].answer)
    # if ((res49['answers'][0].score >= 0.6) and (res49['answers'][0].score <= 1) ):
    #      print(res49.get('query'),res49['answers'][0].answer)
    if ((res50['answers'][0].score >= 0.6) and (res50['answers'][0].score <= 1) ):
        print(res50.get('query'),res50['answers'][0].answer)


    if ((res51['answers'][0].score >= 0.6) and (res51['answers'][0].score <= 1) ):
        print(res51.get('query'),res51['answers'][0].answer)
    if ((res52['answers'][0].score >= 0.6) and (res52['answers'][0].score <= 1) ):
        print(res52.get('query'),res52['answers'][0].answer)
    if ((res53['answers'][0].score >= 0.6) and (res53['answers'][0].score <= 1) ):
        print(res3.get('query'),res3['answers'][0].answer)
    # if ((res54['answers'][0].score >= 0.6) and (res54['answers'][0].score <= 1) ):
    #      print(res54.get('query'),res54['answers'][0].answer)
    # if ((res55['answers'][0].score >= 0.6) and (res55['answers'][0].score <= 1) ):
    #      print(res55.get('query'),res55['answers'][0].answer)
    if ((res56['answers'][0].score >= 0.6) and (res56['answers'][0].score <= 1) ):
        print(res56.get('query'),res56['answers'][0].answer)     
    # if ((res57['answers'][0].score >= 0.6) and (res57['answers'][0].score <= 1) ):
    # #      print(res57.get('query'),res57['answers'][0].answer)
    # if ((res58['answers'][0].score >= 0.6) and (res58['answers'][0].score <= 1) ):
    #      print(res58.get('query'),res58['answers'][0].answer)
    # if ((res59['answers'][0].score >= 0.6) and (res59['answers'][0].score <= 1) ):
    #      print(res59.get('query'),res59['answers'][0].answer)
    # if ((res60['answers'][0].score >= 0.6) and (res60['answers'][0].score <= 1) ):
    #      print(res60.get('query'),res60['answers'][0].answer)


    # if ((res61['answers'][0].score >= 0.6) and (res61['answers'][0].score <= 1) ):
    #      print(res61.get('query'),res61['answers'][0].answer)
    if ((res62['answers'][0].score >= 0.6) and (res62['answers'][0].score <= 1) ):
        print(res62.get('query'),res62['answers'][0].answer)
    if ((res63['answers'][0].score >= 0.6) and (res63['answers'][0].score <= 1) ):
        print(res63.get('query'),res63['answers'][0].answer)
    if ((res64['answers'][0].score >= 0.6) and (res64['answers'][0].score <= 1) ):
        print(res64.get('query'),res64['answers'][0].answer)
    if ((res65['answers'][0].score >= 0.6) and (res65['answers'][0].score <= 1) ):
        print(res65.get('query'),res65['answers'][0].answer)
    if ((res66['answers'][0].score >= 0.6) and (res66['answers'][0].score <= 1) ):
        print(res66.get('query'),res66['answers'][0].answer)     
    if ((res67['answers'][0].score >= 0.6) and (res67['answers'][0].score <= 1) ):
        print(res67.get('query'),res67['answers'][0].answer)
    if ((res68['answers'][0].score >= 0.6) and (res68['answers'][0].score <= 1) ):
        print(res68.get('query'),res68['answers'][0].answer)
    if ((res69['answers'][0].score >= 0.6) and (res69['answers'][0].score <= 1) ):
        print(res69.get('query'),res69['answers'][0].answer)
    if ((res70['answers'][0].score >= 0.6) and (res70['answers'][0].score <= 1) ):
        print(res70.get('query'),res70['answers'][0].answer)


    if ((res71['answers'][0].score >= 0.6) and (res71['answers'][0].score <= 1) ):
        print(res71.get('query'),res71['answers'][0].answer)
    if ((res72['answers'][0].score >= 0.6) and (res72['answers'][0].score <= 1) ):
        print(res72.get('query'),res72['answers'][0].answer)
    if ((res73['answers'][0].score >= 0.6) and (res73['answers'][0].score <= 1) ):
        print(res73.get('query'),res73['answers'][0].answer)
    if ((res74['answers'][0].score >= 0.6) and (res74['answers'][0].score <= 1) ):
        print(res74.get('query'),res74['answers'][0].answer)
    if ((res75['answers'][0].score >= 0.6) and (res75['answers'][0].score <= 1) ):
        print(res75.get('query'),res75['answers'][0].answer)
    
    # if ((res77['answers'][0].score >= 0.6) and (res77['answers'][0].score <= 1) ):
    #      print(res77.get('query'),res77['answers'][0].answer)
    # if ((res78['answers'][0].score >= 0.6) and (res78['answers'][0].score <= 1) ):
    #      print(res78.get('query'),res78['answers'][0].answer)
    # if ((res79['answers'][0].score >= 0.6) and (res79['answers'][0].score <= 1) ):
    #      print(res79.get('query'),res79['answers'][0].answer)
    # if ((res80['answers'][0].score >= 0.6) and (res80['answers'][0].score <= 1) ):
    #      print(res80.get('query'),res80['answers'][0].answer)

    myData={}
    list1=['decription 1?','decription 2?','decription 3?','decription 4?']
    myData={res1.get('query'):res1['answers'][0].answer, 
            res2.get('query'):res2['answers'][0].answer, 
            res3.get('query'):res3['answers'][0].answer,
            res9.get('query'):res9['answers'][0].answer,
            res23.get('query'):res23['answers'][0].answer,
            res24.get('query'):res24['answers'][0].answer,
            res25.get('query'):res25['answers'][0].answer,
            res47.get('query'):res47['answers'][0].answer,
            res71.get('query'):res71['answers'][0].answer,
            res75.get('query'):res75['answers'][0].answer,
            # res37.get('query'):res37['answers'][0].answer,
            # res38.get('query'):res38['answers'][0].answer,
            # res39.get('query'):res39['answers'][0].answer,
            # res76.get('query'):res76['answers'][0].answer,
            # res77.get('query'):res77['answers'][0].answer,
            # res78.get('query'):res78['answers'][0].answer,
            # res79.get('query'):res79['answers'][0].answer,
            # res80.get('query'):res80['answers'][0].answer
            }
    for i in list1:
        if myData[i] is not None:
            print(myData[i])
            continue
        else:
            break
    
    return myData


    