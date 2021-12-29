import os
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from numpy import savez_compressed
import sys

def load_base_images(path, size=(112,112)):
    base_images_list=list()
    #  Load the data
    os.chdir(sys.path[1] + path)
    rootdir = os.getcwd()
    print(rootdir)
    for subdir, dirs, files in os.walk(rootdir):
                        os.chdir(subdir)
                        for file in files:
                        # load and resize the image
                            print(file,'normal')
                            pixels = load_img(file, target_size=size)
                            # convert to numpy array
                            pixels = img_to_array(pixels)
                            base_images_list.append(pixels)
                            if(len(base_images_list)==600):
	                            return [asarray(base_images_list)]
def load_encrypted_image(path, size=(112,112)):
    encrypted_images_list=list()
    #  Load the data
    os.chdir(sys.path[1] + path)
    rootdir = os.getcwd()
    print(rootdir)
    for subdir, dirs, files in os.walk(rootdir):
                        os.chdir(subdir)
                        for file in files:
                            print(file,'encrypted')
                            pixels = load_img(file, target_size=size)
                            # convert to numpy array
                            pixels = img_to_array(pixels)
                            encrypted_images_list.append(pixels)
                            if(len(encrypted_images_list)==600):
	                            return [asarray(encrypted_images_list)]

# load dataset
base_images_array=asarray(load_base_images('\Datasets\CASIA-WebFace\images'))
encrypted_images_array = asarray(load_encrypted_image('\Datasets\L_w4o6_CASIA-WebFace\images'))
print('Loaded: ', base_images_array.shape, encrypted_images_array.shape)
# save as compressed numpy array
os.chdir(sys.path[1] + '\Datasets')
rootdir = os.getcwd()
filename = 'maps_112_600_l.npz'
savez_compressed(filename, base_images_array, encrypted_images_array)
print('Saved dataset: ', filename)
