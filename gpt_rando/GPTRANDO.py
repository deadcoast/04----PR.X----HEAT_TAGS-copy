import os
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from typing import Any

import content
import self
from sqlalchemy import null










def find_next(self):
    """
    Finds the next occurrence of the search query and highlights it.
    """
    if self.search_query:
        self.search_index = self.text_widget.search(self.search_query, self.search_index, stopindex=tk.END)
        if self.search_index:
            self.add_search_highlight(
                self.search_index,
                f"{self.search_index}+{len(self.search_query)}c",
            )
            self.search_index = self.text_widget.index(
                f"{self.search_index}+{len(self.search_query)}c"
            )
        else:
            self.search_index = "1.0"
            self._display_message("No more occurrences found.")


def find_previous(self):
    """
    Finds the previous occurrence of the search query and highlights it.
    """
    if self.search_query:
        self.search_index = self.text_widget.search(self.search_query, self.search_index, stopindex="1.0",
                                                    backwards=True)
        if self.search_index:
            self.add_search_highlight(
                self.search_index,
                f"{self.search_index}+{len(self.search_query)}c",
            )
            self.search_index = self.text_widget.index(
                f"{self.search_index}+{len(self.search_query)}c"
            )
        else:
            self.search_index = tk.END
            self._display_message("No more occurrences found.")















self.parent = parent
self.palette = palette or {}
self.text_widget = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
self.text_widget.pack(fill=tk.BOTH, expand=True)

self.setup_text_formatting()
self.set_content(content)
self.apply_palette()

self.setup_text_formatting()
self.set_content(content)
self.apply_palette()


def setup_text_formatting(self):
    """
    Configures the various text formatting options for the Flare widget.
    """
    bold_font = font.Font(family='Courier New', size=12, weight='bold')
    italic_font = font.Font(family='Courier New', size=12, slant='italic')

    self.text_widget.tag_configure('bold', font=bold_font)
    self.text_widget.tag_configure('italic', font=italic_font)

    self.text_widget.bind('<Control-b>', self.toggle_bold)
    self.text_widget.bind('<Control-i>', self.toggle_italic)


def toggle_bold(self, event):
    """
    Toggles the bold formatting for the selected text.
    """
    self.toggle_formatting('bold')


def toggle_italic(self, event):
    """
    Toggles the italic formatting for the selected text.
    """
    self.toggle_formatting('italic')


def toggle_formatting(self, tag):
    """
    Generic method to toggle the specified text formatting tag.
    """
    start, end = self.text_widget.tag_ranges('sel')
    if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
        self.text_widget.tag_remove(tag, start, end)
    else:
        self.text_widget.tag_add(tag, start, end)


def set_content(self, content):
    """
    Sets the content of the Flare widget.
    """
    self.text_widget.delete('1.0', tk.END)
    self.text_widget.insert('1.0', content)


def get_content(self):
    """
    Retrieves the current content of the Flare widget.
    """
    return self.text_widget.get('1.0', tk.END).strip()


def apply_palette(self):
    """
    Applies the specified color palette to the Flare widget.
    """
    self.text_widget.configure(
        background=self.palette.get('secondary', '#303030'),
        foreground=self.palette.get('primary', '#505050'),
        insertbackground=self.palette.get('tertiary', '#202020')
    )


def setup_text_formatting(self):
    """
    Configures the various text formatting options for the Flare widget.
    """
    bold_font = font.Font(family='Courier New', size=12, weight='bold')
    italic_font = font.Font(family='Courier New', size=12, slant='italic')

    self.text_widget.tag_configure('bold', font=bold_font)
    self.text_widget.tag_configure('italic', font=italic_font)

    self.text_widget.bind('<Control-b>', self.toggle_bold)
    self.text_widget.bind('<Control-i>', self.toggle_italic)


def toggle_bold(self, event):
    """
    Toggles the bold formatting for the selected text.
    """
    self.toggle_formatting('bold')


def toggle_italic(self, event):
    """
    Toggles the italic formatting for the selected text.
    """
    self.toggle_formatting('italic')


def toggle_formatting(self, tag):
    """
    Generic method to toggle the specified text formatting tag.
    """
    start, end = self.text_widget.tag_ranges('sel')
    if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
        self.text_widget.tag_remove(tag, start, end)
    else:
        self.text_widget.tag_add(tag, start, end)


def set_content(self, content):
    """
    Sets the content of the Flare widget.
    """
    self.text_widget.delete('1.0', tk.END)
    self.text_widget.insert('1.0', content)


def get_content(self):
    """
    Retrieves the current content of the Flare widget.
    """
    return self.text_widget.get('1.0', tk.END).strip()


def apply_palette(self):
    """
    Applies the specified color palette to the Flare widget.
    """
    self.text_widget.configure(
        background=self.palette.get('secondary', '#303030'),
        foreground=self.palette.get('primary', '#505050'),
        insertbackground=self.palette.get('tertiary', '#202020')
    )

    import tkinter as tk
    from tkinter import font
    class InlineSearchManager:
        """
        Provides advanced inline search functionality for the HEAT UP editor.
        """

    def init(self, text_widget):
        self.text_widget = text_widget

    self.search_query = ""
    self.search_index = "1.0"
    self.search_highlights = []
    self.setup_search_bar()
    self.setup_bindings()


def setup_search_bar(self):
    """
    Creates the search bar UI elements and integrates them into the editor.
    """
    self.search_bar = tk.Frame(self.text_widget)
    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    self.search_entry = tk.Entry(self.search_bar, font=font.Font(family='Courier New', size=12))
    self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    self.search_entry.bind("<Return>", self.perform_search)

    self.search_next_button = tk.Button(self.search_bar, text="Next", command=self.find_next)
    self.search_next_button.pack(side=tk.LEFT, padx=5)

    self.search_prev_button = tk.Button(self.search_bar, text="Previous", command=self.find_previous)
    self.search_prev_button.pack(side=tk.LEFT, padx=5)

    self.search_close_button = tk.Button(self.search_bar, text="Close", command=self.hide_search_bar)
    self.search_close_button.pack(side=tk.LEFT, padx=5)


def setup_bindings(self):
    """
    Binds keyboard shortcuts for invoking the inline search functionality.
    """
    self.text_widget.bind("<Control-f>", self.prompt_search_query)


def prompt_search_query(self, event=None):
    """
    Prompts the user for a search query and initiates the search.
    """
    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    self.search_entry.focus_set()


def perform_search(self, event=None):
    """
    Performs the inline search based on the user's query.
    """
    self.search_query = self.search_entry.get()
    self.search_index = "1.0"
    self.clear_search_highlights()
    self.find_next()


def find_next(self):
    """
    Finds the next occurrence of the search query and highlights it.
    """
    if self.search_query:
        self.search_index = self.text_widget.search(self.search_query, self.search_index, stopindex=tk.END)
        if self.search_index:
            self.add_search_highlight(
                self.search_index,
                f"{self.search_index}+{len(self.search_query)}c",
            )
            self.search_index = self.text_widget.index(
                f"{self.search_index}+{len(self.search_query)}c"
            )
        else:
            self.search_index = "1.0"


def find_previous(self):
    """
    Finds the previous occurrence of the search query and highlights it.
    """
    if self.search_query:
        self.search_index = self.text_widget.search(self.search_query, self.search_index, stopindex="1.0",
                                                    backwards=True)
        if self.search_index:
            self.add_search_highlight(
                self.search_index,
                f"{self.search_index}+{len(self.search_query)}c",
            )
            self.search_index = self.text_widget.index(
                f"{self.search_index}+{len(self.search_query)}c"
            )
        else:
            self.search_index = tk.END


def add_search_highlight(self, start_index, end_index):
    """
    Adds a highlight to the search results.
    """
    self.text_widget.tag_add("search_highlight", start_index, end_index)
    self.text_widget.tag_config("search_highlight", background="yellow")
    self.search_highlights.append((start_index, end_index))


def clear_search_highlights(self):
    """
    Removes all search result highlights from the text widget.
    """
    for start_index, end_index in self.search_highlights:
        self.text_widget.tag_remove("search_highlight", start_index, end_index)
    self.search_highlights.clear()


def hide_search_bar(self):
    """
    Hides the search bar and clears the search highlights.
    """
    self.search_bar.pack_forget()
    self.clear_search_highlights()
