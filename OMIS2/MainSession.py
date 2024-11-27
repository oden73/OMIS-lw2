from flask import Flask, redirect, render_template, request

from view.StandtardInterfaceFactory import StandardInterfaceFactory
from view.Application import Application

class MainSession:
    def __init__(self) -> None:
        self.app: Flask = Flask(__name__)
        self.register_additional_routes()

    def register_additional_routes(self):
        @self.app.route('/')
        def home():
            return redirect('/login')

        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                return redirect('/active_orders')
                # return redirect('/courier_active_orders')
                # return redirect('/admin_user_management')

            return render_template('login.html')

        @self.app.route('/register', methods=['GET', 'POST'])
        def register():
            if request.method == 'POST':
                return redirect('/active_orders')
                # return redirect('/courier_active_orders')
                # return redirect('/admin_user_management')

            return render_template('register.html')

        # client routing

        @self.app.route('/active_orders')
        def active_orders():
            return render_template('active_orders.html')

        @self.app.route('/client_profile')
        def client_profile():
            return render_template('client_profile.html')

        @self.app.route('/parcel_history')
        def parcel_history():
            return render_template('parcel_history.html')

        @self.app.route('/order_token')
        def order_token():
            return render_template('order_token.html')

        @self.app.route('/client_chat')
        def client_chat():
            return render_template('client_chat.html')

        @self.app.route('/courier_active_orders')
        def courier_active_orders():
            return render_template('courier_active_orders.html')

        @self.app.route('/courier_profile')
        def courier_profile():
            return render_template('courier_profile.html')

        @self.app.route('/courier_chat')
        def courier_chat():
            return render_template('courier_chat.html')

        @self.app.route('/courier_client_chat')
        def courier_client_chat():
            return render_template('courier_client_chat.html')

        @self.app.route('/admin_user_management')
        def admin_user_management():
            return render_template('admin_user_management.html')

        @self.app.route('/admin_profile')
        def admin_profile():
            return render_template('admin_profile.html')

        @self.app.route('/admin_delivery_points')
        def admin_delivery_points():
            return render_template('admin_delivery_points.html')

        @self.app.route('/admin_chat')
        def admin_chat():
            return render_template('admin_chat.html')

    def launch(self) -> None:
        interface_factory: StandardInterfaceFactory = StandardInterfaceFactory()
        application: Application = Application()


        self.app.run(debug=True)


if __name__ == '__main__':
    session: MainSession = MainSession()
    session.launch()
