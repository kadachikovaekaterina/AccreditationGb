import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Random;


public class Main {

    public static void main(String[] args) throws IOException {

        BufferedWriter writer = new BufferedWriter(new FileWriter("result.txt"));

        for (int i = 0; i < 10; i++) {
           Toy toy = Get();
           writer.write(toy.toString() + "\n");
        }
        writer.close();
    }

    public static void put(PriorityQueue pq, Toy toy) {

        int count = toy.getWeight() / 10;
        for (int i = 0; i < count; i++) {
            pq.add(toy);
        }
    }

    public static Toy Get() {
        Comparator<Toy> comparator = new Comparator<Toy>() {
            @Override
            public int compare(Toy o1, Toy o2) {
                return o1.getWeight() - o2.getWeight();
            }
        };
        Toy constructor = new Toy(1, "Конструктор", 20);
        Toy robot = new Toy(2, "Робот", 20);
        Toy doll = new Toy(3, "Кукла", 60);
        PriorityQueue<Toy> prizes = new PriorityQueue<>(comparator);
        put(prizes, constructor);
        put(prizes, robot);
        put(prizes, doll);
        Toy result = null;
        Random random = new Random();
        int element = random.nextInt(0, prizes.size());
        for (int i = 0; i <= element; i++) {
            result = prizes.poll();
        }
        return result;

    }
    }





