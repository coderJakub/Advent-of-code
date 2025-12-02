package helper;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FileReader {
    Path file;

    public List<String> readLines() {
        try {
            return Files.readAllLines(this.file);
        } catch (IOException e) {
            System.err.println("Fehler beim Lesen der Datei: " + this.file);
            e.printStackTrace();
            return List.of(); // Leere Liste zurückgeben
        }
    }

    public String readAll() {
        try {
            return Files.readString(this.file);
        } catch (IOException e) {
            System.err.println("Fehler beim Lesen der Datei: " + this.file);
            e.printStackTrace();
            return "";
        }
    }

    public FileReader(String[] args) throws Exception {
        if (args.length != 1) throw new Exception("Needs input file");
        this.file = Path.of(args[0]);
    }
}