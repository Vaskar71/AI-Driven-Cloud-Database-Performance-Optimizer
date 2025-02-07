# AI-Based Cloud Database Management System  
🚀 **An AI-powered database management system that optimizes query performance and safeguards data integrity using Flask, SQLAlchemy, and Scikit-learn.**

## 📖 Description  

The **AI-Based Cloud Database Management System** is a Flask-powered API that allows users to manage simulated cloud database transactions while utilizing a basic AI model to suggest query optimizations. The project enables **storing, retrieving, and analyzing** database transactions while providing **automated AI-based recommendations** to improve performance.  

This system simulates a **real-world cloud database** where AI-driven analytics optimize query execution times based on **historical transaction data**.

---

## 🛠 Tech Stack & Why  

| **Technology**       | **Purpose** |
|----------------------|-------------|
| **Flask**           | Lightweight web framework for API development. |
| **Flask-SQLAlchemy** | ORM for managing database interactions. |
| **SQLite**          | Simple and efficient local database. |
| **Scikit-learn**    | AI module for performance optimization. |
| **pandas**          | Data handling and preprocessing. |
| **python-dotenv**   | Securely managing environment variables. |

🔹 **Why These Technologies?**  
- Flask is **easy to use** and **lightweight**, perfect for building RESTful APIs.  
- SQLAlchemy simplifies database operations without complex SQL queries.  
- SQLite provides a **lightweight, embedded database** for local testing.  
- Scikit-learn enables **simple AI-based performance tuning** using regression models.  

---

## 🏗 Installation & Setup  

### 🔹 1. Clone the Repository  
```bash
git clone https://github.com/Vaskar71/AI-Driven-Cloud-Database-Performance-Optimizer.git
cd AI-Cloud-DB-Management
```

### 🔹 2. Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 🔹 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 🔹 4. Set Up Environment Variables  
Create a `.env` file and add the following configuration:  
```ini
FLASK_APP=app.py
FLASK_DEBUG=1
DATABASE_URL=sqlite:///cloud_db.sqlite3
SECRET_KEY=your_secret_key
```

### 🔹 5. Initialize the Database  
```bash
python -c "from app import db; db.create_all()"
```

### 🔹 6. Run the Flask Application  
```bash
python app.py
```

---

## 🚀 Usage  

### 1️⃣ **Check if the API is Running**  
Visit `http://127.0.0.1:5000/` in your browser. You should see:  
```
Welcome to the AI-Based Cloud Database Management System!
```

### 2️⃣ **Adding a New Transaction (POST Request)**  
Use Postman or `cURL` to send a request:  
```bash
curl -X POST http://127.0.0.1:5000/transaction -H "Content-Type: application/json" \
-d '{"operation":"INSERT","data":"Sample data","performance_metric":2.0}'
```

### 3️⃣ **Retrieving All Transactions (GET Request)**  
```bash
curl http://127.0.0.1:5000/transactions
```

### 4️⃣ **Run the AI Optimization Simulation**  
```bash
python simulation.py
```

---

## ⭐ Features  

✅ **Flask REST API** for handling database transactions.  
✅ **SQLite Integration** to store and retrieve transactions.  
✅ **Basic AI Module** to analyze and suggest query optimizations.  
✅ **Automated Transaction Simulation** for testing system behavior.  
✅ **Postman & cURL Support** for easy API interaction.  
✅ **Error Handling & Debugging** to prevent unexpected crashes.  

---

## ⚙️ Configuration  

| **Environment Variable** | **Description** |
|-------------------------|-----------------|
| `FLASK_APP`             | Defines the Flask entry point. |
| `FLASK_DEBUG`           | Enables debugging mode. |
| `DATABASE_URL`          | Sets the database connection URL. |
| `SECRET_KEY`            | Used for session security. |

To modify AI behavior, adjust the **training dataset** inside `ai_optimizer.py`.  

---

## 🔥 API Endpoints  

| **Method** | **Endpoint**       | **Description** |
|------------|--------------------|----------------|
| **GET**    | `/`                | Welcome message. |
| **POST**   | `/transaction`      | Adds a new database transaction. |
| **GET**    | `/transactions`     | Retrieves all stored transactions. |

Example Request (POST `/transaction`):  
```json
{
  "operation": "INSERT",
  "data": "Sample entry",
  "performance_metric": 2.5
}
```

Example Response (201 Created):  
```json
{
  "message": "Transaction added successfully.",
  "id": 1
}
```

---

## 🤖 AI Optimization Module  

- Uses **Linear Regression (Scikit-learn)** to predict the best database optimization level based on performance metrics.  
- Called automatically after every **transaction** to suggest improvements.  
- Can be tested manually by running:  
  ```bash
  python ai_optimizer.py
  ```

Expected Output:  
```
For a performance metric of 1.8, Suggested optimization level: 3.10
```

---

## 📸 Screenshots  

📌 **[Attach relevant screenshots here]**  
- ✅ Flask API running (`python app.py`)  
- ✅ Postman API test (`POST /transaction`)  
- ✅ Transaction logs (`GET /transactions`)  
- ✅ AI Optimization Output (`python simulation.py`)  
- ✅ Database Structure in SQLite  

---

## 🤝 Contributing  

We welcome contributions! To contribute:  
1. **Fork** this repository.  
2. Create a new **branch** (`git checkout -b feature-branch`).  
3. Commit your changes (`git commit -m "Added new feature"`).  
4. Push the branch (`git push origin feature-branch`).  
5. Create a **Pull Request**.  

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for detailed guidelines.  

---

## 📜 License  

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) for details.  

---

## 📩 Contact  

For issues and feedback, create a GitHub Issue or contact:  
📧 **Email:** vaskarb.cs.20@nitj.ac.in  
 

