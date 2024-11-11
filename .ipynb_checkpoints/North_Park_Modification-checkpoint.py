from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import copy
import os
from datetime import datetime



now = datetime.now()
current_date = now.date()

ad1_path = rf'C:\Users\16196\Food Ads/north_park_ads_/{current_date}_1.jpg'
ad2_path = rf'C:\Users\16196\Food Ads/north_park_ads_/{current_date}_2.jpg'

def gray_image(path, path2):
    image = Image.open(path)

    gray_image1 = image.convert("L")

    image_matrix = np.array(gray_image1)




    hot_deals_xl = 230
    hot_deals_xu = 348
    
    hot_deals = image_matrix[hot_deals_xl:hot_deals_xu]

    hot_deals_1_xl = 0
    hot_deals_1_xu = 10000
    hot_deals_1_yl = 10
    hot_deals_1_yu = 210
    
    hot_deals_1 = hot_deals[hot_deals_1_xl:hot_deals_1_xu, hot_deals_1_yl:hot_deals_1_yu]
    # plt.imshow(hot_deals_1)
    # plt.show()
    
    
    
    hot_deals_2_xl = 0
    hot_deals_2_xu = 10000
    hot_deals_2_yl = 215
    hot_deals_2_yu = 420
    
    hot_deals_2 = hot_deals[hot_deals_2_xl:hot_deals_2_xu, hot_deals_2_yl:hot_deals_2_yu]
    # plt.imshow(hot_deals_2)
    # plt.show()
    
    
    
    hot_deals_3_xl = 0
    hot_deals_3_xu = 10000
    hot_deals_3_yl = 425
    hot_deals_3_yu = 625
    
    hot_deals_3 = hot_deals[hot_deals_3_xl:hot_deals_3_xu, hot_deals_3_yl:hot_deals_3_yu]
    # plt.imshow(hot_deals_3)
    # plt.show()
    
    
    hot_deals_4_xl = 0
    hot_deals_4_xu = 10000
    hot_deals_4_yl = 625
    hot_deals_4_yu = -10
    
    hot_deals_4 = hot_deals[hot_deals_4_xl:hot_deals_4_xu, hot_deals_4_yl:hot_deals_4_yu]
    # plt.imshow(hot_deals_4)
    # plt.show()

    

    grocery_xl = 390
    grocery_xu = 500
    
    grocery = image_matrix[grocery_xl:grocery_xu]


    grocery_1_xl = 0
    grocery_1_xu = 10000 
    grocery_1_yl = 10
    grocery_1_yu = 210
    
    grocery_1 =  grocery[grocery_1_xl:grocery_1_xu,grocery_1_yl:grocery_1_yu]
    
    # plt.imshow(grocery_1)
    # plt.show
    
    
    grocery_2_xl = 0
    grocery_2_xu = 10000 
    grocery_2_yl = 215
    grocery_2_yu = 420
    
    grocery_2 =  grocery[grocery_2_xl:grocery_2_xu,grocery_2_yl:grocery_2_yu]
    
    # plt.imshow(grocery_2)
    # plt.show
    
    
    grocery_3_xl = 0
    grocery_3_xu = 10000 
    grocery_3_yl = 425
    grocery_3_yu = 625
    
    grocery_3 =  grocery[grocery_3_xl:grocery_3_xu,grocery_3_yl:grocery_3_yu]
    
    # plt.imshow(grocery_3)
    # plt.show
    
    
    grocery_4_xl = 0
    grocery_4_xu = 10000 
    grocery_4_yl = 625
    grocery_4_yu = -10
    
    grocery_4 =  grocery[grocery_4_xl:grocery_4_xu,grocery_4_yl:grocery_4_yu]
    
    # plt.imshow(grocery_4)
    # plt.show


    produce_xl = 532
    produce_xu = -20
    
    produce = image_matrix[produce_xl:produce_xu]




    produce_1_xl = 0
    produce_1_xu = 176
    produce_1_yl = 10
    produce_1_yu = 214
    
    produce_1 = produce[produce_1_xl:produce_1_xu,produce_1_yl:produce_1_yu]
    # plt.imshow(produce_1)
    # plt.show()
    
    produce_2_xl = 0
    produce_2_xu = 176
    produce_2_yl = 219
    produce_2_yu = 420
    
    produce_2 = produce[produce_2_xl:produce_2_xu,produce_2_yl:produce_2_yu]
    # plt.imshow(produce_2)
    # plt.show()
    
    
    
    produce_3_xl = 0
    produce_3_xu = 176
    produce_3_yl = 425
    produce_3_yu = 620
    
    produce_3 = produce[produce_3_xl:produce_3_xu,produce_3_yl:produce_3_yu]
    # plt.imshow(produce_3)
    # plt.show()
    
    
    produce_4_xl = 0
    produce_4_xu = 176
    produce_4_yl = 627
    produce_4_yu = -10
    
    produce_4 = produce[produce_4_xl:produce_4_xu,produce_4_yl:produce_4_yu]
    # plt.imshow(produce_4)
    # plt.show()
    
    
    produce_5_xl = 178
    produce_5_xu = 350
    produce_5_yl = 10
    produce_5_yu = 214
    
    produce_5 = produce[produce_5_xl:produce_5_xu,produce_5_yl:produce_5_yu]
    # plt.imshow(produce_5)
    # plt.show()
    
    produce_6_xl = 178
    produce_6_xu = 350
    produce_6_yl = 219
    produce_6_yu = 420
    
    produce_6 = produce[produce_6_xl:produce_6_xu,produce_6_yl:produce_6_yu]
    # plt.imshow(produce_6)
    # plt.show()
    
    
    
    produce_7_xl = 178
    produce_7_xu = 350
    produce_7_yl = 425
    produce_7_yu = 620
    
    produce_7 = produce[produce_7_xl:produce_7_xu,produce_7_yl:produce_7_yu]
    # plt.imshow(produce_7)
    # plt.show()
    
    
    produce_8_xl = 178
    produce_8_xu = 350
    produce_8_yl = 627
    produce_8_yu = -10
    
    produce_8 = produce[produce_8_xl:produce_8_xu,produce_8_yl:produce_8_yu]
    # plt.imshow(produce_8)
    # plt.show()
    
    
    produce_9_xl = 354
    produce_9_xu = 10000
    produce_9_yl = 10
    produce_9_yu = 214
    
    produce_9 = produce[produce_9_xl:produce_9_xu,produce_9_yl:produce_9_yu]
    # plt.imshow(produce_9)
    # plt.show()
    
    produce_10_xl = 354
    produce_10_xu = 10000
    produce_10_yl = 215
    produce_10_yu = 420
    
    produce_10 = produce[produce_10_xl:produce_10_xu,produce_10_yl:produce_10_yu]
    # plt.imshow(produce_10)
    # plt.show()
    
    
    
    produce_11_xl = 354
    produce_11_xu = 10000
    produce_11_yl = 425
    produce_11_yu = 620
    
    produce_11 = produce[produce_11_xl:produce_11_xu,produce_11_yl:produce_11_yu]
    # plt.imshow(produce_11)
    # plt.show()
    
    
    produce_12_xl = 354
    produce_12_xu = 10000
    produce_12_yl = 627
    produce_12_yu = -10
    
    produce_12 = produce[produce_12_xl:produce_12_xu,produce_12_yl:produce_12_yu]
    # plt.imshow(produce_12)
    # plt.show()


    image2 = Image.open(path2)

    gray_image2 = image2.convert("L")
    
    image_matrix2 = np.array(gray_image2)

    grocery_2_xl = 58
    grocery_2_xu = 242
    
    grocery_2 = image_matrix2[grocery_2_xl:grocery_2_xu]

    grocery_2_1_xl = 0
    grocery_2_1_xu = 90 
    grocery_2_1_yl = 10
    grocery_2_1_yu = 213
    
    grocery_2_1 =  grocery_2[grocery_2_1_xl:grocery_2_1_xu,grocery_2_1_yl:grocery_2_1_yu]
    
    # plt.imshow(grocery_2_1)
    # plt.show
    
    
    grocery_2_2_xl = 0
    grocery_2_2_xu = 90 
    grocery_2_2_yl = 215
    grocery_2_2_yu = 420
    
    grocery_2_2 =  grocery_2[grocery_2_2_xl:grocery_2_2_xu,grocery_2_2_yl:grocery_2_2_yu]
    
    # plt.imshow(grocery_2_2)
    # plt.show
    
    
    grocery_2_3_xl = 0
    grocery_2_3_xu = 90 
    grocery_2_3_yl = 425
    grocery_2_3_yu = 625
    
    grocery_2_3 =  grocery_2[grocery_2_3_xl:grocery_2_3_xu,grocery_2_3_yl:grocery_2_3_yu]
    
    # plt.imshow(grocery_2_3)
    # plt.show
    
    
    grocery_2_4_xl = 0
    grocery_2_4_xu = 90 
    grocery_2_4_yl = 625
    grocery_2_4_yu = -10
    
    grocery_2_4 =  grocery_2[grocery_2_4_xl:grocery_2_4_xu,grocery_2_4_yl:grocery_2_4_yu]
    
    # plt.imshow(grocery_2_4)
    # plt.show
    
    
    
    
    grocery_2_5_xl = 95
    grocery_2_5_xu = 10000 
    grocery_2_5_yl = 10
    grocery_2_5_yu = 213
    
    grocery_2_5 =  grocery_2[grocery_2_5_xl:grocery_2_5_xu,grocery_2_5_yl:grocery_2_5_yu]
    
    # plt.imshow(grocery_2_5)
    # plt.show
    
    
    grocery_2_6_xl = 95
    grocery_2_6_xu = 10000 
    grocery_2_6_yl = 215
    grocery_2_6_yu = 420
    
    grocery_2_6 =  grocery_2[grocery_2_6_xl:grocery_2_6_xu,grocery_2_6_yl:grocery_2_6_yu]
    
    # plt.imshow(grocery_2_6)
    # plt.show
    
    
    grocery_2_7_xl = 95
    grocery_2_7_xu = 10000 
    grocery_2_7_yl = 425
    grocery_2_7_yu = 625
    
    grocery_2_7 =  grocery_2[grocery_2_7_xl:grocery_2_7_xu,grocery_2_7_yl:grocery_2_7_yu]
    
    # plt.imshow(grocery_2_7)
    # plt.show
    
    
    grocery_2_8_xl = 95
    grocery_2_8_xu = 10000 
    grocery_2_8_yl = 625
    grocery_2_8_yu = -10
    
    grocery_2_8 =  grocery_2[grocery_2_8_xl:grocery_2_8_xu,grocery_2_8_yl:grocery_2_8_yu]
    
    # plt.imshow(grocery_2_8)
    # plt.show


    meat_xl = 292
    meat_xu = 475
    
    meat = image_matrix2[meat_xl:meat_xu]




    meat_1_xl = 0 
    meat_1_xu = 95
    meat_1_yl = 10
    meat_1_yu = 283
    
    
    meat_1 = meat[meat_1_xl:meat_1_xu,meat_1_yl:meat_1_yu]
    # plt.imshow(meat_1)
    # plt.show()
    
    
    
    meat_2_xl = 0 
    meat_2_xu = 95
    meat_2_yl = 285
    meat_2_yu = 550
    
    
    meat_2 = meat[meat_2_xl:meat_2_xu,meat_2_yl:meat_2_yu]
    # plt.imshow(meat_2)
    # plt.show()
    
    
    meat_3_xl = 0 
    meat_3_xu = 95
    meat_3_yl = 558
    meat_3_yu = -10
    
    
    meat_3 = meat[meat_3_xl:meat_3_xu,meat_3_yl:meat_3_yu]
    # plt.imshow(meat_3)
    # plt.show()
    
    
    meat_4_xl = 100
    meat_4_xu = 10000
    meat_4_yl = 10
    meat_4_yu = 283
    
    meat_4 = meat[meat_4_xl:meat_4_xu,meat_4_yl:meat_4_yu]
    # plt.imshow(meat_4)
    # plt.show()
    
    
    
    meat_5_xl = 100 
    meat_5_xu = 10000
    meat_5_yl = 285
    meat_5_yu = 550
    
    meat_5 = meat[meat_5_xl:meat_5_xu,meat_5_yl:meat_5_yu]
    # plt.imshow(meat_5)
    # plt.show()
    
    
    meat_6_xl = 100 
    meat_6_xu = 10000
    meat_6_yl = 558
    meat_6_yu = -10
    
    meat_6 = meat[meat_6_xl:meat_6_xu,meat_6_yl:meat_6_yu]
    # plt.imshow(meat_6)
    # plt.show()


    kitchen_xl = 525
    kitchen_xu = 705
    
    kitchen = image_matrix2[kitchen_xl:kitchen_xu]





    kitchen_1_xl = 0 
    kitchen_1_xu = 95
    kitchen_1_yl = 10
    kitchen_1_yu = 283
    
    
    kitchen_1 = kitchen[kitchen_1_xl:kitchen_1_xu,kitchen_1_yl:kitchen_1_yu]
    # plt.imshow(kitchen_1)
    # plt.show()
    
    
    
    kitchen_2_xl = 0 
    kitchen_2_xu = 95
    kitchen_2_yl = 285
    kitchen_2_yu = 550
    
    
    kitchen_2 = kitchen[kitchen_2_xl:kitchen_2_xu,kitchen_2_yl:kitchen_2_yu]
    # plt.imshow(kitchen_2)
    # plt.show()
    
    
    kitchen_3_xl = 0 
    kitchen_3_xu = 95
    kitchen_3_yl = 558
    kitchen_3_yu = -10
    
    
    kitchen_3 = kitchen[kitchen_3_xl:kitchen_3_xu,kitchen_3_yl:kitchen_3_yu]
    # plt.imshow(kitchen_3)
    # plt.show()
    
    
    kitchen_4_xl = 90
    kitchen_4_xu = 10000
    kitchen_4_yl = 10
    kitchen_4_yu = 283
    
    kitchen_4 = kitchen[kitchen_4_xl:kitchen_4_xu,kitchen_4_yl:kitchen_4_yu]
    # plt.imshow(kitchen_4)
    # plt.show()
    
    
    
    kitchen_5_xl = 90 
    kitchen_5_xu = 10000
    kitchen_5_yl = 285
    kitchen_5_yu = 550
    
    kitchen_5 = kitchen[kitchen_5_xl:kitchen_5_xu,kitchen_5_yl:kitchen_5_yu]
    # plt.imshow(kitchen_5)
    # plt.show()
    
    
    kitchen_6_xl = 90 
    kitchen_6_xu = 10000
    kitchen_6_yl = 558
    kitchen_6_yu = -10
    
    kitchen_6 = kitchen[kitchen_6_xl:kitchen_6_xu,kitchen_6_yl:kitchen_6_yu]
    # plt.imshow(kitchen_6)
    # plt.show()


    deli_xl = 760
    deli_xu = -145
    
    deli = image_matrix2[deli_xl:deli_xu]



    deli_1_xl = 0
    deli_1_xu = 90 
    deli_1_yl = 10
    deli_1_yu = 213
    
    deli_1 =  deli[deli_1_xl:deli_1_xu,deli_1_yl:deli_1_yu]
    
    # plt.imshow(deli_1)
    # plt.show
    
    
    deli_2_xl = 0
    deli_2_xu = 90 
    deli_2_yl = 215
    deli_2_yu = 420
    
    deli_2 =  deli[deli_2_xl:deli_2_xu,deli_2_yl:deli_2_yu]
    
    # plt.imshow(deli_2)
    # plt.show
    
    
    deli_3_xl = 0
    deli_3_xu = 90 
    deli_3_yl = 425
    deli_3_yu = 625
    
    deli_3 =  deli[deli_3_xl:deli_3_xu,deli_3_yl:deli_3_yu]
    
    # plt.imshow(deli_3)
    # plt.show
    
    
    deli_4_xl = 0
    deli_4_xu = 90 
    deli_4_yl = 625
    deli_4_yu = -10
    
    deli_4 =  deli[deli_4_xl:deli_4_xu,deli_4_yl:deli_4_yu]
    
    # plt.imshow(deli_4)
    # plt.show
    
    
    
    
    deli_5_xl = 95
    deli_5_xu = 10000 
    deli_5_yl = 10
    deli_5_yu = 213
    
    deli_5 =  deli[deli_5_xl:deli_5_xu,deli_5_yl:deli_5_yu]
    
    # plt.imshow(deli_5)
    # plt.show
    
    
    deli_6_xl = 95
    deli_6_xu = 10000 
    deli_6_yl = 215
    deli_6_yu = 420
    
    deli_6 =  deli[deli_6_xl:deli_6_xu,deli_6_yl:deli_6_yu]
    
    # plt.imshow(deli_6)
    # plt.show
    
    
    deli_7_xl = 95
    deli_7_xu = 10000 
    deli_7_yl = 425
    deli_7_yu = 625
    
    deli_7 =  deli[deli_7_xl:deli_7_xu,deli_7_yl:deli_7_yu]
    
    # plt.imshow(deli_7)
    # plt.show
    
    
    deli_8_xl = 95
    deli_8_xu = 10000 
    deli_8_yl = 625
    deli_8_yu = -10
    
    deli_8 =  deli[deli_8_xl:deli_8_xu,deli_8_yl:deli_8_yu]
    
    # plt.imshow(deli_8)
    # plt.show


    def save_image_from_matrix(matrix, filename, folder_path):
            image = Image.fromarray(matrix)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            image.save(os.path.join(folder_path, filename))

    hot_deals_list = [
        ("hot_deals_1", hot_deals_1),
        ("hot_deals_2", hot_deals_2),
        ("hot_deals_3", hot_deals_3),
        ("hot_deals_4", hot_deals_4)
    ]

    grocery_list = [
        ("grocery_1", grocery_1),
        ("grocery_2", grocery_2),
        ("grocery_3", grocery_3),
        ("grocery_4", grocery_4),
    ]
    produce_list = [
        ("produce_1", produce_1),
        ("produce_2", produce_2),
        ("produce_3", produce_3),
        ("produce_4", produce_4),
        ("produce_5", produce_5),
        ("produce_6", produce_6),
        ("produce_7", produce_7),
        ("produce_8",produce_8), 
        ("produce_9", produce_9),
        ("produce_10", produce_10),
        ("produce_11", produce_11),
        ("produce_12",produce_12)
    ]
    
    grocery_2_list = [
        ("grocery_2_1", grocery_2_1),
        ("grocery_2_2", grocery_2_2),
        ("grocery_2_3", grocery_2_3),
        ("grocery_2_4", grocery_2_4),
        ("grocery_2_5", grocery_2_5),
        ("grocery_2_6", grocery_2_6),
        ("grocery_2_7", grocery_2_7),
        ("grocery_2_8", grocery_2_8)
    ]
    meat_list = [
        ("meat_1", meat_1),
        ("meat_2", meat_2),
        ("meat_3", meat_3),
        ("meat_4", meat_4),
        ("meat_5", meat_5),
        ("meat_6", meat_6)
    ]
        
    kitchen_list = [
        ("kitchen_1", kitchen_1),
        ("kitchen_2", kitchen_2),
        ("kitchen_3", kitchen_3),
        ("kitchen_4", kitchen_4),
        ("kitchen_5", kitchen_5),
        ("kitchen_6", kitchen_6)
    ]
    deli_list = [
        ("deli_1", deli_1),
        ("delis_2", deli_2),
        ("deli_3", deli_3),
        ("deli_4", deli_4),
        ("deli_5", deli_5),
        ("deli_6", deli_6),
        ("deli_7", deli_7),
        ("deli_8", deli_8)
    ]


    folder_path = 'gray_north_park_pics'


    lists = [
        (hot_deals_list, 'hot_deals'),
        (grocery_list, 'grocery_items'),
        (produce_list, 'produce_list_items'),
        (grocery_2_list, 'grocery_2_items'),
        (meat_list, 'meat_items'),
        (kitchen_list, 'kitchen_items'),
        (deli_list, 'deli_items'),
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
            filename = f'gray_{name}_{i}.png'
            save_image_from_matrix(all_items[index], filename, folder_path)
            index += 1

gray_image(ad1_path, ad2_path)

def norm_image(path, path2):
    image = Image.open(path)


    image_matrix = np.array(image)
    hot_deals_xl = 230
    hot_deals_xu = 348
    
    hot_deals = image_matrix[hot_deals_xl:hot_deals_xu]

    hot_deals_1_xl = 0
    hot_deals_1_xu = 10000
    hot_deals_1_yl = 10
    hot_deals_1_yu = 210
    
    hot_deals_1 = hot_deals[hot_deals_1_xl:hot_deals_1_xu, hot_deals_1_yl:hot_deals_1_yu]
    # plt.imshow(hot_deals_1)
    # plt.show()
    
    
    
    hot_deals_2_xl = 0
    hot_deals_2_xu = 10000
    hot_deals_2_yl = 215
    hot_deals_2_yu = 420
    
    hot_deals_2 = hot_deals[hot_deals_2_xl:hot_deals_2_xu, hot_deals_2_yl:hot_deals_2_yu]
    # plt.imshow(hot_deals_2)
    # plt.show()
    
    
    
    hot_deals_3_xl = 0
    hot_deals_3_xu = 10000
    hot_deals_3_yl = 425
    hot_deals_3_yu = 625
    
    hot_deals_3 = hot_deals[hot_deals_3_xl:hot_deals_3_xu, hot_deals_3_yl:hot_deals_3_yu]
    # plt.imshow(hot_deals_3)
    # plt.show()
    
    
    hot_deals_4_xl = 0
    hot_deals_4_xu = 10000
    hot_deals_4_yl = 625
    hot_deals_4_yu = -10
    
    hot_deals_4 = hot_deals[hot_deals_4_xl:hot_deals_4_xu, hot_deals_4_yl:hot_deals_4_yu]
    # plt.imshow(hot_deals_4)
    # plt.show()

    

    grocery_xl = 390
    grocery_xu = 500
    
    grocery = image_matrix[grocery_xl:grocery_xu]


    grocery_1_xl = 0
    grocery_1_xu = 10000 
    grocery_1_yl = 10
    grocery_1_yu = 210
    
    grocery_1 =  grocery[grocery_1_xl:grocery_1_xu,grocery_1_yl:grocery_1_yu]
    
    # plt.imshow(grocery_1)
    # plt.show
    
    
    grocery_2_xl = 0
    grocery_2_xu = 10000 
    grocery_2_yl = 215
    grocery_2_yu = 420
    
    grocery_2 =  grocery[grocery_2_xl:grocery_2_xu,grocery_2_yl:grocery_2_yu]
    
    # plt.imshow(grocery_2)
    # plt.show
    
    
    grocery_3_xl = 0
    grocery_3_xu = 10000 
    grocery_3_yl = 425
    grocery_3_yu = 625
    
    grocery_3 =  grocery[grocery_3_xl:grocery_3_xu,grocery_3_yl:grocery_3_yu]
    
    # plt.imshow(grocery_3)
    # plt.show
    
    
    grocery_4_xl = 0
    grocery_4_xu = 10000 
    grocery_4_yl = 625
    grocery_4_yu = -10
    
    grocery_4 =  grocery[grocery_4_xl:grocery_4_xu,grocery_4_yl:grocery_4_yu]
    
    # plt.imshow(grocery_4)
    # plt.show


    produce_xl = 532
    produce_xu = -20
    
    produce = image_matrix[produce_xl:produce_xu]




    produce_1_xl = 0
    produce_1_xu = 176
    produce_1_yl = 10
    produce_1_yu = 214
    
    produce_1 = produce[produce_1_xl:produce_1_xu,produce_1_yl:produce_1_yu]
    # plt.imshow(produce_1)
    # plt.show()
    
    produce_2_xl = 0
    produce_2_xu = 176
    produce_2_yl = 219
    produce_2_yu = 420
    
    produce_2 = produce[produce_2_xl:produce_2_xu,produce_2_yl:produce_2_yu]
    # plt.imshow(produce_2)
    # plt.show()
    
    
    
    produce_3_xl = 0
    produce_3_xu = 176
    produce_3_yl = 425
    produce_3_yu = 620
    
    produce_3 = produce[produce_3_xl:produce_3_xu,produce_3_yl:produce_3_yu]
    # plt.imshow(produce_3)
    # plt.show()
    
    
    produce_4_xl = 0
    produce_4_xu = 176
    produce_4_yl = 627
    produce_4_yu = -10
    
    produce_4 = produce[produce_4_xl:produce_4_xu,produce_4_yl:produce_4_yu]
    # plt.imshow(produce_4)
    # plt.show()
    
    
    produce_5_xl = 178
    produce_5_xu = 350
    produce_5_yl = 10
    produce_5_yu = 214
    
    produce_5 = produce[produce_5_xl:produce_5_xu,produce_5_yl:produce_5_yu]
    # plt.imshow(produce_5)
    # plt.show()
    
    produce_6_xl = 178
    produce_6_xu = 350
    produce_6_yl = 219
    produce_6_yu = 420
    
    produce_6 = produce[produce_6_xl:produce_6_xu,produce_6_yl:produce_6_yu]
    # plt.imshow(produce_6)
    # plt.show()
    
    
    
    produce_7_xl = 178
    produce_7_xu = 350
    produce_7_yl = 425
    produce_7_yu = 620
    
    produce_7 = produce[produce_7_xl:produce_7_xu,produce_7_yl:produce_7_yu]
    # plt.imshow(produce_7)
    # plt.show()
    
    
    produce_8_xl = 178
    produce_8_xu = 350
    produce_8_yl = 627
    produce_8_yu = -10
    
    produce_8 = produce[produce_8_xl:produce_8_xu,produce_8_yl:produce_8_yu]
    # plt.imshow(produce_8)
    # plt.show()
    
    
    produce_9_xl = 354
    produce_9_xu = 10000
    produce_9_yl = 10
    produce_9_yu = 214
    
    produce_9 = produce[produce_9_xl:produce_9_xu,produce_9_yl:produce_9_yu]
    # plt.imshow(produce_9)
    # plt.show()
    
    produce_10_xl = 354
    produce_10_xu = 10000
    produce_10_yl = 215
    produce_10_yu = 420
    
    produce_10 = produce[produce_10_xl:produce_10_xu,produce_10_yl:produce_10_yu]
    # plt.imshow(produce_10)
    # plt.show()
    
    
    
    produce_11_xl = 354
    produce_11_xu = 10000
    produce_11_yl = 425
    produce_11_yu = 620
    
    produce_11 = produce[produce_11_xl:produce_11_xu,produce_11_yl:produce_11_yu]
    # plt.imshow(produce_11)
    # plt.show()
    
    
    produce_12_xl = 354
    produce_12_xu = 10000
    produce_12_yl = 627
    produce_12_yu = -10
    
    produce_12 = produce[produce_12_xl:produce_12_xu,produce_12_yl:produce_12_yu]
    # plt.imshow(produce_12)
    # plt.show()


    image2 = Image.open(path2)

    
    image_matrix2 = np.array(image2)

    grocery_2_xl = 58
    grocery_2_xu = 242
    
    grocery_2 = image_matrix2[grocery_2_xl:grocery_2_xu]

    grocery_2_1_xl = 0
    grocery_2_1_xu = 90 
    grocery_2_1_yl = 10
    grocery_2_1_yu = 213
    
    grocery_2_1 =  grocery_2[grocery_2_1_xl:grocery_2_1_xu,grocery_2_1_yl:grocery_2_1_yu]
    
    # plt.imshow(grocery_2_1)
    # plt.show
    
    
    grocery_2_2_xl = 0
    grocery_2_2_xu = 90 
    grocery_2_2_yl = 215
    grocery_2_2_yu = 420
    
    grocery_2_2 =  grocery_2[grocery_2_2_xl:grocery_2_2_xu,grocery_2_2_yl:grocery_2_2_yu]
    
    # plt.imshow(grocery_2_2)
    # plt.show
    
    
    grocery_2_3_xl = 0
    grocery_2_3_xu = 90 
    grocery_2_3_yl = 425
    grocery_2_3_yu = 625
    
    grocery_2_3 =  grocery_2[grocery_2_3_xl:grocery_2_3_xu,grocery_2_3_yl:grocery_2_3_yu]
    
    # plt.imshow(grocery_2_3)
    # plt.show
    
    
    grocery_2_4_xl = 0
    grocery_2_4_xu = 90 
    grocery_2_4_yl = 625
    grocery_2_4_yu = -10
    
    grocery_2_4 =  grocery_2[grocery_2_4_xl:grocery_2_4_xu,grocery_2_4_yl:grocery_2_4_yu]
    
    # plt.imshow(grocery_2_4)
    # plt.show
    
    
    
    
    grocery_2_5_xl = 95
    grocery_2_5_xu = 10000 
    grocery_2_5_yl = 10
    grocery_2_5_yu = 213
    
    grocery_2_5 =  grocery_2[grocery_2_5_xl:grocery_2_5_xu,grocery_2_5_yl:grocery_2_5_yu]
    
    # plt.imshow(grocery_2_5)
    # plt.show
    
    
    grocery_2_6_xl = 95
    grocery_2_6_xu = 10000 
    grocery_2_6_yl = 215
    grocery_2_6_yu = 420
    
    grocery_2_6 =  grocery_2[grocery_2_6_xl:grocery_2_6_xu,grocery_2_6_yl:grocery_2_6_yu]
    
    # plt.imshow(grocery_2_6)
    # plt.show
    
    
    grocery_2_7_xl = 95
    grocery_2_7_xu = 10000 
    grocery_2_7_yl = 425
    grocery_2_7_yu = 625
    
    grocery_2_7 =  grocery_2[grocery_2_7_xl:grocery_2_7_xu,grocery_2_7_yl:grocery_2_7_yu]
    
    # plt.imshow(grocery_2_7)
    # plt.show
    
    
    grocery_2_8_xl = 95
    grocery_2_8_xu = 10000 
    grocery_2_8_yl = 625
    grocery_2_8_yu = -10
    
    grocery_2_8 =  grocery_2[grocery_2_8_xl:grocery_2_8_xu,grocery_2_8_yl:grocery_2_8_yu]
    
    # plt.imshow(grocery_2_8)
    # plt.show


    meat_xl = 292
    meat_xu = 475
    
    meat = image_matrix2[meat_xl:meat_xu]




    meat_1_xl = 0 
    meat_1_xu = 95
    meat_1_yl = 10
    meat_1_yu = 283
    
    
    meat_1 = meat[meat_1_xl:meat_1_xu,meat_1_yl:meat_1_yu]
    # plt.imshow(meat_1)
    # plt.show()
    
    
    
    meat_2_xl = 0 
    meat_2_xu = 95
    meat_2_yl = 285
    meat_2_yu = 550
    
    
    meat_2 = meat[meat_2_xl:meat_2_xu,meat_2_yl:meat_2_yu]
    # plt.imshow(meat_2)
    # plt.show()
    
    
    meat_3_xl = 0 
    meat_3_xu = 95
    meat_3_yl = 558
    meat_3_yu = -10
    
    
    meat_3 = meat[meat_3_xl:meat_3_xu,meat_3_yl:meat_3_yu]
    # plt.imshow(meat_3)
    # plt.show()
    
    
    meat_4_xl = 100
    meat_4_xu = 10000
    meat_4_yl = 10
    meat_4_yu = 283
    
    meat_4 = meat[meat_4_xl:meat_4_xu,meat_4_yl:meat_4_yu]
    # plt.imshow(meat_4)
    # plt.show()
    
    
    
    meat_5_xl = 100 
    meat_5_xu = 10000
    meat_5_yl = 285
    meat_5_yu = 550
    
    meat_5 = meat[meat_5_xl:meat_5_xu,meat_5_yl:meat_5_yu]
    # plt.imshow(meat_5)
    # plt.show()
    
    
    meat_6_xl = 100 
    meat_6_xu = 10000
    meat_6_yl = 558
    meat_6_yu = -10
    
    meat_6 = meat[meat_6_xl:meat_6_xu,meat_6_yl:meat_6_yu]
    # plt.imshow(meat_6)
    # plt.show()


    kitchen_xl = 525
    kitchen_xu = 705
    
    kitchen = image_matrix2[kitchen_xl:kitchen_xu]





    kitchen_1_xl = 0 
    kitchen_1_xu = 95
    kitchen_1_yl = 10
    kitchen_1_yu = 283
    
    
    kitchen_1 = kitchen[kitchen_1_xl:kitchen_1_xu,kitchen_1_yl:kitchen_1_yu]
    # plt.imshow(kitchen_1)
    # plt.show()
    
    
    
    kitchen_2_xl = 0 
    kitchen_2_xu = 95
    kitchen_2_yl = 285
    kitchen_2_yu = 550
    
    
    kitchen_2 = kitchen[kitchen_2_xl:kitchen_2_xu,kitchen_2_yl:kitchen_2_yu]
    # plt.imshow(kitchen_2)
    # plt.show()
    
    
    kitchen_3_xl = 0 
    kitchen_3_xu = 95
    kitchen_3_yl = 558
    kitchen_3_yu = -10
    
    
    kitchen_3 = kitchen[kitchen_3_xl:kitchen_3_xu,kitchen_3_yl:kitchen_3_yu]
    # plt.imshow(kitchen_3)
    # plt.show()
    
    
    kitchen_4_xl = 90
    kitchen_4_xu = 10000
    kitchen_4_yl = 10
    kitchen_4_yu = 283
    
    kitchen_4 = kitchen[kitchen_4_xl:kitchen_4_xu,kitchen_4_yl:kitchen_4_yu]
    # plt.imshow(kitchen_4)
    # plt.show()
    
    
    
    kitchen_5_xl = 90 
    kitchen_5_xu = 10000
    kitchen_5_yl = 285
    kitchen_5_yu = 550
    
    kitchen_5 = kitchen[kitchen_5_xl:kitchen_5_xu,kitchen_5_yl:kitchen_5_yu]
    # plt.imshow(kitchen_5)
    # plt.show()
    
    
    kitchen_6_xl = 90 
    kitchen_6_xu = 10000
    kitchen_6_yl = 558
    kitchen_6_yu = -10
    
    kitchen_6 = kitchen[kitchen_6_xl:kitchen_6_xu,kitchen_6_yl:kitchen_6_yu]
    # plt.imshow(kitchen_6)
    # plt.show()


    deli_xl = 760
    deli_xu = -145
    
    deli = image_matrix2[deli_xl:deli_xu]



    deli_1_xl = 0
    deli_1_xu = 90 
    deli_1_yl = 10
    deli_1_yu = 213
    
    deli_1 =  deli[deli_1_xl:deli_1_xu,deli_1_yl:deli_1_yu]
    
    # plt.imshow(deli_1)
    # plt.show
    
    
    deli_2_xl = 0
    deli_2_xu = 90 
    deli_2_yl = 215
    deli_2_yu = 420
    
    deli_2 =  deli[deli_2_xl:deli_2_xu,deli_2_yl:deli_2_yu]
    
    # plt.imshow(deli_2)
    # plt.show
    
    
    deli_3_xl = 0
    deli_3_xu = 90 
    deli_3_yl = 425
    deli_3_yu = 625
    
    deli_3 =  deli[deli_3_xl:deli_3_xu,deli_3_yl:deli_3_yu]
    
    # plt.imshow(deli_3)
    # plt.show
    
    
    deli_4_xl = 0
    deli_4_xu = 90 
    deli_4_yl = 625
    deli_4_yu = -10
    
    deli_4 =  deli[deli_4_xl:deli_4_xu,deli_4_yl:deli_4_yu]
    
    # plt.imshow(deli_4)
    # plt.show
    
    
    
    
    deli_5_xl = 95
    deli_5_xu = 10000 
    deli_5_yl = 10
    deli_5_yu = 213
    
    deli_5 =  deli[deli_5_xl:deli_5_xu,deli_5_yl:deli_5_yu]
    
    # plt.imshow(deli_5)
    # plt.show
    
    
    deli_6_xl = 95
    deli_6_xu = 10000 
    deli_6_yl = 215
    deli_6_yu = 420
    
    deli_6 =  deli[deli_6_xl:deli_6_xu,deli_6_yl:deli_6_yu]
    
    # plt.imshow(deli_6)
    # plt.show
    
    
    deli_7_xl = 95
    deli_7_xu = 10000 
    deli_7_yl = 425
    deli_7_yu = 625
    
    deli_7 =  deli[deli_7_xl:deli_7_xu,deli_7_yl:deli_7_yu]
    
    # plt.imshow(deli_7)
    # plt.show
    
    
    deli_8_xl = 95
    deli_8_xu = 10000 
    deli_8_yl = 625
    deli_8_yu = -10
    
    deli_8 =  deli[deli_8_xl:deli_8_xu,deli_8_yl:deli_8_yu]
    
    # plt.imshow(deli_8)
    # plt.show


    def save_image_from_matrix(matrix, filename, folder_path):
            image = Image.fromarray(matrix)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            image.save(os.path.join(folder_path, filename))

    hot_deals_list = [
        ("hot_deals_1", hot_deals_1),
        ("hot_deals_2", hot_deals_2),
        ("hot_deals_3", hot_deals_3),
        ("hot_deals_4", hot_deals_4)
    ]

    grocery_list = [
        ("grocery_1", grocery_1),
        ("grocery_2", grocery_2),
        ("grocery_3", grocery_3),
        ("grocery_4", grocery_4),
    ]
    produce_list = [
        ("produce_1", produce_1),
        ("produce_2", produce_2),
        ("produce_3", produce_3),
        ("produce_4", produce_4),
        ("produce_5", produce_5),
        ("produce_6", produce_6),
        ("produce_7", produce_7),
        ("produce_8",produce_8), 
        ("produce_9", produce_9),
        ("produce_10", produce_10),
        ("produce_11", produce_11),
        ("produce_12",produce_12)
    ]
    
    grocery_2_list = [
        ("grocery_2_1", grocery_2_1),
        ("grocery_2_2", grocery_2_2),
        ("grocery_2_3", grocery_2_3),
        ("grocery_2_4", grocery_2_4),
        ("grocery_2_5", grocery_2_5),
        ("grocery_2_6", grocery_2_6),
        ("grocery_2_7", grocery_2_7),
        ("grocery_2_8", grocery_2_8)
    ]
    meat_list = [
        ("meat_1", meat_1),
        ("meat_2", meat_2),
        ("meat_3", meat_3),
        ("meat_4", meat_4),
        ("meat_5", meat_5),
        ("meat_6", meat_6)
    ]
        
    kitchen_list = [
        ("kitchen_1", kitchen_1),
        ("kitchen_2", kitchen_2),
        ("kitchen_3", kitchen_3),
        ("kitchen_4", kitchen_4),
        ("kitchen_5", kitchen_5),
        ("kitchen_6", kitchen_6)
    ]
    meat_1_list = [
        ("meat_1_1", meat_1_1),
        ("meat_1_2", meat_1_2),
        ("meat_1_3", meat_1_3),
        ("meat_1_4", meat_1_4)
    ]

    bulk_list = [
        ("bulk_1", bulk_1),
        ("bulk_2", bulk_2)
    ]

    deli_and_bakery_list = [
        ("deli_and_bakery_1", meat_1_1),
        ("meat_1_2", meat_1_2),
        ("meat_1_3", meat_1_3),
        ("meat_1_4", meat_1_4)
    ]

    folder_path = 'north_park_pics'


    lists = [
        (hot_deals_list, 'hot_deals'),
        (grocery_list, 'grocery_items'),
        (produce_list, 'produce_list_items'),
        (grocery_2_list, 'grocery_2_items'),
        (meat_list, 'meat_items'),
        (kitchen_list, 'kitchen_items'),
        (deli_list, 'deli_items'),
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