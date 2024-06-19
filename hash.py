import bcrypt

# Ejemplo de cómo generar un hash de contraseña
# mi_contraseña_segura1 -- en adelante
# contraseña_especialista1 -- en adelante
# contraseña_administrador1 -- en adelante
password = "contraseña_administrador3"
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# hashed es lo que almacenarás en la base de datos
print('CONTRASEÑA:', hashed)
