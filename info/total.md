We are going to experiment with various bullet shapes and designs.
As basis for our designs, we will use the [spheroid](http://en.wikipedia.org/wiki/Spheroid).
Let's make the preliminary calculations.

We know the height and the width (in centimeters) for this spheroid.
You should create a function to calculate the volume (cubic inches) and the surface area (square centimeters).

![Spheroid](spheroid.svg)

**Tips:** Be careful with _sin_<sup>-1</sup>_x_ -- this is _arcsin_.

**Input:** Two arguments. A height and a width as integers.

**Output:** The volume and the surface area as a list/tuple of floats. The results should be accurate to two decimals.

**Example:**

```python
spheroid(4, 2) == [8.38, 21.48] # or (8.38, 21.48)
spheroid(2, 2) == [4.19, 12.57]
spheroid(2, 4) == [16.76, 34.69]
```

**How it is used:**

This is a simple math task, but we want to introduce you to the ubiquitous spheroid.

For example, the prolate spheroid is the shape of the ball in several sports such as in rugby and Australian football. In American football, a more pointed prolate spheroid is used.
Several moons of the Solar system approximate prolate spheroids in shape, though they are actually scalene.
Examples of these are Mimas, Enceladus, and Tethys which orbit Saturn and Miranda which orbits Uranus.

Even the true shape of the Earth is an Oblate Spheroid, though it is only very slightly oblate.
The diameter from the North Pole to the South Pole (the shortest diameter) is approximately 12,714 km.
The equatorial diameter (the longest diameter) is approximately 12,756 km.
This is not a big difference, but it does mean the Earth is not quite a sphere.

**Precondition:**

```python
0 < width < 100
0 < height < 100
```
