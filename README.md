# 📊 Numerical Analysis - Python Laboratories

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)]()

> Repository containing Python implementations of the main numerical methods studied in Numerical Analysis, with practical applications and usage examples.

## 🎯 Overview

This repository contains complete and functional implementations of fundamental numerical algorithms, developed as part of the practical work for the Numerical Analysis course. Each laboratory addresses a specific topic with robust implementations, input validation, and interactive user interfaces.

## 🚀 Available Laboratories

### 🔢 [Lab 01: Number Base Conversion (2-62)](lab01%20-%20Mudançã%20de%20bases%202-62/)
**Conversion between number bases from 2 to 62**

- **Main file**: `changeBaseMerged - final.py`
- **Features**:
  - Conversion of real numbers between bases 2 to 62
  - Support for negative numbers and decimals
  - Automatic digit mapping (0-9, A-Z, a-z)
  - Robust input validation
  - Configurable precision (8 decimal places default)

**Usage example**:
```python
# Convert 853674.07523901 from base 10 to base 16
# Result: D0A2A.133A
```

### 🔍 [Lab 02: Root Approximation](lab02%20-%20Aproximacoes%20de%20Raizes%20(funcoes)/)
**Iterative methods for finding function zeros**

- **Main file**: `Main.py`
- **Implemented methods**:
  - **Bisection Method**: Guaranteed convergence for continuous functions
  - **Newton's Method**: Quadratic convergence (requires derivative)
  - **Secant Method**: Derivative approximation by finite differences

**Characteristics**:
- Interactive interface for equation input
- Support for trigonometric and exponential functions
- Interval and convergence validation
- Configurable tolerances and maximum iterations

### 🧮 [Lab 03: Linear Equation Systems](lab03%20-%20Raizes%20de%20sistemas%20de%20equacoes%20Lineares/)
**Solving linear systems Ax = b**

- **Main file**: `Main.py`
- **Implemented methods**:
  - **Gauss-Jordan Elimination**: Exact solution for square systems
  - **Jacobi Method**: Iterative method for diagonally dominant systems
  - **Gauss-Seidel Method**: Jacobi variant with accelerated convergence

**Features**:
- Matrix input up to 3x3
- Visualization of all iterations
- Convergence analysis
- Intuitive interface for data input

### 📐 [Lab 04: Numerical Integration](lab04%20-%20Integracao%20Numerica/)
**Newton-Cotes formulas for numerical integration**

- **Main file**: `Main.py`
- **Closed Formulas**:
  - Trapezoidal Rule (degree 1)
  - Simpson's 1/3 Rule (degree 2)
  - Simpson's 3/8 Rule (degree 3)
  - Boole's Rule (degree 4)
- **Open Formulas**:
  - Midpoint Rule (degree 0)
  - Degree 1 Rule
  - Milne's Rule (degree 2)
  - Degree 3 Rule

**Resources**:
- Input by function or discrete points
- Configurable integration intervals
- Configurable precision (8 decimal places default)

### 🌐 [Lab 05: Newton's Method for Non-Linear Systems](lab05%20-%20Metodos%20de%20newton/)
**Extension of Newton's method for multivariate systems**

- **Main file**: `Metodo_Newton -ENL.py`
- **Features**:
  - Solving systems of non-linear equations
  - Automatic Jacobian matrix calculation
  - Support for trigonometric, exponential and logarithmic functions
  - Configurable tolerances and stopping criteria

**Applications**:
- Transcendental equation systems
- Optimization problems
- Electrical circuit analysis
- Physical phenomena modeling

## 🛠️ Requirements and Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Dependencies
```bash
pip install numpy sympy
```

### Installation
```bash
# Clone the repository
git clone https://github.com/kanekitakitos/analise-numerica.git

# Navigate to the directory
cd analise-numerica

# Run any laboratory
python "lab01 - Mudançã de bases 2-62/changeBaseMerged - final.py"
```

## 🔧 Project Structure

```
analise-numerica/
├── lab01 - Mudançã de bases 2-62/
│   ├── AN_Lab1.pdf
│   ├── changeBaseMerged - final.py
│   └── changeBaseMerged - final abecedario.py
├── lab02 - Aproximacoes de Raizes (funcoes)/
│   ├── AN_Lab2.pdf
│   ├── Main.py
│   ├── Metodo_Bissecao.py
│   ├── Metodo_Newton.py
│   └── Metodo_Secante.py
├── lab03 - Raizes de sistemas de equacoes Lineares/
│   ├── AN_Lab3.pdf
│   ├── Main.py
│   ├── Metodo_de_Elimininação_Gauss_Jordan.py
│   ├── Metodo_de_Gauss_Seidel.py
│   └── Metodo_de_Jacobi.py
├── lab04 - Integracao Numerica/
│   ├── AN_Lab4.pdf
│   ├── Main.py
│   ├── Newton_Cotes_Aberta.py
│   └── Newton_Cotes_Fechada.py
├── lab05 - Metodos de newton/
│   ├── AN_Lab5.pdf
│   └── Metodo_Newton -ENL.py
└── README.md
```

## 📚 Documentation

Each laboratory has a PDF file (`AN_Lab*.pdf`) containing:
- **Complete problem statement**
- **Specific technical requirements**
- **Evaluation criteria**
- **Test examples**
- **Theoretical considerations**

## 🧪 Testing and Validation

All algorithms have been tested with:
- **Standard test cases** from literature
- **Robust input validation**
- **Comprehensive error handling**
- **Convergence verification** for iterative methods

## 🎓 Educational Applications

This repository is ideal for:
- **Numerical Analysis students**
- **Scientific Computing courses**
- **Applied Mathematics laboratories**
- **Reference for numerical implementations**

## 🤝 Contributions

Contributions are welcome! To contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is under the MIT license.

## 👨‍💻 Author

Developed as part of the practical work for the **Numerical Analysis** course.

---

⭐ **If this repository was helpful, consider giving it a star!**
