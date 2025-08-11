import num as np
vector = np.array([1,2,3])# Crea un vectir de numpy constante
print(vector)
print("version ", np.___version___)
print("tipo de dato ", type(vector)) # tipo de dato
print("dimension ", vector.ndim) # dimension del vector
print("forma ", vector.shape) # forma del vector
#Crear vector de ceros
vector_ceros = np.zeros(5)
print("vector de ceros ", vector_ceros)
#crear vector para llenar con unos
vector_unos = np.ones(5)
print("vector de unos ", vector_unos)
#crear vector con un rango de numeros
vector_rango = np.arange(10) # crea un vector con un rango de numeros 
print("vector de rango ", vector_rango)