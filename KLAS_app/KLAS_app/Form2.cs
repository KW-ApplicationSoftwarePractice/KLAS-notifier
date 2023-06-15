using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using Microsoft.Toolkit.Uwp.Notifications;

namespace Win_KLAS
{
    public partial class Main_Form : Form
    {
        string[] lecture = null ;
        string[] work = null;
        string[] quiz = null;

        string ID;
        string PW;

        public Main_Form(string ID, string PW)
        {
            InitializeComponent();
            this.ID = ID;
            this.PW = PW;
        }

        private void Main_Form_Load(object sender, EventArgs e)
        {
            string[] data = { "강의", "과제", "퀴즈" };
            menu_cb.Items.AddRange(data);
            menu_cb.SelectedIndex = 0;

            lecture_list.View = View.Details;

            Data_refresh();
        }

        private void Data_refresh()
        {
            Process process = new Process();

            process.StartInfo.UseShellExecute = false;

            process.StartInfo.FileName = @"C:\\python\\python.exe";
            process.StartInfo.Arguments = @"KLAS_py\klas_renew.py " + ID + " " + PW;

            process.StartInfo.RedirectStandardOutput = true;

            process.Start();

            process.WaitForExit();

            string output = process.StandardOutput.ReadToEnd();

            Process apro = new Process();

            apro.StartInfo.UseShellExecute = false;

            apro.StartInfo.FileName = @"C:\\python\\python.exe";
            apro.StartInfo.Arguments = @"KLAS_py\klas_event_execute.py " + ID + " " + PW;

            apro.StartInfo.RedirectStandardOutput = true;

            apro.Start();

            apro.WaitForExit();

            string alert = apro.StandardOutput.ReadToEnd();

            if (alert == "0\r\n")
            {
                new ToastContentBuilder()
                 .AddArgument("action", "viewConversation")
                 .AddArgument("conversationId", 9813)
                 .AddText("KLAS")
                 .AddText("새로운 게시글이 올라왔습니다!")
                 .Show();
            }

            string[] slash = new string[] { "####" };
            string[] sep = output.Split(slash, StringSplitOptions.None);

            for (int i=0; i<sep.Length; i++)
            {
                if (i == 0)
                {
                    lecture = sep[i].Split(new char[] { '\n' }, StringSplitOptions.RemoveEmptyEntries);
                }

                else if (i == 1)
                {
                    work = sep[i].Split(new char[] { '\n' }, StringSplitOptions.RemoveEmptyEntries);
                }

                else if (i == 2)
                {
                    quiz = sep[i].Split(new char[] { '\n' }, StringSplitOptions.RemoveEmptyEntries);
                }
            }

            col_change();
        }

        private void load_btn_Click(object sender, EventArgs e)
        {
            col_change();
        }

        private void col_change()
        {
            lecture_list.Clear();

            string[] str;

            if (menu_cb.SelectedIndex == 0)
            {
                str = lecture;
            }
            else if (menu_cb.SelectedIndex == 1)
            {
                str = work;
            }
            else
            {
                str = quiz;
            }

            lecture_list.BeginUpdate();

            if (str.Length>0)
            {
                foreach (string line in str)
                {
                    if (line != "\r")
                    {
                        string[] separater = new string[] { "////" };
                        string[] info = line.Split(separater, StringSplitOptions.None);
                        ListViewItem item = new ListViewItem(info[0]);
                        item.SubItems.Add(info[1]);
                        item.SubItems.Add(info[2]);

                        lecture_list.Items.Add(item);
                    }
                }
            }

            lecture_list.Columns.Add("과목명", 200, HorizontalAlignment.Left);
            lecture_list.Columns.Add("제목", 150, HorizontalAlignment.Left);
            lecture_list.Columns.Add("기간", 100, HorizontalAlignment.Left);

            lecture_list.EndUpdate();

            this.Refresh();
        }

        private void out_btn_Click(object sender, EventArgs e)
        {
            Owner.Show();
            Close();
        }

        private void section_btn_Click(object sender, EventArgs e)
        {
            Data_refresh();
        }

        private void download_btn_Click(object sender, EventArgs e)
        {
            Process process = new Process();

            process.StartInfo.UseShellExecute = false;

            process.StartInfo.FileName = @"C:\\python\\python.exe";
            process.StartInfo.Arguments = @"KLAS_py\klas_dl.py " + ID + " " + PW;

            process.Start();

            process.WaitForExit();
        }
    }
}