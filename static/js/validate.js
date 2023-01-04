
document.getElementById('form').addEventListener('submit', function (e) {
    var id = document.getElementById("ID").value;
    var university = document.getElementById('university').value;
    var courses = document.getElementsByClassName('Course');
    var gender = document.getElementsByClassName('gender');
    for (let i = 0; i < gender.length; i++){
        if (gender[i].checked) break;
        window.alert("Select a gender");
        e.preventDefault();
        return;
    }

    var status = document.getElementsByClassName('status');
    for (let i = 0; i < gender.length; i++){
        if (status[i].checked) break;
        window.alert("Select a status");
        e.preventDefault();
        return;
    }
    for (let i = 0; i < courses.length; i++){
        if (courses[i].value === ""){
            window.alert(`You have empty fields for course number {i}`);
            e.preventDefault();
            return;
        }
    }

    for (let i = 0; i < id.length; i++){
        if (isNaN(id)) {
            window.alert("ID is invalid, Please only use numbers");
            e.preventDefault()
            return;
        }
    }

    for (let i = 0; i < university.length; i++){
        if (!isNaN(university)){
            window.alert("university cannot contain numbers");
            e.preventDefault();
            return ;
        }
    }


});


