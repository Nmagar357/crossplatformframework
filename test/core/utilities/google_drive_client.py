import string
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleDriveClient:

    ##  *** !!! PLEASE DO NOT RUN THIS - COULD CAUSE ACCOUNTS TO LOCK !!! ***

    def __init__(self, log_utility):
        """
        Initializes the Google Drive Client.
        Enables use of Google Drive API; Workbook/worksheet, read/write, input/output.
        Dependencies:
            * gspread
            * oauth2client
            * PyOpenSSL

        INSTRUCTIONS:
        In order to start using the client you must do the following:
        * Install dependencies locally
        * Share workbook/spreadsheet with 'nyteqa@nyteqa-225320.iam.gserviceaccount.com'
        *
        """
        self.name = "GoogleDriveClient"
        self.log = log_utility
        self.workbook = None
        self.workbook_id = None
        self.worksheet = None
        self.worksheet_id = None

        self.share_accounts = ['neil.norton@nytimes.com']  # , 'olimon.ibragimov@nytimes.com']
        self.suite_helpers_bin = '{0}/bin'.format(__file__.split('/google_drive_client')[0])
        self.service_client_json = '{0}/nyteqa.json'.format(self.suite_helpers_bin)
        self.client_email = 'nyteqa@nyteqa-225320.iam.gserviceaccount.com'
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.service_client_json, self.scope)
        self.client = gspread.authorize(self.credentials)

    def get_workbook(self, workbook_name=None, workbook_key=None, workbook_url=None):
        """
        Returns a workbook (and assigns it as the class workbook) based on either the given workbook_name,
        workbook_key, or workbook_url.
        :param workbook_name: str(), name of workbook
        :param workbook_key: str(), key of workbook
        :param workbook_url: str(), URL of workbook
        :return: obj(), workbook object
        """
        if workbook_name is not None:
            self.workbook = self.client.open(workbook_name)
        elif workbook_key is not None:
            self.workbook = self.client.open_by_key(workbook_key)
        elif workbook_url is not None:
            self.workbook = self.client.open_by_url(workbook_url)
        else:
            raise Exception("ERROR: Must provide workbook_name, workbook_key, or workbook_url to get a workbook!")
        return self.workbook

    def add_cols(self, worksheet, col_num):
        """
        Adds col_num to the right side of the worksheet.
        :param worksheet: obj(), worksheet object
        :param col_num: int(), number of cols to add
        :return:
        """
        self.log.debug("Adding col_num={0} number of rows to right side of worksheet={1}".format(worksheet, col_num))
        worksheet.add_cols(col_num)

    def add_rows(self, worksheet, row_num):
        """
        Adds row_num to the bottom of the worksheet.
        :param worksheet: obj(), worksheet object
        :param row_num: int(), number of rows to add
        :return:
        """
        self.log.debug("Adding row_num={0} number of rows to worksheet={1}".format(worksheet, row_num))
        worksheet.add_rows(row_num)

    def clear_worksheet(self, worksheet):
        """
        Clears all data inside a worksheet.
        :param worksheet: obj(), worksheet object
        :return:
        """
        self.log.debug("Clearing all values and data in worksheet={0}".format(worksheet))
        return worksheet.clear()

    def convert_letter_to_number(self, letter):
        """
        Converts a column letter to a column number, and returns that value.
        :param letter: str(), letter of column
        :return: str(), column number
        """
        number = 0
        for char in letter:
            if char in string.ascii_letters:
                number = number * 26 + (ord(char.upper()) - ord('A')) + 1
        self.log.debug("Converted column letter='{0}' to integer number={1}".format(letter, number))
        return number

    def convert_cell_name_to_tuple(self, cell_name='A1'):
        """
        Convert a cell name location into a tuple cell address.
        :param cell_name: str(), a cell's name location
        :return: tuple(), [<row>, <col>]
        """
        row = '0'
        col = '0'
        for i, char in enumerate(cell_name):
            if char.isdigit() is True:
                row = cell_name[i:]
                col = cell_name[:i]
                break
        row = int(row)
        col = int(self.convert_letter_to_number(col))
        return [row, col]

    def count_columns(self, worksheet):
        """
        Returns column count in given worksheet.
        :param worksheet: obj(), worksheet
        :return:
        """
        col_count = worksheet.col_count
        self.log.debug("worksheet={0} has col_count={1}".format(worksheet, col_count))
        return col_count

    def create_workbook(self, workbook_title, share_accounts=None):
        """
        Creates a new workbook by the given workbook_title, and shares it with share_accounts list.
        :param workbook_title: str(), title of new workbook
        :param share_accounts: list(), a list of accounts to share workbook with
        :return:
        """
        self.log.debug("Creating a new workbook with title='{0}'".format(workbook_title))
        self.workbook = self.client.create(workbook_title)
        self.share_workbook_with_accounts(self.workbook, accounts=share_accounts)
        return self.workbook

    def create_worksheet(self, workbook, worksheet_title, rows=100, cols=20):
        """
        Create a new worksheet in a given workbook, with provided number of rows and columns.
        :param workbook: obj(), workbook to create new sheet in
        :param worksheet_title: str(), title of new worksheet
        :param rows: str(), number of rows in worksheet
        :param cols: str(), number of columns in worksheet
        :return:
        """
        self.log.debug("Adding a new worksheet with worksheet_title={0}, with [rows={1}, cols={2}], to workbook={3}".
                       format(worksheet_title, rows, cols, workbook))
        return workbook.add_worksheet(title=worksheet_title, rows=rows, cols=cols)

    def delete_row(self, worksheet, row=1):
        """
        Deletes a row in the given worksheet.
        :param worksheet: obj(), worksheet object
        :param row: int(), row index to delete
        :return:
        """
        self.log.debug("Deleting row={0} in worksheet={1}".format(row, worksheet))
        return worksheet.delete_row(index=row)

    def delete_workbook(self, workbook):
        """
        Deletes a given workbook.
        :param workbook: obj() workbook object
        :return:
        """
        self.log.debug("Deleting workbook={0}".format(workbook))
        return self.client.del_spreadsheet(workbook.id)

    def delete_worksheet(self, workbook, worksheet):
        """
        Deletes a given worksheet, inside a given workbook.
        :param workbook: obj(), workbook object
        :param worksheet: obj(), worksheet object
        :return:
        """
        self.log.debug("Deleting worksheet={0}, in workbook={1}".format(worksheet, workbook))
        return workbook.del_worksheet(worksheet)

    def duplicate_workbook(self, workbook, new_workbook_title, copy_permissions=False):
        """
        Duplicates an existing workbook, with given new_workbook_title, and can copy permissions.
        :param workbook: obj(), workbook object
        :param new_workbook_title: str(), title of the duplicated new workbook
        :param copy_permissions: bool(), True is copying the permissions from old workbook.
        :return:
        """
        self.log.debug("Duplicating workbook, with new_workbook_title={0}, copy_permissions={1}".format(
            new_workbook_title, copy_permissions))
        return self.client.copy(file_id=workbook.id, title=new_workbook_title, copy_permissions=copy_permissions)

    def duplicate_worksheet(self, worksheet, new_worksheet_name, index=None, sheet_id=None):
        """
        Duplicates an existing worksheet with given new_worksheet_name.
        :param worksheet: obj(), worksheet object
        :param new_worksheet_name: str(), the title of the duplicated new worksheet
        :param index: (optional)
        :param sheet_id: (optional)
        :return: obj(), newly duplicated worksheet
        """
        self.log.debug("Duplicating worksheet={0}, in workbook={1}".format(worksheet, worksheet.spreadsheet))
        return worksheet.duplicate(insert_sheet_index=index, new_sheet_id=sheet_id, new_sheet_name=new_worksheet_name)

    def find_cell_by_value(self, worksheet, value, find_all_matching_cells=False):
        """
        Returns cell objects of first cell that matches given text in worksheet.
        :param value: str(), text string to match on the first cell A1:
        :param worksheet: obj(), worksheet to look for cell with text
        :param find_all_matching_cells: bool(), False (default) Return first matching cell, or True.
        :return: obj(), cell that matches text
        """
        if find_all_matching_cells is False:
            cell = self.__fetch(worksheet).find(value)
            if cell is not None:
                self.log.debug("Found text='{0}' at Row={1} Col={2}".format(value, cell.row, cell.col))
            return cell
        else:
            cell_list = self.__fetch(worksheet).findall(value)
            if cell_list is not None:
                cell_num = len(cell_list)
                self.log.debug("Found {0} cells with matching text='{1}'".format(cell_num + 1, value))
                if cell_num >= 1:
                    for x in range(0, cell_num):
                        self.log.debug("#{0} at Row={1} Col={2}".format(x + 1, cell_list[x].row, cell_list[x].col))
            return cell_list

    def get_cell_data(self, worksheet, cell):
        """
        Returns a worksheet's cell data.
        :param worksheet: obj(), worksheet object
        :param cell: str('A1')/tuple([1,6]), obj({Cell})
        :return: obj(), cell data
        """
        if isinstance(cell, (str,)):
            result = self.convert_cell_name_to_tuple(cell_name=cell)
            row, col = result[0], result[1]
        elif type(cell).__name__ == 'Cell':
            row, col = cell.row, cell.col
        elif isinstance(cell, (tuple,)):
            row, col = cell[0], cell[1]
        else:
            raise Exception("ERROR: Parsing error for cell={0}. Must be one of 'A1', obj({Cell}), or tuple([1,1})")

        data = worksheet.cell(row, col, value_render_option='FORMATTED_VALUE')
        self.log.debug("Returning cell data for cell={0}".format(data))
        return data

    def get_workbook_key(self, workbook_name):
        """
        Returns a workbook key for a given workbook_name
        :param workbook_name: str(), name of the workbook
        :return: str(), workbook_key
        """
        workbooks = {
            'Test Plan Key': '1x1Wul1m4IrnQR_58uS_WzIhPveBaY8AliulfcsuIkZ4'
        }
        key = workbooks[workbook_name]
        self.log.debug('Matched workbook_name={0}, with key={1}'.format(workbook_name, key))
        return key

    def get_workbook_permissions(self, workbook):
        """
        Returns a workbook's permissions.
        :param workbook: obj(), workbook object
        :return: list of permissions
        """
        permissions = workbook.list_permissions()
        self.log.debug('Workbook={0}, permissions={1}'.format(workbook, permissions))
        return permissions

    def get_worksheet_from(self, workbook=None, by_worksheet_number=None, by_worksheet_title=None, ):
        """
        Returns a worksheet for a given workbook. If workbook is not provided, class assigned workbook is used.
        Worksheet can be found by_worksheet_number (the int() of a worksheet in the workbook), or
        by_worksheet_title (the string name of the worksheet title). The worksheet is also assigned as the class
        worksheet (self.worksheet)
        :param workbook: obj(), workbook
        :param by_worksheet_number: int(), an integer number of the worksheet in a workbook
        :param by_worksheet_title: str(), a string title of a worksheet in a workbook
        :return: obj(), worksheet (for a workbook)
        """
        if by_worksheet_number is not None:
            self.worksheet = workbook.get_worksheet(int(by_worksheet_number))
        elif by_worksheet_title is not None:
            self.worksheet = workbook.worksheet(by_worksheet_title)
        else:
            self.worksheet = workbook.sheet1
        return self.worksheet

    def get_worksheets(self, workbook):
        """
        Get a list of all worksheets in a workbook.
        :param workbook: obj(), workbook object
        :return: list(), list of worksheets in a given workbook object
        """
        if workbook is None:
            workbook = self.workbook
        return workbook.worksheets()

    def get_worksheet_values(self, worksheet):
        """
        Returns all values from a worksheet.
        :param worksheet: obj(), worksheet object
        :return:
        """
        values = self.__fetch(worksheet).get_all_values()
        self.log.debug("For worksheet={0}, got values={1}".format(worksheet, values))
        return values

    def get_worksheet_records(self, worksheet):
        """
        Returns all records from a worksheet.
        :param worksheet: obj(), worksheet object
        :return:
        """
        records = self.__fetch(worksheet).get_all_records()
        self.log.debug("For worksheet={0}, got records={1}".format(worksheet, records))
        return records

    def get_worksheet_value_from_a_cell(self, worksheet=None, cell='A1'):
        """
        Returns the value of a cell in a worksheet.
        :param worksheet: obj(), worksheet object, defaults to self.worksheet if None
        :param cell: str(), cell object name, ex: 'A1', 'B560', 'AB9'
        :return: str(), value of cell
        """
        value = self.__fetch(worksheet).acell(cell)
        self.log.debug("For cell={0}, got value={1}".format(cell, value))
        return value

    def get_worksheet_values_from_a_row(self, worksheet=None, row=1):
        """
        Returns values of all cells in a row, in given worksheet.
        :param worksheet: obj(), worksheet object, defaults to self.worksheet if None
        :param row: int(), row number
        :return: array(), array of all values in row
        """
        values = self.__fetch(worksheet).row_values(int(row))
        self.log.debug("For row={0}, got values={1}".format(row, values))
        return values

    def get_worksheet_values_from_a_column(self, worksheet=None, column=1):
        """
        Returns values of all cells in a column, in given worksheet.
        :param worksheet: obj(), worksheet object, defaults to self.worksheet if None
        :param column: int(), column number
        :return: list(), list of all values in column
        """
        values = self.__fetch(worksheet).col_values(int(column))
        self.log.debug("For column={0}, got values={1}".format(column, values))
        return values

    def insert_row(self, worksheet, values=None, index=1, input_type='RAW'):
        """
        Inserts a new row into the worksheet at given index (row).
        :param worksheet: obj(), worksheet object
        :param values: list(), list of values to add to row cells
        :param index: int(), index of row in which to insert row
        :param input_type: str(), the way the values are entered in the sheet ['RAW', 'USER_INPUT']
        :return:
        """
        if values is None:
            values = ['']
        self.log.debug("Inserting new row in worksheet={0}, index={1}, input_type={2}"
                       .format(worksheet.title, index, input_type))
        worksheet.insert_row(values, index, value_input_option=input_type)

    def share_workbook_with_accounts(self, workbook, accounts=None):
        """
        [MACRO] Shares a given workbook with the given list of accounts. Will share with default share accounts if
        none provided.
        :param workbook: obj(), workbook object
        :param accounts: list(), account list to share workbook with
        :return:
        """
        if accounts is None:
            accounts = self.share_accounts
        if isinstance(accounts, (str,)):
            accounts = [accounts]
        if 'nyteqa@gmail.com' not in accounts:
            accounts += 'nyteqa@gmail.com'  # We must always include the QA account in shared accounts for overview
        if isinstance(accounts, (list,)):
            for account in accounts:
                self.__share_workbook(workbook=workbook, email=account, perm_type='user', role='writer', notify=False)

    def update_a_cell(self, worksheet, cell, value):
        """
        Updates a cell's value
        :param worksheet: obj(), worksheet of cell, defaults to self.worksheet if None
        :param cell: str(): cell name 'A1' or, obj('Cell') or, tuple(), cell coordinates [1, 5]
        :param value: str(), value to give to cell
        :return:
        """
        if isinstance(cell, (str,)):
            update = self.__fetch(worksheet).update_acell(cell, value)
        elif type(cell).__name__ == 'Cell':
            update = self.__fetch(worksheet).update_cell(cell.row, cell.col, value)
        elif isinstance(cell, (tuple,)):
            update = self.__fetch(worksheet).update_cell(cell[0], cell[1], value)
        else:
            raise Exception("ERROR: Unable to update a cell, no valid cell format given. Must either be str('A1'), "
                            "obj('Cell'), or tuple([1, 1], but got cell={0} instead!".format(cell))
        self.log.debug("Update result: {0}".format(update))

    def update_cell_range(self, worksheet, value_list=None, cell_range='A1:A2'):
        """
        Updates a worksheet's cell_range, with a given value_list.
        :param worksheet: obj(), worksheet to update, defaults to self.worksheet if None
        :param value_list: list(), ordered list of values
        :param cell_range: str(), cell range to update
        :return:
        """
        assert isinstance(value_list, type(list()))
        assert ':' in cell_range
        assert len(cell_range) >= 5

        sheet = self.__fetch(worksheet)
        cell_list = sheet.range(cell_range)

        self.log.debug("Compiling cell_list with values...")
        for i, cell in enumerate(cell_list):
            cell.value = value_list[i]

        self.log.info("Updating cell_range={0} with value_list={1}".format(cell_range, value_list))
        update = sheet.update_cells(cell_list)
        self.log.debug("Result: {0}".format(update))

    def update_worksheet_title(self, worksheet, worksheet_title):
        """
        Renames the given worksheet's title.
        :param worksheet: obj(), worksheet object
        :param worksheet_title: str() title to rename the worksheet to
        :return:
        """
        self.log.debug("Renaming worksheet with title={0} to worksheet_title='{1}'".format(worksheet.title,
                       worksheet_title))
        worksheet.update_title(worksheet_title)

    def __fetch(self, worksheet=None):
        if worksheet is not None:
            self.log.debug("Fetching argument provided worksheet.")
            return worksheet
        else:
            self.log.debug("Fetching class assigned worksheet.")
            return self.worksheet

    def __share_workbook(self, workbook=None, email=None, perm_type='user', role='writer', notify=True,
                         email_message=None, with_link=False):
        """
        Shares a given workbook with provided arguments.
        :param workbook: obj(), workbook object (if None, self.workbook is used)
        :param email: str(), email of account to share with
        :param perm_type: str(), the account type ['user', 'group', 'domain', 'anyone']
        :param role: str(), primary role for this user ['owner', writer', 'reader']
        :param notify: bool(), True to notify user via email, False if not
        :param email_message: str(), the email to be sent if notify is True
        :param with_link: bool(), whether the link is required for this permission
        :return:
        """
        if workbook is None:
            workbook = self.workbook
        self.log.debug('Sharing workbook={0}, with email={1}, perm_type={2}, role={3}, notify={4}, email_message={5}, '
                       'with_link={6}'.format(workbook.title, email, perm_type, role, notify, email_message, with_link))
        return workbook.share(email, perm_type, role, notify, email_message, with_link)


def run_test():
    # Initialize client
    from test.core.utilities.log_utility import LogUtility

    log_utility = LogUtility()
    client = GoogleDriveClient(log_utility)

    # Create a workbook (shares it with share_accounts)
    workbook = client.create_workbook(workbook_title='New Workbook', share_accounts=client.share_accounts)

    # Create a worksheet
    worksheet = client.create_worksheet(workbook, worksheet_title='New Worksheet')

    # Update a cell with a value
    cell_value = 'New Cell'
    client.update_a_cell(worksheet, cell='A1', value=cell_value)
    client.update_a_cell(worksheet, cell='C1', value=cell_value)

    # Update a cell range with values
    values = ['a', 'b', 'c', 'd', 'e', 'f']
    client.update_cell_range(worksheet, value_list=values, cell_range='A2:F2')

    # Finding all cells by cell value
    cell_matches = client.find_cell_by_value(worksheet, value=cell_value, find_all_matching_cells=True)

    # Update first cell match
    client.update_a_cell(worksheet, cell=cell_matches[0], value='Updated Cell')

    # Get all values in both rows
    for i in range(1, 3):
        client.get_worksheet_values_from_a_row(worksheet, row=i)

    # Get all values from worksheet
    client.get_worksheet_values(worksheet)

    # Get all records from worksheet
    client.get_worksheet_records(worksheet)

    # Delete the worksheet
    client.delete_worksheet(workbook, worksheet)

    # Delete the workbook
    client.delete_workbook(workbook)


if __name__ == '__main__':
    run_test()
