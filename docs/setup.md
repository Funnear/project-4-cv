# Developer Setup: Python + Jupyter + Git Submodules

## Create and Activate Virtual Environment

### For Mac/Linux

```bash
python3 -m venv venv; \
source venv/bin/activate
```

To deactivate:

```bash
deactivate
```

### For Windows

Replace the `pythonPath` with the full path to your 64-bit Python executable:

```
$pythonPath = "C:\Users\YourUsername\AppData\Local\Programs\Python\Python310\python.exe"
& $pythonPath -m venv C:\path\to\your\venv
```

To activate:

```
venv\Scripts\activate
```

To deactivate:

```
deactivate
```

---

## Install Dependencies

Update pip and install required libraries:

```bash
pip install --upgrade pip; \
pip install -r requirements.txt
```

---

## Enable Jupyter Kernel from This Virtual Environment

Precondition: install `ipykernel` in your requirements first.

```bash
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```

Restart VS Code, open a notebook, and:

```python
!which python
```

Then select the correct kernel:
- Click “Select Another Kernel”
- Choose “Jupyter Kernel”
- Refresh and select the environment that matches your current `venv`

---

## Use Git Submodules for Internal Libraries

### Add Submodule

```bash
git submodule add https://github.com/funnear/data_ravers_utils.git src/data_ravers_utils; \
git submodule update --init --recursive
```

### Install Submodule as Editable Package

```bash
pip install -e ./src/data_ravers_utils
```

Restart Jupyter Kernel after that.

### Import Inside Jupyter Notebook

```python
import sys, os

# Append submodule path
module_path = os.path.abspath("./src")
if module_path not in sys.path:
    sys.path.append(module_path)

# Example import
from data_ravers_utils.module_name import some_function
```

---

## Updating or Removing Submodules

### Update

Pull the latest commits from the submodule's default branch (usually main):
```bash
git submodule update --remote --merge; \
git add src/data_ravers_utils; \
git commit -m "Update data_ravers_utils submodule to latest commit"; \
git push origin main
```

### Add changes and sync with submodule source
```bash
cd src/data_ravers_utils; \
git add --all; \
git commit -m "Syncing changes from downstream project"; \
git push origin main; \
cd ../..
```

### Remove submodule completely

```bash
git rm --cached libs/data_ravers_utils; \
rm -rf .git/modules/libs/data_ravers_utils; \
git commit -m "Removed submodule"
```

---