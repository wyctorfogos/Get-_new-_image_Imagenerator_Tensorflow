import os
import cv2


#Arquivo renomeado.
k=0
#def renameMoveFiles():
 #Local que contém os arquivos a serem alterados.
#filename = '/home/julian/docker/ifes-2019-09-09/Teste_classificador/Avaliacao/Avaliacao_11/p001g01 (copy)/'
filename = '/home/julian/docker/ifes-2019-09-09/Modelos_para_treinamento/IMAGES/Modelo_classificador_imagens/Movimento_errado (copy)/'
movefilename = '/home/julian/docker/ifes-2019-09-09/Modelos_para_treinamento/IMAGES/Modelo_classificador_imagens/Movimento_errado (another copy)/'
 #Lista todos os arquivos do diretório
for oldname in os.listdir(filename):
    #Adiciona RZC_ no nome do arquivo.
    newname = "%i" % k
    #Adiciona o diretório ao arquivo.
    #oldname = os.path.join(filename, oldname)
    #Esta definido outro diretório para observar o arquivo sendo renomeado e movido para outro local
    #newname = os.path.join(movefilename,newname)
    #Renomeia todos arquivos
    os.rename(filename+oldname, movefilename+newname)
    print("Renamed")
    k=k+1
    if cv2.waitKey(57) & 0xFF == ord('q'):
        break

#---MAIN---
#def main():
 #Chama a função acima.
 #renameMoveFiles()
   # if __name__ == "__main__":
        #main()