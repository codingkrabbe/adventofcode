Sub main()
Dim position() As String
Dim positionsingle As Variant
Dim k, result, resultlow, high, highest As Long
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
        If i <> CInt(positionsingle) Then
            If CInt(positionsingle) < i Then
                result = result - (CInt(positionsingle) - i)
            Else
                result = result + (CInt(positionsingle) - i)
            End If
        End If
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
