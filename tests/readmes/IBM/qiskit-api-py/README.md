# Python API Client IBM Quantum Experience

The official API Client to use [IBM Quantum Experience](https://quantumexperience.ng.bluemix.net/) in Python.

This package can be use in [Jupyter Notebook](https://jupyter.org/).

* [Installation](#installation)
* [Getting Started](#getting-started)
* [Methods](#methods)
* [GIST Jupyter](#jupyter)
* [Reference](#reference)

## Installation

You can install me using `pip` or `easy_install`. For example, from the command line:

    $ pip install IBMQuantumExperience

To install the package in Jupyter, you have to run in a Notebook:

```python
import pip
def install(package):
   pip.main(['install', package])
install('IBMQuantumExperience')
```

or, if you want the standard output, one could even use the exclamation bang:

```python
! pip install IBMQuantumExperience
```

### Getting Started

Now it's time to begin doing real work with Python and IBM Quantum Experience.

First, import our API Client:

```python
from IBMQuantumExperience import IBMQuantumExperience
```

Then, initialize your IBM Quantum Experience connection by supplying your *token*. You can obtain the token from **Account** area of *Quantum Experience Platform* in *Personal Access Token* section. An optional object knows as *config* has several extra options to customize, like the url of the API:

```python
api = IBMQuantumExperience("token", config)
```

By default, the config parameter is defined like:

```
config = {
   "url": 'https://quantumexperience.ng.bluemix.net/api'
}
```

### Methods

#### Codes

To get the information of a Code, including the last executions about this Code, you only need the codeId:

```python
api.get_code("id_code")
```

To get the information about the last Codes, including the last executions about these Codes, you only need call:

```python
api.get_last_codes()
```

#### Execution

To get all information (including the Code information) about a specific Execution of a Code, you only need the executionId:

```python
api.get_execution("id_execution")
```

To get only the Result about a specific Execution of a Code, you only need the executionId:

```python
api.get_result_from_execution("id_execution")
```

#### Running [QASM 2.0](https://github.com/IBM/qiskit-openqasm)

To execute a [QASM 2.0](https://github.com/IBM/qiskit-openqasm) experiment:

```python
api.run_experiment(qasm, device, shots, name=None, timeout=60)
```

- **qasm**: The QASM 2.0 code to run. Eg: 
``` qasm = 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nh q[0];\ncx q[0],q[2];\nmeasure q[0] -> c[0];\nmeasure q[2] -> c[1];\n'``
- **device**: Type of device to run the experiment. Only two option possibles: *simulator* or *real*. Eg:
```device = 'real' ```
- **shots**: Number of shots of the experiments. Maximum 8192 shots. Eg:
```shots = 1024 ```
- **name**: Name of the experiment. This paramater is optional, by default the name will be 'Experiment \#YmdHMS'. Eg:
```name = 'bell state experiment'``
- **timeout**: Time to wait for the result. The maximum timeout is 300. If the timeout is reached, you obtain the executionId to get the result with the getResultFromExecution method in the future. Eg:
```timeout = 120``

#### Running Jobs [QASM 2.0](https://github.com/IBM/qiskit-openqasm)

To execute jobs about [QASM 2.0](https://github.com/IBM/qiskit-openqasm) experiments:

```python
api.run_jobs(qasms, device, shots, max_credits)
```

- **qasms**: A list of objects with the QASM 2.0 information. Eg: 
```
[
   { 'qasm': 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nh q[0];\ncx q[0],q[2];\nmeasure q[0] -> c[0];\nmeasure q[2] -> c[1];\n'},
   { 'qasm': 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nx q[0];\nmeasure q[0] -> c[0];\n'}
]
```
- **device**: Type of device to run the experiment. Only two option possibles: *simulator* or *real*. Eg:
```device = 'real' ```
- **shots**: Number of shots of the experiments. Maximum 8192 shots. Eg:
```shots = 1024 ```
- **max_credits**: Maximum number of the credits to spend in the executions. If the executions are more expensives, the job is aborted. Eg:
```max_credits = 3```

To get job information:

```python
api.get_job(id_job)
```

- **id_job**: The identifier of the Job. Eg: 
``` 
    id_job = '9de64f58316db3eb6db6da53bf9135ff'
```

#### Get information about a Device

To know the status (if it is running or in maintenance) of a device (real chip 5Q by default) you can run:

```python
api.device_status(device)
```

- **device**: The device to get its availability. By default is the 5 Qubits Real Chip. Eg:
```device='qx5q' ```


#### Jupyter

To show the result and the code in Jupyter, you can use the next snippet that has some visual representation functions:

```
# USER, PLEASE SET CONFIG:
token="_TOKEN_"
# ---- UTILS -----
from IBMQuantumExperience import IBMQuantumExperience
from IPython.display import Image, display
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
api = IBMQuantumExperience(token)
def showImageCode(idCode):
    if (idCode):
        code = api.get_image_code(idCode)
        if (code.get('error', None)):
            print("Failed to recover the Code")
        else:
            display(Image(code['url']))
    else:
        print("Invalid IdCode")
def printBars(values, labels):
    N = len(values)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, values, width, color='r')
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Probabilities')
    ax.set_xticks(ind + (width/2.))
    ax.set_xticklabels(labels)
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%f' % float(height),
                    ha='center', va='bottom')
    autolabel(rects1)
    plt.show()
def showResultsByExecution(executionRaw):
    result = executionRaw.get('result', {})
    data = result.get('data', {})
    print('Execution in ' + executionRaw.get('deviceRunType', 'Unknown') + ' at ' + executionRaw.get('endDate', 'Unknown'))
    if (data.get('p', None)):
        values = data['p']['values']
        labels = data['p']['labels']
        printBars(values, labels)
    else:
        print("Not plotted. Results are: "+str(executionRaw))
def showResultsByIdExecution(idExecution):
    execution = api.get_result_from_execution(idExecution)
    if (execution.get('measure', None)):
        values = execution['measure']['values']
        labels = execution['measure']['labels']
        printBars(values, labels)
    else:
        print("Not plotted. Results are: "+str(execution))
def showLastCodes():
    codes = api.get_last_codes()
    for code in codes:
        print("--------------------------------")
        print("Code " + code.get('name', 'Unknown'))
        print(" ")
        showImageCode(code.get('id', None))
        print("------- Executions -------------")
        for execution in code.get('executions', []):
            showResultsByExecution(execution)
```

## Deploy and Test

If you want participate in the project, you can clone the repository and install the dependencies to run it.

You can do a pull request to improve or add any functionality.

You can run the tests under ```test``` folder. See the test/README file to more information.

## Reference

[IBM Quantum Experience Tutorial](https://quantumexperience.ng.bluemix.net/qstage/#/tutorial?sectionId=c59b3710b928891a1420190148a72cce&pageIndex=0)

[IBM Quantun Experience Community](https://quantumexperience.ng.bluemix.net/qstage/#/community)

[OPENQASM](https://github.com/IBM/qiskit-openqasm)
