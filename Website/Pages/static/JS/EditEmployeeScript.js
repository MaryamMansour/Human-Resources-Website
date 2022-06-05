function DeleteUser(){
    if (confirm("Are You Sure You Want To Delete Employee ?")) {
        alert("Deleted");
        document.getElementById('Delete').tagName.replace("Delete");
        this.f
    }
}


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
            setTimeout(function(){
                document.getElementById('Validation-Message').innerHTML = "";
            },2000)
            return false;
        }
    }

    for (let i = 4; i < 9; i++) {
        if (inputs[i] == "" || inputs[i] > 99999999999) {
            document.getElementById('Validation-Message').innerHTML = "Please Fill All Fields!";
            setTimeout(function(){
                document.getElementById('Validation-Message').innerHTML = "";
            },2000)
            return false;
        }
    }

    if (((inputs[1].includes('@')) && inputs[1].indexOf('@') != (inputs[1].length) - 1)) {
        return true;
    }
}
