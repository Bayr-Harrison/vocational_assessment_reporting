# Create and download Excel file
def create_excel(data, start_date, end_date):
    col_names = [
        'Batch Number', 'Batch Type', 'IATC ID', 'Name', 'Class',
        'Task', 'Score', 'Attendance Status', 'Task Date', 'Sending Date'
    ]
    wb = Workbook()
    ws = wb.active
    ws.title = "Practical Task Results"

    # Write headers
    for col_num, header in enumerate(col_names, 1):
        cell = ws.cell(row=1, column=col_num, value=header)
        cell.fill = PatternFill(start_color="8DE7D3", end_color="8DE7D3", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.font = Font(bold=True)

    # Write data rows
    for row_num, row_data in enumerate(data, 2):
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_num, column=col_num, value=value)
            cell.alignment = Alignment(horizontal="center", vertical="center")

            # Apply conditional formatting
            if col_num == 7:  # Column G ('Score')
                if value is None or value == '':
                    cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")  # Light grey

            if col_num == 8:  # Column H ('Attendance Status')
                if value == 'ABSENT':
                    cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")  # Light grey

            if col_num == 2:  # Column B ('Batch Type')
                if value == 'REGULAR':
                    cell.fill = PatternFill(start_color="DAE8FC", end_color="DAE8FC", fill_type="solid")  # Light blue
                elif value == 'REMEDIAL':
                    cell.fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")  # Light yellow

    # Adjust column widths
    for col in ws.columns:
        max_length = max(len(str(cell.value)) for cell in col if cell.value)
        ws.column_dimensions[get_column_letter(col[0].column)].width = max_length + 2

    # Apply filters and borders
    ws.auto_filter.ref = ws.dimensions
    thin_border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=len(col_names)):
        for cell in row:
            cell.border = thin_border

    # Save to BytesIO
    output = BytesIO()
    wb.save(output)
    output.seek(0)
    return output
