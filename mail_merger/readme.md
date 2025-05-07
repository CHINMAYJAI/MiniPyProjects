# MAIL MERGE

## Overview
MAIL MERGE is a Python-based application that automates the process of sending personalized emails to multiple recipients. It reads recipient data from an Excel sheet, generates customized email content using a generative AI model, and sends the emails using a mail sender module. The application also updates the Excel sheet with the status of each email sent.

## Features
- Reads recipient information from an Excel file (`MailRecipients.xlsx`).
- Generates personalized email content using AI.
- Sends emails to multiple recipients.
- Updates the Excel sheet with the status of each email (Sent/Not Sent).
- Colors cells in the Excel sheet based on the email status.
- Creates a separate file for recipients whose emails were not sent (filename: NotSentRecipients.xlsx).

## Requirements
- Python 3.x
- Pandas
- OpenPyXL
- Any additional libraries used in the project (e.g., for sending emails)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/CHINMAYJAI/MiniPyProjects.git
   cd MiniPyProjects/mail_merge
   ```

2. Install the required packages:
   ```bash
   pip install pandas openpyxl
   ```

## Usage
1. Prepare an Excel file named `MailRecipients.xlsx` with the following columns:
   - `Sno`
   - `ReceiverName`
   - `ReceiverEmail`
   - `SenderName`
   - `SenderEmail`
   - `Post`
   - `CustomMessage`
   - `MailStatus`

**NOTE:** *Format of excel sheet is present inside the same repository (filename: MailRecipients.xlsx)*

2. Run the script:
   ```bash
   python main.py
   ```

3. Check the `MailRecipients.xlsx` file for the email status updates.


## Project Structure

```
MiniPyProjects/
└── Mail_Merge/
    ├── main.py
    |── excel_sheet_reader.py
    ├── gen_ai_mail.py
    ├── mail_sender.py
    ├── coloring_excel_cell_mailNotSent.py
    ├── extract_not_sent_rows.py
    ├── MailRecipients.xlsx
    └── README.md
```


## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the contributors and libraries that made this project possible.

## Contact
For any questions or suggestions, please contact [CHINMAYJAI](https://github.com/CHINMAYJAI).

## Author
[CHINMAY JAIN](https://github.com/CHINMAYJAI/)