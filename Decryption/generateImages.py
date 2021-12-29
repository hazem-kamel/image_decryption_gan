
# example of using saved cyclegan models for image translation
from numpy import load
from numpy import expand_dims
from keras.models import load_model
from keras_contrib.layers.normalization.instancenormalization import InstanceNormalization
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from matplotlib import pyplot
import os
import sys
def load_images(path, size=(112,112)):
                        # load and resize the image
                        pixels = load_img(path, target_size=size)
                        # convert to numpy array
                        pixels = img_to_array(pixels)
                        # transform in a sample
                        pixels = expand_dims(pixels, 0)
                        # scale from [0,255] to [-1,1]
                        pixels = (pixels - 127.5) / 127.5
                        return pixels
# load the image
cust = {'InstanceNormalization': InstanceNormalization}
model_AtoB = load_model('g_model_BtoA_015000.h5', cust)
print(sys.path[0])
os.chdir(sys.path[0] + '/testImages/')
rootdir = os.getcwd()
print(rootdir)
for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print(file)
            image_src = load_images(file)
            # translate image
            image_tar = model_AtoB.predict(image_src)
            # scale from [-1,1] to [0,1]
            image_tar = (image_tar + 1) / 2.0
            # plot the translated image
            pyplot.imshow(image_tar[0])
            pyplot.axis('off')
            pyplot.savefig(rootdir+'/Images_CycleGan/'+file)
