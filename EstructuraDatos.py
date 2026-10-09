# ==========================================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================================

# Importa tkinter para crear la interfaz gráfica.
import tkinter as tk

# Importa messagebox para mostrar mensajes y advertencias.
from tkinter import messagebox

# Importa deque para trabajar con una cola doble.
from collections import deque


# ==========================================================
# CLASE PRINCIPAL DEL PROGRAMA
# ==========================================================

# Define la clase principal de nuestra aplicación.
class DataStructuresApp:

    # Constructor de la clase.
    # Se ejecuta automáticamente cuando se crea la aplicación.
    def __init__(self, root):

        # Guarda la ventana principal dentro de la variable root.
        self.root = root

        # Coloca el título de la ventana.
        self.root.title("Estructuras de Datos")

        # Define el tamaño de la ventana: ancho x alto.
        self.root.geometry("900x650")

        # Evita que el usuario pueda cambiar el tamaño de la ventana.
        self.root.resizable(False, False)

        # ==================================================
        # CREACIÓN DE LAS ESTRUCTURAS DE DATOS
        # ==================================================

        # Crea una lista vacía que utilizaremos como pila.
        self.stack = []

        # Crea una lista vacía que utilizaremos como cola.
        self.queue = []

        # Crea una cola doble utilizando deque.
        self.deque = deque()

        # Crea una lista normal.
        self.list_data = []

        # Crea una lista que representa nuestra lista enlazada.
        self.linked_list = []

        # Muestra el menú principal al iniciar el programa.
        self.show_main_menu()


    # ======================================================
    # FUNCIÓN PARA LIMPIAR LA VENTANA
    # ======================================================

    # Define una función para eliminar los elementos actuales
    # de la ventana.
    def clear_window(self):

        # Recorre todos los elementos que existen en la ventana.
        for widget in self.root.winfo_children():

            # Elimina cada elemento de la ventana.
            widget.destroy()


    # ======================================================
    # MENÚ PRINCIPAL
    # ======================================================

    # Define la función que muestra el menú principal.
    def show_main_menu(self):

        # Limpia la ventana antes de mostrar el menú.
        self.clear_window()

        # Crea el título principal.
        title = tk.Label(
            self.root,
            text="ESTRUCTURAS DE DATOS",
            font=("Arial", 26, "bold")
        )

        # Coloca el título en la ventana.
        title.pack(pady=25)

        # Crea un texto descriptivo debajo del título.
        subtitle = tk.Label(
            self.root,
            text="Seleccione una estructura de datos",
            font=("Arial", 14)
        )

        # Coloca el texto en la ventana.
        subtitle.pack(pady=10)


        # ==================================================
        # BOTÓN DE PILA
        # ==================================================

        # Crea el botón para abrir la pila.
        stack_button = tk.Button(
            self.root,
            text="PILA (STACK)",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            command=self.show_stack
        )

        # Coloca el botón en la ventana.
        stack_button.pack(pady=5)


        # ==================================================
        # BOTÓN DE COLA
        # ==================================================

        # Crea el botón para abrir la cola.
        queue_button = tk.Button(
            self.root,
            text="COLA (QUEUE)",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            command=self.show_queue
        )

        # Coloca el botón en la ventana.
        queue_button.pack(pady=5)


        # ==================================================
        # BOTÓN DE COLA DOBLE
        # ==================================================

        # Crea el botón para abrir la cola doble.
        deque_button = tk.Button(
            self.root,
            text="COLA DOBLE (DEQUE)",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            command=self.show_deque
        )

        # Coloca el botón en la ventana.
        deque_button.pack(pady=5)


        # ==================================================
        # BOTÓN DE LISTA
        # ==================================================

        # Crea el botón para abrir la lista.
        list_button = tk.Button(
            self.root,
            text="LISTA",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            command=self.show_list
        )

        # Coloca el botón en la ventana.
        list_button.pack(pady=5)


        # ==================================================
        # BOTÓN DE LISTA ENLAZADA
        # ==================================================

        # Crea el botón para abrir la lista enlazada.
        linked_button = tk.Button(
            self.root,
            text="LISTA ENLAZADA",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            command=self.show_linked_list
        )

        # Coloca el botón en la ventana.
        linked_button.pack(pady=5)


        # ==================================================
        # BOTÓN SALIR
        # ==================================================

        # Crea el botón para cerrar el programa.
        exit_button = tk.Button(
            self.root,
            text="SALIR",
            font=("Arial", 13),
            width=15,
            command=self.root.destroy
        )

        # Coloca el botón de salida.
        exit_button.pack(pady=15)


    # ======================================================
    # FUNCIÓN PARA CREAR EL LISTVIEW
    # ======================================================

    # Esta función crea el Listbox que utilizaremos
    # para mostrar los resultados.
    def create_list_view(self, parent):

        # Crea un Frame para contener el Listbox.
        frame = tk.Frame(parent)

        # Coloca el Frame en la ventana.
        frame.pack(pady=20)

        # Crea una barra de desplazamiento vertical.
        scrollbar = tk.Scrollbar(frame)

        # Coloca la barra de desplazamiento.
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Crea el Listbox.
        # En Tkinter el equivalente más cercano a ListView
        # es Listbox.
        list_view = tk.Listbox(
            frame,
            width=60,
            height=12,
            font=("Arial", 14),
            yscrollcommand=scrollbar.set
        )

        # Coloca el Listbox dentro del Frame.
        list_view.pack(side=tk.LEFT)

        # Conecta la barra de desplazamiento con el Listbox.
        scrollbar.config(command=list_view.yview)

        # Devuelve el Listbox creado.
        return list_view


    # ======================================================
    # PILA - STACK
    # ======================================================

    # Muestra la pantalla de la pila.
    def show_stack(self):

        # Limpia la ventana.
        self.clear_window()

        # Crea el título de la pila.
        title = tk.Label(
            self.root,
            text="PILA (STACK)",
            font=("Arial", 24, "bold")
        )

        # Coloca el título.
        title.pack(pady=20)

        # Crea una descripción de la pila.
        description = tk.Label(
            self.root,
            text="LIFO: el último elemento en entrar es el primero en salir.",
            font=("Arial", 12)
        )

        # Coloca la descripción.
        description.pack()

        # Crea el Listbox para mostrar los elementos de la pila.
        self.stack_list_view = self.create_list_view(self.root)

        # Crea un Frame para los controles.
        input_frame = tk.Frame(self.root)

        # Coloca el Frame.
        input_frame.pack(pady=10)

        # Crea el campo donde se escribe el dato.
        self.stack_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=25
        )

        # Coloca el campo de texto.
        self.stack_entry.grid(row=0, column=0, padx=5)

        # Crea el botón para agregar un elemento.
        tk.Button(
            input_frame,
            text="Apilar",
            font=("Arial", 12, "bold"),
            command=self.push_stack
        ).grid(row=0, column=1, padx=5)

        # Crea el botón para eliminar el último elemento.
        tk.Button(
            input_frame,
            text="Desapilar",
            font=("Arial", 12, "bold"),
            command=self.pop_stack
        ).grid(row=0, column=2, padx=5)

        # Crea el botón para vaciar la pila.
        tk.Button(
            input_frame,
            text="Vaciar",
            font=("Arial", 12),
            command=self.clear_stack
        ).grid(row=0, column=3, padx=5)

        # Crea el botón para regresar al menú.
        tk.Button(
            self.root,
            text="Regresar al menú",
            font=("Arial", 12),
            command=self.show_main_menu
        ).pack(pady=20)

        # Actualiza el Listbox.
        self.update_stack_view()


    # Agrega un elemento a la pila.
    def push_stack(self):

        # Obtiene el texto escrito por el usuario.
        value = self.stack_entry.get()

        # Comprueba si el campo está vacío.
        if value == "":

            # Muestra una advertencia.
            messagebox.showwarning(
                "Advertencia",
                "Ingrese un dato."
            )

            # Termina la función.
            return

        # Agrega el dato al final de la pila.
        self.stack.append(value)

        # Limpia el campo de texto.
        self.stack_entry.delete(0, tk.END)

        # Actualiza el Listbox.
        self.update_stack_view()


    # Elimina un elemento de la pila.
    def pop_stack(self):

        # Comprueba si la pila está vacía.
        if not self.stack:

            # Muestra una advertencia.
            messagebox.showwarning(
                "Pila vacía",
                "No hay elementos."
            )

            # Termina la función.
            return

        # Elimina el último elemento de la pila.
        value = self.stack.pop()

        # Muestra el elemento eliminado.
        messagebox.showinfo(
            "Resultado",
            value
        )

        # Actualiza el Listbox.
        self.update_stack_view()


    # Elimina todos los elementos de la pila.
    def clear_stack(self):

        # Vacía la lista.
        self.stack.clear()

        # Actualiza el Listbox.
        self.update_stack_view()


    # Actualiza visualmente la pila.
    def update_stack_view(self):

        # Elimina los datos anteriores del Listbox.
        self.stack_list_view.delete(0, tk.END)

        # Recorre la pila desde el último elemento
        # hasta el primero.
        for value in reversed(self.stack):

            # Inserta únicamente el dato.
            # No coloca números ni puntos.
            self.stack_list_view.insert(
                tk.END,
                value
            )


    # ======================================================
    # COLA - QUEUE
    # ======================================================

    # Muestra la pantalla de la cola.
    def show_queue(self):

        # Limpia la ventana.
        self.clear_window()

        # Crea el título.
        title = tk.Label(
            self.root,
            text="COLA (QUEUE)",
            font=("Arial", 24, "bold")
        )

        # Coloca el título.
        title.pack(pady=20)

        # Crea la descripción.
        description = tk.Label(
            self.root,
            text="FIFO: el primero en entrar es el primero en salir.",
            font=("Arial", 12)
        )

        # Coloca la descripción.
        description.pack()

        # Crea el Listbox de la cola.
        self.queue_list_view = self.create_list_view(self.root)

        # Crea el Frame para los controles.
        input_frame = tk.Frame(self.root)

        # Coloca el Frame.
        input_frame.pack(pady=10)

        # Crea el campo de entrada.
        self.queue_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=25
        )

        # Coloca el campo.
        self.queue_entry.grid(row=0, column=0, padx=5)

        # Botón para agregar a la cola.
        tk.Button(
            input_frame,
            text="Encolar",
            font=("Arial", 12, "bold"),
            command=self.enqueue
        ).grid(row=0, column=1, padx=5)

        # Botón para quitar de la cola.
        tk.Button(
            input_frame,
            text="Desencolar",
            font=("Arial", 12, "bold"),
            command=self.dequeue
        ).grid(row=0, column=2, padx=5)

        # Botón para vaciar la cola.
        tk.Button(
            input_frame,
            text="Vaciar",
            font=("Arial", 12),
            command=self.clear_queue
        ).grid(row=0, column=3, padx=5)

        # Botón para regresar al menú.
        tk.Button(
            self.root,
            text="Regresar al menú",
            font=("Arial", 12),
            command=self.show_main_menu
        ).pack(pady=20)

        # Actualiza la vista.
        self.update_queue_view()


    # Agrega un elemento a la cola.
    def enqueue(self):

        # Obtiene el dato del campo.
        value = self.queue_entry.get()

        # Comprueba si está vacío.
        if value == "":

            # Muestra una advertencia.
            messagebox.showwarning(
                "Advertencia",
                "Ingrese un dato."
            )

            # Termina la función.
            return

        # Agrega el elemento al final.
        self.queue.append(value)

        # Limpia el campo.
        self.queue_entry.delete(0, tk.END)

        # Actualiza el Listbox.
        self.update_queue_view()


    # Elimina el primer elemento de la cola.
    def dequeue(self):

        # Comprueba si la cola está vacía.
        if not self.queue:

            # Muestra una advertencia.
            messagebox.showwarning(
                "Cola vacía",
                "No hay elementos."
            )

            # Termina la función.
            return

        # Elimina el primer elemento.
        value = self.queue.pop(0)

        # Muestra el elemento eliminado.
        messagebox.showinfo(
            "Resultado",
            value
        )

        # Actualiza el Listbox.
        self.update_queue_view()


    # Vacía la cola.
    def clear_queue(self):

        # Elimina todos los elementos.
        self.queue.clear()

        # Actualiza la vista.
        self.update_queue_view()


    # Actualiza visualmente la cola.
    def update_queue_view(self):

        # Elimina los elementos anteriores.
        self.queue_list_view.delete(0, tk.END)

        # Recorre todos los elementos.
        for value in self.queue:

            # Muestra solamente el dato.
            self.queue_list_view.insert(
                tk.END,
                value
            ) 


    # ======================================================
    # COLA DOBLE - DEQUE
    # ======================================================

    # Muestra la pantalla de la cola doble.
    def show_deque(self):

        # Limpia la ventana.
        self.clear_window()

        # Crea el título.
        title = tk.Label(
            self.root,
            text="COLA DOBLE (DEQUE)",
            font=("Arial", 24, "bold")
        )

        # Coloca el título.
        title.pack(pady=20)

        # Crea la descripción.
        description = tk.Label(
            self.root,
            text="Permite agregar y eliminar elementos por ambos extremos.",
            font=("Arial", 12)
        )

        # Coloca la descripción.
        description.pack()

        # Crea el Listbox.
        self.deque_list_view = self.create_list_view(self.root)

        # Crea el Frame de controles.
        input_frame = tk.Frame(self.root)

        # Coloca el Frame.
        input_frame.pack(pady=10)

        # Crea el campo de entrada.
        self.deque_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=25
        )

        # Coloca el campo.
        self.deque_entry.grid(row=0, column=0, padx=5)

        # Botón para agregar por la izquierda.
        tk.Button(
            input_frame,
            text="Agregar izquierda",
            font=("Arial", 11, "bold"),
            command=self.add_deque_left
        ).grid(row=0, column=1, padx=5)

        # Botón para agregar por la derecha.
        tk.Button(
            input_frame,
            text="Agregar derecha",
            font=("Arial", 11, "bold"),
            command=self.add_deque_right
        ).grid(row=0, column=2, padx=5)

        # Botón para eliminar por la izquierda.
        tk.Button(
            input_frame,
            text="Eliminar izquierda",
            font=("Arial", 11),
            command=self.remove_deque_left
        ).grid(row=1, column=1, padx=5, pady=5)

        # Botón para eliminar por la derecha.
        tk.Button(
            input_frame,
            text="Eliminar derecha",
            font=("Arial", 11),
            command=self.remove_deque_right
        ).grid(row=1, column=2, padx=5, pady=5)

        # Botón para vaciar la cola doble.
        tk.Button(
            input_frame,
            text="Vaciar",
            font=("Arial", 11),
            command=self.clear_deque
        ).grid(row=1, column=3, padx=5, pady=5)

        # Botón para regresar.
        tk.Button(
            self.root,
            text="Regresar al menú",
            font=("Arial", 12),
            command=self.show_main_menu
        ).pack(pady=20)

        # Actualiza la vista.
        self.update_deque_view()


    # Agrega un dato por la izquierda.
    def add_deque_left(self):

        # Obtiene el dato.
        value = self.deque_entry.get()

        # Comprueba si está vacío.
        if value == "":

            # Muestra advertencia.
            messagebox.showwarning(
                "Advertencia",
                "Ingrese un dato."
            )

            # Termina la función.
            return

        # Agrega el elemento al inicio.
        self.deque.appendleft(value)

        # Limpia el campo.
        self.deque_entry.delete(0, tk.END)

        # Actualiza la vista.
        self.update_deque_view()


    # Agrega un dato por la derecha.
    def add_deque_right(self):

        # Obtiene el dato.
        value = self.deque_entry.get()

        # Comprueba si está vacío.
        if value == "":

            # Muestra advertencia.
            messagebox.showwarning(
                "Advertencia",
                "Ingrese un dato."
            )

            # Termina la función.
            return

        # Agrega el dato al final.
        self.deque.append(value)

        # Limpia el campo.
        self.deque_entry.delete(0, tk.END)

        # Actualiza la vista.
        self.update_deque_view()


    # Elimina el elemento de la izquierda.
    def remove_deque_left(self):

        # Comprueba si está vacía.
        if not self.deque:

            # Muestra advertencia.
            messagebox.showwarning(
                "Cola doble vacía",
                "No hay elementos."
            )

            # Termina la función.
            return

        # Elimina el primer elemento.
        value = self.deque.popleft()

        # Muestra el resultado.
        messagebox.showinfo(
            "Resultado",
            value
        )

        # Actualiza la vista.
        self.update_deque_view()


    # Elimina el elemento de la derecha.
    def remove_deque_right(self):

        # Comprueba si está vacía.
        if not self.deque:

            # Muestra advertencia.
            messagebox.showwarning(
                "Cola doble vacía",
                "No hay elementos."
            )

            # Termina la función.
            return

        # Elimina el último elemento.
        value = self.deque.pop()

        # Muestra el resultado.
        messagebox.showinfo(
            "Resultado",
            value
        )

        # Actualiza la vista.
        self.update_deque_view()


    # Vacía la cola doble.
    def clear_deque(self):

        # Elimina todos los elementos.
        self.deque.clear()

        # Actualiza la vista.
        self.update_deque_view()


    # Actualiza el Listbox de la cola doble.
    def update_deque_view(self):

        # Elimina los elementos anteriores.
        self.deque_list_view.delete(0, tk.END)

        # Recorre los elementos del deque.
        for value in self.deque:

            # Muestra solamente el dato.
            self.deque_list_view.insert(
                tk.END,
                value
            )


    # ======================================================
    # LISTA
    # ======================================================

    # Muestra la pantalla de la lista.
    def show_list(self):

        # Limpia la ventana.
        self.clear_window()

        # Crea el título.
        title = tk.Label(
            self.root,
            text="LISTA",
            font=("Arial", 24, "bold")
        )

        # Coloca el título.
        title.pack(pady=20)

        # Crea la descripción.
        description = tk.Label(
            self.root,
            text="Permite almacenar diferentes elementos y modificarlos.",
            font=("Arial", 12)
        )

        # Coloca la descripción.
        description.pack()

        # Crea el Listbox.
        self.list_list_view = self.create_list_view(self.root)

        # Crea el Frame de controles.
        input_frame = tk.Frame(self.root)

        # Coloca el Frame.
        input_frame.pack(pady=10)

        # Crea el campo de texto.
        self.list_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=25
        )

        # Coloca el campo.
        self.list_entry.grid(row=0, column=0, padx=5)

        # Botón para agregar.
        tk.Button(
            input_frame,
            text="Agregar",
            font=("Arial", 12, "bold"),
            command=self.add_list
        ).grid(row=0, column=1, padx=5)

        # Botón para eliminar.
        tk.Button(
            input_frame,
            text="Eliminar",
            font=("Arial", 12, "bold"),
            command=self.remove_list
        ).grid(row=0, column=2, padx=5)

        # Botón para vaciar.
        tk.Button(
            input_frame,
            text="Vaciar",
            font=("Arial", 12),
            command=self.clear_list
        ).grid(row=0, column=3, padx=5)

        # Botón para regresar.
        tk.Button(
            self.root,
            text="Regresar al menú",
            font=("Arial", 12),
            command=self.show_main_menu
        ).pack(pady=20)

        # Actualiza la vista.
        self.update_list_view()


    # Agrega un elemento a la lista.
    def add_list(self):

        # Obtiene el dato escrito.
        value = self.list_entry.get()

        # Comprueba si está vacío.
        if value == "":

            # Muestra una advertencia.
            messagebox.showwarning(
                "Advertencia",
                "Ingrese un dato."
            )

            # Termina la función.
            return

        # Agrega el dato a la lista.
        self.list_data.append(value)

        # Limpia el campo.
        self.list_entry.delete(0, tk.END)

        # Actualiza el Listbox.
        self.update_list_view()


    # Elimina un elemento seleccionado.
    def remove_list(self):

        # Comprueba si la lista está vacía.
        if not self.list_data:

            # Muestra advertencia.
            messagebox.showwarning(
                "Lista vacía",
                "No hay elementos."
            )

            # Termina la función.
            return

        # Obtiene el elemento seleccionado.
        selected = self.list_list_view.curselection()

        # Comprueba si el usuario seleccionó algo.
        if not selected:

            # Muestra una advertencia.
            messagebox.showwarning(
                "Seleccionar",
                "Seleccione un elemento."
            )

            # Termina la función.
            return

        # Obtiene la posición seleccionada.
        index = selected[0]

        # Elimina el elemento de la lista.
        value = self.list_data.pop(index)

        # Muestra el elemento eliminado.
        messagebox.showinfo(
            "Resultado",
            value
        )

        # Actualiza la vista.
        self.update_list_view()


    # Vacía la lista.
    def clear_list(self):

        # Elimina todos los elementos.
        self.list_data.clear()

        # Actualiza la vista.
        self.update_list_view()


    # Actualiza visualmente la lista.
    def update_list_view(self):

        # Elimina los datos anteriores.
        self.list_list_view.delete(0, tk.END)

        # Recorre todos los elementos.
        for value in self.list_data:

            # Muestra solamente el dato.
            self.list_list_view.insert(
                tk.END,
                value
            )


    # ======================================================
    # LISTA ENLAZADA
    # ======================================================

    # Muestra la pantalla de la lista enlazada.
    def show_linked_list(self):

        # Limpia la ventana.
        self.clear_window()

        # Crea el título.
        title = tk.Label(
            self.root,
            text="LISTA ENLAZADA",
            font=("Arial", 24, "bold")
        )

        # Coloca el título.
        title.pack(pady=20)

        # Crea la descripción.
        description = tk.Label(
            self.root,
            text="Cada nodo contiene un dato y una referencia al siguiente nodo.",
            font=("Arial", 12)
        )

        # Coloca la descripción.
        description.pack()

        # Crea el Listbox.
        self.linked_list_view = self.create_list_view(self.root)

        # Crea el Frame para los controles.
        input_frame = tk.Frame(self.root)

        # Coloca el Frame.
        input_frame.pack(pady=10)

        # Crea el campo de texto.
        self.linked_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=25
        )

        # Coloca el campo.
        self.linked_entry.grid(row=0, column=0, padx=5)

        # Botón para agregar.
        tk.Button(
            input_frame,
            text="Agregar",
            font=("Arial", 12, "bold"),
            command=self.add_linked_list
        ).grid(row=0, column=1, padx=5)

        # Botón para eliminar.
        tk.Button(
            input_frame,
            text="Eliminar",
            font=("Arial", 12, "bold"),
            command=self.remove_linked_list
        ).grid(row=0, column=2, padx=5)

        # Botón para vaciar.
        tk.Button(
            input_frame,
            text="Vaciar",
            font=("Arial", 12),
            command=self.clear_linked_list
        ).grid(row=0, column=3, padx=5)

        # Botón para regresar al menú.
        tk.Button(
            self.root,
            text="Regresar al menú",
            font=("Arial", 12),
            command=self.show_main_menu
        ).pack(pady=20)

        # Actualiza la vista.
        self.update_linked_list_view()


    # Agrega un elemento a la lista enlazada.
    def add_linked_list(self):

        # Obtiene el dato escrito.
        value = self.linked_entry.get()

        # Comprueba si está vacío.
        if value == "":

            # Muestra una advertencia.
            messagebox.showwarning(
                "Advertencia",
                "Ingrese un dato."
            )

            # Termina la función.
            return

        # Agrega el dato.
        self.linked_list.append(value)

        # Limpia el campo.
        self.linked_entry.delete(0, tk.END)

        # Actualiza la vista.
        self.update_linked_list_view()


    # Elimina un elemento seleccionado.
    def remove_linked_list(self):

        # Comprueba si existen elementos.
        if not self.linked_list:

            # Muestra una advertencia.
            messagebox.showwarning(
                "Lista enlazada vacía",
                "No hay elementos."
            )

            # Termina la función.
            return

        # Obtiene el elemento seleccionado.
        selected = self.linked_list_view.curselection()

        # Comprueba si seleccionó algún elemento.
        if not selected:

            # Muestra una advertencia.
            messagebox.showwarning(
                "Seleccionar",
                "Seleccione un elemento."
            )

            # Termina la función.
            return

        # Obtiene la posición seleccionada.
        index = selected[0]

        # Elimina el elemento.
        value = self.linked_list.pop(index)

        # Muestra el elemento eliminado.
        messagebox.showinfo(
            "Resultado",
            value
        )

        # Actualiza la vista.
        self.update_linked_list_view()


    # Vacía la lista enlazada.
    def clear_linked_list(self):

        # Elimina todos los elementos.
        self.linked_list.clear()

        # Actualiza la vista.
        self.update_linked_list_view()


    # Actualiza visualmente la lista enlazada.
    def update_linked_list_view(self):

        # Elimina los elementos anteriores.
        self.linked_list_view.delete(0, tk.END)

        # Recorre todos los elementos.
        for value in self.linked_list:

            # Muestra solamente el dato.
            self.linked_list_view.insert(
                tk.END,
                value
            )


# ==========================================================
# INICIO DEL PROGRAMA
# ==========================================================

# Comprueba que este archivo se está ejecutando directamente.
if __name__ == "__main__":

    # Crea la ventana principal de Tkinter.
    root = tk.Tk()

    # Crea una instancia de nuestra aplicación.
    app = DataStructuresApp(root)

    # Mantiene abierta la ventana y espera las acciones
    # del usuario.
    root.mainloop()