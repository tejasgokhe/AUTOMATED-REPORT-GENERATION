import csv
from collections import defaultdict
from fpdf import FPDF

#ANALYZE CSV DATA
data = defaultdict(list)

with open('marks.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Name']
        marks = int(row['Marks'])
        data[name].append(marks)

#CALCULATE AVERAGE
averages = {}
for name, marks_list in data.items():
    avg = sum(marks_list) / len(marks_list)
    averages[name] = avg

#CREATE PDF REPORT
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt=" Student Marks Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)
for name, avg in averages.items():
    pdf.cell(200, 10, txt=f"{name} - Average Marks: {avg:.2f}", ln=True)

#SAVE PDF
pdf.output("Student_Report.pdf")
print("✅ Report generated as 'Student_Report.pdf'")
