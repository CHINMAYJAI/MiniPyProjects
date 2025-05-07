# NOTE: this file is used to extract the rows in which MailStatus is Not Sent and create the excel file named NotSentRecipients.xlsx which further contains the data where MailStatus is negative
import pandas as pd

def filteringMailStatusAndCreationOfNewExcelFile():
    """Filtering all the not sent mail status and creation of new excel sheet which contains all the filtered not sent mail status data"""
    # Load the original Excel file
    file_path = 'MailRecipients.xlsx'
    df = pd.read_excel(file_path)

    # Remove any unnamed columns that may have been created
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Filter rows where MailStatus is "not sent" (case-insensitive)
    filtered_df = df[df['MailStatus'].str.strip().str.lower() == 'not sent']

    # Save filtered rows to a new Excel file
    filtered_df.to_excel('NotSentRecipients.xlsx', index=False)

    print("Filtered rows with 'not sent' status saved to 'NotSentRecipients.xlsx'")

if __name__ == "__main__":
    pass