from reportlab.platypus import SimpleDocTemplate
# Flowable
from reportlab.platypus import Paragraph, Image, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
import os

fruit = {
    "strawberries": 5,
    "oak": 4,
    "apples": 2,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

# Initializing the file
report = SimpleDocTemplate(os.getcwd() + r"\\report.pdf")
styles = getSampleStyleSheet()
# Header of the file
report_title = Paragraph("My fruits", styles["h1"])

# Adding the table to the file (list-of-lists)
table_data = []
for k, c in fruit.items():
    table_data.append([k, c])

# (Font), (start), (end), (width of the line), (color)
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# Pie chart in PDF file report
report_pie = Pie()

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

# Building the PDF file
report.build([report_title, report_table, report_chart])
