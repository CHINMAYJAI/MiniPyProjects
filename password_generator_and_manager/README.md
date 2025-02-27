# Passcode Manager

## Overview

The Passcode Manager is a secure application designed to generate, store, and manage passcodes. It uses MongoDB for storage and Tkinter for the graphical user interface. The application allows users to add, update, and check passcodes securely by using **Hashing Techniques**.

## Features

- **Add Passcode**: Generate and store a new passcode.
- **Update Passcode**: Update an existing passcode.
- **Check Passcode**: Verify if the entered passcode is correct.
- **Generate Strong Passcode**: Suggest a strong passcode for the user.

## Requirements

- Python 3.x
- Tkinter
- MongoDB
- pymongo
- smtplib
- email.mime

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/CHINMAYJAI/MiniPyProjects.git
    cd MiniPyProjects/password_generator_and_manager
    ```

2. **Install the required Python packages:**
    ```bash
    pip install pymongo
    ```

3. **Set up MongoDB:**
    - Ensure MongoDB is installed and running on your local machine.
    - The application connects to MongoDB at `connectivity link`.

4. **Configure email settings:**
    - Update the `self.email` and `self.password` fields in `passcode_manager.py` with your email credentials.
    - Ensure "Less secure app access" is enabled in your Google account settings if you are using a Gmail account.

## Usage

1. **Run the application:**
    ```bash
    python passcode_manager.py
    ```

2. **Main Menu:**
    - **Add Passcode**: Enter the application name, passcode, and email address. Optionally, generate a strong passcode.
    - **Update Passcode**: Enter the application name, new passcode, and email address to update an existing passcode.
    - **Check Passcode**: Enter the application name, passcode, and email address to verify if the passcode is correct.

## Project Structure

```
MiniPyProjects/
└── password_generator_and_manager/
    ├── assets/
    │   └── logoCJ.png
    ├── passcode_generator.py
    ├── passcode_manager.py
    └── README.md
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please contact [CHINMAYJAI](https://github.com/CHINMAYJAI).

---
## Author
[CHINMAY JAIN](https://github.com/CHINMAYJAI/)
