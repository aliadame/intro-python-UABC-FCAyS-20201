class Estudiante:
  # Indicamos atributos para la clase
  edad = 0 #
  carrera = "Desconocida" #
  universidad = "Desconocida"
  genero = "Masculino"
  
  # Equivalente en java a public Estudiante(public Integer edad, public String carrera) {
  def __init__(self, edad, carrera) :
    self.edad = edad # paso de parametro en constructor
    self.carrera = carrera
  
  # definimos funciones
  def festejar(self) :
    print("Festejando")
    
  def estudiar(self, materia) :
    print("Estudiando " + materia)
    
  def llorar(self) :
    print("Llorando...")
    
  def dormir(self) :
    print("Durmiendo...")
  
  # Ajustamos la edad
  def cambiarEdad(self, edadAlumno) :
    self.edad = edadAlumno
    print("Nueva edad " + str(edadAlumno))
    
# Generamos un nuevo Estudiante
# miguel = Estudiante()
miguel = Estudiante(32, "lógica para programación")
# Imprime: "Estudiando lógica para programación"
miguel.estudiar("lógica para programación")
# imprimimos atributo del objeto
# miguel.cambiarEdad(21) # Imprime: "Nueva edad 21"
print(miguel.edad)