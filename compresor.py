from PIL import Image,UnidentifiedImageError
import os

path_comprimir = "C:/Users/ameri/Downloads/"

def comprime(path_folder, file_name):
    picture = Image.open(path_folder + file_name)
    picture.save(path_folder+'compressed_'+file_name,optimize=True,quality=60)
    os.remove(path_folder+file_name)


for archivo in os.listdir(path_comprimir):     # Lleva la lista de carpetas en descargas
    name, ext = os.path.splitext(path_comprimir + archivo)     
    
    if ext == '':
        
        
        ubicacion_carpeta = f'{name}/'
        impre = f'\n{ubicacion_carpeta}:\t{len(os.listdir(ubicacion_carpeta))} fotos\n'
        i = 1
        for filename in os.listdir(ubicacion_carpeta):  # Llleva la lista de archivos en cada carpeta
            if filename.find('compressed') == -1:
                impre += f'Foto: {i}\t'
                print(impre)
                imagen, extension = os.path.splitext(ubicacion_carpeta + filename)
                
                if extension in ['.jpg','.jpeg','.png']:

                    try:
                        comprime(ubicacion_carpeta,filename)
                        i+=1
                    except UnidentifiedImageError:
                        print('Error')

                os.system('cls')
            else:   print(f'{name}: compressed')

if input('\nPresione enter para terminar...') == '':
    os.system('cls')