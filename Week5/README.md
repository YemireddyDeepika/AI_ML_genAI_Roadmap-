# 🚀 Week 5 – Deep Learning Foundations (Days 31–37)

Week 5 marks the transition from **Machine Learning → Deep Learning**.
In this week, I learned the **core concepts of neural networks** and built my **first real Deep Learning project** using the **MNIST handwritten digit dataset**.

---

# 🧠 Topics Covered

## 🔹 Day 31 – Perceptron

* Basic **single-neuron model** for binary classification
* Linear decision boundary
* Limitation: cannot solve **non-linear problems (XOR)**

📌 Outcome: Understanding the **foundation of neural networks**.

---

## 🔹 Day 32 – Artificial Neural Networks (ANN)

* Multi-layer structure:

  * Input layer
  * Hidden layer(s)
  * Output layer
* Hidden layers enable **non-linear learning**
* ANN can solve **complex real-world patterns**.

📌 Outcome: Clear understanding of **deep learning architecture**.

---

## 🔹 Day 33 – Backpropagation

* Training loop:

  1. Forward propagation
  2. Loss calculation
  3. Gradient computation
  4. Weight update using **gradient descent**
* Concepts:

  * Learning rate
  * Vanishing gradient problem

📌 Outcome: Learned **how neural networks actually learn**.

---

## 🔹 Day 34 – Activation Functions

* **ReLU** → hidden layers (most used)
* **Sigmoid** → binary classification output
* **Softmax** → multi-class classification output

📌 Outcome: Choosing the **right activation for each layer**.

---

## 🔹 Day 35 – Optimizers

* **SGD**, **Momentum**, **Adam** comparison
* Adam provides **fast and stable convergence**
* Importance of **learning rate tuning**.

📌 Outcome: Understanding **efficient neural network training**.

---

# 🧪 Days 36–37 – ANN Project: MNIST Digit Classification

## 📊 Dataset

* **MNIST handwritten digits (0–9)**
* 70,000 grayscale images
* Image size: **28×28 pixels**

## ⚙️ Steps Performed

* Data normalization (0–255 → 0–1)
* Image flattening for ANN (28×28 → 784 features)
* ANN architecture with:

  * Dense hidden layers + ReLU
  * Softmax output layer
* Training using:

  * **Adam optimizer**
  * **Sparse categorical cross-entropy loss**
* Model evaluation on test data
* Visualization of predictions and training accuracy.

## 📈 Result

* Achieved **~95%+ test accuracy** using ANN.
* Demonstrated **complete deep learning workflow** from preprocessing → training → evaluation → prediction.

📌 This is my **first Deep Learning project** and a key **portfolio milestone**.

---

# 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib
* TensorFlow / Keras
* Jupyter Notebook
* Git & GitHub

---

# 📂 Suggested Folder Structure

```
Week5_Deep_Learning/
│
├── Day31_Perceptron/
├── Day32_ANN/
├── Day33_Backpropagation/
├── Day34_Activation_Functions/
├── Day35_Optimizers/
├── Day36_37_MNIST_ANN_Project/
│
└── README.md
```

---

# 🏆 Week 5 Outcome

After completing Week 5, I can:

* Explain **neural network fundamentals** clearly
* Understand **backpropagation, activations, and optimizers**
* Build and train an **ANN model from scratch**
* Work with **image datasets in Deep Learning**
* Deliver a **GitHub-ready Deep Learning project**

➡ This week represents my transition from **ML learner → Deep Learning beginner**.

---

