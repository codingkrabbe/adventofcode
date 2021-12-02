Sub main()
Dim a As Integer
Dim b As Integer
Dim counter As Integer
Dim valold As Integer
Dim valnew As Integer
Dim c As Integer


a = Tabelle1.UsedRange.Rows.Count
For b = 1 To a
valold = Tabelle1.Cells(b, 1) + Tabelle1.Cells(b + 1, 1) + Tabelle1.Cells(b + 2, 1)
c = b + 1
valnew = Tabelle1.Cells(c, 1) + Tabelle1.Cells(c + 1, 1) + Tabelle1.Cells(c + 2, 1)
If valnew > valold Then
counter = counter + 1
End If
Next


MsgBox (counter)
End Sub
