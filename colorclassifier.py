import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import os
from colorir import *
from colorthief import ColorThief
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import extcolors
from colormap import rgb2hex


def resize_image(photo_location):
    input_name = "images/" + photo_location
    output_width = 900                   #set the output size
    img = Image.open(input_name)
    wpercent = (output_width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((output_width,hsize), Image.ANTIALIAS)

    #save
    resize_name = 'resize/resize_' + photo_location  #the resized image name
    img.save(resize_name)                 #output location can be specified before resize_name

    # #read
    # plt.figure(figsize=(9, 9))
    # img_url = resize_name
    # img = plt.imread(img_url)
    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()




def extract_colors(img_url):
    colors_x = extcolors.extract_from_path(img_url, tolerance = 9, limit = 12)
    return colors_x


def createDataframe(input):
    colors_pre_list = str(input).replace('([(', '').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]

    # print(df_rgb)
    # list_rgb = []
    #
    # for item in df_rgb:
    #         print(item)
    #         item = item[1:-1]
    #         my_list = item.split()
    #         new_list = []
    #         for i in range(len(my_list) - 1):
    #             new_list.append(my_list[i][:-1])
    #         for colorValue in new_list:
    #             print(colorValue)
    #             scaled = int(colorValue) / 255
    #             list_rgb.append(scaled)
    #
    #
    # plt.imshow(df_rgb)
    # plt.show()

    # convert RGB to HEX code
    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),
                           int(i.split(", ")[1]),
                           int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]

    df = pd.DataFrame(zip(df_color_up, df_percent), columns=['c_code', 'occurence'])
    return df



#print(df_color)

def plotPie(df_color):
    list_color = list(df_color['c_code'])
    list_precent = [int(i) for i in list(df_color['occurence'])]
    text_c = [c + ' ' + str(round(p*100/sum(list_precent),1)) +'%' for c, p in zip(list_color,
                                                                                   list_precent)]
    fig, ax = plt.subplots(figsize=(180,180),dpi=20)
    wedges, text = ax.pie(list_precent,
                          labels= text_c,
                          labeldistance= 1.05,
                          colors = list_color,
                          textprops={'fontsize': 240, 'color':'black'}
                         )
    #plt.setp(wedges, width=0.3)

    #create space in the center
    #plt.setp(wedges, width=0.36)

    ax.set_aspect("equal")
    fig.set_facecolor('white')
    fig.savefig('temp.png', transparent=True)
    plt.show()

#plot_donut(df_color)


#"39_X2093_Y646_W367_H440.png"

images = ['39_X2093_Y646_W367_H440.png',
          '39_X3293_Y286_W483_H798.png',
          '676_wo_bg_bigO.png', '59_wo_bg_dragonRider.png',
          '39_X1286_Y1457_W846_H580.png', '650_wo_bg_bigC.png',
          '39_X2645_Y893_W568_H378.png', '664_wo_bg_bigI.png', '39_X2062_Y547_W469_H706.png',
          '680_wo_bg_bigS.png', '39_X1665_Y639_W462_H572.png', '39_X3067_Y148_W408_H386.png',
          '39_X0_Y0_W1679_H1749.png', '690_wo_bg_bigU.png']

birds = ['53_wo_bg_redBird.png', '53_wo_bg_blueBird.png', '53_wo_bg_greenBird.png', '53_wo_bg_yellowBird.png']

animals = ['59_wo_bg_rabbit.png', '59_wo_bg_dragon_wolf.png', '59_wo_bg_dragonRider.png', '59_wo_bg_donkeyRider.png', '59_wo_bg_rabbit_2.png']


swirls = ['39_X199_Y434_W1282_H1315.png', '39_X1692_Y1488_W317_H1096.png', '39_X3293_Y286_W483_H798.png', '39_X0_Y90_W351_H461.png', '39_X3293_Y286_W483_H868.png', '39_X3286_Y268_W490_H886.png', '39_X244_Y486_W309_H332.png', '39_X1665_Y639_W462_H572.png', '39_X0_Y0_W1679_H1749.png', '39_X258_Y355_W448_H536.png']

color_dict = {}



def combineFunctions(image_location):
    resize_image(image_location)
    extracted = extract_colors("resize/resize_" + image_location)
    df_color = createDataframe(extracted)
    #plot_donut(df_color)
    color_dict[image_location] = df_color["c_code"]
    return df_color


def categoriseColors(my_df):
    tints_dict = {
        'yellow': 'C6B16E',
        'blue': '#5F73A6',
        'green': '#636E60',
        'red': '#AA5555',
        'grey': '#7F7F7F',
        'pinkish': '#96725F',
        'light grey': '#AAAAAA' }
    tints = Palette('tints', **tints_dict)
    #hex = tints.most_similar('#9c2b2b')
    #name = tints.get_names(tints.most_similar('#9c2b2b'))[0]
    simple_dict = {}
    for x in range(len(my_df)):
        old_hex = my_df["c_code"][x]
        new_hex = tints.most_similar(old_hex)
        simple_dict[new_hex] = simple_dict.get(new_hex, 0) + int(my_df["occurence"][x])
    print(simple_dict)
    new_dict = {"c_code": [], "occurence": []}
    for item in simple_dict:
        new_dict["c_code"].append(item)
        new_dict["occurence"].append(simple_dict[item])
    df_final = pd.DataFrame.from_dict(new_dict)
    return df_final





def getSingleImage(image_location):
    my_df = combineFunctions(image_location)
    print(my_df)
    plotPie(my_df)
    return my_df


def aggregateColors(df_color_total):
    aggregation_functions = {'occurence': 'sum'}
    summed_df = df_color_total.groupby(df_color_total['c_code']).aggregate(aggregation_functions)
    return summed_df


def getAllImages(listFolder):
    df_color_total = pd.DataFrame()
    for image in listFolder:
        df_color_image = combineFunctions(image)
        df_color_total = df_color_total.append(df_color_image, ignore_index = True)
    return df_color_total

df_color_total = getAllImages(animals)

#getSingleImage("53_wo_bg_greenBird.png")


df_categorized = categoriseColors(df_color_total)
print(df_categorized)
plotPie(df_categorized)


#summed_df = aggregateColors(df_color_total)

#plotDonut(df_color_total)


#print(color_dict)

#df_final = pd.DataFrame.from_dict(color_dict)
#df_final.to_csv("color_codes_anjou.csv")
#df_color_total.to_csv("colors_total_birds.csv")



#imported_colors_total = pd.read_csv('colors_total_birds.csv')


#df_test = getSingleImage('53_wo_bg_redBird.png')
#test12 = categoriseColors(df_test)
#print(test12)
#plotDonut(test12)


#print(df_new)

#df_new.to_csv("colors_total_summed_birds.csv")

#imported_colors_total_2 = pd.read_csv('colors_total_summed_birds.csv')

