import tkinter as tk
from tkinter import ttk

class FlexBoxPage(tk.Frame):
    def __init__(self, parent, rows=10, columns=10):
        super().__init__(parent)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.grid(column=0, row=0, sticky="nsew")
        for i in range(rows):
            self.grid_rowconfigure(i, weight=1, uniform="grid")
        for i in range(columns):
            self.grid_columnconfigure(i, weight=1, uniform="grid")

        self.currentframe = 0
        self.currentwidget = 0
        self.frames = []
        self.widgets = []
    
    
    def place_widget(self, widgetfunc, row, column, rowspan=1, columnspan=1, relx=0, rely=0, relwidth=1, relheight=1, margin=0, **kwargs):
        made = False
        #widget manager logic
        for frame in self.frames:
            if frame.row == row and frame.column == column and frame.rowspan == rowspan and frame.columnspan == columnspan:
                widget = _ManagedWidget(frame, self.currentwidget, widgetfunc, column, row, columnspan, rowspan, relx, rely, relwidth, relheight, margin, **kwargs)
                self.currentwidget += 1
                made = True
        if made == False:
            widgetframe = _ManagedFrame(self, self.currentframe, column, row, columnspan, rowspan)
            self.currentframe += 1
            widget = _ManagedWidget(widgetframe, self.currentwidget, widgetfunc, column, row, columnspan, rowspan, relx, rely, relwidth, relheight, margin, **kwargs)
            self.currentwidget += 1
        return widget.id
    



class _ManagedWidget():
    def __init__(self, parent, id, widgetfunc, column, row, columnspan, rowspan, relx, rely, relwidth, relheight, margin, **kwargs):
        margin = self._normalisemargin(margin)
        self.placed_widget = widgetfunc(parent.frame, **kwargs)
        self.placed_widget.place(relx=margin[3], rely=margin[0], relwidth=1-margin[1]-margin[3], relheight=1-margin[0]-margin[2])
        self.id = id
        self.parent = parent
        self.column = column
        self.row = row
        self.columnspan = columnspan
        self.rowspan = rowspan
        parent.addchild({"id":self.id, "widget":self.placed_widget})

    def _normalisemargin(self, margin):
        try:
            length = len(margin)
            if length == 4:
                return tuple(margin)
            if length == 3:
                return (margin[0], margin[1], margin[2], margin[1])
            if length == 2:
                return (margin[0], margin[1], margin[0], margin[1])
        except TypeError:
            return (margin, margin, margin, margin)

class _ManagedFrame():
    def __init__(self, parent, id, column, row, columnspan, rowspan):
        self.frame = tk.Frame(parent)
        self.frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky="nsew")
        self.frame.grid_propagate(False)
        self.id = id
        self.children = []
        self.column= column
        self.row = row
        self.columnspan = columnspan
        self.rowspan = rowspan
        parent.currentframe += 1

    def addchild(self, child):
        self.children.append(child)
    
    def info(self):
        return {
            "id": self.id,
            "children": self.children,
            "column": self.column,
            "row": self.row,
            "columnspan": self.columnspan,
            "rowspan": self.rowspan,
            "frame": self.frame
        }


def StrictGridFrame(parent, column=0, row=0, columnspan=1, rowspan=1):
    frame = tk.Frame(parent)
    frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky="nsew")
    frame.grid_propagate(False)
    return frame

def FullPageGrid(parent, rows=10, columns=10):
    parent.grid(column=0, row=0, sticky="nsew")
    for i in range(rows):
        parent.grid_rowconfigure(i, weight=1, uniform="grid")
    for i in range(columns):
        parent.grid_columnconfigure(i, weight=1, uniform="grid")

