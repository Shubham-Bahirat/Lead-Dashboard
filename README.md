# 🚀 Lead Dashboard (React + FastAPI)

A full-stack CRM (Customer Relationship Management) system with a modern UI and backend API.

## ✨ Features

* Add Leads (Name, Email)
* Update Lead Status (New, Contacted, Closed)
* Dashboard Analytics:

  * Total Leads
  * Converted Leads
  * Conversion Rate
* Responsive UI (Mobile + Desktop)
* Dark Theme Dashboard (Modern UI)

---

# 🧱 Tech Stack

## Frontend

* React.js
* Tailwind CSS
* Axios

## Backend

* FastAPI
* Uvicorn

---

# ⚙️ Project Setup

## 📁 Folder Structure

```
project-root/
│
├── backend/
│   └── main.py
│
└── frontend/
    └── crm-ui/
```

---

# 🔧 Backend Setup (FastAPI)

## 1. Navigate to backend folder

```bash
cd backend
```

## 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\\Scripts\\activate    # Windows
```

## 3. Install dependencies

```bash
pip install fastapi uvicorn
```

## 4. Run server

```bash
uvicorn main:app --reload
```

## 5. Backend URL

```
http://localhost:8000
```

---

# 💻 Frontend Setup (React + Tailwind)

## 1. Navigate to frontend folder

```bash
cd frontend
```

## 2. Create React App

```bash
npx create-react-app crm-ui
cd crm-ui
```

## 3. Install dependencies

```bash
npm install axios
```

---

## 🎨 Install Tailwind CSS (IMPORTANT)

### Step 1:

```bash
npm install -D tailwindcss@3.4.1 postcss autoprefixer
npx tailwindcss init -p
```

### Step 2: Update `tailwind.config.js`

```js
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

### Step 3: Update `src/index.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Step 4: Import CSS

In `src/index.js`

```js
import './index.css';
```

---

## 4. Start frontend

```bash
npm start
```

## 5. Frontend URL

```
http://localhost:3000
```

---

# 🔗 API Endpoints

| Method | Endpoint    | Description   |
| ------ | ----------- | ------------- |
| GET    | /leads      | Get all leads |
| POST   | /leads      | Add new lead  |
| PUT    | /leads/{id} | Update status |
| GET    | /dashboard  | Get analytics |

---

# 📸 UI Preview

* Dashboard cards
* Gmail-style lead list
* Status filters
* Responsive design

---

# ⚠️ Notes

* Data is stored in memory (no database yet)
* Restarting backend will reset data

---

# 🚀 Future Improvements

* PostgreSQL integration
* Authentication (Login system)
* AI Lead Scoring
* Email integration (Gmail-like tracking)
* Charts (Recharts / Chart.js)

---

# 🤝 Contribution

Feel free to fork and improve this project!

---

# 📄 License

This project is open-source and free to use.

---

# 🙌 Author

Built with ❤️ using React & FastAPI
