Title: PyLR, an OpenLR decoder in python
Date: 2014-12-04
Slug: PyLR, an OpenLR decoder in python
Author: Mappy
Tags: OpenLR,Python,OpenSource,English
Summary: An Open source python implementation of OpenLR specification.

# PyLR, an OpenLR decoder in python #

Here, at Mappy, we have decided to release our implementation of the [OpenLR](http://www.openlr.org) specification.

To make a story short, OpenLR is an open source  software project launched by TomTom in september 2009. This is an attempt to provide a location referencing method that works between digital maps of different vendors or versions.

We use traffic informations from 10 countries in Europe in [DATEX](http://datex2.easyway-its.eu/content/datex) format, location reference was provided using the [TMC](https://en.wikipedia.org/wiki/Traffic_message_channel) reference system.
The problem with TMC is that the coverage of the road network is relatively less than optimal. Because TomTom was providing information on a larger portion of the road network (in theory, the whole network could be covered) using its OpenLR scheme, we have decided to drop TMC in favor of OpenLR.

The basics:

OpenLR data provide paths or that must be "decoded" on the destination network (also called 'map' in the OpenLR terminology) by computing the shortest path between location reference points and a bunch of values representing the physical properties of the network at these points.

So, what is PyLR ?

PyLR is a partial Python implementation of the OpenLR specification largely inspired from the reference implementation in Java (available on the OpenLR site).

It is partial in the sense that only parser/decoder is provided, encoding et serializing OpenLR data is not supported at the moment.

While still a work in progress, it is actually used in production here at Mappy.
For information, our implementation fail to decode less than 1% of the collected traffic situations, which correspond mostly to mismatched data with our network database.
 
PyLR implement a decoder from the binary/base64 data representation (xml is not handled at the moment). It implements also a decoder that use an abstract representationof the targeted map.


At the moment, PyLR is not really usable out of the box: you still need to implement a concrete database and a shortest path algorithm for playing with the library.

As stated before, it is a work in progress, we have plan to provide more tools for testing and playing around with the lib: stay tuned !!!!


PyLR is available on [github](https://github.com/Mappy/PyLR) and is released under the Apache licence, version 2.

