
from django.urls import path

from ohs_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("customer_registration", views.customer_registration, name="customer_registration"),
    path("worker_registration", views.worker_registration, name="worker_registration"),
    path("login_page", views.login_page, name="login_page"),
    path("logout_view", views.logout_view, name="logout_view"),

    ####################ADMIN####################

    path("work_add", views.work_add, name="work_add"),
    # delete work
    path("delete_work/<int:id>/", views.delete_work, name="delete_work"),
    # update work
    path("update_work/<int:id>/", views.update_work, name="update_work"),
    path("customers_data", views.customers_data, name="customers_data"),
    # delete customer from customer's data
    path("delete_it/<int:id>/", views.delete_it, name="delete_it"),
    path("workers_data", views.workers_data, name="workers_data"),
    # delete button url for worker's data
    path("delete/<int:id>/", views.delete, name="delete"),
    # update button url for worker's data
    path("update/<int:id>/", views.update, name="update"),
    path("appoinmentview_admin", views.appoinmentview_admin, name="appoinmentview_admin"),
    path("approve_appointment/<int:id>/", views.approve_appointment, name="approve_appointment"),
    path("reject_appointment/<int:id>/", views.reject_appointment, name="reject_appointment"),
    # path("adminbase", views.adminbase, name="admin_base"),
    path("admin_base", views.admin_base, name="admin_base"),
    path("create_bill",views.create_bill,name="create_bill"),
    path("view_bill",views.view_bill,name="view_bill"),
    path("feedbacks", views.feedbacks, name="feedbacks"),
    path("reply_feedback/<int:id>/", views.reply_feedback, name="reply_feedback"),
    path("view_schedule_admin", views.view_schedule_admin, name="view_schedule_admin"),
    # delete worker schedule
    path("delete_worker_schedule/<int:id>/", views.delete_worker_schedule, name="delete_worker_schedule"),
    path("work_view", views.work_view, name="work_view"),

    ####################CUSTOMER####################

    path("feedback", views.feedback, name="feedback"),
    path("view", views.view, name="view"),
    path("appoinment_view", views.appoinment_view, name="appoinment_view"),
    path("appointment_side_profile", views.appointment_side_profile, name="appointment_side_profile"),
    path("appoinment_take_bycustomer/<int:id>/", views.appoinment_take_bycustomer, name="appoinment_take_bycustomer"),
    path("view_workersdatacustomer", views.view_workersdatacustomer, name="view_workersdatacustomer"),
    path("customer_base", views.customer_base, name="customer_base"),
    # path("worker_base", views.customerbase, name="customerbase"),
    path("view_payment_by_customer", views.view_payment_by_customer, name="view_payment_by_customer"),
    path("pay_in_direct/<int:id>/", views.pay_in_direct, name="pay_in_direct"),
    path("pay_bill_online/<int:id>/", views.pay_bill_online, name="pay_bill_online"),
    path("bill_history", views.bill_history, name="bill_history"),
    path("view_schedule_customer", views.view_schedule_customer, name="view_schedule_customer"),
    path("book_appoinment/<int:id>/", views.book_appoinment, name="book_appoinment"),
    path("update_customer_data/<int:id>/", views.update_customer_data, name="update_customer_data"),
    path("customerdata_view_by_customer_filtered", views.customerdata_view_by_customer_filtered, name="customerdata_view_by_customer_filtered"),

    ####################WORKER####################

    path("appoinmentview_worker", views.appoinmentview_worker, name="appoinmentview_worker"),
    # path("workerbase", views.workerbase, name="workerbase"),
    path("worker_base", views.worker_base, name="worker_base"),
    path("addschedule", views.addschedule, name="addschedule"),
    path("workerdata_view_by_worker", views.workerdata_view_by_worker, name="workerdata_view_by_worker"),
    path("view_schedule_worker", views.view_schedule_worker, name="view_schedule_worker"),
    path("workerdata_worker", views.workerdata_worker, name="workerdata_worker"),
    path("workers_work", views.workers_work, name="workers_work"),
    path("update_worker_data/<int:id>/", views.update_worker_data, name="update_worker_data"),
    path("view_filtered_schedule", views.view_filtered_schedule, name="view_filtered_schedule"),
    path("workerdata_view_by_worker_filtered", views.workerdata_view_by_worker_filtered, name="workerdata_view_by_worker_filtered"),


]
