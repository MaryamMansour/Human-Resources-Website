function DisplayMessage() {
    let inputs = [
        document.getElementById('Employee-Name').value,
        document.getElementById('Employee-E-mail').value,
        document.getElementById('Gender').value,
        document.getElementById('Martial-Status').value,
        document.getElementById('Date-Of-Birth').value,
        document.getElementById('Available-Vacations').value,
        document.getElementById('Approved-Vacations').value,
        document.getElementById('Salary').value,
        document.getElementById('ID').value]

    for (let i = 0; i < 5; i++) {
        if (inputs[i] === "") {
            document.getElementById('Validation-Message').innerHTML = "Please Fill All Fields!";
            setTimeout(function () {
                document.getElementById('Validation-Message').innerHTML = "";
            }, 2000)
            return false;
        }
    }

    for (let i = 4; i < 9; i++) {
        if (inputs[i] == "" || inputs[i] > 99999999999) {
            document.getElementById('Validation-Message').innerHTML = "Please Fill All Fields!";
            setTimeout(function () {
                document.getElementById('Validation-Message').innerHTML = "";
            }, 2000)
            return false;
        }
    }

    if (((inputs[1].includes('@')) && inputs[1].indexOf('@') != (inputs[1].length) - 1)) {
        return true;
    }
}
$(document).on('submit', 'addingEmploymentForm', function (event) {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: "{% url 'AddEmployee' %}",
        data: {
            name: $('#Employee-Name').val(),
            mail: $('#Employee-E-mail').val(),
            dateofBirth: $('#Date-Of-Birth').val(),
            address: $('#Address').val(),
            gender: $('#Gender').val(),
            availablevac: $('#Available-Vacations').val(),
            approvedvac: $('#Approved-Vacations').val(),
            salary: $('#Salary').val(),
            phoneNum: $('#Phone-Number').val(),
            maritalstatus: $('#Martial-Status').val(),
            ID: $('#IDD').val(),
        },
        success: function () {
        }
    })
})
