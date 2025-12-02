package helper;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class FileReader {
    Path file;

    public String[] readLines() {
        return this.readAll().split("\n");
    }

    public String[] readCSV(){
        return this.readAll().split(",");
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