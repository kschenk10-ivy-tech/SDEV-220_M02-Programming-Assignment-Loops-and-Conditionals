#!/usr/bin/env python
# coding: utf-8

# <div style="float:left;"><h1>Anaconda Notebooks</h1></div>
# <div style="float:right;"><img width="300" src="https://files.anaconda.com/production/company/Anaconda_Logo_RGB_Corporate.svg" /></div>
# 

# Welcome to Anaconda Notebooks! Here, you can create and run interactive notebooks in a browser, from anywhere, immediately!

# ## Table of Contents
# 
# - [About Anaconda Notebooks](#About-Anaconda-Notebooks)
# - [New to JupyterLab?](#New-to-JupyterLab?)
# - [Conda Environments](#Conda-Environments)
# - [Frequently Asked Questions](#Frequently-Asked-Questions)

# ## About Anaconda Notebooks

# ### What is Anaconda Notebooks?
# 
# Anaconda Notebooks is a hosted [JupyterLab](https://jupyter.org/) service, powered by [PythonAnywhere](https://www.pythonanywhere.com/), that enables you to run JupyterLab notebooks reliably online. We take care of the installation, setup, and infrastructure management, so you can be productive right away. 
# 
# Also, by using a hosted notebook service, you can connect to your notebooks from anywhere and on any device with a browser!
# 
# With your account you get:
# 
# - A hosted JupyterLab instance running in a dedicated [JupyterHub](https://jupyter.org/hub) environment
# - Persistent cloud storage that can be used to store notebooks, environments, data, and more
# - An allotment of CPU seconds every day (see [FAQ](#Frequently-Asked-Questions) below)
# - Pre-configured conda environments with common data science packages 
# - The ability to create your own custom environments

# ### How can I get help?
# 
# Anaconda provides a number of resources should you need help:
# 
# - We offer a catalog of courses through [Anaconda Learning](https://learning.anaconda.cloud) that are included in your subscription
# - Our [community forums](https://community.anaconda.cloud/c/product-help/notebooks) are full of useful content and people that can answer your questions
# - For non-technical requests (billing, login, etc.) you can [submit a ticket](https://support.anaconda.com/hc/en-us/requests/new?ticket_form_id=360006825553) to our user care team
# - Further information is available in our [documentation](https://docs.anaconda.com/free/anaconda-notebooks/index.html)

# <div style="float:left;"><h2>New to JupyterLab?</h2></div>
# <div style="float:right;"><img height="65" width="172" src="https://jupyter.org/assets/logos/rectanglelogo-greytext-orangebody-greymoons.svg" /></div>

# If you haven't used [Jupyter](https://jupyter.org) (Lab or Notebooks) before, read on to get started. 

# ### The Notebook
# 
# The document you're looking at now is actually a notebook! Notebooks, like this one, are made up of cells. Each cell can contain markdown (like this one), code, or raw text.
# 
# You can click on a cell to select it, or use the arrow keys to move up and down through cells. 
# 
# For markdown cells, press **Enter/return** to edit the cell, then **Shift+Enter/return** to display it with formatting. Try that here: select this cell, press **Enter** to view the text in markdown, and then press **Shift+Enter** to display it again.
# 
# Now for some code. The following cell contains a basic Python print statement. Select that cell and press **Shift+Enter** to run the code and see the output beneath it.

# In[ ]:


print("Welcome to Anaconda Notebooks!")


# That's just the very basics, but if you want to learn more, try some of the tutorials at [Anaconda Learning](https://learning.anaconda.cloud).

# ### The JupyterLab Interface
# 
# If you'd like to learn more about the JupyterLab interface, refer to [Jupyterlab's Interface guide](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) to learn the ins and outs of your interactive development environment (IDE).

# <div style="float:left;"><h2>Conda Environments</h2></div>
# <div style="float:right;"><img height="65" width="172" src="https://docs.conda.io/en/latest/_images/conda_logo.svg" /></div>

# This service comes with conda pre-installed, along with "batteries included" environments to get you started.

# ### What are the "batteries included" environments?
# 
# Since custom environments can take up a lot of your storage space, we've provided a number of read-only environments based on the Anaconda Distribution. You cannot add packages to these default environments, so you'll need to create a new environment if you wish to do so.
# 
# The general naming convention is generally "anaconda-\<YEAR>.\<MONTH>-py\<PYTHON_VERSION>" which maps to Anaconda Distribution releases. 

# In[ ]:


# Run this cell to see the list of environments available
get_ipython().system('conda env list')


# Environments beginning with ``/opt/conda`` are read-only default environments.

# In[ ]:


# To see the list of packages in an environment, run this cell
get_ipython().system('conda list')


# ### Creating Custom Environments
# 
# If you need a specific set of packages that are not included in one of our default environments, you can create your own.
# 
# <span style="color:red">**WARNING** Custom environments will use your personal storage space and can easily get quite large, so only include the packages you need.</span>
# 
# To create a new environment, open a new terminal from the Anaconda Notebooks home page. Then, run the command below. You can even use the same command to specify the version of a package to install within your new environment by adding the package and version number to the end of the command.

# In[ ]:


# Run this command to create a custom environment running Python 3.9
# ipykernel is required as well if you'd like to use the environment in a notebook
get_ipython().system('conda create --name <NAME_OF_ENVIRONMENT> python=3.9 ipykernel -y')


# <span style="color:blue">**INFO** Either the ipykernel or notebook package must be in your environment if you'd like to use it as a notebook kernel.</span>

# It should take a minute or two for your environment to be created. Afterwards, the environment will appear in the **Select Kernel** modal (see Activating custom environments below) after roughly 30 seconds. You might need to close and reopen the README.ipynb or refresh the browser for the kernel to appear.

# ### Activating custom environments
# 
# There are a couple ways to activate your environment:
# 
# * Click the kernel at the top right of the notebook ("anaconda-\<YEAR>.\<MONTH>-py\<PYTHON_VERSION>"), then switch to the kernel of the environment you created in the **Select Kernel** modal.
# * From the Launcher, select the notebook displaying your custom environment name.

# ### Installing packages
# 
# You can then install any further packages you need by running the following:

# In[ ]:


get_ipython().system('conda install <PACKAGE_NAME> -y')


# ## Frequently Asked Questions

# ### My notebook is trying to import a package, but I'm getting an error
# 
# The most common cause of errors is a lack of required package(s) installed in your environment. The default environment we provide, based on the Anaconda distribution, provides hundreds of the most common python packages for data science, but it doesn't include everything. You may need to create a custom environment to install the package you need.

# Here are a couple of steps to help resolve this:
# 
# #### Make sure you have the right kernel/environment selected 
# 
# The default `anaconda-<YEAR>.<MONTH>-py<PYTHON_VERSION>` environments have a broad selection of packages, but you may have created a custom environment for your notebook. Separate environments are represented as “kernels” in JupyterLab. You can view and switch between available kernels by clicking the kernel name in the upper-right corner of the content pane.
#     
# #### List the packages available in an environment
# 
# You can see which packages are available in each environment in the terminal by running `conda env list` to list available environments and then `conda list -n <NAME_OF_ENVIRONMENT>` to see packages in that environment.
# 
# **Note:** you can run those commands directly in a code cell within your notebook just by adding a “!” to the front of the command (e.g. `!conda env list`).
# 
# #### Create a custom environment
# 
# If none of your existing environments have the right package(s), either install the package into one of your custom environments with `conda install <PACKAGE>` or create a new custom conda environment with the right packages. See [Creating Custom Environments](#Creating-Custom-Environments) above for instructions.
# 
# Once an environment is created, it will be available as a kernel for running your notebook.
# 

# ### Why isn't my custom environment showing up in the launcher/list of notebook kernels?
# 
# The most common reason is that you don't have the `ipykernel` package in your environment, which is required to use an environment as a notebook kernel.
# 
# You can check if that package is installed by following these steps: 
# 
# - Open a new Terminal from the launcher
# - run `conda list -n <NAME_OF_ENVIRONMENT>`
# - ensure that `ipykernel` is listed
# 
# If not, you can easily install it with `conda install -n <NAME_OF_ENVIRONMENT> ipykernel`

# ### How do I upload a notebook to the service?
# 
# In the Anaconda Notebooks JupyterLab interface, click the **Upload files** button in the File Browser to browse for a local .ipynb file. Then, click **Open**. The notebook will appear in the left-hand menu. 
# 
# You can also drag and drop a notebook from a folder on your system to the file browser to upload it.

# ### How do I save a notebook?
# 
# Like most IDEs or editors, JupyterLab has the standard "Save" and "Save As…" functions that will save a notebook in your directory on our platform. You can also download a notebook file from the File menu to save it locally.

# ### How do I share a notebook?
# 
# For now, the easiest way to share a notebook is to download and then share it as you would any other file. However, a key feature on our near-term roadmap is the ability to share notebooks directly from our platform. Stay tuned!

# ### What do I do if I run out of storage space/go over my quota?
# 
# <span style="color:red">**WARNING** Creating custom environments consumes a large amount of storage. Anaconda recommends free tier Notebooks users avoid custom environments.</span>
# 
# You can check the status of your disk usage via the widget in the top right of the screen, which shows current usage as a percentage of the total space available.
# 
# The option to upgrade your account and expand your storage is coming soon; for now, you will need to either upgrade your subscription or delete some items from your drive:
# 
# #### Do you have any extra notebooks or directories you can remove?
# 
# You can view and delete files from the File Browser in the upper left, or on the command line by launching a terminal.
# 
# #### Do you have any custom conda environments? 
# 
# - Run `conda env list` and see if there are any environments **NOT** in `/opt/conda`. 
# - If there are, you can remove those that you don’t need any more by running `conda env remove -n <NAME_OF_ENVIRONMENT>`.
# - Further, running `conda clean --all` will clean up the cache and some other artifacts.

# ### Are there memory limits on this service?
# 
# On this service, each process is limited to 6GB of memory. If you exceed that, your process will be killed. If you have the need to run much larger processes, please contact Anaconda Sales.

# ### What can I do if my notebook is running really slowly?
# 
# You may have exceeded your CPU usage limit for the day. Our notebook instances have a limit for the maximum number of seconds fully utilizing the CPU. Once an instance hits that limit, it is not shut down, but instead given lower CPU priority and a limit to the amount of compute resources available. This limit is reset every day, so full compute access will be restored the next day.
# 
# To see current progress towards your daily quota, reference the widget in the upper right of the interface that shows current CPU usage vs. the daily limit.
# 
# To better manage your CPU usage, regularly check the **Running Terminals and Kernels** widget in the left sidebar to kill unnecessary kernels when you no longer need them.

# ### I'm registered/signed in—why isn't Notebooks opening?
# 
# Your browser's pop-up blocker (automatically enabled on Firefox and Safari) may have prevented Notebooks from opening. 
# 
# Disable your pop-up blocker and try opening Notebooks again from anaconda.cloud. 

# ### I have upgraded from the free tier to a paid tier, but I am unable to connect to certain websites. Why?
# 
# Unrestricted internet access is only activated in new Notebooks processes. Therefore, Anaconda recommends restarting the kernel or starting a new notebook.
# 
# Free tier users have access to the websites on [our allowlist](https://anaconda.cloud/free-tier-allowlist). 

# In[ ]:




