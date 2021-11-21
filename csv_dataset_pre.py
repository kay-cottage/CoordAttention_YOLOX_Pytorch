# 以HAM10000皮肤癌数据集为例
#Sort images to subfolders first 
import pandas as pd
import os
import shutil

# Dump all images into a folder and specify the path:
data_dir = os.getcwd() + "/all_images/"

# Path to destination directory where we want subfolders
dest_dir = os.getcwd() + "/reorganized/"

# Read the csv file containing image names and corresponding labels
skin_df2 = pd.read_csv('HAM10000_metadata.csv')
print(skin_df2['dx'].value_counts())

label=skin_df2['dx'].unique().tolist()  #Extract labels into a list
label_images = []


# Copy images to new folders
for i in label:
    os.mkdir(dest_dir + str(i) + "/")
    sample = skin_df2[skin_df2['dx'] == i]['image_id']
    label_images.extend(sample)
    for id in label_images:
        shutil.copyfile((data_dir + "/"+ id +".jpg"), (dest_dir + i + "/"+id+".jpg"))
    label_images=[]    
