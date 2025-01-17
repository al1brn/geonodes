# counters

[Source Code](../demos/counters.py)

The elementay digit can be either digital or analogic.

A digital figure is made of 7 elementary segments with a different material
depending on its state : ON or OFF.

A digital clock is built with 4 digits.

A analog figure is built from font. The value displayed is the floor part
of the value passed to the modifier. The figure is then slightly moved
to simulatue wheel rotation.

A counter is made of a variable number of analog figure.


> [!NOTE]
> Modifiers:
> - Digit
> - Digital Clock
> - Digital Counter
> - Figure
> - Wheels Counter

``` python
from geonodes.demos import counters

counters.demo()
```