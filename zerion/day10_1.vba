Sub main()
Dim lines, i, b As Integer
Dim positive() As String
lines = Tabelle1.UsedRange.Rows.Count
For i = 1 To lines
    ReDim Value(Len(Tabelle1.Cells(i, 1)))
    For a = 1 To Len(Tabelle1.Cells(i, 1))
        b = a - 1
        Value(b) = Mid(Tabelle1.Cells(i, 1), a, 1)
        Tabelle1.Cells(i, a + 1) = Value(b)
    Next
    k = 1
    j = 0
     Skip = 0
    For o = 2 To Len(Tabelle1.Cells(i, 1)) + 1
        If Tabelle1.Cells(i, o) = "(" Or Tabelle1.Cells(i, o) = "{" Or Tabelle1.Cells(i, o) = "[" Or Tabelle1.Cells(i, o) = "<" Then
        ReDim Preserve positive(j)
            positive(j) = Tabelle1.Cells(i, o)
            j = j + 1
        ElseIf Tabelle1.Cells(i, o) = ")" Then
            If Not (positive(j - 1) = "(") Then
            Count = Count + 3
            Skip = 1
Else
ReDim Preserve positive(j - 1)
j = j - 1
            End If
                    ElseIf Tabelle1.Cells(i, o) = "}" Then
                    If Not (positive(j - 1) = "{") Then
            Count = Count + 1197
  Skip = 1
Else
ReDim Preserve positive(j - 1)
j = j - 1
            End If
        ElseIf Tabelle1.Cells(i, o) = "]" Then
                    If Not (positive(j - 1) = "[") Then
            Count = Count + 57
 Skip = 1
Else
ReDim Preserve positive(j - 1)
j = j - 1
            End If
        ElseIf Tabelle1.Cells(i, o) = ">" Then
                    If Not (positive(j - 1) = "<") Then
            Count = Count + 25137
 Skip = 1
Else
ReDim Preserve positive(j - 1)
j = j - 1
            End If
                    End If
    If Skip = 1 Then
        Exit For
                End If
    Next
Next
MsgBox (Count)
End Sub
