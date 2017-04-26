[![Build Status](https://travis-ci.org/TaskeHAMANO/hmc_loss.svg?branch=master)](https://travis-ci.org/TaskeHAMANO/hmc_loss)

HMC-loss
====

## Abstruct
Python-implemented hierarchical multi-class validation metrics: HMC-loss .
Original paper is [(Bi&Kwok, 2012)](http://ieeexplore.ieee.org/abstract/document/6413911/) .

## Install
```
pip install hmc_loss
```

## Requirement
* numpy
* Network X

## How to use
This metrics is implemented like scikit-learn metrics.

```
from hmc_loss import hmc_loss_score, get_cost_list
import numpy as np

# Generate label data(2-D array of numpy)
true_label = np.random.randint(2, size(100, 100))
pred_label = np.random.randint(2, size(100, 100))

# Generate test graph(Di-Graph of NetworkX)
graph = nx.gnc_graph(100)
# Generate element list of graph node
label_list = list(range(100))
# Calculate cost of each node in graph
cost_list = get_cost_list(graph, 0, label_list)
# Calculate HMC-loss
hmc_loss_score(true_label, pred_label, graph, 0, label_list, cost_list, alpha=0.5, beta=1.5)

```

## Licence
[MIT](http://choosealicense.com/licenses/mit/)

## Author
[Taske HAMANO](https://github.com/TaskeHAMANO)
