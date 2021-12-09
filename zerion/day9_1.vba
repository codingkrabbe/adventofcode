Sub main()
Dim lines, i, a, b As Integer
Dim value() As String
Dim line As String
lines = Tabelle4.UsedRange.Rows.Count
For i = 1 To lines
    ReDim value(99)
    For a = 1 To Len(Tabelle4.Cells(i, 1))
        b = a - 1
        value(b) = Mid(Tabelle4.Cells(i, 1), a, 1)
        Tabelle4.Cells(i, a + 1) = value(b)
    Next
Next
For i = 1 To lines
    For a = 2 To 101
        If i = 1 Then
            If a = 2 Then
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a + 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i + 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
            ElseIf a = 101 Then
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a - 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i + 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
            Else
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a - 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a + 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i + 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
            End If
        ElseIf i = 100 Then
            If a = 2 Then
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a + 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i - 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
            ElseIf a = 101 Then
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a - 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i - 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
            Else
    
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a - 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a + 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i - 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
            End If
    
    
        Else
            If a = 2 Then
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a + 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i - 1, a) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i + 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
            ElseIf a = 101 Then
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a - 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i - 1, a) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i + 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
            Else
    
                If Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a - 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i, a + 1) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i - 1, a) And Tabelle4.Cells(i, a) < Tabelle4.Cells(i + 1, a) Then
                    lavalow = lavalow + Tabelle4.Cells(i, a) + 1
                End If
    
            End If
        End If
    Next
Next
MsgBox (lavalow)
End Sub
