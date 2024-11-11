from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import copy
import os
from datetime import datetime


ad_path = rf'C:\Users\16196\Food Ads\harvest_ads_\HI_ElCajon_Ad.jpg'


def gray_image(path):
    image = Image.open(path)

    gray_image1 = image.convert("L")

    image_matrix = np.array(gray_image1)


    promo_xl = 542
    promo_xu = 860
    promo_yl = 70
    promo_yu = 950
    promo = image_matrix[promo_xl:promo_xu, promo_yl:promo_yu]
    produce_xl = 952
    produce_xu = 2150
    produce_yl = 70
    produce_yu = -70
    
    produce = image_matrix[produce_xl:produce_xu, produce_yl:produce_yu]
    produce_1_xl = 0
    produce_1_xu = 400
    produce_1_yl = 0
    produce_1_yu = 340
    
    produce_1 = produce[produce_1_xl:produce_1_xu, produce_1_yl:produce_1_yu]
    
    
    
    produce_2_xl = 0
    produce_2_xu = 400
    produce_2_yl = 340
    produce_2_yu = 680
    
    produce_2 = produce[produce_2_xl:produce_2_xu, produce_2_yl:produce_2_yu]
    
    
    
    
    
    produce_3_xl = 0
    produce_3_xu = 400
    produce_3_yl = 680
    produce_3_yu = 1020
    
    produce_3 = produce[produce_3_xl:produce_3_xu, produce_3_yl:produce_3_yu]
    
    
    
    produce_4_xl = 0
    produce_4_xu = 400
    produce_4_yl = 1020
    produce_4_yu = 10000
    
    produce_4 = produce[produce_4_xl:produce_4_xu, produce_4_yl:produce_4_yu]
    
    
    
    
    produce_5_xl = 400
    produce_5_xu = 800
    produce_5_yl = 0
    produce_5_yu = 340
    
    produce_5 = produce[produce_5_xl:produce_5_xu, produce_5_yl:produce_5_yu]
    
    produce_6_xl = 400
    produce_6_xu = 800
    produce_6_yl = 340
    produce_6_yu = 680
    
    produce_6 = produce[produce_6_xl:produce_6_xu, produce_6_yl:produce_6_yu]
    
    
    
    produce_7_xl = 400
    produce_7_xu = 800
    produce_7_yl = 680
    produce_7_yu = 1020
    
    produce_7 = produce[produce_7_xl:produce_7_xu, produce_7_yl:produce_7_yu]
    
    
    produce_8_xl = 400
    produce_8_xu = 800
    produce_8_yl = 1020
    produce_8_yu = 10000
    
    produce_8 = produce[produce_8_xl:produce_8_xu, produce_8_yl:produce_8_yu]
    
    
    
    produce_9_xl = 800
    produce_9_xu = 10000
    produce_9_yl = 0
    produce_9_yu = 340
    
    produce_9 = produce[produce_9_xl:produce_9_xu, produce_9_yl:produce_9_yu]
    
    
    produce_10_xl = 800
    produce_10_xu = 10000
    produce_10_yl = 340
    produce_10_yu = 680
    
    produce_10 = produce[produce_10_xl:produce_10_xu, produce_10_yl:produce_10_yu]
    
    
    
    produce_11_xl = 800
    produce_11_xu = 10000
    produce_11_yl = 680
    produce_11_yu = 1020
    
    produce_11 = produce[produce_11_xl:produce_11_xu, produce_11_yl:produce_11_yu]
    
    
    produce_12_xl = 800
    produce_12_xu = 10000
    produce_12_yl = 1020
    produce_12_yu = 10000
    
    produce_12 = produce[produce_12_xl:produce_12_xu, produce_12_yl:produce_12_yu]
    
    kitchen_xl = 2240
    kitchen_xu = 2710
    kitchen_yl = 70
    kitchen_yu = -70
    
    kitchen = image_matrix[kitchen_xl:kitchen_xu, kitchen_yl:kitchen_yu]
    
    kitchen_1_xl = 0 
    kitchen_1_xu = 10000
    kitchen_1_yl = 0
    kitchen_1_yu = 450
    
    
    kitchen_1 = kitchen[kitchen_1_xl:kitchen_1_xu,kitchen_1_yl:kitchen_1_yu]
    
    
    
    
    kitchen_2_xl = 0 
    kitchen_2_xu = 10000
    kitchen_2_yl = 450
    kitchen_2_yu = 895
    
    
    kitchen_2 = kitchen[kitchen_2_xl:kitchen_2_xu,kitchen_2_yl:kitchen_2_yu]
    
    
    kitchen_3_xl = 0 
    kitchen_3_xu = 10000
    kitchen_3_yl = 910
    kitchen_3_yu = 10000
    
    
    kitchen_3 = kitchen[kitchen_3_xl:kitchen_3_xu,kitchen_3_yl:kitchen_3_yu]
    
    meat_1_xl = 2803
    meat_1_xu = 3050
    meat_1_yl = 70
    meat_1_yu = -70
    
    meat_1 = image_matrix[meat_1_xl:meat_1_xu, meat_1_yl:meat_1_yu]
    
    
    meat_1_1_xl = 0
    meat_1_1_xu = 10000
    meat_1_1_yl = 0
    meat_1_1_yu = 336
    
    meat_1_1 = meat_1[meat_1_1_xl:meat_1_1_xu,meat_1_1_yl:meat_1_1_yu]
    
    
    
    meat_1_2_xl = 0
    meat_1_2_xu = 10000
    meat_1_2_yl = 340
    meat_1_2_yu = 675
    
    meat_1_2 = meat_1[meat_1_2_xl:meat_1_2_xu,meat_1_2_yl:meat_1_2_yu]
    
    
    
    meat_1_3_xl = 0
    meat_1_3_xu = 10000
    meat_1_3_yl = 680
    meat_1_3_yu = 1020
    
    meat_1_3 = meat_1[meat_1_3_xl:meat_1_3_xu,meat_1_3_yl:meat_1_3_yu]
    
    meat_1_4_xl = 0
    meat_1_4_xu = 10000
    meat_1_4_yl = 1030
    meat_1_4_yu = 10000
    
    meat_1_4 = meat_1[meat_1_4_xl:meat_1_4_xu,meat_1_4_yl:meat_1_4_yu]
    
    meat_2_xl = 3310
    meat_2_xu = 4173
    meat_2_yl = 70
    meat_2_yu = -70
    
    meat_2 = image_matrix[meat_2_xl:meat_2_xu, meat_2_yl:meat_2_yu]
    
    
    
    meat_2_1_xl = 0
    meat_2_1_xu = 284
    meat_2_1_yl = 0
    meat_2_1_yu = 670
    
    meat_2_1 = meat_2[meat_2_1_xl:meat_2_1_xu,meat_2_1_yl:meat_2_1_yu]
    
    
    
    meat_2_2_xl = 0
    meat_2_2_xu = 284
    meat_2_2_yl = 680
    meat_2_2_yu = 10000
    
    meat_2_2 = meat_2[meat_2_2_xl:meat_2_2_xu,meat_2_2_yl:meat_2_2_yu]
    
    
    
    meat_2_3_xl = 288
    meat_2_3_xu = 570
    meat_2_3_yl = 0
    meat_2_3_yu = 670
    
    meat_2_3 = meat_2[meat_2_3_xl:meat_2_3_xu,meat_2_3_yl:meat_2_3_yu]
    
    
    meat_2_4_xl = 288
    meat_2_4_xu = 570
    meat_2_4_yl = 680
    meat_2_4_yu = 10000
    
    meat_2_4 = meat_2[meat_2_4_xl:meat_2_4_xu,meat_2_4_yl:meat_2_4_yu]
    
    
    
    
    meat_2_5_xl = 579
    meat_2_5_xu = 10000
    meat_2_5_yl = 0
    meat_2_5_yu = 670
    
    meat_2_5 = meat_2[meat_2_5_xl:meat_2_5_xu,meat_2_5_yl:meat_2_5_yu]
    
    
    meat_2_6_xl = 579
    meat_2_6_xu = 10000
    meat_2_6_yl = 680
    meat_2_6_yu = 10000
    
    meat_2_6 = meat_2[meat_2_6_xl:meat_2_6_xu,meat_2_6_yl:meat_2_6_yu]
    
    
    
    bulk_xl = 4258
    bulk_xu = 4520
    bulk_yl = 70
    bulk_yu = -70
    
    bulk = image_matrix[bulk_xl:bulk_xu, bulk_yl:bulk_yu]
    
    
    
    bulk_1_xl = 0
    bulk_1_xu = 10000
    bulk_1_yl = 0
    bulk_1_yu = 680
    
    bulk_1 = bulk[bulk_1_xl:bulk_1_xu, bulk_1_yl:bulk_1_yu]
    
    
    
    bulk_2_xl = 0
    bulk_2_xu = 10000
    bulk_2_yl = 685
    bulk_2_yu = 10000
    
    bulk_2 = bulk[bulk_2_xl:bulk_2_xu, bulk_2_yl:bulk_2_yu]
    
    
    deli_and_dairy_xl = 4620
    deli_and_dairy_xu = 5120
    deli_and_dairy_yl = 70
    deli_and_dairy_yu = -70
    
    deli_and_dairy = image_matrix[deli_and_dairy_xl:deli_and_dairy_xu, deli_and_dairy_yl:deli_and_dairy_yu]
    
    deli_and_dairy_1_xl = 0
    deli_and_dairy_1_xu = 260
    deli_and_dairy_1_yl = 0
    deli_and_dairy_1_yu = 670
    
    deli_and_dairy_1 = deli_and_dairy[deli_and_dairy_1_xl:deli_and_dairy_1_xu,deli_and_dairy_1_yl:deli_and_dairy_1_yu]
    
    
    deli_and_dairy_2_xl = 0
    deli_and_dairy_2_xu = 260
    deli_and_dairy_2_yl = 685
    deli_and_dairy_2_yu = 10000
    
    deli_and_dairy_2 = deli_and_dairy[deli_and_dairy_2_xl:deli_and_dairy_2_xu,deli_and_dairy_2_yl:deli_and_dairy_2_yu]
    
    
    deli_and_dairy_3_xl = 288
    deli_and_dairy_3_xu = 570
    deli_and_dairy_3_yl = 0
    deli_and_dairy_3_yu = 670
    
    deli_and_dairy_3 = deli_and_dairy[deli_and_dairy_3_xl:deli_and_dairy_3_xu,deli_and_dairy_3_yl:deli_and_dairy_3_yu]
    
    
    deli_and_dairy_4_xl = 288
    deli_and_dairy_4_xu = 570
    deli_and_dairy_4_yl = 685
    deli_and_dairy_4_yu = 10000
    
    deli_and_dairy_4 = deli_and_dairy[deli_and_dairy_4_xl:deli_and_dairy_4_xu,deli_and_dairy_4_yl:deli_and_dairy_4_yu]
    
    
    grocery_xl = 5220
    grocery_xu = -275
    grocery_yl = 70
    grocery_yu = -70
    
    grocery = image_matrix[grocery_xl:grocery_xu, grocery_yl:grocery_yu]
    
    grocery_1_xl = 0
    grocery_1_xu = 260
    grocery_1_yl = 0
    grocery_1_yu = 680
    
    grocery_1 = grocery[grocery_1_xl:grocery_1_xu, grocery_1_yl:grocery_1_yu]
    
    
    grocery_2_xl = 0
    grocery_2_xu = 260
    grocery_2_yl = 690
    grocery_2_yu = 10000
    
    grocery_2 = grocery[grocery_2_xl:grocery_2_xu, grocery_2_yl:grocery_2_yu]
    
    
    
    
    
    grocery_3_xl = 265
    grocery_3_xu = 537
    grocery_3_yl = 0
    grocery_3_yu = 680
    
    grocery_3 = grocery[grocery_3_xl:grocery_3_xu, grocery_3_yl:grocery_3_yu]
    
    
    
    grocery_4_xl = 265
    grocery_4_xu = 537
    grocery_4_yl = 690
    grocery_4_yu = 10000
    
    grocery_4 = grocery[grocery_4_xl:grocery_4_xu, grocery_4_yl:grocery_4_yu]
    
    
    
    
    grocery_5_xl = 540
    grocery_5_xu = 10000
    grocery_5_yl = 0
    grocery_5_yu = 340
    
    grocery_5 = grocery[grocery_5_xl:grocery_5_xu, grocery_5_yl:grocery_5_yu]
    
    
    
    grocery_6_xl = 540
    grocery_6_xu = 10000
    grocery_6_yl = 350
    grocery_6_yu = 680
    
    grocery_6 = grocery[grocery_6_xl:grocery_6_xu, grocery_6_yl:grocery_6_yu]
    
    
    
    grocery_7_xl = 540
    grocery_7_xu = 10000
    grocery_7_yl = 685
    grocery_7_yu = 1020
    
    grocery_7 = grocery[grocery_7_xl:grocery_7_xu, grocery_7_yl:grocery_7_yu]
    
    
    grocery_8_xl = 540
    grocery_8_xu = 10000
    grocery_8_yl = 1025
    grocery_8_yu = 10000
    
    grocery_8 = grocery[grocery_8_xl:grocery_8_xu, grocery_8_yl:grocery_8_yu]



    def save_image_from_matrix(matrix, filename, folder_path):
            image = Image.fromarray(matrix)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            image.save(os.path.join(folder_path, filename))

    promo_list = [
        ("promo", promo)
    ]

    produce_list = [
        ("produce_1", produce_1),
        ("produce_2", produce_2),
        ("produce_3", produce_3),
        ("produce_4", produce_4),
        ("produce_5", produce_5),
        ("produce_6", produce_6),
        ("produce_7", produce_7),
        ("produce_8", produce_8),
        ("produce_9", produce_9),
        ("produce_10", produce_10),
        ("produce_11", produce_11),
        ("produce_12", produce_12),
    ]
    kitchen_list = [
        ("kitchen_1", kitchen_1),
        ("kitchen_2", kitchen_2),
        ("kitchen_3", kitchen_3)
    ]
    
    grocery_list = [
        ("grocery_1", grocery_1),
        ("grocery_2", grocery_2),
        ("grocery_3", grocery_3),
        ("grocery_4", grocery_4),
        ("grocery_5", grocery_5),
        ("grocery_6", grocery_6),
        ("grocery_7", grocery_7),
        ("grocery_8", grocery_8)
    ]
    meat_1_list = [
        ("meat_1_1", meat_1_1),
        ("meat_1_2", meat_1_2),
        ("meat_1_3", meat_1_3),
        ("meat_1_4", meat_1_4)
    ]
        
    meat_2_list = [
        ("meat_2_1", meat_2_1),
        ("meat_2_2", meat_2_2),
        ("meat_2_3", meat_2_3),
        ("meat_2_4", meat_2_4),
        ("meat_2_5", meat_2_5),
        ("meat_2_6", meat_2_6)
    ]
    bulk_list = [
        ("bulk_1", bulk_1),
        ("bulk_2", bulk_2)
    ]

    deli_and_dairy_list = [
        ("deli_and_dairy_1", deli_and_dairy_1),
        ("deli_and_dairy_2", deli_and_dairy_2),
        ("deli_and_dairy_3", deli_and_dairy_3),
        ("deli_and_dairy_4", deli_and_dairy_4)
    ]

    folder_path = 'gray_harvest_pics'
    

    lists = [
        (promo_list, 'promo'),
        (produce_list, 'produce_items'),
        (kitchen_list, 'kitchen_items'),
        (grocery_list, 'grocery_items'),
        (meat_1_list, 'meat_1_items'),
        (meat_2_list, 'meat_2_items'),
        (bulk_list, 'bulk_items'),
        (deli_and_dairy_list, 'deli_and_dairy_items'),
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

gray_image(ad_path)


def norm_image(path):
    image = Image.open(path)


    image_matrix = np.array(image)

    promo_xl = 542
    promo_xu = 860
    promo_yl = 70
    promo_yu = 950
    promo = image_matrix[promo_xl:promo_xu, promo_yl:promo_yu]
    produce_xl = 952
    produce_xu = 2150
    produce_yl = 70
    produce_yu = -70
    
    produce = image_matrix[produce_xl:produce_xu, produce_yl:produce_yu]
    produce_1_xl = 0
    produce_1_xu = 400
    produce_1_yl = 0
    produce_1_yu = 340
    
    produce_1 = produce[produce_1_xl:produce_1_xu, produce_1_yl:produce_1_yu]
    
    
    
    produce_2_xl = 0
    produce_2_xu = 400
    produce_2_yl = 340
    produce_2_yu = 680
    
    produce_2 = produce[produce_2_xl:produce_2_xu, produce_2_yl:produce_2_yu]
    
    
    
    
    
    produce_3_xl = 0
    produce_3_xu = 400
    produce_3_yl = 680
    produce_3_yu = 1020
    
    produce_3 = produce[produce_3_xl:produce_3_xu, produce_3_yl:produce_3_yu]
    
    
    
    produce_4_xl = 0
    produce_4_xu = 400
    produce_4_yl = 1020
    produce_4_yu = 10000
    
    produce_4 = produce[produce_4_xl:produce_4_xu, produce_4_yl:produce_4_yu]
    
    
    
    
    produce_5_xl = 400
    produce_5_xu = 800
    produce_5_yl = 0
    produce_5_yu = 340
    
    produce_5 = produce[produce_5_xl:produce_5_xu, produce_5_yl:produce_5_yu]
    
    produce_6_xl = 400
    produce_6_xu = 800
    produce_6_yl = 340
    produce_6_yu = 680
    
    produce_6 = produce[produce_6_xl:produce_6_xu, produce_6_yl:produce_6_yu]
    
    
    
    produce_7_xl = 400
    produce_7_xu = 800
    produce_7_yl = 680
    produce_7_yu = 1020
    
    produce_7 = produce[produce_7_xl:produce_7_xu, produce_7_yl:produce_7_yu]
    
    
    produce_8_xl = 400
    produce_8_xu = 800
    produce_8_yl = 1020
    produce_8_yu = 10000
    
    produce_8 = produce[produce_8_xl:produce_8_xu, produce_8_yl:produce_8_yu]
    
    
    
    produce_9_xl = 800
    produce_9_xu = 10000
    produce_9_yl = 0
    produce_9_yu = 340
    
    produce_9 = produce[produce_9_xl:produce_9_xu, produce_9_yl:produce_9_yu]
    
    
    produce_10_xl = 800
    produce_10_xu = 10000
    produce_10_yl = 340
    produce_10_yu = 680
    
    produce_10 = produce[produce_10_xl:produce_10_xu, produce_10_yl:produce_10_yu]
    
    
    
    produce_11_xl = 800
    produce_11_xu = 10000
    produce_11_yl = 680
    produce_11_yu = 1020
    
    produce_11 = produce[produce_11_xl:produce_11_xu, produce_11_yl:produce_11_yu]
    
    
    produce_12_xl = 800
    produce_12_xu = 10000
    produce_12_yl = 1020
    produce_12_yu = 10000
    
    produce_12 = produce[produce_12_xl:produce_12_xu, produce_12_yl:produce_12_yu]
    
    kitchen_xl = 2240
    kitchen_xu = 2710
    kitchen_yl = 70
    kitchen_yu = -70
    
    kitchen = image_matrix[kitchen_xl:kitchen_xu, kitchen_yl:kitchen_yu]
    
    kitchen_1_xl = 0 
    kitchen_1_xu = 10000
    kitchen_1_yl = 0
    kitchen_1_yu = 450
    
    
    kitchen_1 = kitchen[kitchen_1_xl:kitchen_1_xu,kitchen_1_yl:kitchen_1_yu]
    
    
    
    
    kitchen_2_xl = 0 
    kitchen_2_xu = 10000
    kitchen_2_yl = 450
    kitchen_2_yu = 895
    
    
    kitchen_2 = kitchen[kitchen_2_xl:kitchen_2_xu,kitchen_2_yl:kitchen_2_yu]
    
    
    kitchen_3_xl = 0 
    kitchen_3_xu = 10000
    kitchen_3_yl = 910
    kitchen_3_yu = 10000
    
    
    kitchen_3 = kitchen[kitchen_3_xl:kitchen_3_xu,kitchen_3_yl:kitchen_3_yu]
    
    meat_1_xl = 2803
    meat_1_xu = 3050
    meat_1_yl = 70
    meat_1_yu = -70
    
    meat_1 = image_matrix[meat_1_xl:meat_1_xu, meat_1_yl:meat_1_yu]
    
    
    meat_1_1_xl = 0
    meat_1_1_xu = 10000
    meat_1_1_yl = 0
    meat_1_1_yu = 336
    
    meat_1_1 = meat_1[meat_1_1_xl:meat_1_1_xu,meat_1_1_yl:meat_1_1_yu]
    
    
    
    meat_1_2_xl = 0
    meat_1_2_xu = 10000
    meat_1_2_yl = 340
    meat_1_2_yu = 675
    
    meat_1_2 = meat_1[meat_1_2_xl:meat_1_2_xu,meat_1_2_yl:meat_1_2_yu]
    
    
    
    meat_1_3_xl = 0
    meat_1_3_xu = 10000
    meat_1_3_yl = 680
    meat_1_3_yu = 1020
    
    meat_1_3 = meat_1[meat_1_3_xl:meat_1_3_xu,meat_1_3_yl:meat_1_3_yu]
    
    meat_1_4_xl = 0
    meat_1_4_xu = 10000
    meat_1_4_yl = 1030
    meat_1_4_yu = 10000
    
    meat_1_4 = meat_1[meat_1_4_xl:meat_1_4_xu,meat_1_4_yl:meat_1_4_yu]
    
    meat_2_xl = 3310
    meat_2_xu = 4173
    meat_2_yl = 70
    meat_2_yu = -70
    
    meat_2 = image_matrix[meat_2_xl:meat_2_xu, meat_2_yl:meat_2_yu]
    
    
    
    meat_2_1_xl = 0
    meat_2_1_xu = 284
    meat_2_1_yl = 0
    meat_2_1_yu = 670
    
    meat_2_1 = meat_2[meat_2_1_xl:meat_2_1_xu,meat_2_1_yl:meat_2_1_yu]
    
    
    
    meat_2_2_xl = 0
    meat_2_2_xu = 284
    meat_2_2_yl = 680
    meat_2_2_yu = 10000
    
    meat_2_2 = meat_2[meat_2_2_xl:meat_2_2_xu,meat_2_2_yl:meat_2_2_yu]
    
    
    
    meat_2_3_xl = 288
    meat_2_3_xu = 570
    meat_2_3_yl = 0
    meat_2_3_yu = 670
    
    meat_2_3 = meat_2[meat_2_3_xl:meat_2_3_xu,meat_2_3_yl:meat_2_3_yu]
    
    
    meat_2_4_xl = 288
    meat_2_4_xu = 570
    meat_2_4_yl = 680
    meat_2_4_yu = 10000
    
    meat_2_4 = meat_2[meat_2_4_xl:meat_2_4_xu,meat_2_4_yl:meat_2_4_yu]
    
    
    
    
    meat_2_5_xl = 579
    meat_2_5_xu = 10000
    meat_2_5_yl = 0
    meat_2_5_yu = 670
    
    meat_2_5 = meat_2[meat_2_5_xl:meat_2_5_xu,meat_2_5_yl:meat_2_5_yu]
    
    
    meat_2_6_xl = 579
    meat_2_6_xu = 10000
    meat_2_6_yl = 680
    meat_2_6_yu = 10000
    
    meat_2_6 = meat_2[meat_2_6_xl:meat_2_6_xu,meat_2_6_yl:meat_2_6_yu]
    
    
    
    bulk_xl = 4258
    bulk_xu = 4520
    bulk_yl = 70
    bulk_yu = -70
    
    bulk = image_matrix[bulk_xl:bulk_xu, bulk_yl:bulk_yu]
    
    
    
    bulk_1_xl = 0
    bulk_1_xu = 10000
    bulk_1_yl = 0
    bulk_1_yu = 680
    
    bulk_1 = bulk[bulk_1_xl:bulk_1_xu, bulk_1_yl:bulk_1_yu]
    
    
    
    bulk_2_xl = 0
    bulk_2_xu = 10000
    bulk_2_yl = 685
    bulk_2_yu = 10000
    
    bulk_2 = bulk[bulk_2_xl:bulk_2_xu, bulk_2_yl:bulk_2_yu]
    
    
    deli_and_dairy_xl = 4620
    deli_and_dairy_xu = 5120
    deli_and_dairy_yl = 70
    deli_and_dairy_yu = -70
    
    deli_and_dairy = image_matrix[deli_and_dairy_xl:deli_and_dairy_xu, deli_and_dairy_yl:deli_and_dairy_yu]
    
    deli_and_dairy_1_xl = 0
    deli_and_dairy_1_xu = 260
    deli_and_dairy_1_yl = 0
    deli_and_dairy_1_yu = 670
    
    deli_and_dairy_1 = deli_and_dairy[deli_and_dairy_1_xl:deli_and_dairy_1_xu,deli_and_dairy_1_yl:deli_and_dairy_1_yu]
    
    
    deli_and_dairy_2_xl = 0
    deli_and_dairy_2_xu = 260
    deli_and_dairy_2_yl = 685
    deli_and_dairy_2_yu = 10000
    
    deli_and_dairy_2 = deli_and_dairy[deli_and_dairy_2_xl:deli_and_dairy_2_xu,deli_and_dairy_2_yl:deli_and_dairy_2_yu]
    
    
    deli_and_dairy_3_xl = 288
    deli_and_dairy_3_xu = 570
    deli_and_dairy_3_yl = 0
    deli_and_dairy_3_yu = 670
    
    deli_and_dairy_3 = deli_and_dairy[deli_and_dairy_3_xl:deli_and_dairy_3_xu,deli_and_dairy_3_yl:deli_and_dairy_3_yu]
    
    
    deli_and_dairy_4_xl = 288
    deli_and_dairy_4_xu = 570
    deli_and_dairy_4_yl = 685
    deli_and_dairy_4_yu = 10000
    
    deli_and_dairy_4 = deli_and_dairy[deli_and_dairy_4_xl:deli_and_dairy_4_xu,deli_and_dairy_4_yl:deli_and_dairy_4_yu]
    
    
    grocery_xl = 5220
    grocery_xu = -275
    grocery_yl = 70
    grocery_yu = -70
    
    grocery = image_matrix[grocery_xl:grocery_xu, grocery_yl:grocery_yu]
    
    grocery_1_xl = 0
    grocery_1_xu = 260
    grocery_1_yl = 0
    grocery_1_yu = 680
    
    grocery_1 = grocery[grocery_1_xl:grocery_1_xu, grocery_1_yl:grocery_1_yu]
    
    
    grocery_2_xl = 0
    grocery_2_xu = 260
    grocery_2_yl = 690
    grocery_2_yu = 10000
    
    grocery_2 = grocery[grocery_2_xl:grocery_2_xu, grocery_2_yl:grocery_2_yu]
    
    
    
    
    
    grocery_3_xl = 265
    grocery_3_xu = 537
    grocery_3_yl = 0
    grocery_3_yu = 680
    
    grocery_3 = grocery[grocery_3_xl:grocery_3_xu, grocery_3_yl:grocery_3_yu]
    
    
    
    grocery_4_xl = 265
    grocery_4_xu = 537
    grocery_4_yl = 690
    grocery_4_yu = 10000
    
    grocery_4 = grocery[grocery_4_xl:grocery_4_xu, grocery_4_yl:grocery_4_yu]
    
    
    
    
    grocery_5_xl = 540
    grocery_5_xu = 10000
    grocery_5_yl = 0
    grocery_5_yu = 340
    
    grocery_5 = grocery[grocery_5_xl:grocery_5_xu, grocery_5_yl:grocery_5_yu]
    
    
    
    grocery_6_xl = 540
    grocery_6_xu = 10000
    grocery_6_yl = 350
    grocery_6_yu = 680
    
    grocery_6 = grocery[grocery_6_xl:grocery_6_xu, grocery_6_yl:grocery_6_yu]
    
    
    
    grocery_7_xl = 540
    grocery_7_xu = 10000
    grocery_7_yl = 685
    grocery_7_yu = 1020
    
    grocery_7 = grocery[grocery_7_xl:grocery_7_xu, grocery_7_yl:grocery_7_yu]
    
    
    grocery_8_xl = 540
    grocery_8_xu = 10000
    grocery_8_yl = 1025
    grocery_8_yu = 10000
    
    grocery_8 = grocery[grocery_8_xl:grocery_8_xu, grocery_8_yl:grocery_8_yu]



    def save_image_from_matrix(matrix, filename, folder_path):
            image = Image.fromarray(matrix)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            image.save(os.path.join(folder_path, filename))

    promo_list = [
        ("promo", promo)
    ]

    produce_list = [
        ("produce_1", produce_1),
        ("produce_2", produce_2),
        ("produce_3", produce_3),
        ("produce_4", produce_4),
        ("produce_5", produce_5),
        ("produce_6", produce_6),
        ("produce_7", produce_7),
        ("produce_8", produce_8),
        ("produce_9", produce_9),
        ("produce_10", produce_10),
        ("produce_11", produce_11),
        ("produce_12", produce_12),
    ]
    kitchen_list = [
        ("kitchen_1", kitchen_1),
        ("kitchen_2", kitchen_2),
        ("kitchen_3", kitchen_3)
    ]
    
    grocery_list = [
        ("grocery_1", grocery_1),
        ("grocery_2", grocery_2),
        ("grocery_3", grocery_3),
        ("grocery_4", grocery_4),
        ("grocery_5", grocery_5),
        ("grocery_6", grocery_6),
        ("grocery_7", grocery_7),
        ("grocery_8", grocery_8)
    ]
    meat_1_list = [
        ("meat_1_1", meat_1_1),
        ("meat_1_2", meat_1_2),
        ("meat_1_3", meat_1_3),
        ("meat_1_4", meat_1_4)
    ]
        
    meat_2_list = [
        ("meat_2_1", meat_2_1),
        ("meat_2_2", meat_2_2),
        ("meat_2_3", meat_2_3),
        ("meat_2_4", meat_2_4),
        ("meat_2_5", meat_2_5),
        ("meat_2_6", meat_2_6)
    ]
    bulk_list = [
        ("bulk_1", bulk_1),
        ("bulk_2", bulk_2)
    ]

    deli_and_dairy_list = [
        ("deli_and_dairy_1", deli_and_dairy_1),
        ("deli_and_dairy_2", deli_and_dairy_2),
        ("deli_and_dairy_3", deli_and_dairy_3),
        ("deli_and_dairy_4", deli_and_dairy_4)
    ]

    folder_path = 'harvest_pics'
    

    lists = [
        (promo_list, 'promo'),
        (produce_list, 'produce_items'),
        (kitchen_list, 'kitchen_items'),
        (grocery_list, 'grocery_items'),
        (meat_1_list, 'meat_1_items'),
        (meat_2_list, 'meat_2_items'),
        (bulk_list, 'bulk_items'),
        (deli_and_dairy_list, 'deli_and_dairy_items'),
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
norm_image(ad_path)