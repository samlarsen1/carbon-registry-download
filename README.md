# Registry Download

Download carbon project registry (currently vero) and process the data to generate insights.
## How to get started

This repository will use Jupyter Notebooks (running Python) in VS Code - [see this description of the tools that are used together here](https://towardsdatascience.com/getting-started-with-jupyter-notebooks-in-visual-studio-code-5dcccb3f739b)

### Working in VS Code

* Install python 3
  ```bash
  brew install python3
  ```
* [Install Python Extension for VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_install-visual-studio-code-and-the-python-extension) - or just go to 'extensions' on the left-hand menu and search for Python then install it
  * See also (for extra guidance): [Basics of Python in VS Code](https://code.visualstudio.com/docs/languages/python)
* Create a virtual environment for python
  ```python
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Running Code

Open a terminal and run

```python
python3 download.py
```

Now you have the data you can open the following Jupyter notebook file: `example_notebook.ipynb` - it should open as a Python notebook.

See a description of [how Python notebooks work here](https://towardsdatascience.com/getting-started-with-jupyter-notebooks-in-visual-studio-code-5dcccb3f739b)