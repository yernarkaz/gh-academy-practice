package assignments.geoshapes;

public class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double calcArea() {
        return Math.PI * radius * radius;
    }

    public double calcPerimeter() {
        return 2 * Math.PI * radius;
    }

    public String getShapeType() {
        return "Circle";
    }

    @Override
    public String getColor() {
        return "Green";
    }
    
}
