import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class IrisDataFrame {
    private List<Double> sepalLength;
    private List<Double> sepalWidth;
    private List<Double> petalLength;
    private List<Double> petalWidth;
    private List<String> species;
    
    public IrisDataFrame() {
        sepalLength = new ArrayList<>();
        sepalWidth = new ArrayList<>();
        petalLength = new ArrayList<>();
        petalWidth = new ArrayList<>();
        species = new ArrayList<>();
    }
    
    public void addRow(double sl, double sw, double pl, double pw, String sp) {
        sepalLength.add(sl);
        sepalWidth.add(sw);
        petalLength.add(pl);
        petalWidth.add(pw);
        species.add(sp);
    }
    
    public void printSummary() {
        System.out.println("Iris Dataset Summary:");
        System.out.println("Number of rows: " + sepalLength.size());
        System.out.println("\nFirst 5 rows:");
        for (int i = 0; i < Math.min(5, sepalLength.size()); i++) {
            System.out.printf("Row %d: %.1f, %.1f, %.1f, %.1f, %s%n",
                i + 1,
                sepalLength.get(i),
                sepalWidth.get(i),
                petalLength.get(i),
                petalWidth.get(i),
                species.get(i)
            );
        }
    }

    // Getters
    public List<Double> getSepalLength() { return sepalLength; }
    public List<Double> getSepalWidth() { return sepalWidth; }
    public List<Double> getPetalLength() { return petalLength; }
    public List<Double> getPetalWidth() { return petalWidth; }
    public List<String> getSpecies() { return species; }
}

public class p8_dataset_java {
    public static IrisDataFrame readIrisData(String filename) {
        IrisDataFrame dataFrame = new IrisDataFrame();
        
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                // Dividir la línea por comas
                String[] values = line.split(",");
                
                if (values.length == 5) {
                    // Convertir los primeros 4 valores a double
                    double sepalLength = Double.parseDouble(values[0]);
                    double sepalWidth = Double.parseDouble(values[1]);
                    double petalLength = Double.parseDouble(values[2]);
                    double petalWidth = Double.parseDouble(values[3]);
                    // El último valor es la especie (String)
                    String species = values[4].trim();
                    
                    dataFrame.addRow(sepalLength, sepalWidth, petalLength, petalWidth, species);
                }
            }
        } catch (IOException e) {
            System.err.println("Error al leer el archivo: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.err.println("Error al convertir los datos: " + e.getMessage());
        }
        
        return dataFrame;
    }
    
    public static void main(String[] args) {
        String filename = "bezdekIris.data";
        IrisDataFrame irisData = readIrisData(filename);
        irisData.printSummary();
    }
}