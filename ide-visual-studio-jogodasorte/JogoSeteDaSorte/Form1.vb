Public Class Form1
    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub

    Private Sub Label2_Click(sender As Object, e As EventArgs) Handles num1.Click

    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button_sair.Click
        End
    End Sub

    Private Sub Button_jogar_Click(sender As Object, e As EventArgs) Handles Button_jogar.Click
        imagemResultado.Visible = False REM Esconde a imagem 
        Randomize() REM função de randomização numerica
        num1.Text = CStr(Int(Rnd() * 10)) REM o numero é uma string
        num2.Text = CStr(Int(Rnd() * 10))   REM Rnd chamando numero de 0 - 9 (*10)
        num3.Text = CStr(Int(Rnd() * 10)) REM CStr - tranformando o Int em numero string randomico

        REM verificações:
        '777 - Todos iguais'
        If (num1.Text = "7") And (num2.Text = "7") And (num3.Text = "7") Then
            imagemResultado.Image = Image.FromFile("D:\Visual Studio\visualbasic\JogoSeteDaSorte_sln\img\transferir_junto.png")
            imagemResultado.Visible = True
            Beep()
        ElseIf (num1.Text = "7") Or (num2.Text = "7") Or (num3.Text = "7") Then
            imagemResultado.Image = Image.FromFile("D:\Visual Studio\visualbasic\JogoSeteDaSorte_sln\img\images_ganhou2_junto.png")
            imagemResultado.Visible = True
            Beep()
        Else
            imagemResultado.Image = Image.FromFile("D:\Visual Studio\visualbasic\JogoSeteDaSorte_sln\img\pngtree-vector-game-over-press-try-again-png-image_2942726_junto.jpg")
            imagemResultado.Visible = True
            Beep()

        End If


    End Sub

    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs)

    End Sub

    Private Sub Label2_Click_1(sender As Object, e As EventArgs) Handles Label2.Click

    End Sub

    Private Sub Label4_Click(sender As Object, e As EventArgs) Handles Label4.Click

    End Sub

    Private Sub Label3_Click(sender As Object, e As EventArgs) Handles Label3.Click

    End Sub
End Class
