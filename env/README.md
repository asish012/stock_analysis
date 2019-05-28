## Python Environment

#### Prerequisites

* *Anaconda3*: Download [Anaconda](https://www.anaconda.com/download/) for Python 3 from the official website and install it to your system.
    During the installation you are asked to add the `conda` command to your `PATH` variable - do that NOT.
    Instead activate conda for your user with the following command:

        echo ". <ANACONDA INSTALLATION FOLDER>/etc/profile.d/conda.sh" >> ~/.bash_profile

#### Create / Update environment

The script `env/create.sh` creates and installs a python environment in `env/conda-env-investing` folder, containing all project dependencies.
The dependencies are specified in the file `env/dependencies.yml`, which is a conda environment file (see https://conda.io/docs/user-guide/tasks/manage-environments.html#).

    # create a new environment or update existing
    ./env/create.sh

#### Using the environment

The environment can simply be used by IDE's like [PyCharm](https://www.jetbrains.com/pycharm/) by pointing the python executable to `env/conda-env-investing/bin/python3.6`.

To (de)-activate the environment use the following commands:

    # activation
    conda activate ./env/conda-env-investing

    # deactivation
    conda deactivate

Tools like jupyter can then be started directly from this environment:

    # start jupyter
    jupyter-notebook
