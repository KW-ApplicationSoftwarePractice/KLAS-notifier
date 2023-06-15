namespace Win_KLAS
{
    partial class Login_Form
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.login_btn = new System.Windows.Forms.Button();
            this.ID_tb = new System.Windows.Forms.TextBox();
            this.PW_tb = new System.Windows.Forms.TextBox();
            this.ID = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // login_btn
            // 
            this.login_btn.Location = new System.Drawing.Point(217, 127);
            this.login_btn.Name = "login_btn";
            this.login_btn.Size = new System.Drawing.Size(91, 31);
            this.login_btn.TabIndex = 0;
            this.login_btn.Text = "로그인";
            this.login_btn.UseVisualStyleBackColor = true;
            this.login_btn.Click += new System.EventHandler(this.login_btn_Click);
            // 
            // ID_tb
            // 
            this.ID_tb.Location = new System.Drawing.Point(69, 26);
            this.ID_tb.Name = "ID_tb";
            this.ID_tb.Size = new System.Drawing.Size(239, 25);
            this.ID_tb.TabIndex = 1;
            // 
            // PW_tb
            // 
            this.PW_tb.Location = new System.Drawing.Point(69, 77);
            this.PW_tb.Name = "PW_tb";
            this.PW_tb.PasswordChar = '*';
            this.PW_tb.Size = new System.Drawing.Size(239, 25);
            this.PW_tb.TabIndex = 2;
            this.PW_tb.KeyDown += new System.Windows.Forms.KeyEventHandler(this.PW_tb_KeyDown);
            // 
            // ID
            // 
            this.ID.AutoSize = true;
            this.ID.Location = new System.Drawing.Point(43, 29);
            this.ID.Name = "ID";
            this.ID.Size = new System.Drawing.Size(20, 15);
            this.ID.TabIndex = 3;
            this.ID.Text = "ID";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(32, 80);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(31, 15);
            this.label1.TabIndex = 4;
            this.label1.Text = "PW";
            // 
            // Login_Form
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(327, 180);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.ID);
            this.Controls.Add(this.PW_tb);
            this.Controls.Add(this.ID_tb);
            this.Controls.Add(this.login_btn);
            this.Name = "Login_Form";
            this.Text = "Login";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button login_btn;
        private System.Windows.Forms.TextBox ID_tb;
        private System.Windows.Forms.TextBox PW_tb;
        private System.Windows.Forms.Label ID;
        private System.Windows.Forms.Label label1;
    }
}

