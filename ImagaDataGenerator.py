import tensorflow as tf
from is_wire.core import Logger
import cv2
import json
from google.protobuf.json_format import ParseDict
from utils import load_options
import argparse
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array


log = Logger(name='WatchVideos')
with open('keymap.json', 'r') as f:
    keymap = json.load(f)
options = load_options(print_options=False)


datagen=tf.keras.preprocessing.image.ImageDataGenerator(
    featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    zca_epsilon=1e-06,
    rotation_range=30,
    width_shift_range=0.0,
    height_shift_range=0.0,
    brightness_range=None,
    shear_range=0.0,
    zoom_range=0.0,
    channel_shift_range=0.0,
    fill_mode="nearest",
    cval=0.0,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=None,
    preprocessing_function=None,
    data_format=None,
    validation_split=0.0,
    dtype=None,
)
#'TIME_UP_GO_GRAYSCALE','CAMINHADA_EM_CIRCULO_GRAYSCALE',
categorias=['IDA_E_VOLTA__DUAS_VEZES_GRAYSCALE','ELEVACAO_EXCESSIVA_DO_CALCANHAR_GRASCALE','CIRCUNDACAO_DO_PE_GRAYSCALE','ASSIMETRIA_DO_COMPRIMENTO_DE_PASSO_GRAYSCALE']

for categoria in categorias:
    for t in range(0,94):
        image = load_img(options.folder+'/videos_4_ciclos/IMAGENS_SOMADAS_4_CICLOS/6_TIPOS_DE_MOVIMENTOS_GRAYSCALE/{}/'.format(categoria)+'{:05d}.png'.format(t))
        pic_array = img_to_array(image)
        pic_array = pic_array.reshape((1,) + pic_array.shape)
        count = 0
        for batch in datagen.flow(pic_array, batch_size=5,save_to_dir=options.folder+'/videos_4_ciclos/IMAGENS_SOMADAS_4_CICLOS/6_TIPOS_DE_MOVIMENTOS_GRAYSCALE/6_TIPOS_DE_MOVIMENTOS_GRAYSCALE_IMAGENS_GERADAS/{}/'.format(categoria), save_prefix='{:05d}'.format(t), save_format='png'):
            count += 1
            if count > 100:
                break
