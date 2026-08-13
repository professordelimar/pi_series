# Reproducibility Guide

**Author:** Nelson Ribeiro-Filho

This document defines recommended procedures for reproducible numerical experiments in the Pi Series project.

## 1. Computational environment

For every final experiment intended for scientific comparison, record:

- Python version;
- operating system;
- processor when execution time is analyzed;
- package versions;
- precision configuration;
- number of repetitions used in timing experiments.

A dependency snapshot may be generated with:

```bash
pip freeze > environment.txt
```

## 2. Reference value

Use an arbitrary-precision reference value for π.

For example:

```python
import mpmath as mp

mp.mp.dps = 100
pi_reference = mp.pi
```

The reference precision must exceed the precision being evaluated.

## 3. Error metrics

At minimum, record:

- absolute error;
- relative error;
- number of correct decimal digits.

Do not compare only the visually displayed decimal representation.

## 4. Iteration count

The meaning of one iteration must be clearly defined for each method.

Different algorithms perform different amounts of work per iteration, so iteration count alone should not be interpreted as computational efficiency.

## 5. Execution time

Timing experiments should:

- exclude plotting whenever possible;
- exclude file saving whenever possible;
- use repeated measurements;
- report a representative statistic such as median or mean;
- use the same machine when methods are directly compared.

Python's `time.perf_counter()` is appropriate for many experiments.

## 6. Precision

Clearly distinguish between:

- standard double precision;
- arbitrary precision;
- algorithmic convergence;
- floating-point limitations.

A method may theoretically continue converging even after standard floating-point arithmetic can no longer represent the improvement.

## 7. Stopping criteria

Possible stopping criteria include:

- fixed number of iterations;
- target absolute error;
- target relative error;
- target number of correct digits;
- maximum execution time.

The selected criterion must be reported.

## 8. Random methods

For Monte Carlo methods:

- record the random seed;
- record the number of samples;
- repeat experiments using multiple seeds when statistical variability is being studied.

Example:

```python
import numpy as np

rng = np.random.default_rng(42)
```

## 9. Data tables

Final comparison tables should preferably include:

- method name;
- number of iterations or samples;
- approximation of π;
- absolute error;
- relative error;
- correct decimal digits;
- execution time;
- precision setting.

## 10. Figures

Figures intended for scientific use should clearly identify:

- axes;
- units when applicable;
- logarithmic scales;
- method names;
- number of iterations or samples;
- error metric.

## 11. Final publication results

Before generating final tables and figures for a scientific manuscript:

1. recreate the Python environment;
2. verify dependency versions;
3. run all methods from a clean state;
4. regenerate the result tables;
5. regenerate all figures;
6. verify numerical consistency;
7. archive the final configuration used in the publication.

## 12. Source-code changes

Changes affecting algorithms, stopping criteria, error metrics or benchmark procedures should be committed separately in Git so that the scientific evolution of the project remains traceable.
