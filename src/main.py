import logging
import sys
from tkinter import*
from myapp import main, settings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info(f'{settings.APP_NAME} {settings.APP_VERSION}')

# run the app
main(sys.argv[1:])
raiz=Tk()
miframe=Frame(raiz,width=500,height=400)
miframe.pack()
my_label=Label(miframe,text='hola mundo',fg='red')
my_label.place(x=100,y=200)
my_label2=Label(miframe,text='texto del label 2',fg='black')
my_label2.place(x=100,y=220)
my_label3=Label(miframe,text='texto del label 3',fg='black')
my_label3.place(x=100,y=250)
#my_label4=Label(miframe,text='texto del label 4',fg='black')
#my_label4.place(x=100,y=270)
raiz.mainloop()