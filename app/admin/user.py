from flask_admin.contrib.sqla import ModelView


class WeightView(ModelView):
    column_list = ('value_in_kg', 'user_id')
    column_filters = ['user_id']
    form_columns = ['value_in_kg', 'timestamp', 'user_id']