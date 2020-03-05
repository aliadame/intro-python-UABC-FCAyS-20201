class Estudiante:
  # Indicamos atributos para la clase
  edad = 0
  carrera = "Desconocida"
  universidad = "Desconocida"
  genero = "Femenino"
  
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
    print("Nueva edad ", edadAlumno)
    
# Generamos un nuevo Estudiante
miguel = Estudiante()
miguel.estudiar("lógica para programación")
# imprimimos atributo del objeto
miguel.cambiarEdad(21)
print(miguel.edad)