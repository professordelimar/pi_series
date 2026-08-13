# Pi Series

Computational experiments for comparing different numerical methods, infinite series, products and algorithms for approximating the mathematical constant **π (pi)**.

## About

This repository contains Python implementations and numerical experiments designed to compare different approaches for approximating π.

The project emphasizes not only the numerical value obtained by each method, but also its **convergence behavior, accuracy, computational cost and efficiency**.

The repository is intended for mathematical experimentation, teaching, numerical analysis and reproducible scientific research.

One of its main objectives is to provide the computational basis for a comparative scientific study of π approximation methods.

## Research questions

The computational experiments may investigate questions such as:

- How quickly does each method converge to π?
- How many iterations are required to obtain a given number of correct decimal digits?
- How does absolute error decrease as the number of iterations increases?
- How does relative error behave?
- What is the computational cost of each method?
- Which methods offer the best balance between accuracy and execution time?
- How do classical infinite series compare with modern high-convergence algorithms?
- How stable are the methods under finite-precision arithmetic?
- How does arbitrary-precision arithmetic affect the results?

## Methods

The repository may include implementations of classical and modern approaches such as:

### Infinite series

- Gregory-Leibniz series
- Nilakantha series
- Madhava-type series
- Arctangent series
- Machin-like formulas
- Basel-related formulations when mathematically appropriate

### Infinite products

- Wallis product
- Viète product

### Iterative algorithms

- Gauss-Legendre algorithm
- Arithmetic-geometric mean methods

### High-convergence formulas

- Ramanujan-type series
- Chudnovsky algorithm

### Geometric methods

- Polygon approximation
- Inscribed and circumscribed polygon methods

### Stochastic methods

- Monte Carlo estimation

### Additional experiments

Other mathematically valid approximation methods may be added for comparison.

## Evaluation metrics

Each method should preferably be evaluated using a common set of metrics.

### Accuracy

- Absolute error
- Relative error
- Number of correct decimal digits
- Difference from a high-precision reference value

For an approximation \\(\\pi_n\\), the absolute error can be defined as:

\\[
E_{abs} = |\\pi - \\pi_n|
\\]

and the relative error as:

\\[
E_{rel} = \\frac{|\\pi - \\pi_n|}{|\\pi|}
\\]

### Convergence

Possible convergence analyses include:

- error versus iteration;
- logarithm of error versus iteration;
- number of correct digits versus iteration;
- empirical convergence rate;
- asymptotic behavior.

### Computational performance

Possible computational metrics include:

- execution time;
- number of iterations;
- number of arithmetic operations when practical;
- memory usage when relevant;
- precision level;
- accuracy per unit of computational time.

## Reference value of π

For high-precision comparisons, the reference value should not be limited to standard double-precision floating-point arithmetic.

Arbitrary-precision tools such as **mpmath** or **SymPy** may be used to generate reference values with a controlled number of decimal digits.

Example:

```python
import mpmath as mp

mp.mp.dps = 100
pi_reference = mp.pi
```

## Experimental principles

To ensure fair comparisons between methods:

1. use the same reference value of π;
2. record the number of iterations;
3. record execution time using the same measurement strategy;
4. use consistent precision settings;
5. distinguish convergence error from floating-point limitations;
6. repeat timing experiments when necessary;
7. avoid including plotting time in algorithm execution time;
8. store results in reproducible tables;
9. document stopping criteria;
10. record software and dependency versions when producing final scientific results.

## Suggested outputs

Computational experiments may generate:

- convergence curves;
- absolute-error curves;
- relative-error curves;
- execution-time comparisons;
- accuracy-versus-time plots;
- number-of-digits-versus-iteration plots;
- summary tables;
- ranking of algorithms according to different criteria.

## Programming language

The primary programming language is **Python**.

Typical scientific-computing tools used in this repository include:

- NumPy
- SciPy
- Matplotlib
- Pandas
- SymPy
- mpmath
- Jupyter

## Installation

Clone the repository:

```bash
git clone https://github.com/professordelimar/pi_series.git
```

Enter the repository:

```bash
cd pi_series
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the codes

Python scripts can generally be executed with:

```bash
python filename.py
```

Jupyter notebooks can be opened with:

```bash
jupyter notebook
```

Specific experimental parameters should be documented inside individual scripts, notebooks or configuration files.

## Reproducibility

Scientific comparisons should be reproducible.

The main principles for reproducing experiments are described in:

[REPRODUCIBILITY.md](REPRODUCIBILITY.md)

## Scientific use

This repository is designed to support numerical experimentation and research on approximation algorithms for π.

When results from this repository are used in a manuscript, presentation or scientific publication, the exact method, precision, stopping criterion, number of repetitions and computational environment should be documented.

## References

The project uses historical and modern references in numerical analysis, infinite series, approximation theory and algorithms for computing π.

See [REFERENCES.md](REFERENCES.md).

## Citation

If this repository or its codes contribute to academic work, please cite the repository and any associated scientific publication.

Citation metadata are provided in [CITATION.cff](CITATION.cff).

## Related repository

General numerical mathematics codes are maintained separately in:

- https://github.com/professordelimar/matematica

## Author

**Nelson Ribeiro-Filho**

## Copyright and ownership

Original source code, documentation and other original materials in this repository belong to:

**64.200.407 NELSON DE LIMA RIBEIRO FILHO - ME**  
**CNPJ 64.200.407/0001-45**

All rights reserved unless explicitly stated otherwise.

See [LICENSE](LICENSE) for details.

## Social links

- Instagram: https://www.instagram.com/professordelimar/
- YouTube: https://www.youtube.com/@professordelimar
