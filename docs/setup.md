# Developer Setup: Python 3.11 for Tensorflow + Jupyter

## Create and Activate Virtual Environment

### Only for Mac on Apple silicon

If Python 3.11 is not installed:

```bash
brew install python@3.11; \
```

```bash
/opt/homebrew/opt/python@3.11/bin/python3.11 -m venv .venv; \
source .venv/bin/activate```

```bash
pip install --upgrade pip setuptools wheel; \
pip install -r requirements.txt; \
python -m ipykernel install --user --name=venv --display-name "CV project Python 3.11 (venv)"
```

Restart VS Code, open a notebook, and:

```python
!which python
```

Then select the correct kernel:
- Click “Select Another Kernel”
- Choose “Jupyter Kernel”
- Refresh and select the environment that matches your current `venv`

