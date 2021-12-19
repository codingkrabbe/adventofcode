Sub main()
Dim coord1() As String
Dim coord2() As String
coord1 = Split(Tabelle16.Cells(1, 1), "=")
For i = 1 To UBound(coord1)
coord2 = Split(coord1(i), "..")
Tabelle16.Cells(i, i + 1) = coord2(0)
Tabelle16.Cells(i, i + 2) = coord2(1)
Next
Tabelle16.Cells(1, 3) = Left(Tabelle16.Cells(1, 3), 2)
For i = 10000 + Tabelle16.Cells(2, 3) To 10000 + Tabelle16.Cells(2, 4)
    For a = 10000 + Tabelle16.Cells(1, 2) To 10000 + Tabelle16.Cells(1, 3)
        Tabelle16.Cells(a, i) = "#"
    Next
Next
    probex = 0
    probey = 0

    For velox = 11 To Tabelle16.Cells(1, 3)
        For veloy = 0 To 250
        highy = 0
            probexvelo = velox
            probeyvelo = veloy
                probex = 0
    probey = 0
            hit = 0

            Do
            probex = probex + probexvelo
            probey = probey + probeyvelo
            If Not probexvelo = 0 Then
            probexvelo = probexvelo - 1
            End If
            If probey > highy Then
            highy = probey
            End If
                         probeyvelo = probeyvelo - 1
          
                    If probey = 10147 Then
                    g = 1
                    End If
                        If probex <= Tabelle16.Cells(1, 3) And probex >= Tabelle16.Cells(1, 2) And probey <= Tabelle16.Cells(2, 4) And probey >= Tabelle16.Cells(2, 3) Then
            hit = 1
            End If
            toomuch = toomuch + 1
            If veloy = 35 And toomuch = 60 Then
            h = 1
            End If
            Loop Until probex > Tabelle16.Cells(1, 3) Or probey < Tabelle16.Cells(2, 4) Or hit = 1
            If hit = 1 Then
                                                If highnew < highy Then
                highnew = highy
                End If
            End If
       Next
         Next

MsgBox (highnew)
End Sub
