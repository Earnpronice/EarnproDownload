import os
import zipfile

exclude_dirs = {'node_modules', '.git', 'dist', '__pycache__'}
exclude_files = {'EarnPro_Full_Project.zip'}

os.makedirs('public', exist_ok=True)
zip_path = 'public/EarnPro_Full_Project.zip'

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in files:
            if f in exclude_files:
                continue
            full_p = os.path.join(root, f)
            arc_name = os.path.relpath(full_p, '.')
            zipf.write(full_p, arc_name)

print(f"Zip created successfully: {zip_path} ({os.path.getsize(zip_path)} bytes)")
