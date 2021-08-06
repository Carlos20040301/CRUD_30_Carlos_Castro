from tkinter import *
from tkinter import ttk

from mysql.connector import cursor
import demo_database

window = Tk()
frame_app = Frame(window, width=850, height=650, )
window.title('Mostrar Registros')
my_table = ttk.Treeview(window)
frame_app.pack()




# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
n_cuenta = StringVar()
id_usuario = StringVar()
edad = StringVar()
nombre_apellido = StringVar()
contrasena = StringVar()

def crear_registro():
# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
# Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
    n_cuenta = entry_ncuenta.get()
    id_usuario = entry_id.get()
    edad = entry_edad.get()
    nombre_apellido = entry_nombre.get()
    contrasena = entry_contra.get()

    entry_ncuenta.delete(0,END)
    entry_id.delete(0,END)
    entry_edad.delete(0,END)
    entry_nombre.delete(0,END)
    entry_contra.delete(0,END)
    entry_ncuenta.focus()
    

    
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
    demo_db = demo_database.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
    demo_db.insert_db(n_cuenta, id_usuario, edad, nombre_apellido,contrasena)




import mysql.connector
connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_banco")

cursor = connection.cursor()
cursor.execute("SELECT N_CUENTA, ID_USUARIO, EDAD,NOMBRE_APELLIDO, CONTRASENA FROM TBL_USUARIOS")


     
    
    
my_table = ttk.Treeview(window)
    

registro=0
for fila in cursor:
    registro=registro+1
    print(str(fila))
    n_cuenta =fila[0]
    id_usuario = fila[1]  
    edad = fila[2]
    nombre_apellido = fila[3]
    contrasena = fila[4]
    my_table.insert(parent="", index="end", iid=registro, text=str(registro),
        values=(n_cuenta,id_usuario, edad, nombre_apellido,contrasena))
connection.close() 
 


        # Define Our Columns 
my_table['columns'] = ('N_CUENTA', 'ID_USUARIO', 'EDAD','NOMBRE_APELLIDO')

        # Formate Our Columns
my_table.column('#0', width=0, minwidth=0)
my_table.column('N_CUENTA', anchor=W, width=70)
my_table.column('ID_USUARIO', anchor=W, width=80)
my_table.column('EDAD', anchor=W, width=50)
my_table.column('NOMBRE_APELLIDO', anchor=W, width=130)


        # Create Headings
my_table.heading('#0', text='ID_CAMPO', anchor=W)
my_table.heading('N_CUENTA', text='N_CUENTA', anchor=W)
my_table.heading('ID_USUARIO', text='ID_USUARIO', anchor=W)
my_table.heading('EDAD', text='EDAD', anchor=W)
my_table.heading('NOMBRE_APELLIDO', text='NOMBRE_APELLIDO', anchor=W)




        # Pack to the screen
Label(text="Usuarios En Línea",
      font=("Century Gothic", "16","bold"),
      fg="white",
      bg=("#58FF33"),
      width=20).place(x=500,y=300)
my_table.place(x=500, y=350)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=900, height=100,bg="#E8A3FC")
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=900, height=120,bg="#E8A3FC")
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=900, height=500,bg="#E8A3FC")
frame_options.grid(row=2, column=0)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="Insertar Usuario",
              font=("Century Gothic", "16","bold"),
              fg="white",
              bg=("#A200FE"),
              width=83)
              
title.place(x=0, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="TRANSFERCLOUD", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT,
              bg=("#E8A3FC")  )
title1.place(x=350, y=10)
title2 = Label(frame_title, 
              text="Todos los campos son obligartorios.", 
              font=("Century Gothic", "14"),
              justify=LEFT,
              bg=("#E8A3FC")  )
title2.place(x=300, y=50)


# Widgets dentro del contender OPTIONS
frame_form = Frame(frame_options, width=350, height=500, bg="#6472FF")
frame_form.place(x=25, y=-10)
label_nombre = Label(frame_form, 
              text="N° Cuenta:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#6472FF")
label_nombre.place(x=30, y=30)

entry_ncuenta = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_ncuenta.place(x=30, y=70)

label_id = Label(frame_form, 
              text="ID_Usuario:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#6472FF")
label_id.place(x=30, y=110)

entry_id = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_id.place(x=30, y=150)


label_edad = Label(frame_form, 
              text="EDAD:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#6472FF")
label_edad.place(x=30, y=190)
entry_edad = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_edad.place(x=30, y=230)

label_nombre = Label(frame_form, 
              text="Nombre y Apellido:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#6472FF")
label_nombre.place(x=30, y=270)
entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_nombre.place(x=30, y=310)


label_contra = Label(frame_form, 
              text="Contraseña:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#6472FF")
label_contra.place(x=30, y=350)
entry_contra = Entry(frame_form, justify=LEFT, width=25,show="*", 
                font=("Century Gothic", "14"))
entry_contra.place(x=30, y=390)


button_agregar = Button(frame_form, text="Crear Usuario", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_registro)
button_agregar.place(x=110, y=430)

window.mainloop()






