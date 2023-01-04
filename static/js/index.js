    tbody = document.getElementById("tbody");

let students = [
    {id: 1, Name:"Ahmed" , birth:"17/6/2001" ,GPA:3.24 ,Gender: "Male",Level:3 ,statue:"Active" ,department:"CS"},
    {id: 2, Name:"Sayed" , birth:"1/1/2001" ,GPA:3 ,Gender: "Male",Level:3 ,statue:"inactive" ,department:"IS"},
    {id: 3, Name:"hassan" , birth:"5/6/2002" ,GPA:4 ,Gender: "Male",Level:3 ,statue:"Active" ,department:"IT"},
    {id: 4, Name:"youssef" , birth:"17/11/2017" ,GPA:4 ,Gender: "Male",Level:4 ,statue:"inactive" ,department:"CS"},
    {id: 5, Name:"mohammed" , birth:"17/3/2001" ,GPA:3 ,Gender: "Male",Level:3 ,statue:"Active" ,department:"DS"},
    {id: 6, Name:"khaled" , birth:"17/2/2001" ,GPA:2 ,Gender: "Male",Level:2 ,statue:"inactive" ,department:"AI"},
    {id: 7, Name:"manar" , birth:"17/4/2001" ,GPA:1 ,Gender: "Female",Level:2 ,statue:"Active" ,department:"DS"},
    {id: 8, Name:"mariam" , birth:"17/5/2001" ,GPA:2.0 ,Gender: "Female",Level:3 ,statue:"inactive" ,department:"CS"},
    {id: 9, Name:"asmaa" , birth:"17/8/2001" ,GPA:2.25 ,Gender: "Female",Level:1 ,statue:"Active" ,department:"CS"},
    {id: 10, Name:"Shimaa" , birth:"10/6/2003" ,GPA:3.03 ,Gender: "Female",Level:3 ,statue:"inactive" ,department:"IT"},
];

function showActiveAndInactive()
{
    let td;
    students.map(i=>
    {
        console.log(i);
            const tr = document.createElement("tr");
                for (const key in i)
                {
                    td = document.createElement("td");
                    td.append(i[key]);
                    tr.appendChild(td)
                }
            tbody.appendChild(tr);
    });
}
showActiveAndInactive();