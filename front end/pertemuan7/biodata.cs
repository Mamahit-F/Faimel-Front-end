using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace BiodataProgram
{
    public partial class MainForm : Form
    {
        private List<Person> biodataList;
        private DataGridView dataGridView;
        private Panel inputPanel;
        private Panel displayPanel;
        
        // Input controls
        private TextBox txtNama, txtTempat, txtAlamat, txtNomorHP, txtEmail, txtHobi, txtCita;
        private DateTimePicker dtpTanggalLahir;
        private ComboBox cmbJenisKelamin, cmbAgama, cmbKewarganegaraan;
        private PictureBox picFoto;
        private string fotoPath = "";

        public MainForm()
        {
            InitializeComponent();
            biodataList = new List<Person>();
        }

        private void InitializeComponent()
        {
            this.Size = new Size(1200, 800);
            this.Text = "Program Biodata - Input & Output";
            this.StartPosition = FormStartPosition.CenterScreen;
            this.BackColor = Color.FromArgb(240, 248, 255);

            CreateInputPanel();
            CreateDisplayPanel();
        }

        private void CreateInputPanel()
        {
            inputPanel = new Panel
            {
                Size = new Size(580, 750),
                Location = new Point(10, 10),
                BackColor = Color.White,
                BorderStyle = BorderStyle.FixedSingle
            };

            // Title
            Label titleLabel = new Label
            {
                Text = "📝 INPUT BIODATA",
                Font = new Font("Segoe UI", 16, FontStyle.Bold),
                ForeColor = Color.FromArgb(70, 130, 180),
                Size = new Size(560, 40),
                Location = new Point(10, 10),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // Photo section
            picFoto = new PictureBox
            {
                Size = new Size(120, 120),
                Location = new Point(10, 60),
                BorderStyle = BorderStyle.FixedSingle,
                SizeMode = PictureBoxSizeMode.Zoom,
                BackColor = Color.LightGray,
                Image = CreateDefaultImage()
            };

            Button btnBrowseFoto = new Button
            {
                Text = "📷 Browse Foto",
                Size = new Size(120, 30),
                Location = new Point(10, 190),
                BackColor = Color.FromArgb(70, 130, 180),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat
            };
            btnBrowseFoto.Click += BtnBrowseFoto_Click;

            // Input fields with icons
            int yPos = 60;
            int fieldHeight = 35;
            int spacing = 40;

            // Nama Lengkap
            CreateLabeledInput("👤 Nama Lengkap:", ref txtNama, 150, yPos);
            yPos += spacing;

            // Tempat Lahir
            CreateLabeledInput("📍 Tempat Lahir:", ref txtTempat, 150, yPos);
            yPos += spacing;

            // Tanggal Lahir
            Label lblTanggal = new Label
            {
                Text = "📅 Tanggal Lahir:",
                Location = new Point(150, yPos),
                Size = new Size(120, 25),
                Font = new Font("Segoe UI", 9),
                ForeColor = Color.FromArgb(70, 130, 180)
            };
            dtpTanggalLahir = new DateTimePicker
            {
                Location = new Point(280, yPos),
                Size = new Size(280, fieldHeight),
                Format = DateTimePickerFormat.Long
            };
            yPos += spacing;

            // Alamat
            CreateLabeledInput("🏠 Alamat:", ref txtAlamat, 150, yPos, true);
            yPos += spacing + 20;

            // Jenis Kelamin
            Label lblJenisKelamin = new Label
            {
                Text = "⚧ Jenis Kelamin:",
                Location = new Point(150, yPos),
                Size = new Size(120, 25),
                Font = new Font("Segoe UI", 9),
                ForeColor = Color.FromArgb(70, 130, 180)
            };
            cmbJenisKelamin = new ComboBox
            {
                Location = new Point(280, yPos),
                Size = new Size(280, fieldHeight),
                DropDownStyle = ComboBoxStyle.DropDownList
            };
            cmbJenisKelamin.Items.AddRange(new[] { "Laki-laki", "Perempuan" });
            yPos += spacing;

            // Agama
            Label lblAgama = new Label
            {
                Text = "🕌 Agama:",
                Location = new Point(150, yPos),
                Size = new Size(120, 25),
                Font = new Font("Segoe UI", 9),
                ForeColor = Color.FromArgb(70, 130, 180)
            };
            cmbAgama = new ComboBox
            {
                Location = new Point(280, yPos),
                Size = new Size(280, fieldHeight),
                DropDownStyle = ComboBoxStyle.DropDownList
            };
            cmbAgama.Items.AddRange(new[] { "Islam", "Kristen", "Katolik", "Hindu", "Budha", "dll." });
            yPos += spacing;

            // Kewarganegaraan
            Label lblKewarganegaraan = new Label
            {
                Text = "🌏 Kewarganegaraan:",
                Location = new Point(150, yPos),
                Size = new Size(120, 25),
                Font = new Font("Segoe UI", 9),
                ForeColor = Color.FromArgb(70, 130, 180)
            };
            cmbKewarganegaraan = new ComboBox
            {
                Location = new Point(280, yPos),
                Size = new Size(280, fieldHeight)
            };
            cmbKewarganegaraan.Items.AddRange(new[] { "WNI", "WNA" });
            cmbKewarganegaraan.Text = "WNI";
            yPos += spacing;

            // Nomor HP
            CreateLabeledInput("📱 Nomor HP:", ref txtNomorHP, 150, yPos);
            yPos += spacing;

            // Email
            CreateLabeledInput("📧 Email:", ref txtEmail, 150, yPos);
            yPos += spacing;

            // Hobi
            CreateLabeledInput("🎯 Hobi:", ref txtHobi, 150, yPos, true);
            yPos += spacing + 20;

            // Cita-cita
            CreateLabeledInput("🎓 Cita-cita:", ref txtCita, 150, yPos, true);
            yPos += spacing + 40;

            // Buttons
            Button btnSimpan = new Button
            {
                Text = "💾 Simpan Data",
                Size = new Size(130, 40),
                Location = new Point(280, yPos),
                BackColor = Color.FromArgb(34, 139, 34),
                ForeColor = Color.White,
                Font = new Font("Segoe UI", 10, FontStyle.Bold),
                FlatStyle = FlatStyle.Flat
            };
            btnSimpan.Click += BtnSimpan_Click;

            Button btnClear = new Button
            {
                Text = "🗑️ Clear",
                Size = new Size(100, 40),
                Location = new Point(430, yPos),
                BackColor = Color.FromArgb(220, 20, 60),
                ForeColor = Color.White,
                Font = new Font("Segoe UI", 10, FontStyle.Bold),
                FlatStyle = FlatStyle.Flat
            };
            btnClear.Click += BtnClear_Click;

            // Add controls to input panel
            inputPanel.Controls.AddRange(new Control[] {
                titleLabel, picFoto, btnBrowseFoto,
                lblTanggal, dtpTanggalLahir,
                lblJenisKelamin, cmbJenisKelamin,
                lblAgama, cmbAgama,
                lblKewarganegaraan, cmbKewarganegaraan,
                btnSimpan, btnClear
            });

            this.Controls.Add(inputPanel);
        }

        private void CreateLabeledInput(string labelText, ref TextBox textBox, int x, int y, bool isMultiLine = false)
        {
            Label label = new Label
            {
                Text = labelText,
                Location = new Point(x, y),
                Size = new Size(120, 25),
                Font = new Font("Segoe UI", 9),
                ForeColor = Color.FromArgb(70, 130, 180)
            };

            textBox = new TextBox
            {
                Location = new Point(x + 130, y),
                Size = new Size(280, isMultiLine ? 60 : 25),
                Multiline = isMultiLine,
                ScrollBars = isMultiLine ? ScrollBars.Vertical : ScrollBars.None
            };

            inputPanel.Controls.Add(label);
            inputPanel.Controls.Add(textBox);
        }

        private void CreateDisplayPanel()
        {
            displayPanel = new Panel
            {
                Size = new Size(580, 750),
                Location = new Point(600, 10),
                BackColor = Color.White,
                BorderStyle = BorderStyle.FixedSingle
            };

            // Title
            Label titleLabel = new Label
            {
                Text = "📊 DATA BIODATA",
                Font = new Font("Segoe UI", 16, FontStyle.Bold),
                ForeColor = Color.FromArgb(70, 130, 180),
                Size = new Size(560, 40),
                Location = new Point(10, 10),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // DataGridView
            dataGridView = new DataGridView
            {
                Size = new Size(560, 600),
                Location = new Point(10, 60),
                BackgroundColor = Color.White,
                BorderStyle = BorderStyle.Fixed3D,
                AllowUserToAddRows = false,
                AllowUserToDeleteRows = false,
                ReadOnly = true,
                AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill,
                RowHeadersVisible = false,
                SelectionMode = DataGridViewSelectionMode.FullRowSelect
            };

            SetupDataGridView();

            // Export button
            Button btnExport = new Button
            {
                Text = "📄 Export to CSV",
                Size = new Size(140, 35),
                Location = new Point(10, 680),
                BackColor = Color.FromArgb(70, 130, 180),
                ForeColor = Color.White,
                Font = new Font("Segoe UI", 9, FontStyle.Bold),
                FlatStyle = FlatStyle.Flat
            };
            btnExport.Click += BtnExport_Click;

            Button btnDelete = new Button
            {
                Text = "🗑️ Delete Selected",
                Size = new Size(140, 35),
                Location = new Point(160, 680),
                BackColor = Color.FromArgb(220, 20, 60),
                ForeColor = Color.White,
                Font = new Font("Segoe UI", 9, FontStyle.Bold),
                FlatStyle = FlatStyle.Flat
            };
            btnDelete.Click += BtnDelete_Click;

            displayPanel.Controls.AddRange(new Control[] { titleLabel, dataGridView, btnExport, btnDelete });
            this.Controls.Add(displayPanel);
        }

        private void SetupDataGridView()
        {
            dataGridView.Columns.Clear();
            dataGridView.Columns.Add("Nama", "👤 Nama");
            dataGridView.Columns.Add("TempatTanggalLahir", "📅 Tempat, Tgl Lahir");
            dataGridView.Columns.Add("JenisKelamin", "⚧ Jenis Kelamin");
            dataGridView.Columns.Add("Agama", "🕌 Agama");
            dataGridView.Columns.Add("Alamat", "🏠 Alamat");
            dataGridView.Columns.Add("NomorHP", "📱 No. HP");
            dataGridView.Columns.Add("Email", "📧 Email");
            dataGridView.Columns.Add("Hobi", "🎯 Hobi");
            dataGridView.Columns.Add("Cita", "🎓 Cita-cita");

            // Set column widths
            dataGridView.Columns["Nama"].Width = 100;
            dataGridView.Columns["TempatTanggalLahir"].Width = 120;
            dataGridView.Columns["JenisKelamin"].Width = 80;
            dataGridView.Columns["Agama"].Width = 70;
            dataGridView.Columns["Alamat"].Width = 100;
            dataGridView.Columns["NomorHP"].Width = 100;
            dataGridView.Columns["Email"].Width = 120;
            dataGridView.Columns["Hobi"].Width = 80;
            dataGridView.Columns["Cita"].Width = 80;

            // Style the header
            dataGridView.ColumnHeadersDefaultCellStyle.BackColor = Color.FromArgb(70, 130, 180);
            dataGridView.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
            dataGridView.ColumnHeadersDefaultCellStyle.Font = new Font("Segoe UI", 9, FontStyle.Bold);
            dataGridView.ColumnHeadersHeight = 35;

            // Style the rows
            dataGridView.DefaultCellStyle.Font = new Font("Segoe UI", 8);
            dataGridView.AlternatingRowsDefaultCellStyle.BackColor = Color.FromArgb(240, 248, 255);
            dataGridView.RowTemplate.Height = 30;
        }

        private Image CreateDefaultImage()
        {
            Bitmap img = new Bitmap(120, 120);
            using (Graphics g = Graphics.FromImage(img))
            {
                g.Clear(Color.LightGray);
                g.DrawString("📷\nNo Photo", new Font("Segoe UI", 12), Brushes.Gray, new RectangleF(0, 0, 120, 120), 
                    new StringFormat { Alignment = StringAlignment.Center, LineAlignment = StringAlignment.Center });
            }
            return img;
        }

        private void BtnBrowseFoto_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog ofd = new OpenFileDialog())
            {
                ofd.Filter = "Image Files|*.jpg;*.jpeg;*.png;*.bmp;*.gif";
                ofd.Title = "Pilih Foto";
                
                if (ofd.ShowDialog() == DialogResult.OK)
                {
                    try
                    {
                        picFoto.Image = Image.FromFile(ofd.FileName);
                        fotoPath = ofd.FileName;
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show($"Error loading image: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
        }

        private void BtnSimpan_Click(object sender, EventArgs e)
        {
            try
            {
                if (ValidateInput())
                {
                    Person person = new Person
                    {
                        Nama = txtNama.Text.Trim(),
                        Tempat = txtTempat.Text.Trim(),
                        TanggalLahir = dtpTanggalLahir.Value,
                        Alamat = txtAlamat.Text.Trim(),
                        JenisKelamin = cmbJenisKelamin.Text,
                        Agama = cmbAgama.Text,
                        Kewarganegaraan = cmbKewarganegaraan.Text,
                        NomorHP = txtNomorHP.Text.Trim(),
                        Email = txtEmail.Text.Trim(),
                        Hobi = txtHobi.Text.Trim(),
                        Cita = txtCita.Text.Trim(),
                        FotoPath = fotoPath
                    };

                    biodataList.Add(person);
                    RefreshDataGridView();
                    ClearInputs();
                    
                    MessageBox.Show("✅ Data berhasil disimpan!", "Sukses", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private bool ValidateInput()
        {
            if (string.IsNullOrWhiteSpace(txtNama.Text))
            {
                MessageBox.Show("Nama lengkap harus diisi!", "Validasi", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                txtNama.Focus();
                return false;
            }
            
            if (string.IsNullOrWhiteSpace(txtTempat.Text))
            {
                MessageBox.Show("Tempat lahir harus diisi!", "Validasi", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                txtTempat.Focus();
                return false;
            }
            
            if (cmbJenisKelamin.SelectedIndex == -1)
            {
                MessageBox.Show("Jenis kelamin harus dipilih!", "Validasi", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                cmbJenisKelamin.Focus();
                return false;
            }
            
            if (cmbAgama.SelectedIndex == -1)
            {
                MessageBox.Show("Agama harus dipilih!", "Validasi", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                cmbAgama.Focus();
                return false;
            }

            return true;
        }

        private void RefreshDataGridView()
        {
            dataGridView.Rows.Clear();
            foreach (var person in biodataList)
            {
                string tempatTanggal = $"{person.Tempat}, {person.TanggalLahir.ToString("dd/MM/yyyy")}";
                dataGridView.Rows.Add(
                    person.Nama,
                    tempatTanggal,
                    person.JenisKelamin,
                    person.Agama,
                    person.Alamat,
                    person.NomorHP,
                    person.Email,
                    person.Hobi,
                    person.Cita
                );
            }
        }

        private void BtnClear_Click(object sender, EventArgs e)
        {
            ClearInputs();
        }

        private void ClearInputs()
        {
            txtNama.Clear();
            txtTempat.Clear();
            txtAlamat.Clear();
            txtNomorHP.Clear();
            txtEmail.Clear();
            txtHobi.Clear();
            txtCita.Clear();
            cmbJenisKelamin.SelectedIndex = -1;
            cmbAgama.SelectedIndex = -1;
            cmbKewarganegaraan.SelectedIndex = 0;
            dtpTanggalLahir.Value = DateTime.Now;
            picFoto.Image = CreateDefaultImage();
            fotoPath = "";
        }

        private void BtnDelete_Click(object sender, EventArgs e)
        {
            if (dataGridView.SelectedRows.Count > 0)
            {
                if (MessageBox.Show("Apakah Anda yakin ingin menghapus data yang dipilih?", "Konfirmasi", 
                    MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
                {
                    int index = dataGridView.SelectedRows[0].Index;
                    biodataList.RemoveAt(index);
                    RefreshDataGridView();
                    MessageBox.Show("✅ Data berhasil dihapus!", "Sukses", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
            else
            {
                MessageBox.Show("Pilih data yang ingin dihapus!", "Peringatan", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void BtnExport_Click(object sender, EventArgs e)
        {
            if (biodataList.Count == 0)
            {
                MessageBox.Show("Tidak ada data untuk diekspor!", "Peringatan", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            using (SaveFileDialog sfd = new SaveFileDialog())
            {
                sfd.Filter = "CSV files (*.csv)|*.csv";
                sfd.Title = "Export Data ke CSV";
                sfd.FileName = $"Biodata_{DateTime.Now:yyyyMMdd_HHmmss}.csv";

                if (sfd.ShowDialog() == DialogResult.OK)
                {
                    try
                    {
                        ExportToCSV(sfd.FileName);
                        MessageBox.Show("✅ Data berhasil diekspor ke CSV!", "Sukses", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show($"Error saat export: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
        }

        private void ExportToCSV(string filename)
        {
            using (StreamWriter sw = new StreamWriter(filename))
            {
                // Write header
                sw.WriteLine("Nama,Tempat Lahir,Tanggal Lahir,Alamat,Jenis Kelamin,Agama,Kewarganegaraan,Nomor HP,Email,Hobi,Cita-cita");
                
                // Write data
                foreach (var person in biodataList)
                {
                    sw.WriteLine($"\"{person.Nama}\",\"{person.Tempat}\",\"{person.TanggalLahir:dd/MM/yyyy}\"," +
                               $"\"{person.Alamat}\",\"{person.JenisKelamin}\",\"{person.Agama}\"," +
                               $"\"{person.Kewarganegaraan}\",\"{person.NomorHP}\",\"{person.Email}\"," +
                               $"\"{person.Hobi}\",\"{person.Cita}\"");
                }
            }
        }
    }

    public class Person
    {
        public string Nama { get; set; }
        public string Tempat { get; set; }
        public DateTime TanggalLahir { get; set; }
        public string Alamat { get; set; }
        public string JenisKelamin { get; set; }
        public string Agama { get; set; }
        public string Kewarganegaraan { get; set; }
        public string NomorHP { get; set; }
        public string Email { get; set; }
        public string Hobi { get; set; }
        public string Cita { get; set; }
        public string FotoPath { get; set; }
    }

    // Program entry point
    public class Program
    {
        [STAThread]
        public static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}