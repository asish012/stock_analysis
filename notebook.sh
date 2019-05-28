#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate env/conda-env-investing/
jupyter-notebook --notebook-dir ./stock_analysis --MappingKernelManager.root_dir='./'
conda deactivate
