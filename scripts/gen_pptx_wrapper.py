"""Wrapper to generate PPTX to a temp path outside OneDrive lock."""
import os, shutil

os.chdir(r"C:\Users\Admin\OneDrive\Desktop\RR")

# Read and patch the script to output to Desktop temp
with open("scripts/generate_presentation_pptx.py", "r", encoding="utf-8-sig") as f:
    code = f.read()

temp_out = r"C:\Users\Admin\Desktop\RR_pptx_out.pptx"
final_out = r"C:\Users\Admin\OneDrive\Desktop\RR\public\downloads\Rajasthan_Royals_SupeRR_Selector_Round1_Presentation.pptx"

# Replace save section with temp path version
old_save = '''# ─── SAVE PRESENTATION ───────────────────────────────────────────────────────
import shutil, tempfile
out_path = "public/downloads/Rajasthan_Royals_SupeRR_Selector_Round1_Presentation.pptx"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
# Save to temp file first to avoid OneDrive lock on the target path
with tempfile.NamedTemporaryFile(suffix=".pptx", delete=False, dir=os.path.dirname(out_path)) as tmp:
    tmp_path = tmp.name
prs.save(tmp_path)
# Replace target atomically
if os.path.exists(out_path):
    os.remove(out_path)
shutil.move(tmp_path, out_path)
print(f"Master Presentation Generated Successfully: {out_path} (24 slides)")'''

new_save = '''# ─── SAVE PRESENTATION ───────────────────────────────────────────────────────
out_path = r"C:\\Users\\Admin\\Desktop\\RR_pptx_out.pptx"
prs.save(out_path)
print(f"Master Presentation Generated Successfully: {out_path} (24 slides)")'''

if old_save in code:
    code = code.replace(old_save, new_save)
    print("Patched save section")
else:
    print("WARNING: Could not find save section to patch — looking for fallback")
    # Try simpler replacement
    code = code.replace(
        'out_path = "public/downloads/Rajasthan_Royals_SupeRR_Selector_Round1_Presentation.pptx"',
        f'out_path = r"C:\\Users\\Admin\\Desktop\\RR_pptx_out.pptx"'
    )

exec(compile(code, "generate_presentation_pptx.py", "exec"), {"__name__": "__main__"})

# Now copy to final destination (overwrite)
if os.path.exists(temp_out):
    # Try to copy over the locked file using low-level file replacement
    import ctypes
    # Try MoveFileEx with REPLACE_EXISTING
    MOVEFILE_REPLACE_EXISTING = 0x1
    MOVEFILE_WRITE_THROUGH = 0x8
    result = ctypes.windll.kernel32.MoveFileExW(temp_out, final_out, MOVEFILE_REPLACE_EXISTING)
    if result:
        print(f"Moved to final: {final_out}")
    else:
        err = ctypes.windll.kernel32.GetLastError()
        print(f"MoveFileEx failed with error {err}, trying copy...")
        shutil.copy2(temp_out, final_out)
        os.remove(temp_out)
        print(f"Copied to final: {final_out}")
else:
    print("ERROR: temp file not generated!")
