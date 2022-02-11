def mayus(func):
    def envoltura(string):
        return func(string).upper()
    return envoltura


@mayus
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('cristian'))