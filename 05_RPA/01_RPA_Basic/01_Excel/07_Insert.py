from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8 번재 줄이 비어짐
# ws.insert_rows(8, 5) # 8번째 줄 위에 5줄이 삽입됨

# ws.insert_cols(2) # B번째 열이 비어짐
# ws.insert_cols(2, 3) # B번째 열 부터 3칸이 비어줌 


# wb.save("sample_insert_rows.xlsx")
wb.save("sample_insert_cols.xlsx")