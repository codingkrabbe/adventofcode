Sub main()
Dim position() As String
Dim positionsingle As Variant
Dim a, zuege, k, result, resultlow, high, highest As Long
position = Split(Tabelle3.Cells(1, 1), ",")
For i = 0 To UBound(position)
    high = CInt(position(i))
    If high > highest Then
        highest = high
    End If
Next
k = 0
For i = 0 To highest
    result = 0
    For Each positionsingle In position
    sprit = 0
        If i <> CInt(positionsingle) Then
            If CInt(positionsingle) < i Then
                zuege = (CInt(positionsingle) - i) * -1
                For a = 1 To zuege
                    sprit = sprit + a
                Next
            Else
                zuege = CInt(positionsingle) - i
                For a = 1 To zuege
                    sprit = sprit + a
                Next
            End If
        End If
    result = result + sprit
    Next
    If k = 0 Then
        resultlow = result
    End If
    If result < resultlow Then
        resultlow = result
    End If
    k = k + 1
Next
MsgBox (resultlow)
End Sub
