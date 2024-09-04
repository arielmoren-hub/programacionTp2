# Dado el siguiente diagrama de clases:

# MaestroPizzero
# <<Atributos de clase>>
# <<Atributos de instancia>>
# nombre: string
# pizzasPorCocinar: Pizza[]
# pizzasPorEntregar: Pizza[]
# <<Constructores>>
# MaestroPizzero(nom: string)
# <<Comandos>>
# establecerNombre(nom: string)
# tomarPedido(var: str): Pizza
# Requiere var no vacío
# cocinar()
# entregar(): Pizza[]
# <<Consultas>>
# obtenerNombre(): string
# obtenerPizzasPorCocinar(): Pizza[]
# obtenerPizzasPorEntregar(): Pizza[]

# Genere la clase MaestroPizzero, conteniendo los atributos y servicios mencionados en
# el diagrama de clases anterior.
#   i. El comando tomarPedido debe crear un nuevo objeto de la clase Pizza,
#   de la variedad indicada en el parámetro formal var. Una vez inicializado
#   dicho objeto, debe este agregarse a la lista referenciada por el atributo
#   pizzasPorCocinar.
#   ii. El comando cocinar debe tomar todos los objetos de la clase Pizza de la
#   lista pizzasPorCocinar y depositarlos en una segunda lista,
#   pizzasPorEntregar. Si no hay pizzas por ser cocinadas, el comando no
#   tiene efecto sobre el estado interno del objeto.
#   iii. El comando entregar retorna hasta un máximo de 2 objetos de la clase
#   Pizza de la lista pizzasPorEntregar, removiéndolos de ella. Si no hay
#   pizzas para ser entregadas, se debe retornar una lista vacía

# TODO all