# Doc demo, target MD

> This is a demo of class 'Doc' which allows to build document with a set a basic instructions.

## How to use

One initialized, the Doc offers a set of writing instructions:

- [header](#headers) : Create a header at a certain level (starting from 0)
- [para](#para) : Create a simple paragraph
- descr : Write text as description
- new_line : Write a new line
- sepa : Write an horizontal separator
- bullets : List of bullet points
- source : Write source code

## Headers

Headers are created with `doc.header` method. The level start from 0 for the main top title
This section uses the level 1 style. See below for upper levels:

### Level 2

#### Level 3

##### Level 4

``` python
doc.header(title, level=0)
```
## Para

Text is written with `doc.para` method.
The paragraph uses the current 'bullets' context. see bullets

``` python
doc.para(text, new_line=True)
```
### Arguments:

- text (str) : Text to write
- new_line (bool=True) : Add an additional new line at the end

## Descr

The 'doc.descr', method use the '>' bullet for the paragraphs.

## Bullet points

Bullet points allow to write list with bullet points or numbers:

- First item : Item description
- Second item : Items of a list can simple text or a couple (item, description)
- Not described item
- With a sub list : Lists can be nested
  1. Order item : Example of an order list
  1. Other ordered items : Which follows the same principe
  1. Not described item
- Item : Back to the main list

  Text can be added to a bullet point as a complementary paragraph to the current bullet.


End of demo