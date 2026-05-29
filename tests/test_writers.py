import os
from sakipro.reports.writers import export_to_markdown, export_to_excel, export_to_docx

def test_export_to_markdown(tmp_path):
    output_dir = tmp_path / "output"
    filepath = export_to_markdown("# Test Report\n\nContent here.", "test_cmd", str(output_dir))
    
    assert os.path.exists(filepath)
    with open(filepath, "r") as f:
        content = f.read()
    assert "# Test Report" in content

def test_export_to_excel(tmp_path):
    output_dir = tmp_path / "output"
    data = [{"No": 1, "Indikator": "IKU 1", "Hasil": "OK"}]
    filepath = export_to_excel(data, "test_excel", str(output_dir))
    
    assert os.path.exists(filepath)
    assert filepath.endswith(".xlsx")

def test_export_to_docx(tmp_path):
    output_dir = tmp_path / "output"
    filepath = export_to_docx("# Test Laporan\nBaris isi laporan.", "test_docx", str(output_dir))
    
    assert os.path.exists(filepath)
    assert filepath.endswith(".docx")
