from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import copy
import os
from datetime import datetime



now = datetime.now()
current_date = now.date()

            
ad1_path = rf'C:\Users\16196\Food Ads\valley_food_ads_\{current_date}_1.jpg'
ad2_path = rf'C:\Users\16196\Food Ads\valley_food_ads_\{current_date}_2.jpg'

def gray_image(path, path2):
    image = Image.open(path)

    gray_image1 = image.convert("L")

    image_matrix = np.array(gray_image1)

    hot_deals_xl = 365
    hot_deals_xu = 1050

    hot_deals = image_matrix[hot_deals_xl :hot_deals_xu]
    

    hot_deals_1_xl = 0
    hot_deals_1_xu = 376
    hot_deals_1_yl = 598
    hot_deals_1_yu = 10000

    hot_deals_1 = hot_deals[hot_deals_1_xl:hot_deals_1_xu, hot_deals_1_yl:hot_deals_1_yu]




    hot_deals_2_xl = 0
    hot_deals_2_xu = 376
    hot_deals_2_yl = 0
    hot_deals_2_yu = 590

    hot_deals_2 = hot_deals[hot_deals_2_xl:hot_deals_2_xu, hot_deals_2_yl:hot_deals_2_yu]




    hot_deals_3_xl = 377
    hot_deals_3_xu = 10000
    hot_deals_3_yl = 0
    hot_deals_3_yu = 296

    hot_deals_3 = hot_deals[hot_deals_3_xl:hot_deals_3_xu, hot_deals_3_yl:hot_deals_3_yu]


    hot_deals_4_xl = 377
    hot_deals_4_xu = 10000
    hot_deals_4_yl = 299
    hot_deals_4_yu = 590

    hot_deals_4 = hot_deals[hot_deals_4_xl:hot_deals_4_xu, hot_deals_4_yl:hot_deals_4_yu]



    hot_deals_5_xl = 377
    hot_deals_5_xu = 10000
    hot_deals_5_yl = 595
    hot_deals_5_yu = 888

    hot_deals_5 = hot_deals[hot_deals_5_xl:hot_deals_5_xu, hot_deals_5_yl:hot_deals_5_yu]



    hot_deals_6_xl = 377
    hot_deals_6_xu = 10000
    hot_deals_6_yl = 890
    hot_deals_6_yu = 10000


    hot_deals_6 = hot_deals[hot_deals_6_xl:hot_deals_6_xu, hot_deals_6_yl:hot_deals_6_yu]


    produce_xl = 1143
    produce_xu = 1780

    produce = image_matrix[produce_xl:produce_xu]

    produce_1_xl = 0
    produce_1_xu = 320
    produce_1_yl = 0
    produce_1_yu = 295

    produce_1 = produce[produce_1_xl:produce_1_xu,produce_1_yl:produce_1_yu]
   

    produce_2_xl = 0
    produce_2_xu = 320
    produce_2_yl = 300
    produce_2_yu = 590

    produce_2 = produce[produce_2_xl:produce_2_xu,produce_2_yl:produce_2_yu]
   



    produce_3_xl = 0
    produce_3_xu = 320
    produce_3_yl = 595
    produce_3_yu = 888

    produce_3 = produce[produce_3_xl:produce_3_xu,produce_3_yl:produce_3_yu]
    


    produce_4_xl = 0
    produce_4_xu = 320
    produce_4_yl = 890
    produce_4_yu = 10000

    produce_4 = produce[produce_4_xl:produce_4_xu,produce_4_yl:produce_4_yu]
    


    produce_5_xl = 324
    produce_5_xu = 10000
    produce_5_yl = 0
    produce_5_yu = 295

    produce_5 = produce[produce_5_xl:produce_5_xu,produce_5_yl:produce_5_yu]
    

    produce_6_xl = 324
    produce_6_xu = 10000
    produce_6_yl = 300
    produce_6_yu = 590

    produce_6 = produce[produce_6_xl:produce_6_xu,produce_6_yl:produce_6_yu]
    



    produce_7_xl = 324
    produce_7_xu = 10000
    produce_7_yl = 595
    produce_7_yu = 888

    produce_7 = produce[produce_7_xl:produce_7_xu,produce_7_yl:produce_7_yu]
    


    produce_8_xl = 324
    produce_8_xu = 10000
    produce_8_yl = 890
    produce_8_yu = 10000

    produce_8 = produce[produce_8_xl:produce_8_xu,produce_8_yl:produce_8_yu]
    

    meat_xl = 1871
    meatxu = -40

    meat = image_matrix[meat_xl:meatxu]


    meat_1_xl = 0 
    meat_1_xu = 310
    meat_1_yl = 0
    meat_1_yu = 296


    meat_1 = meat[meat_1_xl:meat_1_xu,meat_1_yl:meat_1_yu]




    meat_2_xl = 0 
    meat_2_xu = 310
    meat_2_yl = 302
    meat_2_yu = 595


    meat_2 = meat[meat_2_xl:meat_2_xu,meat_2_yl:meat_2_yu]




    meat_3_xl = 0 
    meat_3_xu = 310
    meat_3_yl = 600
    meat_3_yu = 888


    meat_3 = meat[meat_3_xl:meat_3_xu,meat_3_yl:meat_3_yu]


    meat_4_xl = 0 
    meat_4_xu = 310
    meat_4_yl = 900
    meat_4_yu = 10000

    meat_4 = meat[meat_4_xl:meat_4_xu,meat_4_yl:meat_4_yu]



    meat_5_xl = 317 
    meat_5_xu = 10000
    meat_5_yl = 0
    meat_5_yu = 296

    meat_5 = meat[meat_5_xl:meat_5_xu,meat_5_yl:meat_5_yu]


    meat_6_xl = 317 
    meat_6_xu = 10000
    meat_6_yl = 302
    meat_6_yu = 595

    meat_6 = meat[meat_6_xl:meat_6_xu,meat_6_yl:meat_6_yu]


    meat_7_xl = 317 
    meat_7_xu = 10000
    meat_7_yl = 600
    meat_7_yu = 888

    meat_7 = meat[meat_7_xl:meat_7_xu,meat_7_yl:meat_7_yu]


    meat_8_xl = 317 
    meat_8_xu = 10000
    meat_8_yl = 900
    meat_8_yu = 10000


    meat_8 = meat[meat_8_xl:meat_8_xu,meat_8_yl:meat_8_yu]


    image2 = Image.open(path2)

    gray_image2 = image2.convert("L")


    image_matrix2 = np.array(gray_image2)




    grocery_xl = 82
    grocery_xu = 1235

    grocery = image_matrix2[grocery_xl:grocery_xu]


    grocery_1_xl = 0
    grocery_1_xu = 400 
    grocery_1_yl = 0
    grocery_1_yu = 305

    grocery_1 =  grocery[grocery_1_xl:grocery_1_xu,grocery_1_yl:grocery_1_yu]



    grocery_2_xl = 0
    grocery_2_xu = 400 
    grocery_2_yl = 305
    grocery_2_yu = 600

    grocery_2 =  grocery[grocery_2_xl:grocery_2_xu,grocery_2_yl:grocery_2_yu]



    grocery_3_xl = 0
    grocery_3_xu = 400 
    grocery_3_yl = 605
    grocery_3_yu = 910

    grocery_3 =  grocery[grocery_3_xl:grocery_3_xu,grocery_3_yl:grocery_3_yu]



    grocery_4_xl = 0
    grocery_4_xu = 400 
    grocery_4_yl = 905
    grocery_4_yu = 10000

    grocery_4 =  grocery[grocery_4_xl:grocery_4_xu,grocery_4_yl:grocery_4_yu]


    #row 2

    grocery_5_xl = 400
    grocery_5_xu = 780 
    grocery_5_yl = 0
    grocery_5_yu = 305

    grocery_5 =  grocery[grocery_5_xl:grocery_5_xu,grocery_5_yl:grocery_5_yu]


    grocery_6_xl = 400
    grocery_6_xu = 780
    grocery_6_yl = 305
    grocery_6_yu = 600

    grocery_6 =  grocery[grocery_6_xl:grocery_6_xu,grocery_6_yl:grocery_6_yu]



    grocery_7_xl = 400
    grocery_7_xu = 780 
    grocery_7_yl = 605
    grocery_7_yu = 910
    grocery_7 =  grocery[grocery_7_xl:grocery_7_xu,grocery_7_yl:grocery_7_yu]


    grocery_8_xl = 400
    grocery_8_xu = 780 
    grocery_8_yl = 905
    grocery_8_yu = 10000

    grocery_8 =  grocery[grocery_8_xl:grocery_8_xu,grocery_8_yl:grocery_8_yu]

    #row 2

    grocery_9_xl = 780
    grocery_9_xu = 10000 
    grocery_9_yl = 0
    grocery_9_yu = 305

    grocery_9 =  grocery[grocery_9_xl:grocery_9_xu,grocery_9_yl:grocery_9_yu]


    grocery_10_xl = 780
    grocery_10_xu = 10000
    grocery_10_yl = 305
    grocery_10_yu = 600

    grocery_10 =  grocery[grocery_10_xl:grocery_10_xu,grocery_10_yl:grocery_10_yu]




    grocery_11_xl = 780
    grocery_11_xu = 10000 
    grocery_11_yl = 605
    grocery_11_yu = 910

    grocery_11 =  grocery[grocery_11_xl:grocery_11_xu,grocery_11_yl:grocery_11_yu]


    grocery_12_xl = 780
    grocery_12_xu = 10000 
    grocery_12_yl = 905
    grocery_12_yu = 10000

    grocery_12 =  grocery[grocery_12_xl:grocery_12_xu,grocery_12_yl:grocery_12_yu]


    valley_kitchen_xl = 1330
    valley_kitchen_xu = 1590
    valley_kitchen = image_matrix2[valley_kitchen_xl:valley_kitchen_xu]



    valley_kitchen_1_yl = 0
    valley_kitchen_1_yu = 297


    valley_kitchen_1 = valley_kitchen[:,valley_kitchen_1_yl:valley_kitchen_1_yu]


    valley_kitchen_2_yl = 300
    valley_kitchen_2_yu = 590

    valley_kitchen_2 = valley_kitchen[:,valley_kitchen_2_yl:valley_kitchen_2_yu]



    valley_kitchen_3_yl = 593
    valley_kitchen_3_yu = 888

    valley_kitchen_3 = valley_kitchen[:,valley_kitchen_3_yl:valley_kitchen_3_yu]



    valley_kitchen_4_yl = 888
    valley_kitchen_4_yu = 10000

    valley_kitchen_4 = valley_kitchen[:,valley_kitchen_4_yl:valley_kitchen_4_yu]


    bulk_foods_xl = 1678
    bulk_foods_xu = 1960
    bulk_foods = image_matrix2[bulk_foods_xl:bulk_foods_xu]

    
    bulk_foods_1_yl = 0
    bulk_foods_1_yu = 298

    bulk_foods_1 = bulk_foods[:,bulk_foods_1_yl:bulk_foods_1_yu]


    bulk_foods_2_yl = 300
    bulk_foods_2_yu = 593

    bulk_foods_2 = bulk_foods[:,bulk_foods_2_yl:bulk_foods_2_yu]


    bulk_foods_3_yl = 596
    bulk_foods_3_yu = 888
    bulk_foods_3 = bulk_foods[:,bulk_foods_3_yl:bulk_foods_3_yu]


    bulk_foods_4_yl = 894
    bulk_foods_4_yu = 10000
    bulk_foods_4 = bulk_foods[:,bulk_foods_4_yl:bulk_foods_4_yu]

        
    dairy_and_frozen_xl = 2000
    dairy_and_frozen_xu = -40
    dairy_and_frozen_yl = 0 
    dairy_and_frozen_yu = 595

    dairy_and_frozen = image_matrix2[dairy_and_frozen_xl:dairy_and_frozen_xu, dairy_and_frozen_yl:dairy_and_frozen_yu]


    dairy_and_frozen_1_xl = 0
    dairy_and_frozen_1_xu = 250
    dairy_and_frozen_1_yl = 0
    dairy_and_frozen_1_yu = 290

    dairy_and_frozen_1 = dairy_and_frozen[dairy_and_frozen_1_xl:dairy_and_frozen_1_xu,dairy_and_frozen_1_yl:dairy_and_frozen_1_yu]


    dairy_and_frozen_2_xl = 0
    dairy_and_frozen_2_xu = 250
    dairy_and_frozen_2_yl = 300
    dairy_and_frozen_2_yu = -2

    dairy_and_frozen_2 = dairy_and_frozen[dairy_and_frozen_2_xl:dairy_and_frozen_2_xu,dairy_and_frozen_2_yl:dairy_and_frozen_2_yu]


    dairy_and_frozen_3_xl = 250
    dairy_and_frozen_3_xu = -15
    dairy_and_frozen_3_yl = 0
    dairy_and_frozen_3_yu = 290

    dairy_and_frozen_3 = dairy_and_frozen[dairy_and_frozen_3_xl:dairy_and_frozen_3_xu,dairy_and_frozen_3_yl:dairy_and_frozen_3_yu]



    dairy_and_frozen_4_xl = 250
    dairy_and_frozen_4_xu = -15
    dairy_and_frozen_4_yl = 300
    dairy_and_frozen_4_yu = -2

    dairy_and_frozen_4 = dairy_and_frozen[dairy_and_frozen_4_xl:dairy_and_frozen_4_xu,dairy_and_frozen_4_yl:dairy_and_frozen_4_yu]


    deli_and_bakery_xl = 2000
    deli_and_bakery_xu = -40
    deli_and_bakery_yl = 600
    deli_and_bakery_yu = 10000

    deli_and_bakery = image_matrix2[deli_and_bakery_xl:deli_and_bakery_xu, deli_and_bakery_yl:deli_and_bakery_yu]

    deli_and_bakery_1_xl = 0 
    deli_and_bakery_1_xu = 265
    deli_and_bakery_1_yl = 0
    deli_and_bakery_1_yu = 285

    deli_and_bakery_1 = deli_and_bakery[deli_and_bakery_1_xl:deli_and_bakery_1_xu, deli_and_bakery_1_yl:deli_and_bakery_1_yu]



    deli_and_bakery_2_xl = 0 
    deli_and_bakery_2_xu = 265
    deli_and_bakery_2_yl = 290
    deli_and_bakery_2_yu = 10000

    deli_and_bakery_2 = deli_and_bakery[deli_and_bakery_2_xl:deli_and_bakery_2_xu, deli_and_bakery_2_yl:deli_and_bakery_2_yu]



    deli_and_bakery_3_xl = 270 
    deli_and_bakery_3_xu = -10
    deli_and_bakery_3_yl = 0
    deli_and_bakery_3_yu = 285

    deli_and_bakery_3 = deli_and_bakery[deli_and_bakery_3_xl:deli_and_bakery_3_xu, deli_and_bakery_3_yl:deli_and_bakery_3_yu]



    deli_and_bakery_4_xl = 270  
    deli_and_bakery_4_xu = -10
    deli_and_bakery_4_yl = 290
    deli_and_bakery_4_yu = 10000

    deli_and_bakery_4 = deli_and_bakery[deli_and_bakery_4_xl:deli_and_bakery_4_xu, deli_and_bakery_4_yl:deli_and_bakery_4_yu]


    def save_image_from_matrix(matrix, filename, folder_path):
        image = Image.fromarray(matrix)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        image.save(os.path.join(folder_path, filename))

    hot_deals_list = [
    ("hot_deals_1", hot_deals_1),
    ("hot_deals_2", hot_deals_2),
    ("hot_deals_3", hot_deals_3),
    ("hot_deals_4", hot_deals_4),
    ("hot_deals_5", hot_deals_5),
    ("hot_deals_6", hot_deals_6)
]
    produce_list = [
    ("produce_1", produce_1),
    ("produce_2", produce_2),
    ("produce_3", produce_3),
    ("produce_4", produce_4),
    ("produce_5", produce_5),
    ("produce_6", produce_6),
    ("produce_7", produce_7),
    ("produce_8",produce_8)
]
    meat_list = [
    ("meat_1", meat_1),
    ("meat_2", meat_2),
    ("meat_3", meat_3),
    ("meat_4", meat_4),
    ("meat_5", meat_5),
    ("meat_6", meat_6),
    ("meat_7", meat_7),
    ("meat_8",meat_8)
]
    grocery_list = [
    ("grocery_1", grocery_1),
    ("grocery_2", grocery_2),
    ("grocery_3", grocery_3),
    ("grocery_4", grocery_4),
    ("grocery_5", grocery_5),
    ("grocery_6", grocery_6),
    ("grocery_7", grocery_7),
    ("grocery_8",grocery_8),
    ("grocery_9",grocery_9),
    ("grocery_10",grocery_10),
    ("grocery_11",grocery_11),
    ("grocery_12",grocery_12)
]
    valley_kitchen_list = [
    ("valley_kitchen_1", valley_kitchen_1),
    ("valley_kitchen_2", valley_kitchen_2),
    ("valley_kitchen_3", valley_kitchen_3),
    ("valley_kitchen_4", valley_kitchen_4)
]
    bulk_foods_list = [
    ("bulk_foods_1", bulk_foods_1),
    ("bulk_foods_2", bulk_foods_2),
    ("bulk_foods_3", bulk_foods_3),
    ("bulk_foods_4", bulk_foods_4)
]
    dairy_and_frozen_list = [
    ("dairy_and_frozen_1", dairy_and_frozen_1),
    ("dairy_and_frozen_2", dairy_and_frozen_2),
    ("dairy_and_frozen_3", dairy_and_frozen_3),
    ("dairy_and_frozens_4", dairy_and_frozen_4)
]
    deli_and_bakery_list = [
    ("deli_and_bakery_1", deli_and_bakery_1),
    ("deli_and_bakery_2", deli_and_bakery_2),
    ("deli_and_bakery_3", deli_and_bakery_3),
    ("deli_and_bakery_4", deli_and_bakery_4)
]

    folder_path = 'gray_valley_food_pics'

    lists = [
        (hot_deals_list, 'hot_deals'),
        (produce_list, 'produce_items'),
        (meat_list, 'meat_items'),
        (grocery_list, 'grocery_items'),
        (valley_kitchen_list, 'valley_kitchen_items'),
        (bulk_foods_list, 'bulk_foods_items'),
        (dairy_and_frozen_list, 'dairy_and_frozen_items'),
        (deli_and_bakery_list, 'deli_and_bakery_items')
    ]

    items_dict = {}
    lengths_dict = {}

    for lst, name in lists:
        items_dict[name] = [lst[i][1] for i in range(len(lst))]
        lengths_dict[name] = len(items_dict[name])

    all_items = []
    for name in lengths_dict:
        all_items.extend(items_dict[name])
    len_all_items = len(all_items)

    index = 0
    for name, length in lengths_dict.items():
        for i in range(length):
            filename = f'{name}_{i}.png'
            save_image_from_matrix(all_items[index], filename, folder_path)
            index += 1
    


gray_image(ad1_path, ad2_path)




def norm_image(path, path2):
    image = Image.open(path)


    image_matrix = np.array(image)

    hot_deals_xl = 365
    hot_deals_xu = 1050

    hot_deals = image_matrix[hot_deals_xl :hot_deals_xu]
    

    hot_deals_1_xl = 0
    hot_deals_1_xu = 376
    hot_deals_1_yl = 598
    hot_deals_1_yu = 10000

    hot_deals_1 = hot_deals[hot_deals_1_xl:hot_deals_1_xu, hot_deals_1_yl:hot_deals_1_yu]




    hot_deals_2_xl = 0
    hot_deals_2_xu = 376
    hot_deals_2_yl = 0
    hot_deals_2_yu = 590

    hot_deals_2 = hot_deals[hot_deals_2_xl:hot_deals_2_xu, hot_deals_2_yl:hot_deals_2_yu]




    hot_deals_3_xl = 377
    hot_deals_3_xu = 10000
    hot_deals_3_yl = 0
    hot_deals_3_yu = 296

    hot_deals_3 = hot_deals[hot_deals_3_xl:hot_deals_3_xu, hot_deals_3_yl:hot_deals_3_yu]


    hot_deals_4_xl = 377
    hot_deals_4_xu = 10000
    hot_deals_4_yl = 299
    hot_deals_4_yu = 590

    hot_deals_4 = hot_deals[hot_deals_4_xl:hot_deals_4_xu, hot_deals_4_yl:hot_deals_4_yu]



    hot_deals_5_xl = 377
    hot_deals_5_xu = 10000
    hot_deals_5_yl = 595
    hot_deals_5_yu = 888

    hot_deals_5 = hot_deals[hot_deals_5_xl:hot_deals_5_xu, hot_deals_5_yl:hot_deals_5_yu]



    hot_deals_6_xl = 377
    hot_deals_6_xu = 10000
    hot_deals_6_yl = 890
    hot_deals_6_yu = 10000


    hot_deals_6 = hot_deals[hot_deals_6_xl:hot_deals_6_xu, hot_deals_6_yl:hot_deals_6_yu]


    produce_xl = 1143
    produce_xu = 1780

    produce = image_matrix[produce_xl:produce_xu]

    produce_1_xl = 0
    produce_1_xu = 320
    produce_1_yl = 0
    produce_1_yu = 295

    produce_1 = produce[produce_1_xl:produce_1_xu,produce_1_yl:produce_1_yu]
   

    produce_2_xl = 0
    produce_2_xu = 320
    produce_2_yl = 300
    produce_2_yu = 590

    produce_2 = produce[produce_2_xl:produce_2_xu,produce_2_yl:produce_2_yu]
   



    produce_3_xl = 0
    produce_3_xu = 320
    produce_3_yl = 595
    produce_3_yu = 888

    produce_3 = produce[produce_3_xl:produce_3_xu,produce_3_yl:produce_3_yu]
    


    produce_4_xl = 0
    produce_4_xu = 320
    produce_4_yl = 890
    produce_4_yu = 10000

    produce_4 = produce[produce_4_xl:produce_4_xu,produce_4_yl:produce_4_yu]
    


    produce_5_xl = 324
    produce_5_xu = 10000
    produce_5_yl = 0
    produce_5_yu = 295

    produce_5 = produce[produce_5_xl:produce_5_xu,produce_5_yl:produce_5_yu]
    

    produce_6_xl = 324
    produce_6_xu = 10000
    produce_6_yl = 300
    produce_6_yu = 590

    produce_6 = produce[produce_6_xl:produce_6_xu,produce_6_yl:produce_6_yu]
    



    produce_7_xl = 324
    produce_7_xu = 10000
    produce_7_yl = 595
    produce_7_yu = 888

    produce_7 = produce[produce_7_xl:produce_7_xu,produce_7_yl:produce_7_yu]
    


    produce_8_xl = 324
    produce_8_xu = 10000
    produce_8_yl = 890
    produce_8_yu = 10000

    produce_8 = produce[produce_8_xl:produce_8_xu,produce_8_yl:produce_8_yu]
    

    meat_xl = 1871
    meatxu = -40

    meat = image_matrix[meat_xl:meatxu]


    meat_1_xl = 0 
    meat_1_xu = 310
    meat_1_yl = 0
    meat_1_yu = 296


    meat_1 = meat[meat_1_xl:meat_1_xu,meat_1_yl:meat_1_yu]




    meat_2_xl = 0 
    meat_2_xu = 310
    meat_2_yl = 302
    meat_2_yu = 595


    meat_2 = meat[meat_2_xl:meat_2_xu,meat_2_yl:meat_2_yu]




    meat_3_xl = 0 
    meat_3_xu = 310
    meat_3_yl = 600
    meat_3_yu = 888


    meat_3 = meat[meat_3_xl:meat_3_xu,meat_3_yl:meat_3_yu]


    meat_4_xl = 0 
    meat_4_xu = 310
    meat_4_yl = 900
    meat_4_yu = 10000

    meat_4 = meat[meat_4_xl:meat_4_xu,meat_4_yl:meat_4_yu]



    meat_5_xl = 317 
    meat_5_xu = 10000
    meat_5_yl = 0
    meat_5_yu = 296

    meat_5 = meat[meat_5_xl:meat_5_xu,meat_5_yl:meat_5_yu]


    meat_6_xl = 317 
    meat_6_xu = 10000
    meat_6_yl = 302
    meat_6_yu = 595

    meat_6 = meat[meat_6_xl:meat_6_xu,meat_6_yl:meat_6_yu]


    meat_7_xl = 317 
    meat_7_xu = 10000
    meat_7_yl = 600
    meat_7_yu = 888

    meat_7 = meat[meat_7_xl:meat_7_xu,meat_7_yl:meat_7_yu]


    meat_8_xl = 317 
    meat_8_xu = 10000
    meat_8_yl = 900
    meat_8_yu = 10000


    meat_8 = meat[meat_8_xl:meat_8_xu,meat_8_yl:meat_8_yu]


    image2 = Image.open(path2)



    image_matrix2 = np.array(image2)




    grocery_xl = 82
    grocery_xu = 1235

    grocery = image_matrix2[grocery_xl:grocery_xu]


    grocery_1_xl = 0
    grocery_1_xu = 400 
    grocery_1_yl = 0
    grocery_1_yu = 305

    grocery_1 =  grocery[grocery_1_xl:grocery_1_xu,grocery_1_yl:grocery_1_yu]



    grocery_2_xl = 0
    grocery_2_xu = 400 
    grocery_2_yl = 305
    grocery_2_yu = 600

    grocery_2 =  grocery[grocery_2_xl:grocery_2_xu,grocery_2_yl:grocery_2_yu]



    grocery_3_xl = 0
    grocery_3_xu = 400 
    grocery_3_yl = 605
    grocery_3_yu = 910

    grocery_3 =  grocery[grocery_3_xl:grocery_3_xu,grocery_3_yl:grocery_3_yu]



    grocery_4_xl = 0
    grocery_4_xu = 400 
    grocery_4_yl = 905
    grocery_4_yu = 10000

    grocery_4 =  grocery[grocery_4_xl:grocery_4_xu,grocery_4_yl:grocery_4_yu]


    #row 2

    grocery_5_xl = 400
    grocery_5_xu = 780 
    grocery_5_yl = 0
    grocery_5_yu = 305

    grocery_5 =  grocery[grocery_5_xl:grocery_5_xu,grocery_5_yl:grocery_5_yu]


    grocery_6_xl = 400
    grocery_6_xu = 780
    grocery_6_yl = 305
    grocery_6_yu = 600

    grocery_6 =  grocery[grocery_6_xl:grocery_6_xu,grocery_6_yl:grocery_6_yu]



    grocery_7_xl = 400
    grocery_7_xu = 780 
    grocery_7_yl = 605
    grocery_7_yu = 910
    grocery_7 =  grocery[grocery_7_xl:grocery_7_xu,grocery_7_yl:grocery_7_yu]


    grocery_8_xl = 400
    grocery_8_xu = 780 
    grocery_8_yl = 905
    grocery_8_yu = 10000

    grocery_8 =  grocery[grocery_8_xl:grocery_8_xu,grocery_8_yl:grocery_8_yu]

    #row 2

    grocery_9_xl = 780
    grocery_9_xu = 10000 
    grocery_9_yl = 0
    grocery_9_yu = 305

    grocery_9 =  grocery[grocery_9_xl:grocery_9_xu,grocery_9_yl:grocery_9_yu]


    grocery_10_xl = 780
    grocery_10_xu = 10000
    grocery_10_yl = 305
    grocery_10_yu = 600

    grocery_10 =  grocery[grocery_10_xl:grocery_10_xu,grocery_10_yl:grocery_10_yu]




    grocery_11_xl = 780
    grocery_11_xu = 10000 
    grocery_11_yl = 605
    grocery_11_yu = 910

    grocery_11 =  grocery[grocery_11_xl:grocery_11_xu,grocery_11_yl:grocery_11_yu]


    grocery_12_xl = 780
    grocery_12_xu = 10000 
    grocery_12_yl = 905
    grocery_12_yu = 10000

    grocery_12 =  grocery[grocery_12_xl:grocery_12_xu,grocery_12_yl:grocery_12_yu]


    valley_kitchen_xl = 1330
    valley_kitchen_xu = 1590
    valley_kitchen = image_matrix2[valley_kitchen_xl:valley_kitchen_xu]



    valley_kitchen_1_yl = 0
    valley_kitchen_1_yu = 297


    valley_kitchen_1 = valley_kitchen[:,valley_kitchen_1_yl:valley_kitchen_1_yu]


    valley_kitchen_2_yl = 300
    valley_kitchen_2_yu = 590

    valley_kitchen_2 = valley_kitchen[:,valley_kitchen_2_yl:valley_kitchen_2_yu]



    valley_kitchen_3_yl = 593
    valley_kitchen_3_yu = 888

    valley_kitchen_3 = valley_kitchen[:,valley_kitchen_3_yl:valley_kitchen_3_yu]



    valley_kitchen_4_yl = 888
    valley_kitchen_4_yu = 10000

    valley_kitchen_4 = valley_kitchen[:,valley_kitchen_4_yl:valley_kitchen_4_yu]


    bulk_foods_xl = 1678
    bulk_foods_xu = 1960
    bulk_foods = image_matrix2[bulk_foods_xl:bulk_foods_xu]

    
    bulk_foods_1_yl = 0
    bulk_foods_1_yu = 298

    bulk_foods_1 = bulk_foods[:,bulk_foods_1_yl:bulk_foods_1_yu]


    bulk_foods_2_yl = 300
    bulk_foods_2_yu = 593

    bulk_foods_2 = bulk_foods[:,bulk_foods_2_yl:bulk_foods_2_yu]


    bulk_foods_3_yl = 596
    bulk_foods_3_yu = 888
    bulk_foods_3 = bulk_foods[:,bulk_foods_3_yl:bulk_foods_3_yu]


    bulk_foods_4_yl = 894
    bulk_foods_4_yu = 10000
    bulk_foods_4 = bulk_foods[:,bulk_foods_4_yl:bulk_foods_4_yu]

        
    dairy_and_frozen_xl = 2000
    dairy_and_frozen_xu = -40
    dairy_and_frozen_yl = 0 
    dairy_and_frozen_yu = 595

    dairy_and_frozen = image_matrix2[dairy_and_frozen_xl:dairy_and_frozen_xu, dairy_and_frozen_yl:dairy_and_frozen_yu]


    dairy_and_frozen_1_xl = 0
    dairy_and_frozen_1_xu = 250
    dairy_and_frozen_1_yl = 0
    dairy_and_frozen_1_yu = 290

    dairy_and_frozen_1 = dairy_and_frozen[dairy_and_frozen_1_xl:dairy_and_frozen_1_xu,dairy_and_frozen_1_yl:dairy_and_frozen_1_yu]


    dairy_and_frozen_2_xl = 0
    dairy_and_frozen_2_xu = 250
    dairy_and_frozen_2_yl = 300
    dairy_and_frozen_2_yu = -2

    dairy_and_frozen_2 = dairy_and_frozen[dairy_and_frozen_2_xl:dairy_and_frozen_2_xu,dairy_and_frozen_2_yl:dairy_and_frozen_2_yu]


    dairy_and_frozen_3_xl = 250
    dairy_and_frozen_3_xu = -15
    dairy_and_frozen_3_yl = 0
    dairy_and_frozen_3_yu = 290

    dairy_and_frozen_3 = dairy_and_frozen[dairy_and_frozen_3_xl:dairy_and_frozen_3_xu,dairy_and_frozen_3_yl:dairy_and_frozen_3_yu]



    dairy_and_frozen_4_xl = 250
    dairy_and_frozen_4_xu = -15
    dairy_and_frozen_4_yl = 300
    dairy_and_frozen_4_yu = -2

    dairy_and_frozen_4 = dairy_and_frozen[dairy_and_frozen_4_xl:dairy_and_frozen_4_xu,dairy_and_frozen_4_yl:dairy_and_frozen_4_yu]


    deli_and_bakery_xl = 2000
    deli_and_bakery_xu = -40
    deli_and_bakery_yl = 600
    deli_and_bakery_yu = 10000

    deli_and_bakery = image_matrix2[deli_and_bakery_xl:deli_and_bakery_xu, deli_and_bakery_yl:deli_and_bakery_yu]

    deli_and_bakery_1_xl = 0 
    deli_and_bakery_1_xu = 265
    deli_and_bakery_1_yl = 0
    deli_and_bakery_1_yu = 285

    deli_and_bakery_1 = deli_and_bakery[deli_and_bakery_1_xl:deli_and_bakery_1_xu, deli_and_bakery_1_yl:deli_and_bakery_1_yu]



    deli_and_bakery_2_xl = 0 
    deli_and_bakery_2_xu = 265
    deli_and_bakery_2_yl = 290
    deli_and_bakery_2_yu = 10000

    deli_and_bakery_2 = deli_and_bakery[deli_and_bakery_2_xl:deli_and_bakery_2_xu, deli_and_bakery_2_yl:deli_and_bakery_2_yu]



    deli_and_bakery_3_xl = 270 
    deli_and_bakery_3_xu = -10
    deli_and_bakery_3_yl = 0
    deli_and_bakery_3_yu = 285

    deli_and_bakery_3 = deli_and_bakery[deli_and_bakery_3_xl:deli_and_bakery_3_xu, deli_and_bakery_3_yl:deli_and_bakery_3_yu]



    deli_and_bakery_4_xl = 270  
    deli_and_bakery_4_xu = -10
    deli_and_bakery_4_yl = 290
    deli_and_bakery_4_yu = 10000

    deli_and_bakery_4 = deli_and_bakery[deli_and_bakery_4_xl:deli_and_bakery_4_xu, deli_and_bakery_4_yl:deli_and_bakery_4_yu]


    def save_image_from_matrix(matrix, filename, folder_path):
        image = Image.fromarray(matrix)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        image.save(os.path.join(folder_path, filename))

    hot_deals_list = [
    ("hot_deals_1", hot_deals_1),
    ("hot_deals_2", hot_deals_2),
    ("hot_deals_3", hot_deals_3),
    ("hot_deals_4", hot_deals_4),
    ("hot_deals_5", hot_deals_5),
    ("hot_deals_6", hot_deals_6)
]
    produce_list = [
    ("produce_1", produce_1),
    ("produce_2", produce_2),
    ("produce_3", produce_3),
    ("produce_4", produce_4),
    ("produce_5", produce_5),
    ("produce_6", produce_6),
    ("produce_7", produce_7),
    ("produce_8",produce_8)
]
    meat_list = [
    ("meat_1", meat_1),
    ("meat_2", meat_2),
    ("meat_3", meat_3),
    ("meat_4", meat_4),
    ("meat_5", meat_5),
    ("meat_6", meat_6),
    ("meat_7", meat_7),
    ("meat_8",meat_8)
]
    grocery_list = [
    ("grocery_1", grocery_1),
    ("grocery_2", grocery_2),
    ("grocery_3", grocery_3),
    ("grocery_4", grocery_4),
    ("grocery_5", grocery_5),
    ("grocery_6", grocery_6),
    ("grocery_7", grocery_7),
    ("grocery_8",grocery_8),
    ("grocery_9",grocery_9),
    ("grocery_10",grocery_10),
    ("grocery_11",grocery_11),
    ("grocery_12",grocery_12)
]
    valley_kitchen_list = [
    ("valley_kitchen_1", valley_kitchen_1),
    ("valley_kitchen_2", valley_kitchen_2),
    ("valley_kitchen_3", valley_kitchen_3),
    ("valley_kitchen_4", valley_kitchen_4)
]
    bulk_foods_list = [
    ("bulk_foods_1", bulk_foods_1),
    ("bulk_foods_2", bulk_foods_2),
    ("bulk_foods_3", bulk_foods_3),
    ("bulk_foods_4", bulk_foods_4)
]
    dairy_and_frozen_list = [
    ("dairy_and_frozen_1", dairy_and_frozen_1),
    ("dairy_and_frozen_2", dairy_and_frozen_2),
    ("dairy_and_frozen_3", dairy_and_frozen_3),
    ("dairy_and_frozens_4", dairy_and_frozen_4)
]
    deli_and_bakery_list = [
    ("deli_and_bakery_1", deli_and_bakery_1),
    ("deli_and_bakery_2", deli_and_bakery_2),
    ("deli_and_bakery_3", deli_and_bakery_3),
    ("deli_and_bakery_4", deli_and_bakery_4)
]

    folder_path = 'valley_food_pics'

    lists = [
        (hot_deals_list, 'hot_deals'),
        (produce_list, 'produce_items'),
        (meat_list, 'meat_items'),
        (grocery_list, 'grocery_items'),
        (valley_kitchen_list, 'valley_kitchen_items'),
        (bulk_foods_list, 'bulk_foods_items'),
        (dairy_and_frozen_list, 'dairy_and_frozen_items'),
        (deli_and_bakery_list, 'deli_and_bakery_items')
    ]

    items_dict = {}
    lengths_dict = {}

    for lst, name in lists:
        items_dict[name] = [lst[i][1] for i in range(len(lst))]
        lengths_dict[name] = len(items_dict[name])

    all_items = []
    for name in lengths_dict:
        all_items.extend(items_dict[name])
    len_all_items = len(all_items)

    index = 0
    for name, length in lengths_dict.items():
        for i in range(length):
            filename = f'{name}_{i}.png'
            save_image_from_matrix(all_items[index], filename, folder_path)
            index += 1

norm_image(ad1_path, ad2_path)
