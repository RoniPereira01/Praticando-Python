import os
import shutil
import pdb

print("Iniciando...")
#saber diretorio principal
pasta_base = os.getcwd()

#criar caminho para as pasta
pasta_png = os.path.join(pasta_base, "Arqpng")
pasta_pdf = os.path.join(pasta_base, "Arqpdf")
pasta_jpg = os.path.join(pasta_base, "Arqjpg")
print("Criando pasta para destino")

#cria pasta de destino 
os.makedirs(pasta_png, exist_ok= True)
os.makedirs(pasta_pdf, exist_ok=True)
os.makedirs(pasta_jpg, exist_ok=True)

#mover tipo de arquivo para cada pasta criada
def organizar_arquivo():
    arquivos = os.listdir(pasta_base)
    for arquivo in arquivos:
        caminho_completo =os.path.join(pasta_base, arquivo)
        if os.path.isfile(caminho_completo):
            if arquivo.lower().endswith(".png"):
                print(f"Movendo {arquivo} para {pasta_png}")
                shutil.move(caminho_completo,pasta_png)
            elif arquivo.lower().endswith(".pdf"):
                print(f"movendo {arquivo} para {pasta_pdf}")
                shutil.move(caminho_completo,pasta_pdf)
            elif arquivo.lower().endswith(".jpg"):
                print(f"movendo {arquivo} para {pasta_jpg}")
                shutil.move(caminho_completo,pasta_jpg)

organizar_arquivo()