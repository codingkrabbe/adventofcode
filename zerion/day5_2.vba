Sub main()
Dim lines, i As Integer
Dim coordinates() As String
Dim startcor(0) As String
Dim stopcor(0) As String
lines = Tabelle2.UsedRange.Rows.Count
lines = Tabelle2.UsedRange.Rows.Count

For i = 1 To lines
    coordinates = Split(Tabelle2.Cells(i, 1), " -> ")
    Tabelle2.Cells(i, 2).NumberFormat = "@"
    Tabelle2.Cells(i, 2) = coordinates(0)
    Tabelle2.Cells(i, 3).NumberFormat = "@"
    Tabelle2.Cells(i, 3) = coordinates(1)
    coordinates = Split(Tabelle2.Cells(i, 2), ",")
    Tabelle2.Cells(i, 4) = coordinates(0) + 1
    Tabelle2.Cells(i, 5) = coordinates(1) + 1
    coordinates = Split(Tabelle2.Cells(i, 3), ",")
    Tabelle2.Cells(i, 6) = coordinates(0) + 1
    Tabelle2.Cells(i, 7) = coordinates(1) + 1
    
    'Tabelle13.Cells(i, Tabelle2.Cells(i, 4)) = Tabelle13.Cells(i, Tabelle2.Cells(i, 4)) + "1"
    
    'For a = Tabelle2.Cells(i, 4) To Tabelle2.Cells(i, 6)
    'Tabelle2.Cells(i, a) = Tabelle2.Cells(i, a) & "1"
    'Next
    counterx = 0
    countery = 0
    If Tabelle2.Cells(i, 4) = Tabelle2.Cells(i, 6) Then
        If Tabelle2.Cells(i, 5) < Tabelle2.Cells(i, 7) Then
            countery = Tabelle2.Cells(i, 7) - Tabelle2.Cells(i, 5)
       Else
            countery = Tabelle2.Cells(i, 7) - Tabelle2.Cells(i, 5)
        End If
    
        ElseIf Tabelle2.Cells(i, 5) = Tabelle2.Cells(i, 7) Then
        
        If Tabelle2.Cells(i, 4) < Tabelle2.Cells(i, 6) Then
            counterx = Tabelle2.Cells(i, 6) - Tabelle2.Cells(i, 4)
        Else
            counterx = Tabelle2.Cells(i, 6) - Tabelle2.Cells(i, 4)
        End If
    Else
            If Tabelle2.Cells(i, 4) < Tabelle2.Cells(i, 6) Then
            counterx = Tabelle2.Cells(i, 6) - Tabelle2.Cells(i, 4)
        Else
            counterx = Tabelle2.Cells(i, 6) - Tabelle2.Cells(i, 4)
        End If
            If Tabelle2.Cells(i, 5) < Tabelle2.Cells(i, 7) Then
            countery = Tabelle2.Cells(i, 7) - Tabelle2.Cells(i, 5)
       Else
            countery = Tabelle2.Cells(i, 7) - Tabelle2.Cells(i, 5)
        End If
    
    End If
    Z = 0
    If countery > 0 And counterx = 0 Then
        For k = Tabelle2.Cells(i, 5) To Tabelle2.Cells(i, 7)
            Tabelle13.Cells(Tabelle2.Cells(i, 5) + Z, Tabelle2.Cells(i, 4)) = CInt(Tabelle13.Cells(Tabelle2.Cells(i, 5) + Z, Tabelle2.Cells(i, 4))) + 1
            Z = Z + 1
        Next
    ElseIf countery < 0 And counterx = 0 Then
        For k = Tabelle2.Cells(i, 7) To Tabelle2.Cells(i, 5)
            Tabelle13.Cells(Tabelle2.Cells(i, 7) + Z, Tabelle2.Cells(i, 4)) = CInt(Tabelle13.Cells(Tabelle2.Cells(i, 7) + Z, Tabelle2.Cells(i, 4))) + 1
            Z = Z + 1
        Next
    ElseIf counterx > 0 And countery = 0 Then
        For k = Tabelle2.Cells(i, 4) To Tabelle2.Cells(i, 6)
            Tabelle13.Cells(Tabelle2.Cells(i, 5), Tabelle2.Cells(i, 4) + Z) = CInt(Tabelle13.Cells(Tabelle2.Cells(i, 5), Tabelle2.Cells(i, 4) + Z)) + 1
            Z = Z + 1
        Next
    ElseIf counterx < 0 And countery = 0 Then
        For k = Tabelle2.Cells(i, 6) To Tabelle2.Cells(i, 4)
            Tabelle13.Cells(Tabelle2.Cells(i, 5), Tabelle2.Cells(i, 6) + Z) = CInt(Tabelle13.Cells(Tabelle2.Cells(i, 5), Tabelle2.Cells(i, 6) + Z)) + 1
            Z = Z + 1
        Next
    End If
    
    If countery > 0 And counterx > 0 Then
                For k = Tabelle2.Cells(i, 5) To Tabelle2.Cells(i, 7)
            Tabelle13.Cells(Tabelle2.Cells(i, 5) + Z, Tabelle2.Cells(i, 4) + Z) = CInt(Tabelle13.Cells(Tabelle2.Cells(i, 5) + Z, Tabelle2.Cells(i, 4) + Z)) + 1
            Z = Z + 1
        Next
    ElseIf countery > 0 And counterx < 0 Then
                    For k = Tabelle2.Cells(i, 5) To Tabelle2.Cells(i, 7)
            Tabelle13.Cells(Tabelle2.Cells(i, 7) - Z, Tabelle2.Cells(i, 6) + Z) = CInt(Tabelle13.Cells(Tabelle2.Cells(i, 7) - Z, Tabelle2.Cells(i, 6) + Z)) + 1
            Z = Z + 1
        Next
    ElseIf countery < 0 And counterx < 0 Then
            For k = Tabelle2.Cells(i, 7) To Tabelle2.Cells(i, 5)
            Tabelle13.Cells(Tabelle2.Cells(i, 7) + Z, Tabelle2.Cells(i, 6) + Z) = CInt(Tabelle13.Cells(Tabelle2.Cells(i, 7) + Z, Tabelle2.Cells(i, 6) + Z)) + 1
            Z = Z + 1
        Next
    ElseIf countery < 0 And counterx > 0 Then
                For k = Tabelle2.Cells(i, 7) To Tabelle2.Cells(i, 5)
            Tabelle13.Cells(Tabelle2.Cells(i, 7) + Z, Tabelle2.Cells(i, 6) - Z) = CInt(Tabelle13.Cells(Tabelle2.Cells(i, 7) + Z, Tabelle2.Cells(i, 6) - Z)) + 1
            Z = Z + 1
        Next
    End If
           
Next
For i = 1 To 1008
    For n = 1 To 1008
        If Tabelle13.Cells(i, n) > 1 Then
        c = c + 1
        End If
    Next
Next
MsgBox (c)
End Sub
