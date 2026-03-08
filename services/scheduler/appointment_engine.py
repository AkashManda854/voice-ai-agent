appointments = []

def book_appointment(patient, doctor, time):

    for appt in appointments:
        if appt["doctor"] == doctor and appt["time"] == time:
            return "Slot already booked"

    appointment = {
        "patient": patient,
        "doctor": doctor,
        "time": time
    }

    appointments.append(appointment)

    return "Appointment booked successfully"


def cancel_appointment(patient):

    for appt in appointments:
        if appt["patient"] == patient:
            appointments.remove(appt)
            return "Appointment cancelled"

    return "No appointment found"


def check_availability():
    return ["10 AM", "2 PM", "4 PM"]