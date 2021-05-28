for row_number,row_data in enumerate(fetchen):
            self.DrugsTable.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.DrugsTable.setItem(row_number,colum_number,QTableWidgetItem(str(data)))