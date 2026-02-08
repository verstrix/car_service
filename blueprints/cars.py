from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models import db, Car, Role, WorkOrder, User, WorkOrderPart

cars_bp = Blueprint("cars", __name__, url_prefix="/cars")


@cars_bp.route("/", methods=["GET", "POST"])
@login_required
def list_cars():

    # MANAGER: sees all cars
    if current_user.role == Role.MANAGER:
        cars = Car.query.order_by(Car.id.desc()).all()

    # MECHANIC: sees all cars (you can change this if needed)
    elif current_user.role == Role.MECHANIC:
        cars = Car.query.order_by(Car.id.desc()).all()

    # CLIENT: sees only their own cars
    else:
        cars = Car.query.filter_by(owner_name=current_user.username).order_by(Car.id.desc()).all()

    return render_template("cars.html", cars=cars)


@cars_bp.route("/<int:car_id>")
@login_required
def car_details(car_id):
    car = Car.query.get_or_404(car_id)

    # SECURITY: Clients can only view their own cars
    if current_user.role == Role.CLIENT and car.owner_name != current_user.username:
        flash("Нямате право да виждате този автомобил.", "danger")
        return redirect(url_for("cars.list_cars"))

    orders = WorkOrder.query.filter_by(car_id=car_id).all()
    mechanics = User.query.filter_by(role=Role.MECHANIC).all()

    return render_template(
        "car_details.html",
        car=car,
        orders=orders,
        mechanics=mechanics
    )


@cars_bp.route("/delete/<int:car_id>", methods=["POST"])
@login_required
def delete_car(car_id):
    if current_user.role != Role.MANAGER:
        flash("Само мениджъри могат да изтриват автомобили.", "danger")
        return redirect(url_for("cars.list_cars"))

    car = Car.query.get_or_404(car_id)

    # A car is deletable only if all related work orders are completed (or there are none)
    active_orders = WorkOrder.query.filter(WorkOrder.car_id == car.id, WorkOrder.status != 'completed').first()
    if active_orders:
        flash("Не може да изтриете този автомобил: има активни работни поръчки.", "danger")
        return redirect(url_for("cars.car_details", car_id=car.id))

    # Delete related completed work orders and their used-parts entries to avoid FK integrity errors
    completed_orders = WorkOrder.query.filter_by(car_id=car.id).all()
    for order in completed_orders:
        # delete WorkOrderPart entries for this order
        WorkOrderPart.query.filter_by(work_order_id=order.id).delete()
        db.session.delete(order)

    db.session.delete(car)
    db.session.commit()
    flash("Автомобилът е изтрит.", "success")
    return redirect(url_for("cars.list_cars"))
