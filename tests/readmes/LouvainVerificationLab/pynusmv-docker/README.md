# Pynusmv-Docker

This repository contains the dockerfile configurations associated with the different images related to pynusmv.
In particular, it containts:

## python
The content of this folder corresponds to the `louvainverificationlab/pynusmv` image on dockerhub. 
This image serves the purpose of providing you with an immediate access to a working python3 process having pynusmv installed.

### How to use it
To use this image, simply type the following command:
```
docker run -it louvainverificationlab/pynusmv
```

## manylinux
The content of this folder corresponds to the `louvainverificationlab/pynusmv-manylinux` image on dockerhub.
This container lets you build versions of pynusmv that should be binary compatible accross a wide range of linux platforms (this is the environment used to produce the linux wheels that are published on PyPI).

### How to use it
To produce the binary wheels, just run: 
```
docker run -it louvainverificationlab/pynusmv-manylinux bash
cd pynusmv
git pull # or checkout TAG
../release.sh
```

**Your wheels are located in /pynusmv/wheelhouse**
**Don't forget to remove the .linux_x86_64 suffix to publish these on PyPI**

## build
The content of this folder corresponds to the `louvainverificationlab/pynusmv-build` image on dockerhub.
This container provides you with a nice playground to tweak and build your version of pynusmv.

### How to use it
To use this image, proceed as follows:
```
docker run -it louvainverificationlab/build bash
```

and then
```
cd home
git clone https://github.com/LouvainVerificationLab/pynusmv.git
cd pynusmv

# Do whatever changes you like to the source code

python3 setup.py install
```

### References:
- https://github.com/LouvainVerificationLab/pynusmv
- https://www.python.org/dev/peps/pep-0513/
- https://github.com/pypa/manylinux
- https://github.com/pypa/python-manylinux-demo 
