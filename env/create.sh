#!/usr/bin/env bash

set -e

ROOT=$(dirname "$0")
ENV_NAME="conda-env-investing"
ENV_PATH="${ROOT}/${ENV_NAME}"

function print_info () {
  echo ""
  echo "+-----------------------------------+"
  echo " $1"
  echo "+-----------------------------------+"
  echo ""
}

print_info "install/update conda environment"
if [ -d ${ENV_PATH} ]; then
    echo "exists already -> updating"
    echo
    conda env update -f ${ROOT}/dependencies.yml -p ${ENV_PATH}
else
    conda env create -f ${ROOT}/dependencies.yml -p ${ENV_PATH}
fi

print_info "list of installed packages"
conda list -p ${ENV_PATH}
