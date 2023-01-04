const from = document.getElementById('form')
const id = document.getElementById('id')
const name = document.getElementById('name')
const university = document.getElementById('university')
const Department = document.getElementById('Department')
const Course = document.getElementById('Course')


from.addEventListener('submit',(e)=>{
    let masseage = []
    if(name.value ===' ' || name.value==null)
    {
        masseage.push('Please, Enter Your Name')

    }
    e.preventDefault()
})

