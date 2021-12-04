Sub main()
Dim value As Variant
Dim command() As String
Dim lines, i, lenghtrow, counter  As Integer
Dim gamma, epsilon As String
Dim gammadec, epsilondec As Long
lines = Tabelle3.UsedRange.Rows.Count
For i = 1 To lines
value = Tabelle3.Cells(i, 1)
For x = 1 To 12
If x <= Len(value) Then
Tabelle3.Cells(i, 14 - x) = Left(Right(value, x), 1)
Else
Tabelle3.Cells(i, 14 - x) = 0
End If
Next
Next
For x = 2 To 13
counter = 0
For i = 1 To lines
If Tabelle3.Cells(i, x) = 1 Then
counter = counter + 1
End If
If i = lines Then
If counter > lines / 2 Then
gamma = gamma & "1"
epsilon = epsilon & "0"
Else
gamma = gamma & "0"
epsilon = epsilon & "1"
End If
End If
Next
Next
For i = 1 To Len(gamma)
gammadec = gammadec + CLng((Left(Right(gamma, i), 1)) * 2 ^ (i - 1))
epsilondec = epsilondec + CLng((Left(Right(epsilon, i), 1)) * 2 ^ (i - 1))
Next
MsgBox (gammadec * epsilondec)
End Sub
