Sub main()
Dim polymer() As String
Dim polymerintro() As String
Dim i, lines As Integer
lines = Tabelle10.UsedRange.Rows.Count


ReDim polymer(Len(Tabelle10.Cells(1, 1)) - 1)
    For a = 1 To Len(Tabelle10.Cells(1, 1))
        b = a - 1
        
        polymer(b) = Mid(Tabelle10.Cells(1, 1), a, 1)
        Tabelle11.Cells(a, 1) = polymer(b)
    Next
For i = 3 To lines
    polymerintro = Split(Tabelle10.Cells(i, 1), " -> ")
    Tabelle10.Cells(i, 2) = polymerintro(0)
    Tabelle10.Cells(i, 3) = polymerintro(1)
Next

For d = 1 To 10

polact = 1
polline = Tabelle11.UsedRange.Rows.Count
For i = 1 To polline
    If i = 1 Then
    polcomb = Tabelle11.Cells(i, 1) & Tabelle11.Cells(i + 1, 1)
    For v = 3 To lines
        If polcomb = Tabelle10.Cells(v, 2) Then
            Tabelle11.Cells(i + 1, 1).EntireRow.Insert
            Tabelle11.Cells(i + 1, 1) = Tabelle10.Cells(v, 3)
        End If
     Next
    Else
    polact = polact + 2
    polcomb = Tabelle11.Cells(polact, 1) & Tabelle11.Cells(polact + 1, 1)
    For v = 3 To lines
        If polcomb = Tabelle10.Cells(v, 2) Then
            Tabelle11.Cells(polact + 1, 1).EntireRow.Insert
            Tabelle11.Cells(polact + 1, 1) = Tabelle10.Cells(v, 3)
        End If
     Next
    End If

Next
Next


g = 1
For r = 1 To Tabelle11.UsedRange.Rows.Count
found = 0
    If r = 1 Then
        Tabelle11.Cells(g, 2) = Tabelle11.Cells(g, 1)
        Tabelle11.Cells(g, 3) = Tabelle11.Cells(g, 3) + 1
    Else
    For e = 1 To g
        If Tabelle11.Cells(e, 2) = Tabelle11.Cells(r, 1) Then
        Tabelle11.Cells(e, 3) = Tabelle11.Cells(e, 3) + 1
        found = 1
        End If
    Next
        If found = 0 Then
        Tabelle11.Cells(g + 1, 2) = Tabelle11.Cells(r, 1)
        Tabelle11.Cells(g + 1, 3) = Tabelle11.Cells(g + 1, 3) + 1
        g = g + 1
        End If
End If
Next

low = Tabelle11.UsedRange.Rows.Count
For t = 1 To g
    If high < Tabelle11.Cells(t, 3) Then
        high = Tabelle11.Cells(t, 3)
    End If
    If low > Tabelle11.Cells(t, 3) Then
     low = Tabelle11.Cells(t, 3)
    End If
Next
    result = high - low
    MsgBox (result)
End Sub
