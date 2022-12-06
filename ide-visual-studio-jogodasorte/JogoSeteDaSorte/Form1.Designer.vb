<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Descartar substituições de formulário para limpar a lista de componentes.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Exigido pelo Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'OBSERVAÇÃO: o procedimento a seguir é exigido pelo Windows Form Designer
    'Pode ser modificado usando o Windows Form Designer.  
    'Não o modifique usando o editor de códigos.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Panel1 = New System.Windows.Forms.Panel()
        Me.Panel2 = New System.Windows.Forms.Panel()
        Me.Panel3 = New System.Windows.Forms.Panel()
        Me.num1 = New System.Windows.Forms.Label()
        Me.num2 = New System.Windows.Forms.Label()
        Me.num3 = New System.Windows.Forms.Label()
        Me.Button_jogar = New System.Windows.Forms.Button()
        Me.Button_sair = New System.Windows.Forms.Button()
        Me.imagemResultado = New System.Windows.Forms.PictureBox()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.Panel1.SuspendLayout()
        Me.Panel2.SuspendLayout()
        Me.Panel3.SuspendLayout()
        CType(Me.imagemResultado, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Font = New System.Drawing.Font("Segoe UI Black", 20.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.ForeColor = System.Drawing.Color.OrangeRed
        Me.Label1.Location = New System.Drawing.Point(12, 27)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(151, 37)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "7 da Sorte"
        '
        'Panel1
        '
        Me.Panel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.Panel1.Controls.Add(Me.num1)
        Me.Panel1.Location = New System.Drawing.Point(565, 27)
        Me.Panel1.Name = "Panel1"
        Me.Panel1.Size = New System.Drawing.Size(134, 100)
        Me.Panel1.TabIndex = 1
        '
        'Panel2
        '
        Me.Panel2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.Panel2.Controls.Add(Me.num2)
        Me.Panel2.Location = New System.Drawing.Point(565, 148)
        Me.Panel2.Name = "Panel2"
        Me.Panel2.Size = New System.Drawing.Size(134, 100)
        Me.Panel2.TabIndex = 2
        '
        'Panel3
        '
        Me.Panel3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.Panel3.Controls.Add(Me.num3)
        Me.Panel3.Location = New System.Drawing.Point(565, 277)
        Me.Panel3.Name = "Panel3"
        Me.Panel3.Size = New System.Drawing.Size(134, 100)
        Me.Panel3.TabIndex = 3
        '
        'num1
        '
        Me.num1.AutoSize = True
        Me.num1.Font = New System.Drawing.Font("Impact", 30.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.num1.Location = New System.Drawing.Point(46, 29)
        Me.num1.Name = "num1"
        Me.num1.Size = New System.Drawing.Size(41, 48)
        Me.num1.TabIndex = 0
        Me.num1.Text = "0"
        '
        'num2
        '
        Me.num2.AutoSize = True
        Me.num2.Font = New System.Drawing.Font("Impact", 30.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.num2.Location = New System.Drawing.Point(45, 29)
        Me.num2.Name = "num2"
        Me.num2.Size = New System.Drawing.Size(41, 48)
        Me.num2.TabIndex = 0
        Me.num2.Text = "0"
        '
        'num3
        '
        Me.num3.AutoSize = True
        Me.num3.Font = New System.Drawing.Font("Impact", 30.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.num3.Location = New System.Drawing.Point(45, 29)
        Me.num3.Name = "num3"
        Me.num3.Size = New System.Drawing.Size(41, 48)
        Me.num3.TabIndex = 0
        Me.num3.Text = "0"
        '
        'Button_jogar
        '
        Me.Button_jogar.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Button_jogar.Location = New System.Drawing.Point(437, 197)
        Me.Button_jogar.Name = "Button_jogar"
        Me.Button_jogar.Size = New System.Drawing.Size(75, 34)
        Me.Button_jogar.TabIndex = 4
        Me.Button_jogar.Text = "Jogar !"
        Me.Button_jogar.UseVisualStyleBackColor = True
        '
        'Button_sair
        '
        Me.Button_sair.Location = New System.Drawing.Point(713, 415)
        Me.Button_sair.Name = "Button_sair"
        Me.Button_sair.Size = New System.Drawing.Size(75, 23)
        Me.Button_sair.TabIndex = 5
        Me.Button_sair.Text = "Sair"
        Me.Button_sair.UseVisualStyleBackColor = True
        '
        'imagemResultado
        '
        Me.imagemResultado.Location = New System.Drawing.Point(12, 96)
        Me.imagemResultado.Name = "imagemResultado"
        Me.imagemResultado.Size = New System.Drawing.Size(378, 342)
        Me.imagemResultado.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        Me.imagemResultado.TabIndex = 6
        Me.imagemResultado.TabStop = False
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(434, 391)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(132, 13)
        Me.Label2.TabIndex = 7
        Me.Label2.Text = "Criado por Rafael Gouveia"
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(434, 404)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(151, 13)
        Me.Label3.TabIndex = 8
        Me.Label3.Text = "rafaelgouveiamelo@gmail.com"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(434, 420)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(65, 13)
        Me.Label4.TabIndex = 9
        Me.Label4.Text = "30/11/2022"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.imagemResultado)
        Me.Controls.Add(Me.Button_sair)
        Me.Controls.Add(Me.Button_jogar)
        Me.Controls.Add(Me.Panel3)
        Me.Controls.Add(Me.Panel2)
        Me.Controls.Add(Me.Panel1)
        Me.Controls.Add(Me.Label1)
        Me.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Name = "Form1"
        Me.Text = "Jogo 7 Da Sorte"
        Me.Panel1.ResumeLayout(False)
        Me.Panel1.PerformLayout()
        Me.Panel2.ResumeLayout(False)
        Me.Panel2.PerformLayout()
        Me.Panel3.ResumeLayout(False)
        Me.Panel3.PerformLayout()
        CType(Me.imagemResultado, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents Label1 As Label
    Friend WithEvents Panel1 As Panel
    Friend WithEvents Panel2 As Panel
    Friend WithEvents Panel3 As Panel
    Friend WithEvents num1 As Label
    Friend WithEvents num2 As Label
    Friend WithEvents num3 As Label
    Friend WithEvents Button_jogar As Button
    Friend WithEvents Button_sair As Button
    Friend WithEvents imagemResultado As PictureBox
    Friend WithEvents Label2 As Label
    Friend WithEvents Label3 As Label
    Friend WithEvents Label4 As Label
End Class
