# AY 128 Course Materials - Spring 2026

This is the main GitHub repository for the course materials of AY 128 (Astronomy Data Science Lab) at UC Berkeley.

The Course website is located at [https://ucb-datalab.github.io/](https://ucb-datalab.github.io/).


## Setting up a work environment

### DataHub

For those enrolled in the course, you can head over to [astro.datahub.berkeley.edu](https://astro.datahub.berkeley.edu) which should have all the necessary dependencies installed for the course.

Then, open a Terminal window and clone this repo:

 ```
 git clone https://github.com/ucb-datalab/course_materials_sp2026.git
 ```

### Local Environment

You may wish to work directly from your laptop. We use [uv](https://docs.astral.sh/uv/) for fast Python package management.

   1. Install uv (if not already installed):

 ```
 curl -LsSf https://astral.sh/uv/install.sh | sh
 ```

   2. Clone this repo:

 ```
 git clone https://github.com/ucb-datalab/course_materials_sp2026.git
 ```

  3. Run the setup script:

 ```
 cd course_materials_sp2026
 ./setup_env.sh
 ```

  Or manually:

 ```
 cd course_materials_sp2026
 uv venv --python 3.12 --prompt ay128
 source .venv/bin/activate
 uv pip install -r requirements.txt
 ```

## Running Jupyter

After setting up your environment, activate it and start Jupyter:

```bash
source .venv/bin/activate
jupyter notebook
```

Or use uv to run directly without activating:

```bash
uv run jupyter notebook
```

To start JupyterLab instead:

```bash
uv run jupyter lab
```

## Notebook Presentation Styling

The lecture notebooks use custom styling for better readability during class.

The styling is automatically applied when you open any notebook - no need to run any cells. The `setup_env.sh` script installs:
- **Custom CSS** (from `styles/ay128_custom.css` to `~/.jupyter/custom/custom.css`) - Instant styling on page load
- **IPython startup script** - Makes talktools helper functions available

For dynamic customization (e.g., dark mode), you can use:
```python
from talktools import configure
configure(theme="dark")  # or theme="light", font_size="130%", etc.
```

## Keeping it up to date

 We often make changes to the lecture material and so to sync with the latest, you should do a

 ```
 git pull
 ```

Periodically in the `course_materials_sp2026` directory. If you've edited a file that is due to be changed, this can cause conflicts. Doing a `git stash` before the `pull` should help. But to avoid this, consider making a copy of any repo file you'd like to edit.


