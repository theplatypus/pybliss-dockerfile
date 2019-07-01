# Pybliss-Dockerfile

## Synopsis

Bliss is a (great) tool to check wether or not two graphs share an isomorphism, developed by Tommi Junttila and Petteri Kaski [Engineering an efficient canonical labeling tool for large and sparse graphs](http://www.siam.org/proceedings/alenex/2007/alx07_013junttilat.pdf). The work provided here is theirs.

Its sources (C++) are provided on the project [website](http://www.tcs.hut.fi/Software/bliss/) under LGPL licence, and for convenience, a Python wrapper have also been published.

Unfortunately the bindings require Python 2.x, which is quite rare as a default environment by now.

We provide here a Dockerfile of this wrapper, to get you straight to a working installation, with a few little modifications of the original : 

 - add installation of PyBliss module, so you don't have to manually add path, `import PyBliss` will work everywhere
 - add a parser function `from_dimacs`
 - add extra test script of canonical traces

## Usage 

### Prerequisites 

A working docker engine. See `https://docs.docker.com/install/`, or 

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

### Get started

```bash
# build image
docker build -t pybliss .

# run the image in an interactive container
docker run -it --rm pybliss
```

From now you are inside a debian-based anaconda container, with PyBliss available in your favorite python interpreter, `python` or `ipython`.

### Python usage

```python
import PyBliss

G = PyBliss.from_dimacs('./data/ag/ag2-3-1')
H = PyBliss.from_dimacs('./data/ag/ag2-3-2')

print(str(G.relabel(G.canonical_labeling())))

str(H.relabel(H.canonical_labeling())) == str(G.relabel(G.canonical_labeling()))
```

See `test_enumerate.py` and `test_iso.py` for further test cases.

