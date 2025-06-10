package ejercici1;

public class main {
    public static void main(String[] args) {
       
        Caja<String> cajaPalabras = new Caja<>();
        cajaPalabras.guardar("Hola Mundo");
        

        Caja<Integer> cajaNumeros = new Caja<>();
        cajaNumeros.guardar(42);
       
        System.out.println("Caja 1 contiene: " + cajaPalabras.obtener());
        System.out.println("Caja 2 contiene: " + cajaNumeros.obtener());
    }
}

class Caja<T> {
    private T objeto;
    
    public void guardar(T objeto) {
        this.objeto = objeto;
    }
    
    public T obtener() {
        return objeto;
    }
}

