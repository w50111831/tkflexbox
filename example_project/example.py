"""
tkflexbox Showcase Project
--------------------------
A complete demonstration of the tkflexbox library and its FlexBoxFrame class.

Features:
- Fully responsive grid layout using FlexBoxFrame
- Demonstrates `place_widget` for nested components
- Visual grid guide showing grid mechanism
- Text and interactive elements showing flexibility and scalability

Usage:
1. Install tkflexbox (ensure it's in the same directory or installed via pip)
2. Run: python main.py
"""

import tkinter as tk
from tkinter import ttk
from tkflexbox import FlexBoxFrame


class ShowcaseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tkflexbox Showcase")
        self.geometry("900x600")
        self.configure(bg="#1e1e1e")

        # Create main FlexBox layout
        main = FlexBoxFrame(self, rows=10, columns=10)

        # Header
        header = main.place_widget(
            tk.Frame, row=0, column=0, rowspan=1, columnspan=10, margin=(0.02, 0.02)
        )
        self.build_header(header)

        # Left panel - features
        sidebar = main.place_widget(
            tk.Frame, row=1, column=0, rowspan=9, columnspan=3, margin=(0.02, 0.02, 0.02, 0.02)
        )
        self.build_sidebar(sidebar)

        # Main content - demo area
        demo = main.place_widget(
            tk.Frame, row=1, column=3, rowspan=9, columnspan=7, margin=(0.02, 0.02, 0.02, 0.0)
        )
        self.build_demo_area(demo)

    # -------------------
    # Header
    # -------------------
    def build_header(self, frame):
        flex = FlexBoxFrame(frame, rows=1, columns=10)
        title = flex.place_widget(
            tk.Label,
            row=0,
            column=0,
            columnspan=10,
            margin=(0, 0),
            text="tkflexbox Showcase",
            bg="#2d2d2d",
            fg="white",
            font=("Segoe UI", 20, "bold"),
        )

    # -------------------
    # Sidebar
    # -------------------
    def build_sidebar(self, frame):
        flex = FlexBoxFrame(frame, rows=6, columns=1)

        title = flex.place_widget(
            tk.Label,
            row=0,
            column=0,
            text="Features",
            bg="#2b2b2b",
            fg="white",
            font=("Segoe UI", 14, "bold"),
        )

        desc = [
            "✔ Responsive grid layout",
            "✔ Unified placement via place_widget()",
            "✔ Margin handling and nesting",
            "✔ Perfect alignment control",
            "✔ Easy to combine with ttk widgets",
            "✔ Flexible scaling & propagation",
        ]

        for i, text in enumerate(desc, start=1):
            flex.place_widget(
                tk.Label,
                row=i,
                column=0,
                text=text,
                anchor="w",
                bg="#1e1e1e",
                fg="white",
                font=("Segoe UI", 10),
                margin=(0.01, 0.02),
            )

    # -------------------
    # Demo Area
    # -------------------
    def build_demo_area(self, frame):
        flex = FlexBoxFrame(frame, rows=10, columns=10)

        # Grid visualization toggle
        info_label = flex.place_widget(
            tk.Label,
            row=0,
            column=0,
            columnspan=10,
            margin=(0.01, 0.02),
            text="Grid Visualization (10x10)",
            bg="#2d2d2d",
            fg="white",
            font=("Segoe UI", 12, "bold"),
        )

        # Draw light grid lines to visualize layout
        for r in range(1, 10):
            for c in range(10):
                flex.place_widget(
                    tk.Frame,
                    row=r,
                    column=c,
                    margin=(0.005, 0.005),
                    bg="#3a3a3a",
                )

        # Example content box to show flexibility
        sample_box = flex.place_widget(
            tk.Frame,
            row=3,
            column=2,
            rowspan=4,
            columnspan=6,
            margin=(0.01, 0.01),
            bg="#0078d7",
        )

        inner = FlexBoxFrame(sample_box, rows=3, columns=3)
        inner.place_widget(
            tk.Label,
            row=1,
            column=1,
            text="Nested FlexBoxFrame\nCentered Content",
            bg="#0078d7",
            fg="white",
            font=("Segoe UI", 11),
        )


if __name__ == "__main__":
    ShowcaseApp().mainloop()
