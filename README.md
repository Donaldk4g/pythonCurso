#steps

este proyecto busca el nombre grafica la poblacion de un pais 

para crear espacios virtuales se realiza de la siguiente forma:

https://pypi.org/ ## en esta pagina encuentras todas la librerias que quieres utilizar en python

se instala desde la terminal de comando o utilizando git
pip install matplotlib ##  se ingresa de esta manera este es un ejemplo para instalacion de la libreria matplotlib

el archivo gitrinore se utiliza para no subir cosas inesesarias a github 

## creacion ambiente virtial##
verificar la version de pip utilizmos en comando 

pip -V
pip freeze  --me dice las librerias que estan instaladas  tanto a nivel local como en un entorno virtual

entramos a git nos dirigimos a la carpeta donde vamos a trabajar en nuestro proyecto para mirar la ruta donde estamos ubicados utilizamos el comando pdw

primero verificamos donde se esta ejecutando python con el comando  which python

primero verificamos donde se esta ejecutando pip con el comando  which pip

sudo apt install -y python-venv  -- comando para la creacion  de paquetes virtuales

entro a la carpeta donde voy a instalar el ambiente creo el ambiente con el comando 
python3 -m venv env

para activar el ambiente
source env/bin/activate

dessactivar el ambiente
deactivate

ya podemos instalar las librerias que necesitemos

 pip3 freeze > requirements.txt  crea un archivo para mirar las librerias que se van a instalar

 pip3 install -r requirements.txt

-------------------------------------------
la libreia de pandas sirve para trabajar con csv en el codigo esta el ejemplo facilita mucho el trabajo

