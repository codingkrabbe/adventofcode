Sub main()
Dim cooridnates() As String
Dim i, lines As Integer
Tabelle8.Range("a1:XFD10000").Clear
lines = Tabelle7.UsedRange.Rows.Count
For i = 1 To lines

    coordinates = Split(Tabelle7.Cells(i, 1), ",")
    Tabelle8.Cells(CInt(coordinates(1) + 1), CInt(coordinates(0)) + 1) = "X"
    If CInt(coordinates(0)) + 1 > highcell Then
        highcell = CInt(coordinates(0)) + 1
    End If
    If CInt(coordinates(1)) + 1 > highline Then
    highline = CInt(coordinates(1)) + 1
    End If
    If Not Tabelle7.Cells(i, 2) = "" Then
    fold = Split(Tabelle7.Cells(i, 2), "=")
    Tabelle7.Cells(i, 3) = Right(fold(0), 1)
    Tabelle7.Cells(i, 4) = fold(1) + 1
    lastline = i
    End If
Next
For i = 1 To lastline
        If Tabelle7.Cells(i, 3) = "x" Then
        col = 1

            For o = Tabelle7.Cells(i, 4) To highcell
                    For k = 1 To highline
                    If Tabelle8.Cells(k, o) = "X" Then
                    Tabelle8.Cells(k, Tabelle7.Cells(i, 4) - (col) + 1) = "X"
                    Tabelle8.Cells(k, o) = ""
                    End If
                Next
                col = col + 1
            Next
        End If
        If Tabelle7.Cells(i, 3) = "y" Then
        Rowli = 1
            For o = Tabelle7.Cells(i, 4) To highline
                    For k = 1 To highcell
                    If Tabelle8.Cells(o, k) = "X" Then
                    Tabelle8.Cells(Tabelle7.Cells(i, 4) - (Rowli) + 1, k) = "X"
                    Tabelle8.Cells(o, k) = ""
                    End If
                Next
                Rowli = Rowli + 1
            Next
        End If
Next
End Sub
