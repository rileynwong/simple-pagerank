# simple-pagerank

Pagerank using directed graph. See [demo](demo.py) for usage.

Graphs are represented by nodes containing pointers to inbound and outbound neighbors.

This implementation calculates the general case for each node:
![pagerank](https://i.imgur.com/7QZPQ9c.png)


## Tests
To run tests, install [nosetests](http://nose.readthedocs.io/en/latest/usage.html) with:
`$ pip install`

And then simply run:
`$ nosetests` 
