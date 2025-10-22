# tkflexbox

A python library to implement flexbox like functionality to tkinter.


## install
```bash
pip install tkflexbox
```

## example usage
```bash
import tkinter as tk
from tkinter import ttk
from tkflexbox import FlexBoxFrame

root = tk.Tk()
page = FlexBoxFrame(root, rows=5, columns=5)
page.place_widget(ttk.Button, row=1, column=3, columnspan=2, text='Hello world')

root.mainloop()

```
