package assignments.geoshapes;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Shape> shapes = new ArrayList<Shape>();
        shapes.add(new Rectangle(5, 10));
        shapes.add(new Square(5));
        shapes.add(new Circle(5));
        for (Shape shape : shapes) {
            shape.draw();
            System.out.println();
        }
    }
}
