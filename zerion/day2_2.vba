Sub main()
Dim commandInput As Variant
Dim command() As String
Dim lines, i, depth, horiz, icommand  As Integer
Dim result, aim As Long
lines = Tabelle2.UsedRange.Rows.Count
For i = 1 To lines
commandInput = Tabelle2.Cells(i, 1)
command = Split(commandInput, " ")
If command(0) = "up" Then
aim = aim - CInt(command(1))
ElseIf command(0) = "down" Then
aim = aim + CInt(command(1))
ElseIf command(0) = "forward" Then
horiz = horiz + CInt(command(1))
depth = depth + (aim * CInt(command(1)))
End If
Next
result = horiz * depth
MsgBox (result)
End Sub
