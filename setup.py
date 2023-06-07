from setuptools import setup


#paquete distribuible en python y como se crea
#con esto hemos configurado y creado un archivo o paquete distribuible

#python setup.py sdist <--- este comando crea el paquete distribuible como paquetecalculos dentro de dist

#la carpeta dist tambien se hizo de manera automatica con el comando de setup en la consola

#teniendo este archivo creado ya esta disponible y listo para ser distribuido

setup(

    name="paquetecalculos",
    version="1.0.0",
    description="Paquete de redondeo y potencias",
    author="Arthas_dk",
    author_email="kevin.andresfontt@gmail.com",
    url="www.kevinfonttlizama.github.io",
    packages=["calculos","calculos.redondeo_potencias"]
    

)

#para instalar el paquete primero debemos navegar por la consola llegar al directorio de donde se encuentra el paquete que vamos a instalar

#en este caso seria la ruta C:\Users\kevin\OneDrive\Escritorio\python\dist 

#entonces ejecutamos el siguiente comando cuando estemos en el directorio correspondiente 

#pip3 install paquetecalculos-1.0.0.tar.gz

#esto instalaria en nuestro sistema el paquete mencionado que acabamos de crear, pero tambien sirve para cualquier otro paquete que nos hayan compartido
# 
# 
# 

