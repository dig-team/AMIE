package amie.rules.format;

public class FastLocaleDouble {
    public static double parse(String text) {
        if (text == null) {
            throw new IllegalArgumentException("Input cannot be null");
        }
        // Replace decimal comma with dot
        return Double.parseDouble(text.replace(',', '.'));
    }
}
