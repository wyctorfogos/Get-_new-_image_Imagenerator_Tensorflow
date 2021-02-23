import os
import re
import sys
import cv2
import json
import time
import argparse
import numpy as np
import math
import statistics
from moviepy.editor import *
from utils import load_options
from utils import to_labels_array, to_labels_dict
from video_loader import MultipleVideoLoader
from is_wire.core import Logger
from collections import defaultdict, OrderedDict
from utils import get_np_image
#from PIL import ImageGrab
from is_msgs.image_pb2 import ObjectAnnotations
from is_msgs.image_pb2 import HumanKeypoints as HKP
from google.protobuf.json_format import ParseDict
from itertools import permutations


#def verifica_tempo(intervalo_de_tempo, aux_soma_frame,r):
    #print(number_frames,k)
#    aux_soma_frame= aux_soma_frame*255.0
#    cv2.imwrite(options.folder+'videos_4_ciclos/IMAGENS_SOMADAS_4_CICLOS/'+'03_{:02d}.png'.format(r), aux_soma_frame)
#    aux_soma_frame*=0
#    print("aqui")
#    r=r+1
#    return aux_soma_frame,r



def verifica_numero_do_frame(num_frames, k, aux_diferenca_frame):
    b,g,r = cv2.split(aux_diferenca_frame)
    zero_array = np.zeros_like(b)
    b = cv2.merge([b,zero_array,zero_array])
    g = cv2.merge([zero_array,g,zero_array])
    r = cv2.merge([zero_array,zero_array,r])
    resultado= None
    if (k<=int(num_frames/6)):
        resultado = r
    elif (k>int(num_frames/6) and (k<=int(2*num_frames/6))):
        resultado= g
    else:
        resultado=b
    return resultado

log = Logger(name='WatchVideos')
with open('keymap.json', 'r') as f:
    keymap = json.load(f)
options = load_options(print_options=False)

#categorias=['TIME_UP_GO_GRAYSCALE']
#categorias=['CAMINHADA_EM_CIRCULO_GRAYSCALE','IDA_E_VOLTA__DUAS_VEZES_GRAYSCALE']
categorias=['TIME_UP_GO_GRAYSCALE','CAMINHADA_EM_CIRCULO_GRAYSCALE','IDA_E_VOLTA__DUAS_VEZES_GRAYSCALE','ELEVACAO_EXCESSIVA_DO_CALCANHAR_GRASCALE','CIRCUNDACAO_DO_PE_GRAYSCALE','ASSIMETRIA_DO_COMPRIMENTO_DE_PASSO_GRAYSCALE']
for  categoria in categorias:
    t=0
    for l in range(0,13):
        aux_diferenca_frame=[0]
        aux_soma_frame=[0]
        frame_anterior=[0]
        #tempo_inicial=time.time()
        #tempo_final=331
        #intervalo_de_tempo=0
        for i in range(0,4):
            capture = cv2.VideoCapture(options.folder+"/CAPTURA_DE_DADOS_PARTICIPANTES/PARTICIPANTE_{:02d}/{}/p001g01c{:02d}.mp4".format(l,categoria,i))
            num_frames= int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
            #num_frames=num_frames/2
            print(num_frames)
            k=0
            if not capture.isOpened:
                print('Unable to open: ' + args.input)
                exit(0)

            while True:
                ret, frame = capture.read()
                
                #frame=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                if frame is None:
                    break
                if k!=0:
                    frame=(frame/255.0)
                    aux_diferenca_frame=(frame-frame_anterior)
                    #print(aux_diferenca_frame)
                    ##cv2.imshow('Frame', aux_diferenca_frame)
                    #cv.imshow('FG Mask', fgMask)

                    #Separação dos frames pelas cores
                    ##aux_diferenca_frame=verifica_numero_do_frame(num_frames, k, aux_diferenca_frame)
                    
                    ##cv2.imshow('aux_diferenca_frame',aux_diferenca_frame)
                    if (k%2==0):
                        aux_soma_frame=aux_soma_frame+aux_diferenca_frame

                    
                    keyboard = cv2.waitKey(30)
                    #intervalo_de_tempo=time.time()-tempo_inicial
                    
                    #if intervalo_de_tempo>=1.5:
                    #    aux_soma_frame, r=verifica_tempo(intervalo_de_tempo, aux_soma_frame,r)
                    #print(k)
                    if  (((num_frames-1)==k)): #or (k==(0.5*num_frames))):###keyboard == ord('s'):
                        aux_soma_frame= aux_soma_frame*255.0
                        cv2.imwrite(options.folder+'/videos_4_ciclos/IMAGENS_SOMADAS_4_CICLOS/6_TIPOS_DE_MOVIMENTOS_GRAYSCALE/{}/'.format(categoria)+'{:05d}.png'.format(t), aux_soma_frame)
                        aux_soma_frame=0
                        k=0
                        print("aqui")
                        t=t+1
                        continue
                    #print(k,num_frames)
                    if keyboard == 'q' or keyboard == 27:
                        break
                k=k+1
                #Atualiza o frame que será comparado na próxima iteração
                frame_anterior=frame
            cv2.waitKey(1000)
            



#tempo_final=time.time()-tempo_inicial
#print("tempo total:{:02f} s".format(tempo_final))
#number_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

#cv2.imshow('Frame', np.abs(aux_soma_frame))