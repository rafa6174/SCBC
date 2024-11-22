import tkinter as tk
from tkinter import scrolledtext

# Respuestas predefinidas sobre cálculo
def chatbot_respuesta(mensaje):
	respuestas = {
		"derivadas": "Las derivadas representan el cambio instantáneo de una función. Revisa las notas de cálculo diferencial para más información.",
		"integrales": "Las integrales calculan el área bajo una curva. Consulta las notas de cálculo integral para más detalles.",
		"límites": "El límite describe el valor al que se aproxima una función. ¡Es fundamental en cálculo diferencial!",
		"teorema fundamental": "El Teorema Fundamental del Cálculo conecta las derivadas y las integrales. Mira tus notas de cálculo para ejemplos prácticos.",
		"adiós": "¡Adiós! Espero haberte ayudado.",
		"referencias": "Cálculo de Tom Apostol, Cálculo de Spivak para teoría y ejercicios, y el Granville para ejercicios.",
		"¿qué temas siguen?": "Sería buena idea que estudiaras cálculo de varias variables.",
		"teorema del valor intermedio": "Es un teorema que dice que si una función continua cambia de signo entonces tiene al menos un cero."
	}
	return respuestas.get(mensaje.lower(), "Lo siento, no entiendo esa consulta. Intenta preguntar sobre derivadas, integrales, límites o referencias.")

# Función para mostrar el chatbot en una ventana emergente
def mostrar_chatbot():
	def enviar():
		mensaje = entrada.get()
		if mensaje.lower() == "adiós":
			ventana.destroy()
		else:
			ventana_chat.insert(tk.END, f"Tú: {mensaje}\n")
			respuesta = chatbot_respuesta(mensaje)
			ventana_chat.insert(tk.END, f"Chatbot: {respuesta}\n")
		entrada.delete(0, tk.END)

	# Crear ventana principal
	ventana = tk.Toplevel()  # Usa Toplevel para crear una ventana emergente
	ventana.title("Chatbot de Referencias de Cálculo")
	ventana.geometry("500x600")

	# Título
	titulo = tk.Label(ventana, text="Chatbot de Cálculo", font=("Helvetica", 16, "bold"))
	titulo.pack(pady=10)

	# Área de chat
	ventana_chat = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, height=20, state='normal')
	ventana_chat.pack(padx=10, pady=10)
	ventana_chat.insert(tk.END, "Chatbot: ¡Hola! Pregunta sobre cálculo: derivadas, integrales, límites o el teorema fundamental, referencias o ¿Qué temas siguen?.\n")

	# Entrada de texto
	entrada = tk.Entry(ventana, width=50, font=("Helvetica", 12))
	entrada.pack(padx=10, pady=5)

	# Botón de enviar
	btn_enviar = tk.Button(ventana, text="Enviar", command=enviar, font=("Helvetica", 12), bg="lightblue")
	btn_enviar.pack(pady=10)

	ventana.mainloop()
