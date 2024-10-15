package assignments.geoshapes;

public abstract class Shape implements Drawable, Colorable {
    public abstract double calcArea();
    public abstract double calcPerimeter();
    public String getShapeType();

    @Override
    public void draw() {
        // Calculate the area and perimeter of the shape
        double area = this.calcArea();
        double perimeter = this.calcPerimeter();
        // Print the area and perimeter of the shape
        System.out.println("Drawing a " + this.getShapeType());
        System.out.println("Area: " + area);
        System.out.println("Perimeter: " + perimeter);
        System.out.println("Color: : " + this.getColor());
    }
}
