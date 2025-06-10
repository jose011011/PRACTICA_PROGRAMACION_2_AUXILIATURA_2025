package ejercicio01;
import java.io.*;
import java.util.*;

class Empleado {
    private String nombre;
    private int edad;
    private double salario;

    public Empleado(String nombre, int edad, double salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public double getSalario() {
        return salario;
    }

    @Override
    public String toString() {
        return nombre + "," + edad + "," + salario;
    }

    public static Empleado desdeTexto(String linea) {
        String[] partes = linea.trim().split(",");
        String nombre = partes[0];
        int edad = Integer.parseInt(partes[1]);
        double salario = Double.parseDouble(partes[2]);
        return new Empleado(nombre, edad, salario);
    }
}

class ArchivoEmpleado {
    private String nombreArchivo;

    public ArchivoEmpleado(String nombreArchivo) {
        this.nombreArchivo = nombreArchivo;
    }

    public void crearArchivo() {
        try (PrintWriter pw = new PrintWriter(new FileWriter(nombreArchivo))) {
            // Archivo creado vacío
            System.out.println("Archivo creado correctamente.");
        } catch (IOException e) {
            System.out.println("Error creando el archivo: " + e.getMessage());
        }
    }

    public void guardarEmpleado(Empleado empleado) {
        try (PrintWriter pw = new PrintWriter(new FileWriter(nombreArchivo, true))) {
            pw.println(empleado.toString());
            System.out.println("Empleado " + empleado.getNombre() + " guardado con éxito.");
        } catch (IOException e) {
            System.out.println("Error guardando empleado: " + e.getMessage());
        }
    }

    public List<Empleado> cargarEmpleados() {
        List<Empleado> empleados = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(nombreArchivo))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                empleados.add(Empleado.desdeTexto(linea));
            }
        } catch (FileNotFoundException e) {
            System.out.println("El archivo no existe.");
        } catch (IOException e) {
            System.out.println("Error leyendo el archivo: " + e.getMessage());
        }
        return empleados;
    }

    public Empleado buscaEmpleado(String nombre) {
        List<Empleado> empleados = cargarEmpleados();
        for (Empleado emp : empleados) {
            if (emp.getNombre().equalsIgnoreCase(nombre)) {
                return emp;
            }
        }
        return null;
    }

    public Empleado mayorSalario(double sueldo) {
        List<Empleado> empleados = cargarEmpleados();
        for (Empleado emp : empleados) {
            if (emp.getSalario() > sueldo) {
                return emp;
            }
        }
        return null;
    }
}

public class main {
    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.txt");
        archivo.crearArchivo();
        archivo.guardarEmpleado(new Empleado("Ana", 30, 2500));
        archivo.guardarEmpleado(new Empleado("Luis", 28, 3200));
        archivo.guardarEmpleado(new Empleado("Carlos", 40, 1500));

        Empleado empleado = archivo.buscaEmpleado("Luis");
        if (empleado != null) {
            System.out.println("Empleado encontrado: " + empleado.getNombre() + ", " + empleado.getEdad() + ", " + empleado.getSalario());
        } else {
            System.out.println("Empleado no encontrado.");
        }

        Empleado empleadoMayor = archivo.mayorSalario(2000);
        if (empleadoMayor != null) {
            System.out.println("Empleado con mayor salario: " + empleadoMayor.getNombre() + ", " + empleadoMayor.getSalario());
        } else {
            System.out.println("Ninguno tiene salario mayor.");
        }
    }
}

