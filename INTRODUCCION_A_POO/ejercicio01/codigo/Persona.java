public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    
    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    
    public String mostrarSaludo() {
        return "hola, soy " + nombre + " de " + ciudad;
    }

    
    public String esMayor() {
        if (edad >= 18) {
            return "es mayor de edad " + nombre;
        } else {
            return "no es mayor de edad " + nombre;
        }
    }

    public static void main(String[] args) {
        Persona p1 = new Persona("jose", 14, "La Paz");
        Persona p2 = new Persona("juan", 20, "Santa Cruz");
        Persona p3 = new Persona("daniel", 19, "El Alto");

        String pe1 = p1.mostrarSaludo();
        String pe2 = p2.mostrarSaludo();
        String pe3 = p3.mostrarSaludo();

        System.out.println(pe1);
        System.out.println(pe2);
        System.out.println(pe3);

        String per1 = p1.esMayor();
        String per2 = p2.esMayor();
        String per3 = p3.esMayor();

        System.out.println(per1);
        System.out.println(per2);
        System.out.println(per3);
    }
}