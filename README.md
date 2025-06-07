
# AccuKnox User Management Tests

This repository contains the manual and automated test cases for the User Management module in the OrangeHRM application.

## 🔗 Application Under Test (AUT)

- URL: [https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
- Credentials:
  - Username: `Admin`
  - Password: `admin123`

## 📦 Project Structure

```
accuknox-user-management-tests/
│
├── tests/                  # Test scripts for each test case
│   └── test_add_user.py
│   └── test_search_user.py
│   └── test_edit_user.py
│   └── test_delete_user.py
│
├── pages/                  # Page Object Model (POM) classes
│   └── login_page.py
│   └── dashboard_page.py
│   └── admin_page.py
│
├── conftest.py             # Pytest fixtures
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🚀 Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/your-username/accuknox-user-management-tests.git
cd accuknox-user-management-tests
```

2. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```

3. Run test cases:
```bash
pytest tests/
```

## 🧪 Playwright Version

- Tested with Playwright **v1.44+**

## 📄 Manual Test Cases

Manual test cases are included in the Excel file: `AccuKnox_Manual_Test_Cases.xlsx`

## 📌 Notes

- All test cases are automated using Playwright and follow the Page Object Model (POM).
- Ensure a stable internet connection as the application is hosted online.
