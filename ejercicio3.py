# Se agrega el siguiente diagrama, el cual representa a los mozos de la pizzería a modelar:

# Mozo
# <<Atributos de clase>>
# <<Atributos de instancia>>
# nombre: string
# pizzas: Pizza[]
# <<Constructores>>
# Mozo(nom: string)
# <<Comandos>>
# establecerNombre(nom: string)
# tomarPizzas(pizzas: Pizza[])
# Requiere pizzas ligado
# servirPizzas()
# <<Consultas>>
# obtenerNombre(): string
# obtenerPizzas(): Pizza[]
# obtenerEstadoLibre(): boolean

# Habiendo analizado el diagrama, genere la clase Mozo con los atributos y servicios
# mencionados en dicho diagrama.
#   a. El atributo pizzas se inicializa como una lista vacía.
#   b. El comando tomarPizzas agrega los objetos de la clase Pizza referenciados por
#   el parámetro formal pizzas. El mozo puede tomar hasta un máximo de 2 pizzas.
#   c. servirPizzas limpia la lista pizzas, haciendo entrega de los pedidos a los clientes.
#   d. obtenerEstadoLibre debe retornar True si es que la lista referenciada por el
#   atributo pizzastiene una longitud de entre 0 y 1. Así mismo, debe retornar False
#   si su tamaño es igual a 2.

# TODO all