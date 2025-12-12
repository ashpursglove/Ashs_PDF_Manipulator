# """
# modules/theme.py

# Dark-blue + vibrant-orange Qt stylesheet shared across the app.

# This keeps the look consistent across widgets, tabs, buttons, etc.
# """

# VIBRANT_ORANGE = "#FF7A00"
# DARK_BG = "#050B1A"
# MID_BG = "#0B1020"
# LIGHT_TEXT = "#F5F5F5"
# MUTED_TEXT = "#C0C4D0"
# BORDER_COLOR = "#20263A"
# INPUT_BG = "#101627"


# DARK_BLUE_ORANGE_QSS = f"""
# /* ------------------------
#    GENERAL APPLICATION
# -------------------------*/
# QWidget {{
#     background-color: {DARK_BG};
#     color: {LIGHT_TEXT};
#     font-size: 13px;
#     font-family: "Segoe UI", "Roboto", "Arial";
# }}

# QMainWindow {{
#     background-color: {DARK_BG};
# }}

# QLabel {{
#     color: {LIGHT_TEXT};
# }}

# QLineEdit, QSpinBox {{
#     background-color: {INPUT_BG};
#     color: {LIGHT_TEXT};
#     border: 1px solid {BORDER_COLOR};
#     border-radius: 4px;
#     padding: 4px 6px;
#     selection-background-color: {VIBRANT_ORANGE};
# }}

# QLineEdit:disabled, QSpinBox:disabled {{
#     color: {MUTED_TEXT};
#     background-color: #060A13;
# }}

# QPushButton {{
#     background-color: {VIBRANT_ORANGE};
#     color: #000000;
#     border-radius: 4px;
#     padding: 6px 10px;
#     font-weight: 600;
# }}

# QPushButton::hover {{
#     background-color: #FF9A33;
# }}

# QPushButton::disabled {{
#     background-color: #444444;
#     color: #888888;
# }}

# QGroupBox {{
#     border: 1px solid {BORDER_COLOR};
#     border-radius: 6px;
#     margin-top: 16px;
#     padding: 8px 10px;
# }}

# QGroupBox::title {{
#     subcontrol-origin: margin;
#     left: 12px;
#     padding: 0 4px 0 4px;
#     color: {MUTED_TEXT};
#     background-color: {DARK_BG};
# }}

# /* ------------------------
#    TABS
# -------------------------*/
# QTabWidget::pane {{
#     border: 1px solid {BORDER_COLOR};
#     background: {MID_BG};
#     border-radius: 4px;
# }}

# QTabBar::tab {{
#     background: {MID_BG};
#     color: {MUTED_TEXT};
#     padding: 6px 12px;
#     border-top-left-radius: 4px;
#     border-top-right-radius: 4px;
#     margin-right: 2px;
# }}

# QTabBar::tab:selected {{
#     background: {DARK_BG};
#     color: {LIGHT_TEXT};
#     font-weight: 600;
# }}

# QTabBar::tab:hover {{
#     background: #151C30;
# }}

# /* ------------------------
#    SCROLLBARS
# -------------------------*/
# QScrollArea {{
#     background-color: {DARK_BG};
#     border: none;
# }}

# QScrollBar:vertical {{
#     background: {MID_BG};
#     width: 12px;
#     margin: 0px;
#     border-radius: 5px;
# }}

# QScrollBar::handle:vertical {{
#     background: {VIBRANT_ORANGE};
#     min-height: 20px;
#     border-radius: 5px;
# }}

# QScrollBar::add-line:vertical,
# QScrollBar::sub-line:vertical {{
#     height: 0px;
# }}

# QScrollBar:horizontal {{
#     background: {MID_BG};
#     height: 12px;
#     margin: 0px;
#     border-radius: 5px;
# }}

# QScrollBar::handle:horizontal {{
#     background: {VIBRANT_ORANGE};
#     min-width: 20px;
#     border-radius: 5px;
# }}

# QScrollBar::add-line:horizontal,
# QScrollBar::sub-line:horizontal {{
#     width: 0px;
# }}

# /* ------------------------
#    STATUS LABEL
# -------------------------*/
# QLabel#statusLabel {{
#     color: {MUTED_TEXT};
#     font-size: 11px;
# }}
# """












"""
modules/theme.py

Dark-blue + vibrant-orange Qt stylesheet shared across the app.

This keeps the look consistent across widgets, tabs, buttons, etc.
"""

VIBRANT_ORANGE = "#FF7A00"
DARK_BG = "#050B1A"
MID_BG = "#0B1020"
LIGHT_TEXT = "#F5F5F5"
MUTED_TEXT = "#C0C4D0"
BORDER_COLOR = "#20263A"
INPUT_BG = "#101627"


DARK_BLUE_ORANGE_QSS = f"""
/* ------------------------
   GENERAL APPLICATION
-------------------------*/
QWidget {{
    background-color: {DARK_BG};
    color: {LIGHT_TEXT};
    font-size: 13px;
    font-family: "Segoe UI", "Roboto", "Arial";
}}

QMainWindow {{
    background-color: {DARK_BG};
}}

QLabel {{
    color: {LIGHT_TEXT};
}}

QLineEdit, QSpinBox {{
    background-color: {INPUT_BG};
    color: {LIGHT_TEXT};
    border: 1px solid {BORDER_COLOR};
    border-radius: 4px;
    padding: 4px 6px;
    selection-background-color: {VIBRANT_ORANGE};
}}

QLineEdit:disabled, QSpinBox:disabled {{
    color: {MUTED_TEXT};
    background-color: #060A13;
}}

QPushButton {{
    background-color: {VIBRANT_ORANGE};
    color: #000000;
    border-radius: 4px;
    padding: 6px 10px;
    font-weight: 600;
}}

QPushButton::hover {{
    background-color: #FF9A33;
}}

QPushButton::disabled {{
    background-color: #444444;
    color: #888888;
}}

QGroupBox {{
    border: 1px solid {BORDER_COLOR};
    border-radius: 6px;
    margin-top: 16px;
    padding: 8px 10px;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 4px 0 4px;
    color: {MUTED_TEXT};
    background-color: {DARK_BG};
}}

/* ------------------------
   TABS
-------------------------*/
QTabWidget::pane {{
    border: 1px solid {BORDER_COLOR};
    background: {MID_BG};
    border-radius: 4px;
}}

QTabBar::tab {{
    background: {MID_BG};
    color: {MUTED_TEXT};
    padding: 6px 12px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    margin-right: 2px;
    min-width: 130px;  /* Make tabs wide enough for 'Merge PDFs' / 'Split PDF' */
}}

QTabBar::tab:selected {{
    background: {DARK_BG};
    color: {LIGHT_TEXT};
    font-weight: 600;
}}

QTabBar::tab:hover {{
    background: #151C30;
}}

/* ------------------------
   SCROLLBARS
-------------------------*/
QScrollArea {{
    background-color: {DARK_BG};
    border: none;
}}

QScrollBar:vertical {{
    background: {MID_BG};
    width: 12px;
    margin: 0px;
    border-radius: 5px;
}}

QScrollBar::handle:vertical {{
    background: {VIBRANT_ORANGE};
    min-height: 20px;
    border-radius: 5px;
}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QScrollBar:horizontal {{
    background: {MID_BG};
    height: 12px;
    margin: 0px;
    border-radius: 5px;
}}

QScrollBar::handle:horizontal {{
    background: {VIBRANT_ORANGE};
    min-width: 20px;
    border-radius: 5px;
}}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {{
    width: 0px;
}}

/* ------------------------
   STATUS LABEL
-------------------------*/
QLabel#statusLabel {{
    color: {MUTED_TEXT};
    font-size: 11px;
}}
"""
