# Databricks notebook source
# MAGIC %md Test runner for `pytest`

# COMMAND ----------

#!cp ../requirements.txt ~/.
#%pip install -r ~/requirements.txt
#%pip install -r ../requirements.txt

# Install packages individually
%pip install attrs==21.4.0
%pip install cycler==0.11.0
%pip install fonttools==4.33.3
%pip install iniconfig==1.1.1
%pip install kiwisolver==1.4.2
%pip install matplotlib==3.5.1
%pip install numpy
%pip install packaging==21.3
%pip install pandas==1.4.2
%pip install pillow==9.3.0
%pip install pluggy==1.0.0
%pip install py==1.11.0
%pip install py4j==0.10.9.5
%pip install pyarrow
%pip install pyparsing==3.0.8
%pip install pyspark==3.2.2
%pip install pytest==7.2.0
%pip install python-dateutil==2.8.2
%pip install pytz==2022.1
%pip install six==1.16.0
%pip install tomli==2.0.1
%pip install wget==3.2

# import os

# # os.chdir('..')
# current_dir = os.getcwd()
# print(f"Files in {current_dir}:\n")
# with os.scandir(current_dir) as entries:
#     for entry in entries:
#         print(entry.name)


# print(f"Current path is {os.getcwd()} ")
# requirements_path = '../requirements.txt'

# if os.path.exists(requirements_path):
#     with open(requirements_path, 'r') as file:
#         print(file.read())
#     %pip install -r requirements_path
# else:
#     print(f"File {requirements_path} does not exist.")

# COMMAND ----------

# pytest.main runs our tests directly in the notebook environment, providing
# fidelity for Spark and other configuration variables.
#
# A limitation of this approach is that changes to the test will be
# cache by Python's import caching mechanism.
#
# To iterate on tests during development, we restart the Python process 
# and thus clear the import cache to pick up changes.
dbutils.library.restartPython()

import pytest
import os
import sys

# Run all tests in the repository root.
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
repo_root = os.path.dirname(os.path.dirname(notebook_path))
os.chdir(f'/Workspace/{repo_root}')
%pwd

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

retcode = pytest.main([".", "-p", "no:cacheprovider"])

# Fail the cell execution if we have any test failures.
assert retcode == 0, 'The pytest invocation failed. See the log above for details.'
