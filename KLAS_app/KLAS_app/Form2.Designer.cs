namespace Win_KLAS
{
    partial class Main_Form
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lecture_list = new System.Windows.Forms.ListView();
            this.menu_cb = new System.Windows.Forms.ComboBox();
            this.load_btn = new System.Windows.Forms.Button();
            this.out_btn = new System.Windows.Forms.Button();
            this.section_btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lecture_list
            // 
            this.lecture_list.HideSelection = false;
            this.lecture_list.Location = new System.Drawing.Point(13, 13);
            this.lecture_list.Name = "lecture_list";
            this.lecture_list.Size = new System.Drawing.Size(442, 176);
            this.lecture_list.TabIndex = 0;
            this.lecture_list.UseCompatibleStateImageBehavior = false;
            // 
            // menu_cb
            // 
            this.menu_cb.FormattingEnabled = true;
            this.menu_cb.Location = new System.Drawing.Point(13, 206);
            this.menu_cb.Name = "menu_cb";
            this.menu_cb.Size = new System.Drawing.Size(121, 23);
            this.menu_cb.TabIndex = 1;
            // 
            // load_btn
            // 
            this.load_btn.Location = new System.Drawing.Point(150, 199);
            this.load_btn.Name = "load_btn";
            this.load_btn.Size = new System.Drawing.Size(86, 34);
            this.load_btn.TabIndex = 2;
            this.load_btn.Text = "불러오기";
            this.load_btn.UseVisualStyleBackColor = true;
            this.load_btn.Click += new System.EventHandler(this.load_btn_Click);
            // 
            // out_btn
            // 
            this.out_btn.Location = new System.Drawing.Point(358, 199);
            this.out_btn.Name = "out_btn";
            this.out_btn.Size = new System.Drawing.Size(97, 34);
            this.out_btn.TabIndex = 3;
            this.out_btn.Text = "로그아웃";
            this.out_btn.UseVisualStyleBackColor = true;
            this.out_btn.Click += new System.EventHandler(this.out_btn_Click);
            // 
            // section_btn
            // 
            this.section_btn.Location = new System.Drawing.Point(256, 199);
            this.section_btn.Name = "section_btn";
            this.section_btn.Size = new System.Drawing.Size(84, 34);
            this.section_btn.TabIndex = 4;
            this.section_btn.Text = "세션 갱신";
            this.section_btn.UseVisualStyleBackColor = true;
            this.section_btn.Click += new System.EventHandler(this.section_btn_Click);
            // 
            // Main_Form
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(466, 245);
            this.Controls.Add(this.section_btn);
            this.Controls.Add(this.out_btn);
            this.Controls.Add(this.load_btn);
            this.Controls.Add(this.menu_cb);
            this.Controls.Add(this.lecture_list);
            this.Name = "Main_Form";
            this.Text = "KLAS";
            this.Load += new System.EventHandler(this.Main_Form_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListView lecture_list;
        private System.Windows.Forms.ComboBox menu_cb;
        private System.Windows.Forms.Button load_btn;
        private System.Windows.Forms.Button out_btn;
        private System.Windows.Forms.Button section_btn;
    }
}