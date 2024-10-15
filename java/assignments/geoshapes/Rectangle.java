package assignments.geoshapes;

public class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double calcArea() {
        return width * height;
    }

    public double calcPerimeter() {
        return 2 * (width + height);
    }

    public String getShapeType() {
        return "Rectangle";
    }

    @Override
    public String getColor() {
        return "Blue";
    }
    
}
