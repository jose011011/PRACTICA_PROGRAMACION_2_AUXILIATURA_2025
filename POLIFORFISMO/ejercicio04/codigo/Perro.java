public class Perro {
    private String nombre;
    private int edad;
    private String raza;

    public Perro(String nombre, int edad, String raza) {
        this.nombre = nombre;
        this.edad = edad;
        this.raza = raza;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Edad: " + edad + ", Raza: " + raza;
    }

    public void hacerSonido() {
        System.out.println("el " + nombre + " Guau");
    }

    public void moverse() {
        System.out.println("El perro corre");
    }

    // Método main en la clase Perro
    public static void main(String[] args) {
        Perro perro = new Perro("Firulais", 5, "Labrador");
        Gato gato = new Gato("gorda", "Blanco");
        Pajaro pajaro = new Pajaro("pajaro loca", "Canario");

        System.out.println(perro);
        perro.hacerSonido();
        perro.moverse();

        System.out.println(gato);
        gato.hacerSonido();
        gato.moverse();

        System.out.println(pajaro);
        pajaro.hacerSonido();
        pajaro.moverse();
    }
}