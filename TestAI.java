import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class TestAI {
    public static void main(String[] args) {
        try {
            URL url = new URL("http://localhost:5000/predict");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            String jsonInput = "{\"cgpa\":8.5,\"skills\":7,\"projects\":3}";

            OutputStream os = conn.getOutputStream();
            os.write(jsonInput.getBytes());
            os.flush();
            os.close();

            Scanner scanner = new Scanner(conn.getInputStream());
            while (scanner.hasNext()) {
                System.out.println(scanner.nextLine());
            }
            scanner.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}