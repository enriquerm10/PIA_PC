import pywhatkit

def inicio():
    # Importamos el ModuMódulo

    # Usamos Un try-except
    try:
      # Enviamos el mensaje
      pywhatkit.sendwhatmsg("+528129372333",  
                            "Mensaje De Prueba",
                            23,18)
      print("Mensaje Enviado")
      
    except:
      print("Ocurrio Un Error")
