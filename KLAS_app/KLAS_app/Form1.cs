using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Win_KLAS
{
    public partial class Login_Form : Form
    {
        public Login_Form()
        {
            InitializeComponent();
        }

        private void login_btn_Click(object sender, EventArgs e)
        {
            this.Hide();

            Point P_point = this.Location;
            Main_Form md = new Main_Form(ID_tb.Text, PW_tb.Text);

            ID_tb.Text = "";
            PW_tb.Text = "";

            md.StartPosition = FormStartPosition.Manual;
            md.Location = new Point(P_point.X, P_point.Y);
            md.Owner = this;
            md.FormClosed += new FormClosedEventHandler(child_close);
            md.ShowDialog();
        }

        private void child_close(object obj, EventArgs e)
        {
            this.Show();
        }
    }
}