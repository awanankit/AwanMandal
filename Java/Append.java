public class Append {
    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40};
        int umber = 50;
        int[] array = new int[numbers.length + 1];
        System.arraycopy(numbers, 0, array, 0, numbers.length);
        array[numbers.length] = umber;
        for (int i =0; i < array.length; i++) {
            System.out.println(array[i]);
            
    }
}
'

