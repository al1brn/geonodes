# fields

[Source Code](../demos/fields.py)

To compute an electromagnetic, you need two sets of locations:
- location of the electric charges
- location of the points in the spac where you want to compute the field

The modifiers and groups form two parts:
- field computation at given positions
- field visu either as arrows or as lines of fields

To visualize a field, you have to stack 3 groupds:
1. Compute a field giving E and B (for instance "Compute Electric Charges")
2. Chose points where to compute the field (for instance with "Field Computation Points" group)
3. Chose Arrows or Lines of Field to visualize E or B

The modifier "Fields Show Case" is an example of this process.

> [!NOTE]
> Modifiers:
> - Field Computation Points: generated points in space where to compute the field
> - Field Lines: visualize the lines of fields at starting positions
> - Field Arrows: visualize field arrows at given positions
> - Compute Electric Charges: compute E and B from a set of electric charges
> - Compute Solenoid: compute E & B for a solenoid
> - Compute Magnet: compute B for a normalized magnet
> - Fields Show Case: shows how to combine the modifiers to visualize fields

``` python
from geonodes.demos import fields

fields.demo()
```