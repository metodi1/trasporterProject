class Single_Line_details_obj:
    def __int__(self, material_line, address_line, line_name, transporter_name):
        self.material_line = material_line
        self.address_line = address_line
        self.line_name = line_name
        self.transporter_name = transporter_name


class Single_Task_details_obj:
    def __int__(self, id, s_number, line_address, warehouse_address, transporter, line, status_line, status_warehouse,
                start_time, end_time):
        self.id = id
        self.s_number = s_number
        self.line_address = line_address
        self.warehouse_address = warehouse_address
        self.transporter = transporter
        self.line = line
        self.status_line = status_line
        self.status_warehouse = status_warehouse
        self.start_time = start_time
        self.end_time = end_time


class Transporter_statistic_closed:
    def __int__(self, transporter, today_closed_orders, total_closed_orders, today_likes, total_likes, likers,
                curren_user_like=False, show_heart=False):
        self.transporter = transporter
        self.today_closed_orders = today_closed_orders
        self.total_closed_orders = total_closed_orders
        self.today_likes = today_likes
        self.likers = list()
        self.curren_user_like = curren_user_like
        self.show_heart = show_heart
