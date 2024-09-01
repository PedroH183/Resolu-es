import java.util.ArrayList;
import java.util.List;

class Fibo{

    public static List<Integer> fibonacciLista(int numeroDesejado){
        List<Integer> sequencia_fibonnaci = new ArrayList<>();
        sequencia_fibonnaci.add(0);
        sequencia_fibonnaci.add(1);

        int i = 1;
        while (sequencia_fibonnaci.get(i) < numeroDesejado) {
            sequencia_fibonnaci.add(sequencia_fibonnaci.get(i) + sequencia_fibonnaci.get(i - 1));
            i++;
        }

        return sequencia_fibonnaci;
    }

    public static boolean estaContidoFibonacciSeq(List<Integer> fibonacciLista, int elemento) {
        return fibonacciLista.contains(elemento);
    }

    public static void printSequence(List<Integer> fibSequence){
        for(int i = 0; i < fibSequence.size() ; ++i){
            System.out.println(fibSequence.get(i));
        }
    }

    public static void main(String[] args) {
        List<Integer> arr =  fibonacciLista(13);
        printSequence(arr);
        System.out.println(estaContidoFibonacciSeq(arr, 13));
    }
}