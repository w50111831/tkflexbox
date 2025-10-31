# tkflexbox

A python library to implement flexbox like functionality to tkinter.

Latest release:
I have fully recoded the internal engine so that now I store all details about widgets as well as their ID for easy manipulation.
I should now be able to start adding wrapping and auto placement :D

<!-- ROADMAP -->
## Roadmap

- [x] Create dynamic grid sizing engine base thing
- [x] Add margin paremeter functionality
- [x] Create place_widget function 
- [ ] Add direction parameter ('row' | 'column')
- [ ] Dynanmic wrapping to start new rows
    - [x] Track widget cells
    - [x] Track widget size
    - [ ] Create a declarative API such as flex.add(widget, grow=2, shrink=1, basis=0.3, align='center') rather than using place_widget
    - [ ] Recalculate layout based on window size
    - [ ] scrolling integration if can't fit content on page
- [ ] Alignment (justify-content / align-items)
- [ ] Gap system (gap, row_gap, column_gap)
- [ ] Z-index property



See the [open issues](https://github.com/w50111831/tkflexbox/issues) for a full list of proposed features (and known issues).

## install
```bash
pip install tkflexbox
```

## example usage
```python
import tkflexbox
from tkflexbox import FlexBoxFrame
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('800x800')
page = FlexBoxPage(root, rows=5, columns=5)
button1 = page.place_widget(ttk.Button, row=1, column=2, columnspan=2, text='Button 1', margin=(0.1, 0.05, 0.05, 0.2))
label1 = page.place_widget(ttk.Label, row=0, column=0, text=f'Button 1\'s id is {button1}')
label2 = page.place_widget(ttk.Label, row=1, column=0, text=f'Label 1\'s id is {label1}')


root.mainloop()

```


# Wiki:
## FlexBoxPage class (recommended):
When using tkflexbox I recommend creating a class for each page in your app, and having that class inherit FlexBoxFrame and then call super().__init__()

Since FlexBoxPage already inherits tk.Frame you can then just use this new class as a Frame/Page as you normally would in tkinter, but with the ease of strictly expanding elements to create a nice reactive application.


To create a FlexBoxPage object, use 
```python
flexboxpage = FlexBoxPage(parent, rows=10, columns=10)
```
This creates a Frame/Page that is split up evenly into rows and columns. This grid will expand to fill the current page, and so will elements inside making the page reactive.

## Methods:

### place_widget
```python
flexboxpage.place_widget(widget, row, column, rowspan=1, columnspan=1, relx=0, rely=0, relwidth=1, relheight=1, margin=0, **kwargs)
```
This places a widget into a strict box. The strict box's area is defined using row, column, rowspan and columnspan.
The widget will fill this frame by default but by using the margin feature you choose to only fill a portion of this subframe.
The method also returns the widget so that you can modify it using normal tkinter methods.
### Example:
```python
MainMenuButton = flexboxpage.place_widget(ttk.Button, row=1, column=2, columnspan=2, text='Hello world', margin=(0.1, 0.05, 0.05, 0.2))
```

### StrictGridFrame (deprecated for now, I might add back in future.)
```python
flexboxpage.StrictGridFrame(self, column=0, row=0, columnspan=1, rowspan=1)
```
This creates a subFrame for you to use however you wish. If adding a widget I would recommend using place_widget but there will be times that you must create your own frame and this is an easier way of doing so rather than using my other function not owned by the page class to do so.

This function also returns the Frame so that it can be stored/modified later.
### Example:
```python
MyFrame = flexboxframe.StrictGridFrame(self, column=2, row=4, columnspan=5, rowspan=1)
```

## Functions
> [!WARNING]  
> It is recommended to use the FlexBoxFrame class as this better follows OOP principles and will result in cleaner and possibly more performant code. Only use external functions for rapid prototyping or if you can't use OOP for some reason.

### StrictGridFrame
```python
flexboxframe.StrictGridFrame(self, column=0, row=0, columnspan=1, rowspan=1)
```
This creates a subFrame for you to use however you wish. Returns the frame to be stored/modified later.
### Example:
```python
MyFrame = StrictGridFrame(self, column=2, row=4, columnspan=5, rowspan=1)
```

### FullPageGrid
```python
FullPageGrid(parent, rows=10, columns=10)
```
Creates rows amount of equal rows and columns amount of equal columns in the parent page. All are weighted and so expand to fill the page.
### Example:
```python
root = tk.Tk()

FullPageGrid(root, rows=10, columns=10)
```
Note that this does NOT return the page, only modifies the existing one.
