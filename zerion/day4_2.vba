Sub main()
Dim drawn() As String
Dim line() As String
Dim boards() As String
Dim highline() As String
Dim drawnsingle As Variant
Dim boardsingle As Variant
Dim highlinesingle As Variant
Dim repLine, repLine2 As String
Set arrayobj = CreateObject("System.collections.arraylist")
Dim lines, i, a, b, c, d, e, g, f, result, result1, n, u, p, l, kk, xx, boardscount As Integer
Dim k As Variant
Dim t As Long
lines = Tabelle1.UsedRange.Rows.Count
xx = 1
drawn = Split(Tabelle1.Cells(1, 1), ",")
For i = 3 To lines
    If Tabelle1.Cells(i, 1) = Empty Then
    xx = xx + 1
    Else
 repLine = Replace(Tabelle1.Cells(i, 1), "  ", " ")
 If Left(repLine, 1) = " " Then
 repLine = Right(repLine, Len(repLine) - 1)
End If
line = Split(repLine, " ")
For b = 0 To 4
Tabelle1.Cells(i, b + 2) = line(b)
Next
End If
Next
i = 3
l = 0
For Each drawnsingle In drawn
For b = 0 To 4
    For i = 3 To lines
    If Tabelle1.Cells(i, b + 2) = "" Then
    j = i
    result1 = 0
    End If
    If Tabelle1.Cells(i, b + 2) = CInt(drawnsingle) Then
    Tabelle1.Cells(i, b + 2).Font.Bold = True
                g = 0
            result = 0
                        For f = 2 To 6
                           If Tabelle1.Cells(i, f).Font.Bold = True Then
               g = g + 1
               If g = 5 Then
                 If l > 0 Then

            k = Application.Match(CStr(j), boards, 0)
            If CStr(k) = "Fehler 2042" Then
                                                ReDim Preserve boards(l)
                boards(l) = j
               l = l + 1
                                        boardscount = UBound(boards)
               If l = xx - 1 Then
               n = 1
             End If
             Else
             End If
                                     Else
                                            ReDim Preserve boards(l)
                boards(l) = j
               l = l + 1
                              End If
               End If
               End If
            Next
                        g = 0
            result = 0
            For h = j + 1 To j + 5
            result1 = result1 + Tabelle1.Cells(i, f)
            If Tabelle1.Cells(h, b + 2).Font.Bold = True Then
                          g = g + 1
                          If g = 5 Then
                          If l > 0 Then
            k = Application.Match(CStr(j), boards, 0)
            If CStr(k) = "Fehler 2042" Then
                                                    ReDim Preserve boards(l)
                boards(l) = j
               l = l + 1
               boardscount = UBound(boards)
               If l = xx - 1 Then
               n = 1
                          Else
             End If
                                        End If
                Else
                                            ReDim Preserve boards(l)
                boards(l) = j
               l = l + 1
                              End If
               End If
               End If
                         If n = 1 Then
            For u = j + 1 To j + 5
                For p = 2 To 6
                If Tabelle1.Cells(u, p).Font.Bold Then
                Else
                    result1 = result1 + Tabelle1.Cells(u, p)
                    End If
                Next
            Next
                        result1 = result1 * drawnsingle
            MsgBox (result1)
            GoTo exitt
                        End If
                        Next
    End If
    Next
Next
Next
End Sub
