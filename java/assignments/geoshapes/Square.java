package assignments.geoshapes;

public class Square extends Shape {
    private double side;

    public Square(double side) {
        this.side = side;
    }

    public double calcArea() {
        return side * side;
    }

    public double calcPerimeter() {
        return 4 * side;
    }

    public String getShapeType() {
        return "Square";
    }

    @Override
    public String getColor() {
        return "Orange";   
    }
    
}
